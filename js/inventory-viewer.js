// ==========================================================================
// Interactive Project Viewers & Renderers
// Renders live Excel/ODS tables, DOCX script readers, PDF viewers,
// MP4 video player, and PSD galleries directly inside the portfolio.
// ==========================================================================

(function() {
  function getLang() {
    return document.documentElement.getAttribute('lang') || 'en';
  }

  // ------------------------------------------------------------------------
  // 1. Spreadsheet Viewer (Excel & ODS)
  // ------------------------------------------------------------------------
  function renderSpreadsheet(container, filePath) {
    const data = window.PORTFOLIO_DATA.extractedContent.spreadsheets[filePath];
    if (!data || !data.sheets || Object.keys(data.sheets).length === 0) {
      container.innerHTML = `<div class="empty-state">${getLang() === 'ar' ? 'لا تتوفر بيانات لعرض هذا الجدول' : 'No previewable data found for this spreadsheet'}</div>`;
      return;
    }

    const sheetNames = Object.keys(data.sheets);
    let activeSheet = sheetNames[0];
    let currentMode = 'table'; // 'table' or 'cards'
    let searchQuery = '';

    function render() {
      const rows = data.sheets[activeSheet] || [];
      const headers = rows.length > 0 ? rows[0] : [];
      let bodyRows = rows.length > 1 ? rows.slice(1) : [];

      // Filter rows by search
      if (searchQuery.trim()) {
        const q = searchQuery.toLowerCase();
        bodyRows = bodyRows.filter(row => row.some(cell => String(cell).toLowerCase().includes(q)));
      }

      // Check if this looks like a Social Media Content Plan
      const hasPlanHeaders = headers.some(h => {
        const lh = String(h).toLowerCase();
        return lh.includes('idea') || lh.includes('caption') || lh.includes('design') || lh.includes('كابشن') || lh.includes('فكرة');
      });

      const isAr = getLang() === 'ar';

      let html = `
        <div class="spreadsheet-viewer">
          <!-- Sheet Selector Tabs -->
          <div class="sheet-selector-tabs">
            ${sheetNames.map(name => `
              <button class="sheet-tab-btn ${name === activeSheet ? 'active' : ''}" data-sheet="${name}">
                📊 ${name}
              </button>
            `).join('')}
          </div>

          <!-- Toolbar -->
          <div class="spreadsheet-toolbar">
            <input type="text" class="sheet-search-input" placeholder="${isAr ? 'ابحث في الصفوف والأعمدة...' : 'Search rows and content...'}" value="${searchQuery}">
            <div class="view-mode-toggle">
              <button class="view-mode-btn ${currentMode === 'table' ? 'active' : ''}" data-mode="table">
                ${isAr ? 'عرض الجدول' : 'Table View'}
              </button>
              ${hasPlanHeaders ? `
                <button class="view-mode-btn ${currentMode === 'cards' ? 'active' : ''}" data-mode="cards">
                  ${isAr ? 'عرض الكروت الإعلانية' : 'Card View'}
                </button>
              ` : ''}
            </div>
            <a href="${filePath}" download class="btn btn-sm btn-secondary">
              📥 ${isAr ? 'تحميل الملف الأصلي' : 'Download File'}
            </a>
          </div>

          <div class="sheet-stats" style="font-size:0.8rem; color:var(--text-muted);">
            ${isAr ? `إجمالي النتائج المعروضة: ${bodyRows.length} صف` : `Displaying ${bodyRows.length} rows`}
          </div>

          <!-- Content View -->
          ${currentMode === 'table' ? renderTableView(headers, bodyRows) : renderCardView(headers, bodyRows)}
        </div>
      `;

      container.innerHTML = html;

      // Event Listeners
      container.querySelectorAll('.sheet-tab-btn').forEach(btn => {
        btn.addEventListener('click', () => {
          activeSheet = btn.getAttribute('data-sheet');
          render();
        });
      });

      container.querySelectorAll('.view-mode-btn').forEach(btn => {
        btn.addEventListener('click', () => {
          currentMode = btn.getAttribute('data-mode');
          render();
        });
      });

      const searchInput = container.querySelector('.sheet-search-input');
      if (searchInput) {
        searchInput.addEventListener('input', (e) => {
          searchQuery = e.target.value;
          render();
          const newInp = container.querySelector('.sheet-search-input');
          if (newInp) {
            newInp.focus();
            newInp.selectionStart = newInp.selectionEnd = newInp.value.length;
          }
        });
      }
    }

    function renderTableView(headers, bodyRows) {
      if (headers.length === 0) return '<p class="empty-state">Sheet is empty</p>';
      return `
        <div class="table-container">
          <table class="interactive-table">
            <thead>
              <tr>
                <th style="width:50px;">#</th>
                ${headers.map(h => `<th>${h || '-'}</th>`).join('')}
              </tr>
            </thead>
            <tbody>
              ${bodyRows.map((row, idx) => `
                <tr>
                  <td style="color:var(--text-dim); font-weight:600;">${idx + 1}</td>
                  ${headers.map((_, colIdx) => `<td>${(row[colIdx] || '').replace(/\\n/g, '<br>')}</td>`).join('')}
                </tr>
              `).join('')}
            </tbody>
          </table>
        </div>
      `;
    }

    function renderCardView(headers, bodyRows) {
      const isAr = getLang() === 'ar';
      // Map columns
      const colMap = {};
      headers.forEach((h, i) => {
        const lh = String(h).toLowerCase();
        if (lh.includes('idea') || lh.includes('فكرة')) colMap.idea = i;
        else if (lh.includes('aim') || lh.includes('هدف')) colMap.aim = i;
        else if (lh.includes('design') || lh.includes('تصميم')) colMap.design = i;
        else if (lh.includes('tov') || lh.includes('نبرة')) colMap.tov = i;
        else if (lh.includes('caption') || lh.includes('كابشن') || lh.includes('نص')) colMap.caption = i;
        else if (lh.includes('schedule') || lh.includes('تاريخ') || lh.includes('وقت')) colMap.time = i;
      });

      return `
        <div class="sheet-cards-grid">
          ${bodyRows.map((row, idx) => {
            const idea = colMap.idea !== undefined ? row[colMap.idea] : '';
            const aim = colMap.aim !== undefined ? row[colMap.aim] : '';
            const design = colMap.design !== undefined ? row[colMap.design] : '';
            const tov = colMap.tov !== undefined ? row[colMap.tov] : '';
            const caption = colMap.caption !== undefined ? row[colMap.caption] : '';
            const time = colMap.time !== undefined ? row[colMap.time] : '';

            return `
              <div class="post-plan-card">
                <div class="plan-card-header">
                  <span class="plan-number">Post #${idx + 1}</span>
                  ${time ? `<span class="plan-status">⏰ ${time}</span>` : ''}
                </div>
                ${idea ? `
                  <div class="plan-field">
                    <div class="plan-field-label">${isAr ? 'فكرة المنشور' : 'Core Idea'}</div>
                    <div class="plan-field-val" style="font-weight:600; color:var(--text-primary);">${idea}</div>
                  </div>
                ` : ''}
                ${aim ? `
                  <div class="plan-field">
                    <div class="plan-field-label">${isAr ? 'الهدف التسويقي' : 'Marketing Aim'}</div>
                    <div class="plan-field-val">${aim}</div>
                  </div>
                ` : ''}
                ${design ? `
                  <div class="plan-field">
                    <div class="plan-field-label">${isAr ? 'توجيهات التصميم (Design Brief)' : 'Visual Design Brief'}</div>
                    <div class="plan-field-val" style="font-style:italic; background:rgba(0,0,0,0.3); padding:0.5rem; border-radius:6px;">${design}</div>
                  </div>
                ` : ''}
                ${tov ? `
                  <div class="plan-field">
                    <div class="plan-field-label">${isAr ? 'نبرة الصوت (Tone of Voice)' : 'Tone of Voice'}</div>
                    <div class="plan-field-val" style="color:var(--accent-cyan);">${tov}</div>
                  </div>
                ` : ''}
                ${caption ? `
                  <div class="plan-field">
                    <div class="plan-field-label">${isAr ? 'الكابشن المكتوب (Social Caption)' : 'Written Caption'}</div>
                    <div class="plan-field-val" style="background:rgba(255,255,255,0.03); padding:0.6rem; border-radius:6px; border:1px solid var(--border-subtle);">${caption.replace(/\\n/g, '<br>')}</div>
                  </div>
                ` : ''}
              </div>
            `;
          }).join('')}
        </div>
      `;
    }

    render();
  }

  // ------------------------------------------------------------------------
  // 2. Document & Script Reader (Word DOCX)
  // ------------------------------------------------------------------------
  function renderDocument(container, filePath) {
    const data = window.PORTFOLIO_DATA.extractedContent.documents[filePath];
    const isAr = getLang() === 'ar';

    if (!data || !data.paragraphs || data.paragraphs.length === 0) {
      container.innerHTML = `<div class="empty-state">${isAr ? 'لا يوجد نص متاح لهذا المستند' : 'No document content available'}</div>`;
      return;
    }

    const paras = data.paragraphs;

    let html = `
      <div class="document-reader">
        <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:1.5rem; border-bottom:1px solid var(--border-subtle); padding-bottom:1rem;">
          <h4 style="color:var(--accent-cyan); font-size:1.15rem;">📄 ${data.filename}</h4>
          <a href="${filePath}" download class="btn btn-sm btn-secondary">
            📥 ${isAr ? 'تحميل المستند الأصلي' : 'Download DOCX'}
          </a>
        </div>
        <div class="document-content-flow">
    `;

    paras.forEach(p => {
      const text = p.text;
      if (text.includes('الهوك') || text.startsWith('العنوان:') || text.includes('فكرة التصميم')) {
        html += `
          <div class="script-hook-box">
            <strong>🎯 ${text}</strong>
          </div>
        `;
      } else if (text.includes('السكريبت') || text.includes('الكابشن:') || text.includes('جملة التصميم:')) {
        html += `
          <div style="margin: 1.25rem 0 0.5rem; color:var(--accent-cyan); font-weight:700;">
            ${text}
          </div>
        `;
      } else if (text.startsWith('الطالب') || text.startsWith('الصاحب') || text.startsWith('يرد') || text.startsWith('يدخل')) {
        html += `
          <div class="script-dialogue">
            <div class="script-speaker">${text.split(':')[0]}</div>
            <div class="script-line">${text.includes(':') ? text.substring(text.indexOf(':') + 1) : text}</div>
          </div>
        `;
      } else {
        html += `<p style="margin-bottom:1rem; color:var(--text-secondary);">${text.replace(/\\n/g, '<br>')}</p>`;
      }
    });

    html += `
        </div>
      </div>
    `;

    container.innerHTML = html;
  }

  // ------------------------------------------------------------------------
  // 3. PDF Viewer & Reader
  // ------------------------------------------------------------------------
  function renderPdf(container, filePath) {
    const data = window.PORTFOLIO_DATA.extractedContent.pdfs[filePath];
    const isAr = getLang() === 'ar';

    let html = `
      <div class="pdf-reader-module">
        <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:1.25rem; flex-wrap:wrap; gap:1rem;">
          <div>
            <h4 style="color:var(--accent-cyan); font-size:1.15rem; margin-bottom:0.25rem;">📕 ${data ? data.filename : 'Document'}</h4>
            <span style="font-size:0.85rem; color:var(--text-muted);">${data ? `${data.num_pages} ${isAr ? 'صفحات موثقة' : 'pages'}` : ''}</span>
          </div>
          <div style="display:flex; gap:0.5rem;">
            <a href="${filePath}" target="_blank" class="btn btn-sm btn-primary">
              ↗️ ${isAr ? 'فتح بالحجم الكامل' : 'Open Full Screen'}
            </a>
            <a href="${filePath}" download class="btn btn-sm btn-secondary">
              📥 ${isAr ? 'تحميل ملف PDF' : 'Download PDF'}
            </a>
          </div>
        </div>

        <!-- Embedded Interactive PDF -->
        <div style="width:100%; height:550px; border-radius:var(--radius-md); overflow:hidden; border:1px solid var(--border-subtle); margin-bottom:1.5rem; background:#000;">
          <iframe src="${filePath}#toolbar=1" width="100%" height="100%" style="border:none;"></iframe>
        </div>

        ${data && data.pages && data.pages.length > 0 ? `
          <details style="background:rgba(14,22,40,0.6); padding:1rem 1.25rem; border-radius:var(--radius-md); border:1px solid var(--border-subtle);">
            <summary style="cursor:pointer; color:var(--accent-cyan); font-weight:600;">
              🔍 ${isAr ? 'عرض النص المستخرج للبحث السريع' : 'View Extracted Text for Fast Search'}
            </summary>
            <div style="margin-top:1rem; font-size:0.9rem; line-height:1.7; max-height:300px; overflow-y:auto; padding-right:0.5rem;">
              ${data.pages.map(p => `
                <div style="margin-bottom:1.5rem; border-bottom:1px solid var(--border-subtle); padding-bottom:1rem;">
                  <strong style="color:var(--accent-blue); display:block; margin-bottom:0.5rem;">Page ${p.page}</strong>
                  <p style="white-space:pre-line; color:var(--text-secondary);">${p.text}</p>
                </div>
              `).join('')}
            </div>
          </details>
        ` : ''}
      </div>
    `;

    container.innerHTML = html;
  }

  // ------------------------------------------------------------------------
  // 4. Video Player
  // ------------------------------------------------------------------------
  function renderVideo(container, videoPath, scriptDocPath) {
    const isAr = getLang() === 'ar';
    const filename = videoPath.split('/').pop();

    let html = `
      <div class="video-preview-module">
        <div class="video-player-wrap">
          <video controls preload="metadata" style="width:100%; border-radius:var(--radius-md);">
            <source src="${videoPath}" type="video/mp4">
            Your browser does not support the video tag.
          </video>
        </div>

        <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:1.5rem;">
          <div>
            <h4 style="font-size:1.15rem; color:var(--accent-cyan);">🎬 ${filename}</h4>
            <span style="font-size:0.85rem; color:var(--text-muted);">${isAr ? 'فيديو ترويجي أصلي بدقة عالية' : 'Original HD Production Video'}</span>
          </div>
          <a href="${videoPath}" download class="btn btn-sm btn-secondary">
            📥 ${isAr ? 'تحميل الفيديو' : 'Download Video'}
          </a>
        </div>

        ${scriptDocPath ? `<div id="attached-script-container"></div>` : ''}
      </div>
    `;

    container.innerHTML = html;

    if (scriptDocPath) {
      const scriptCont = container.querySelector('#attached-script-container');
      if (scriptCont) renderDocument(scriptCont, scriptDocPath);
    }
  }

  // ------------------------------------------------------------------------
  // 5. PSD Gallery Viewer
  // ------------------------------------------------------------------------
  function renderPsdGallery(container, psdFiles) {
    const isAr = getLang() === 'ar';

    let html = `
      <div class="psd-gallery-wrap">
        <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:1.25rem;">
          <p style="font-size:0.9rem; color:var(--text-muted);">
            ${isAr ? `معروض ${psdFiles.length} ملف فوتوشوب أصلي (PSD) بمعاينة فورية بصيغة WebP فائقة الدقة` : `Displaying ${psdFiles.length} layered Photoshop masterfiles with high-res WebP previews`}
          </p>
        </div>
        <div class="psd-grid">
          ${psdFiles.map(file => {
            const previewImg = file.preview_image || '';
            return `
              <div class="psd-thumb-card" data-img="${previewImg}" data-psd="${file.path}">
                <img src="${previewImg}" alt="${file.filename}" class="psd-thumb-img" loading="lazy">
                <div class="psd-thumb-footer">
                  <span class="psd-thumb-name" title="${file.filename}">${file.filename}</span>
                  <a href="${file.path}" download class="btn btn-sm btn-secondary" style="padding:0.25rem 0.5rem; font-size:0.75rem;" title="${isAr ? 'تحميل ملف PSD' : 'Download PSD'}">
                    PSD
                  </a>
                </div>
              </div>
            `;
          }).join('')}
        </div>
      </div>
    `;

    container.innerHTML = html;

    // Click to open in full lightbox
    container.querySelectorAll('.psd-thumb-card').forEach(card => {
      card.addEventListener('click', (e) => {
        if (e.target.tagName === 'A') return;
        const imgUrl = card.getAttribute('data-img');
        const psdUrl = card.getAttribute('data-psd');
        openImageLightbox(imgUrl, psdUrl);
      });
    });
  }

  // ------------------------------------------------------------------------
  // Lightbox for any image / artboard
  // ------------------------------------------------------------------------
  function openImageLightbox(imgUrl, downloadUrl) {
    const isAr = getLang() === 'ar';
    const lightbox = document.getElementById('image-lightbox');
    if (!lightbox) return;

    const imgEl = lightbox.querySelector('.lightbox-image');
    const dlBtn = lightbox.querySelector('.lightbox-download-btn');

    if (imgEl) imgEl.src = imgUrl;
    if (dlBtn) dlBtn.href = downloadUrl || imgUrl;

    lightbox.classList.add('active');
  }

  window.portfolioViewer = {
    renderSpreadsheet: renderSpreadsheet,
    renderDocument: renderDocument,
    renderPdf: renderPdf,
    renderVideo: renderVideo,
    renderPsdGallery: renderPsdGallery,
    openImageLightbox: openImageLightbox
  };
})();
