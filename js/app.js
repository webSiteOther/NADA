// ==========================================================================
// Main Application Logic
// Bilingual Management (EN/AR), Project Exploration, Animated Canvas,
// Repository Inventory Explorer, and Modal Coordinator.
// ==========================================================================

(function() {
  let currentLang = 'en';
  let activeCategory = 'all';
  let searchQuery = '';
  let activeProjectId = null;

  // ------------------------------------------------------------------------
  // Initialization
  // ------------------------------------------------------------------------
  document.addEventListener('DOMContentLoaded', () => {
    initLanguage();
    initCanvas();
    renderHeroAndMetrics();
    renderCategories();
    renderProjects();
    renderInventoryExplorer();
    renderAboutSection();
    setupEventListeners();
    setupCounters();
  });

  // ------------------------------------------------------------------------
  // Bilingual System
  // ------------------------------------------------------------------------
  function initLanguage() {
    const saved = localStorage.getItem('nada_portfolio_lang');
    if (saved === 'ar' || saved === 'en') {
      currentLang = saved;
    }
    applyLanguage(currentLang);

    const toggle = document.getElementById('lang-toggle-btn');
    if (toggle) {
      toggle.addEventListener('click', () => {
        currentLang = currentLang === 'en' ? 'ar' : 'en';
        localStorage.setItem('nada_portfolio_lang', currentLang);
        applyLanguage(currentLang);
        renderHeroAndMetrics();
        renderCategories();
        renderProjects();
        renderInventoryExplorer();
        renderAboutSection();
        if (activeProjectId) openProjectModal(activeProjectId);
      });
    }
  }

  function applyLanguage(lang) {
    document.documentElement.setAttribute('lang', lang);
    document.documentElement.setAttribute('dir', lang === 'ar' ? 'rtl' : 'ltr');

    const enOption = document.querySelector('.lang-option-en');
    const arOption = document.querySelector('.lang-option-ar');
    if (enOption && arOption) {
      if (lang === 'en') {
        enOption.classList.add('active');
        arOption.classList.remove('active');
      } else {
        arOption.classList.add('active');
        enOption.classList.remove('active');
      }
    }

    // Translate all elements with data-i18n-en and data-i18n-ar
    document.querySelectorAll('[data-i18n-en]').forEach(el => {
      const txt = el.getAttribute(`data-i18n-${lang}`);
      if (txt) el.textContent = txt;
    });

    document.querySelectorAll('[data-i18n-placeholder-en]').forEach(el => {
      const txt = el.getAttribute(`data-i18n-placeholder-${lang}`);
      if (txt) el.setAttribute('placeholder', txt);
    });
  }

  // ------------------------------------------------------------------------
  // Hero & Metrics
  // ------------------------------------------------------------------------
  function renderHeroAndMetrics() {
    const p = window.PORTFOLIO_DATA.profile;
    const isAr = currentLang === 'ar';

    const heroName = document.getElementById('hero-name');
    const heroTitle = document.getElementById('hero-title');
    const heroDesc = document.getElementById('hero-description');

    if (heroName) heroName.textContent = p.name[currentLang];
    if (heroTitle) heroTitle.textContent = p.title[currentLang];
    if (heroDesc) heroDesc.textContent = p.summary[currentLang];

    // Metrics
    const metricsGrid = document.getElementById('metrics-grid');
    if (metricsGrid && p.verifiedMetrics) {
      metricsGrid.innerHTML = p.verifiedMetrics.map(m => `
        <div class="metric-card">
          <div class="metric-number" data-target="${m.number}">${m.number}${m.suffix}</div>
          <div class="metric-label">${m.label[currentLang]}</div>
        </div>
      `).join('');
    }
  }

  // ------------------------------------------------------------------------
  // Categories Bar
  // ------------------------------------------------------------------------
  function renderCategories() {
    const catsContainer = document.getElementById('category-pills-container');
    if (!catsContainer) return;

    const cats = window.PORTFOLIO_DATA.categories;
    const projs = window.PORTFOLIO_DATA.projects;

    catsContainer.innerHTML = cats.map(c => {
      const count = c.id === 'all' 
        ? projs.length 
        : projs.filter(p => p.category.id === c.id).length;

      return `
        <button class="category-pill ${c.id === activeCategory ? 'active' : ''}" data-cat="${c.id}">
          <span>${c[currentLang]}</span>
          <span class="category-pill-count">${count}</span>
        </button>
      `;
    }).join('');

    catsContainer.querySelectorAll('.category-pill').forEach(btn => {
      btn.addEventListener('click', () => {
        activeCategory = btn.getAttribute('data-cat');
        renderCategories();
        renderProjects();
      });
    });
  }

  // ------------------------------------------------------------------------
  // Projects Grid
  // ------------------------------------------------------------------------
  function renderProjects() {
    const grid = document.getElementById('projects-grid');
    if (!grid) return;

    const projs = window.PORTFOLIO_DATA.projects;
    const isAr = currentLang === 'ar';

    let filtered = projs.filter(p => {
      const matchCat = activeCategory === 'all' || p.category.id === activeCategory;
      if (!matchCat) return false;

      if (!searchQuery.trim()) return true;
      const q = searchQuery.toLowerCase();
      const title = (p.title[currentLang] || '').toLowerCase();
      const tagline = (p.tagline[currentLang] || '').toLowerCase();
      const desc = (p.description[currentLang] || '').toLowerCase();
      const tools = p.tools.join(' ').toLowerCase();

      return title.includes(q) || tagline.includes(q) || desc.includes(q) || tools.includes(q);
    });

    if (filtered.length === 0) {
      grid.innerHTML = `
        <div style="grid-column: 1 / -1; text-align: center; padding: 4rem 1rem; color: var(--text-muted);">
          <p style="font-size: 1.2rem; margin-bottom: 0.5rem;">🔍 ${isAr ? 'لم يتم العثور على مشاريع تطابق البحث' : 'No projects found matching your search'}</p>
          <p style="font-size: 0.9rem;">${isAr ? 'جرب البحث بكلمات أخرى أو اختر تصنيفاً مختلفاً' : 'Try searching for other keywords or select a different category'}</p>
        </div>
      `;
      return;
    }

    grid.innerHTML = filtered.map(p => {
      const title = p.title[currentLang];
      const tagline = p.tagline[currentLang];
      const catName = p.category[currentLang];
      const badge = p.badge ? p.badge[currentLang] : '';
      const cover = p.coverImage || 'WhatsApp Image 2026-10-23 at 10.43.44 PM.jpeg';

      return `
        <article class="project-card" data-id="${p.id}">
          <div class="card-media-wrap">
            <img src="${cover}" alt="${title}" class="card-media-img" loading="lazy">
            ${badge ? `<span class="card-badge">${badge}</span>` : ''}
            <div class="card-quick-actions">
              <button class="quick-action-btn" title="${isAr ? 'استعراض المشروع' : 'Explore Project'}">
                👁️
              </button>
            </div>
          </div>
          <div class="card-content">
            <span class="card-category">${catName}</span>
            <h3 class="card-title">${title}</h3>
            <p class="card-tagline">${tagline}</p>
            <div class="card-tools">
              ${p.tools.slice(0, 4).map(t => `<span class="tool-tag">${t}</span>`).join('')}
              ${p.tools.length > 4 ? `<span class="tool-tag">+${p.tools.length - 4}</span>` : ''}
            </div>
          </div>
        </article>
      `;
    }).join('');

    // Attach card click handlers
    grid.querySelectorAll('.project-card').forEach(card => {
      card.addEventListener('click', () => {
        const pid = card.getAttribute('data-id');
        openProjectModal(pid);
      });
    });
  }

  // ------------------------------------------------------------------------
  // Project Details Modal & Live Interactive Exploration
  // ------------------------------------------------------------------------
  function openProjectModal(projectId) {
    activeProjectId = projectId;
    const proj = window.PORTFOLIO_DATA.projects.find(p => p.id === projectId);
    if (!proj) return;

    const modal = document.getElementById('project-modal');
    if (!modal) return;

    const isAr = currentLang === 'ar';
    const title = proj.title[currentLang];
    const catName = proj.category[currentLang];
    const desc = proj.description[currentLang];
    const highlights = proj.highlights ? proj.highlights[currentLang] : [];

    // Header info
    document.getElementById('modal-project-title').textContent = title;
    document.getElementById('modal-project-category').textContent = catName;

    // Categorize project files
    const spreadsheets = proj.files.filter(f => f.ext === '.xlsx' || f.ext === '.ods');
    const docxDocs = proj.files.filter(f => f.ext === '.docx');
    const pdfs = proj.files.filter(f => f.ext === '.pdf');
    const videos = proj.files.filter(f => f.ext === '.mp4');
    const psdFiles = proj.files.filter(f => f.ext === '.psd');
    const imageFiles = proj.files.filter(f => ['.png', '.jpg', '.jpeg'].includes(f.ext));

    let activeTab = 'overview';

    function renderModalBody() {
      const body = document.getElementById('modal-body-content');
      if (!body) return;

      if (activeTab === 'overview') {
        body.innerHTML = `
          <div style="display:flex; flex-direction:column; gap:2rem;">
            <div>
              <h4 style="color:var(--accent-cyan); font-size:1.1rem; margin-bottom:0.75rem;">
                📌 ${isAr ? 'نظرة عامة على المشروع' : 'Project Overview'}
              </h4>
              <p style="font-size:1.05rem; line-height:1.75; color:var(--text-secondary);">${desc}</p>
            </div>

            ${highlights && highlights.length > 0 ? `
              <div>
                <h4 style="color:var(--accent-blue); font-size:1.1rem; margin-bottom:0.75rem;">
                  ✨ ${isAr ? 'أبرز الإنجازات والخصائص' : 'Key Highlights & Achievements'}
                </h4>
                <div style="display:grid; grid-template-columns:repeat(auto-fill, minmax(280px, 1fr)); gap:1rem;">
                  ${highlights.map(h => `
                    <div style="background:rgba(255,255,255,0.03); border:1px solid var(--border-subtle); padding:0.85rem 1.15rem; border-radius:var(--radius-md);">
                      <strong style="color:var(--accent-cyan); display:block; margin-bottom:0.25rem;">▹ ${h}</strong>
                    </div>
                  `).join('')}
                </div>
              </div>
            ` : ''}

            <div>
              <h4 style="color:var(--accent-violet); font-size:1.1rem; margin-bottom:0.75rem;">
                🛠️ ${isAr ? 'المهارات والتقنيات المستخدمة' : 'Tools & Competencies'}
              </h4>
              <div style="display:flex; flex-wrap:wrap; gap:0.5rem;">
                ${proj.tools.map(t => `<span class="skill-badge">${t}</span>`).join('')}
              </div>
            </div>

            ${imageFiles.length > 0 ? `
              <div>
                <h4 style="color:var(--accent-cyan); font-size:1.1rem; margin-bottom:1rem;">
                  🎨 ${isAr ? 'معرض التصاميم والآرت بورد' : 'Visual Designs & Artboards'} (${imageFiles.length})
                </h4>
                <div style="display:grid; grid-template-columns:repeat(auto-fill, minmax(180px, 1fr)); gap:1rem;">
                  ${imageFiles.slice(0, 12).map(img => `
                    <div class="glass-panel" style="overflow:hidden; cursor:pointer;" onclick="window.portfolioViewer.openImageLightbox('${img.path}')">
                      <img src="${img.path}" alt="${img.filename}" style="width:100%; height:160px; object-fit:cover;" loading="lazy">
                      <div style="padding:0.5rem; font-size:0.72rem; color:var(--text-muted); white-space:nowrap; overflow:hidden; text-overflow:ellipsis;">
                        ${img.filename}
                      </div>
                    </div>
                  `).join('')}
                </div>
              </div>
            ` : ''}
          </div>
        `;
      } else if (activeTab === 'interactive') {
        body.innerHTML = `<div id="interactive-preview-mount"></div>`;
        const mount = document.getElementById('interactive-preview-mount');

        if (spreadsheets.length > 0) {
          window.portfolioViewer.renderSpreadsheet(mount, spreadsheets[0].path);
        } else if (videos.length > 0) {
          const scriptFile = docxDocs.length > 0 ? docxDocs[0].path : null;
          window.portfolioViewer.renderVideo(mount, videos[0].path, scriptFile);
        } else if (docxDocs.length > 0) {
          window.portfolioViewer.renderDocument(mount, docxDocs[0].path);
        } else if (pdfs.length > 0) {
          window.portfolioViewer.renderPdf(mount, pdfs[0].path);
        } else if (psdFiles.length > 0) {
          window.portfolioViewer.renderPsdGallery(mount, psdFiles);
        } else {
          mount.innerHTML = `<p class="empty-state">${isAr ? 'لا تتوفر معاينة تفاعلية لهذا المشروع' : 'No interactive previews available'}</p>`;
        }
      } else if (activeTab === 'files') {
        body.innerHTML = `
          <div>
            <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:1.5rem;">
              <h4 style="font-size:1.1rem; color:var(--accent-cyan);">
                📁 ${isAr ? `إجمالي الملفات المرتبطة: ${proj.files.length} ملف` : `Total Associated Files: ${proj.files.length}`}
              </h4>
            </div>
            <div class="table-container">
              <table class="interactive-table">
                <thead>
                  <tr>
                    <th>${isAr ? 'اسم الملف' : 'Filename'}</th>
                    <th>${isAr ? 'النوع' : 'Extension'}</th>
                    <th>${isAr ? 'الحجم' : 'Size'}</th>
                    <th>${isAr ? 'الإجراء' : 'Action'}</th>
                  </tr>
                </thead>
                <tbody>
                  ${proj.files.map(f => `
                    <tr>
                      <td style="font-weight:600; color:var(--text-primary);">${f.filename}</td>
                      <td><span class="tool-tag">${f.ext}</span></td>
                      <td style="color:var(--text-muted); font-size:0.8rem;">${f.size_formatted}</td>
                      <td>
                        <a href="${f.path}" download class="btn btn-sm btn-secondary" style="padding:0.25rem 0.65rem; font-size:0.75rem;">
                          📥 ${isAr ? 'تحميل' : 'Download'}
                        </a>
                      </td>
                    </tr>
                  `).join('')}
                </tbody>
              </table>
            </div>
          </div>
        `;
      }
    }

    // Modal tabs listeners
    const modalTabs = document.querySelectorAll('.modal-tab-btn');
    modalTabs.forEach(t => {
      t.classList.remove('active');
      if (t.getAttribute('data-tab') === 'overview') t.classList.add('active');

      t.onclick = () => {
        modalTabs.forEach(b => b.classList.remove('active'));
        t.classList.add('active');
        activeTab = t.getAttribute('data-tab');
        renderModalBody();
      };
    });

    renderModalBody();
    modal.classList.add('active');
  }

  // ------------------------------------------------------------------------
  // Full 265-File Repository Explorer
  // ------------------------------------------------------------------------
  function renderInventoryExplorer() {
    const explorerCont = document.getElementById('repository-explorer-container');
    if (!explorerCont) return;

    const inventory = window.PORTFOLIO_DATA.inventory;
    const isAr = currentLang === 'ar';
    let invSearch = '';
    let extFilter = 'all';

    function renderTable() {
      let filtered = inventory.filter(f => {
        if (extFilter !== 'all' && f.ext !== extFilter) return false;
        if (invSearch.trim() && !f.filename.toLowerCase().includes(invSearch.toLowerCase())) return false;
        return true;
      });

      explorerCont.innerHTML = `
        <div class="inventory-explorer">
          <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:1.5rem; flex-wrap:wrap; gap:1rem;">
            <div>
              <h3 style="font-size:1.4rem; font-weight:700; margin-bottom:0.35rem;">
                🗂️ ${isAr ? 'مستكشف ملفات المستودع الشامل (265 ملفاً موثقاً)' : 'Complete Repository File Explorer (265 Files)'}
              </h3>
              <p style="font-size:0.88rem; color:var(--text-muted);">
                ${isAr ? 'فحص كامل وشامل لجميع ملفات المشاريع دون تعديل أو حذف للأصول الأصلية' : 'Full recursive scan of all repository assets preserved with original integrity'}
              </p>
            </div>
            <div style="display:flex; gap:0.75rem; flex-wrap:wrap;">
              <input type="text" id="inv-search-inp" class="sheet-search-input" placeholder="${isAr ? 'ابحث عن أي ملف بالاسم...' : 'Search any file by name...'}" value="${invSearch}">
              <select id="inv-ext-select" class="sheet-search-input" style="min-width:130px; cursor:pointer;">
                <option value="all">${isAr ? 'كل الامتدادات' : 'All Extensions'}</option>
                <option value=".xlsx" ${extFilter === '.xlsx' ? 'selected' : ''}>.xlsx (Excel)</option>
                <option value=".docx" ${extFilter === '.docx' ? 'selected' : ''}>.docx (Word)</option>
                <option value=".pdf" ${extFilter === '.pdf' ? 'selected' : ''}>.pdf (PDFs)</option>
                <option value=".mp4" ${extFilter === '.mp4' ? 'selected' : ''}>.mp4 (Videos)</option>
                <option value=".psd" ${extFilter === '.psd' ? 'selected' : ''}>.psd (Photoshop)</option>
                <option value=".png" ${extFilter === '.png' ? 'selected' : ''}>.png (Artboards)</option>
                <option value=".jpg" ${extFilter === '.jpg' ? 'selected' : ''}>.jpg</option>
                <option value=".ods" ${extFilter === '.ods' ? 'selected' : ''}>.ods (Calc)</option>
              </select>
            </div>
          </div>

          <div style="font-size:0.85rem; color:var(--accent-cyan); margin-bottom:1rem;">
            ${isAr ? `المعروض حالياً: ${filtered.length} من أصل 265 ملفاً` : `Showing ${filtered.length} of 265 files`}
          </div>

          <div class="table-container" style="max-height:460px;">
            <table class="interactive-table">
              <thead>
                <tr>
                  <th style="width:40px;">#</th>
                  <th>${isAr ? 'اسم الملف' : 'Filename'}</th>
                  <th>${isAr ? 'التصنيف' : 'Category'}</th>
                  <th>${isAr ? 'الامتداد' : 'Type'}</th>
                  <th>${isAr ? 'الحجم' : 'Size'}</th>
                  <th>${isAr ? 'المعاينة والتحميل' : 'Preview & Download'}</th>
                </tr>
              </thead>
              <tbody>
                ${filtered.map((item, idx) => `
                  <tr>
                    <td style="color:var(--text-dim); font-size:0.75rem;">${idx + 1}</td>
                    <td style="font-weight:600; color:var(--text-primary); max-width:280px; overflow:hidden; text-overflow:ellipsis; white-space:nowrap;" title="${item.filename}">
                      ${item.filename}
                    </td>
                    <td><span class="tool-tag" style="font-size:0.7rem;">${item.category}</span></td>
                    <td><span class="plan-status" style="font-size:0.7rem;">${item.ext}</span></td>
                    <td style="color:var(--text-muted); font-size:0.8rem;">${item.size_formatted}</td>
                    <td>
                      <div style="display:flex; gap:0.4rem;">
                        ${item.preview_image ? `
                          <button class="btn btn-sm btn-secondary" style="padding:0.2rem 0.5rem; font-size:0.72rem;" onclick="window.portfolioViewer.openImageLightbox('${item.preview_image}')">
                            👁️ ${isAr ? 'معاينة' : 'Preview'}
                          </button>
                        ` : ''}
                        <a href="${item.path}" download class="btn btn-sm btn-secondary" style="padding:0.2rem 0.5rem; font-size:0.72rem;">
                          📥 ${isAr ? 'تحميل' : 'Download'}
                        </a>
                      </div>
                    </td>
                  </tr>
                `).join('')}
              </tbody>
            </table>
          </div>
        </div>
      `;

      // Listeners
      const sInp = explorerCont.querySelector('#inv-search-inp');
      if (sInp) {
        sInp.addEventListener('input', (e) => {
          invSearch = e.target.value;
          renderTable();
          const newS = explorerCont.querySelector('#inv-search-inp');
          if (newS) {
            newS.focus();
            newS.selectionStart = newS.selectionEnd = newS.value.length;
          }
        });
      }

      const sExt = explorerCont.querySelector('#inv-ext-select');
      if (sExt) {
        sExt.addEventListener('change', (e) => {
          extFilter = e.target.value;
          renderTable();
        });
      }
    }

    renderTable();
  }

  // ------------------------------------------------------------------------
  // About & Experience Section
  // ------------------------------------------------------------------------
  function renderAboutSection() {
    const p = window.PORTFOLIO_DATA.profile;
    const isAr = currentLang === 'ar';

    const expTimeline = document.getElementById('experience-timeline');
    if (expTimeline && p.experience) {
      expTimeline.innerHTML = p.experience.map(exp => `
        <div class="timeline-item">
          <div class="timeline-dot"></div>
          <div class="timeline-role">${exp.role[currentLang]}</div>
          <div class="timeline-company">${exp.company[currentLang]} • <span style="color:var(--text-muted); font-size:0.85rem;">${exp.location[currentLang]} (${exp.period[currentLang]})</span></div>
          <ul class="timeline-points">
            ${exp.points[currentLang].map(pt => `<li>${pt}</li>`).join('')}
          </ul>
        </div>
      `).join('');
    }

    const skillsGrid = document.getElementById('core-skills-grid');
    if (skillsGrid && p.skills) {
      skillsGrid.innerHTML = p.skills.core.map(s => `
        <span class="skill-badge">${s[currentLang]}</span>
      `).join('');
    }

    const toolsGrid = document.getElementById('tech-tools-grid');
    if (toolsGrid && p.skills) {
      toolsGrid.innerHTML = p.skills.tools.map(t => `
        <span class="skill-badge" style="border-color:var(--border-accent); color:var(--accent-cyan);">${t}</span>
      `).join('');
    }

    // Education
    const eduEl = document.getElementById('about-education');
    if (eduEl) eduEl.textContent = p.education[currentLang];
  }

  // ------------------------------------------------------------------------
  // General Event Listeners
  // ------------------------------------------------------------------------
  function setupEventListeners() {
    // Search input
    const searchInput = document.getElementById('main-project-search');
    if (searchInput) {
      searchInput.addEventListener('input', (e) => {
        searchQuery = e.target.value;
        renderProjects();
      });
    }

    // Modal Close
    const closeBtn = document.getElementById('modal-close-btn');
    const modal = document.getElementById('project-modal');
    if (closeBtn && modal) {
      closeBtn.addEventListener('click', () => {
        modal.classList.remove('active');
        activeProjectId = null;
      });
      modal.addEventListener('click', (e) => {
        if (e.target === modal) {
          modal.classList.remove('active');
          activeProjectId = null;
        }
      });
    }

    // Lightbox Close
    const lightbox = document.getElementById('image-lightbox');
    const lbClose = document.getElementById('lightbox-close-btn');
    if (lightbox && lbClose) {
      lbClose.addEventListener('click', () => lightbox.classList.remove('active'));
      lightbox.addEventListener('click', (e) => {
        if (e.target === lightbox) lightbox.classList.remove('active');
      });
    }

    // Mobile Menu
    const mobileMenuBtn = document.getElementById('mobile-menu-btn');
    const navMenu = document.getElementById('nav-menu');
    if (mobileMenuBtn && navMenu) {
      mobileMenuBtn.addEventListener('click', () => {
        const isShown = navMenu.style.display === 'flex';
        navMenu.style.display = isShown ? 'none' : 'flex';
      });
    }

    // Escape key closes modals
    document.addEventListener('keydown', (e) => {
      if (e.key === 'Escape') {
        if (modal) modal.classList.remove('active');
        if (lightbox) lightbox.classList.remove('active');
      }
    });
  }

  // ------------------------------------------------------------------------
  // Smooth Animated Number Counters
  // ------------------------------------------------------------------------
  function setupCounters() {
    const observer = new IntersectionObserver((entries) => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          const el = entry.target;
          const target = parseInt(el.getAttribute('data-target') || '0', 10);
          if (target > 0) {
            animateNumber(el, target);
          }
          observer.unobserve(el);
        }
      });
    }, { threshold: 0.5 });

    document.querySelectorAll('.metric-number').forEach(el => observer.observe(el));
  }

  function animateNumber(el, target) {
    const duration = 1600;
    const start = 0;
    const startTime = performance.now();
    const suffix = el.textContent.replace(/[0-9]/g, '');

    function update(now) {
      const elapsed = now - startTime;
      const progress = Math.min(elapsed / duration, 1);
      const ease = 1 - Math.pow(1 - progress, 3);
      const current = Math.floor(start + (target - start) * ease);
      el.textContent = current + suffix;
      if (progress < 1) requestAnimationFrame(update);
    }

    requestAnimationFrame(update);
  }

  // ------------------------------------------------------------------------
  // Animated Interactive Canvas Background
  // ------------------------------------------------------------------------
  function initCanvas() {
    const canvas = document.getElementById('ambient-canvas');
    if (!canvas) return;

    const ctx = canvas.getContext('2d');
    let width = canvas.width = window.innerWidth;
    let height = canvas.height = window.innerHeight;

    window.addEventListener('resize', () => {
      width = canvas.width = window.innerWidth;
      height = canvas.height = window.innerHeight;
    });

    const particles = [];
    const count = Math.min(50, Math.floor(width / 30));

    for (let i = 0; i < count; i++) {
      particles.push({
        x: Math.random() * width,
        y: Math.random() * height,
        vx: (Math.random() - 0.5) * 0.45,
        vy: (Math.random() - 0.5) * 0.45,
        radius: Math.random() * 2 + 1,
        alpha: Math.random() * 0.5 + 0.2
      });
    }

    function loop() {
      ctx.clearRect(0, 0, width, height);

      // Draw subtle connections
      for (let i = 0; i < particles.length; i++) {
        const p1 = particles[i];
        p1.x += p1.vx;
        p1.y += p1.vy;

        if (p1.x < 0) p1.x = width;
        if (p1.x > width) p1.x = 0;
        if (p1.y < 0) p1.y = height;
        if (p1.y > height) p1.y = 0;

        ctx.fillStyle = `rgba(0, 240, 255, ${p1.alpha * 0.6})`;
        ctx.beginPath();
        ctx.arc(p1.x, p1.y, p1.radius, 0, Math.PI * 2);
        ctx.fill();

        for (let j = i + 1; j < particles.length; j++) {
          const p2 = particles[j];
          const dist = Math.hypot(p1.x - p2.x, p1.y - p2.y);
          if (dist < 130) {
            ctx.strokeStyle = `rgba(59, 130, 246, ${0.12 * (1 - dist / 130)})`;
            ctx.lineWidth = 0.8;
            ctx.beginPath();
            ctx.moveTo(p1.x, p1.y);
            ctx.lineTo(p2.x, p2.y);
            ctx.stroke();
          }
        }
      }

      requestAnimationFrame(loop);
    }

    loop();
  }

})();
