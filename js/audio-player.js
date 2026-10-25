// ==========================================================================
// Ambient Audio Experience Controller
// Provides calm, elegant background music, volume control, mute, visualizer,
// session persistence, and auto-pause when project videos play.
// ==========================================================================

(function() {
  const AUDIO_SRC = 'assets/audio/ambient_calm.mp3';
  const STORAGE_KEY = 'nada_portfolio_music_pref';
  
  let audioEl = null;
  let audioCtx = null;
  let synthGain = null;
  let isPlaying = false;
  let currentVolume = 0.45;
  let isMuted = false;
  let isSynthesized = false;
  
  function init() {
    audioEl = new Audio();
    audioEl.src = AUDIO_SRC;
    audioEl.loop = true;
    audioEl.volume = currentVolume;
    audioEl.preload = 'none';

    audioEl.addEventListener('error', function(e) {
      console.warn('HTML5 Audio failed, readying Web Audio synthesizer fallback', e);
      isSynthesized = true;
    });

    // Check saved state (default is paused until visitor interacts)
    const saved = sessionStorage.getItem(STORAGE_KEY);
    if (saved) {
      try {
        const pref = JSON.parse(saved);
        if (typeof pref.volume === 'number') currentVolume = pref.volume;
        if (typeof pref.muted === 'boolean') isMuted = pref.muted;
        audioEl.volume = isMuted ? 0 : currentVolume;
      } catch (err) {}
    }

    setupUI();
    setupVideoWatchers();
  }

  function setupUI() {
    const playBtns = document.querySelectorAll('.music-toggle-btn');
    const visualizers = document.querySelectorAll('.music-visualizer');
    const volumeSliders = document.querySelectorAll('.volume-slider');
    const invitationBanner = document.getElementById('music-invitation-banner');
    const enableBannerBtn = document.getElementById('enable-music-banner-btn');
    const dismissBannerBtn = document.getElementById('dismiss-music-banner-btn');

    playBtns.forEach(btn => {
      btn.addEventListener('click', togglePlay);
    });

    visualizers.forEach(viz => {
      viz.addEventListener('click', togglePlay);
    });

    volumeSliders.forEach(slider => {
      slider.value = currentVolume * 100;
      slider.addEventListener('input', function(e) {
        setVolume(e.target.value / 100);
      });
    });

    if (enableBannerBtn) {
      enableBannerBtn.addEventListener('click', function() {
        play();
        if (invitationBanner) invitationBanner.style.display = 'none';
      });
    }

    if (dismissBannerBtn && invitationBanner) {
      dismissBannerBtn.addEventListener('click', function() {
        invitationBanner.style.display = 'none';
      });
    }
  }

  function updateUI() {
    const controllers = document.querySelectorAll('.music-controller');
    const playBtns = document.querySelectorAll('.music-toggle-btn');
    const volumeSliders = document.querySelectorAll('.volume-slider');

    controllers.forEach(c => {
      if (isPlaying) {
        c.classList.add('playing');
      } else {
        c.classList.remove('playing');
      }
    });

    playBtns.forEach(btn => {
      const playIcon = btn.querySelector('.icon-play');
      const pauseIcon = btn.querySelector('.icon-pause');
      if (playIcon && pauseIcon) {
        playIcon.style.display = isPlaying ? 'none' : 'block';
        pauseIcon.style.display = isPlaying ? 'block' : 'none';
      }
    });

    volumeSliders.forEach(slider => {
      slider.value = (isMuted ? 0 : currentVolume) * 100;
    });
  }

  function play() {
    if (isPlaying) return;

    if (!isSynthesized && audioEl) {
      audioEl.play().then(() => {
        isPlaying = true;
        updateUI();
        saveState();
      }).catch(err => {
        console.warn('Playback error, falling back to procedural synthesizer', err);
        startSynthesizer();
      });
    } else {
      startSynthesizer();
    }
  }

  function pause() {
    if (!isPlaying) return;
    if (audioEl) audioEl.pause();
    if (synthGain && audioCtx) {
      synthGain.gain.setTargetAtTime(0, audioCtx.currentTime, 0.2);
    }
    isPlaying = false;
    updateUI();
    saveState();
  }

  function togglePlay() {
    if (isPlaying) {
      pause();
    } else {
      play();
    }
  }

  function setVolume(val) {
    currentVolume = Math.max(0, Math.min(1, val));
    isMuted = currentVolume === 0;
    if (audioEl) {
      audioEl.volume = isMuted ? 0 : currentVolume;
    }
    if (synthGain && audioCtx) {
      synthGain.gain.setTargetAtTime(isMuted ? 0 : currentVolume * 0.2, audioCtx.currentTime, 0.1);
    }
    updateUI();
    saveState();
  }

  function saveState() {
    try {
      sessionStorage.setItem(STORAGE_KEY, JSON.stringify({
        volume: currentVolume,
        muted: isMuted,
        playing: isPlaying
      }));
    } catch (e) {}
  }

  // Web Audio Fallback Ambient Generator
  function startSynthesizer() {
    try {
      const AudioContext = window.AudioContext || window.webkitAudioContext;
      if (!audioCtx) audioCtx = new AudioContext();
      if (audioCtx.state === 'suspended') audioCtx.resume();

      if (!synthGain) {
        synthGain = audioCtx.createGain();
        synthGain.gain.value = currentVolume * 0.18;
        synthGain.connect(audioCtx.destination);

        // Soft ambient drone frequencies (Eb chord: Eb3, G3, Bb3, D4)
        const freqs = [155.56, 196.00, 233.08, 293.66];
        freqs.forEach((f, idx) => {
          const osc = audioCtx.createOscillator();
          const filter = audioCtx.createBiquadFilter();
          filter.type = 'lowpass';
          filter.frequency.value = 450 + idx * 80;

          osc.type = idx % 2 === 0 ? 'sine' : 'triangle';
          osc.frequency.value = f;

          // Subtle detune
          osc.detune.value = (idx - 1.5) * 4;

          osc.connect(filter);
          filter.connect(synthGain);
          osc.start();
        });
      } else {
        synthGain.gain.setTargetAtTime(currentVolume * 0.18, audioCtx.currentTime, 0.4);
      }

      isPlaying = true;
      updateUI();
      saveState();
    } catch (e) {
      console.warn('Synthesizer unavailable', e);
    }
  }

  // Avoid music clashing with project video playback
  function setupVideoWatchers() {
    document.addEventListener('play', function(e) {
      if (e.target.tagName === 'VIDEO' && isPlaying) {
        pause();
      }
    }, true);
  }

  window.portfolioAudio = {
    play: play,
    pause: pause,
    toggle: togglePlay,
    setVolume: setVolume,
    isPlaying: () => isPlaying
  };

  document.addEventListener('DOMContentLoaded', init);
})();
