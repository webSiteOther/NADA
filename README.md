# Nada Nasser Mohamed — Premium Animated Bilingual Portfolio

> **Content Creator | Social Media Specialist | Marketing Coordinator**  
> Beni Suef, Egypt • 24 Pages Managed • 114K+ Video Views • 265 Original Portfolio Assets

An ultra-premium, responsive, animated, and interactive digital portfolio engineered directly from the complete project repository of **Nada Nasser Mohamed**. 

Designed with a high-end tech aesthetic (Deep Navy `#050811`, Electric Blue, Cyan, and Restrained Violet accents), complete bilingual English & Arabic RTL/LTR support, ambient background music with a live sound visualizer, and **in-browser live previews for all project file types** (Excel, ODS, Word DOCX, PDF, MP4 Video, PSD, and Artboard designs).

---

## 🌟 Key Highlights & Capabilities

### 1. In-Browser Live Interactive Previews (Zero External Redirects)
- **Interactive Spreadsheets (Excel `.xlsx` & `.ods`)**:
  - Live interactive data grid with real-time column/row search.
  - Multi-sheet tab switcher.
  - Toggle between **Table View** and **Card View** (specifically formatted for social media content plans showing Post Idea, Aim, Design Brief, Tone of Voice, and Caption side-by-side).
  - Original file download button.
- **Word Document & Script Reader (`.docx`)**:
  - Formatted editorial reader highlighting video hooks, scene cues, and character dialogue bubbles (e.g. Applied AI comedic script, Baccalaureate workshop dialogue, Al-Saif 80s retro briefs).
- **Embedded PDF Viewer (`.pdf`)**:
  - Full-screen multi-page PDF embed with page navigation, zoom, plus extracted full-text search drawer (e.g. Al-Mansour 22-page master deck, Tameem 8-page competition deck, official 4-page CV).
- **Native Video Player (`.mp4`)**:
  - HTML5 high-definition video player displaying original productions (such as the G-Math challenge, Scientific Center brand video, and Programming curriculum launch) paired with its director script.
- **Adobe Photoshop Masterfiles (`.psd`)**:
  - 23 layered PSD files rendered into crisp WebP previews with full-screen zoomable lightbox and original PSD download options.
- **Visual Design Galleries (`.png`, `.jpg`)**:
  - Over 200 high-resolution artboards, architectural renders, and promotional designs in responsive masonry galleries with lightbox inspection.

### 2. Full 265-File Repository Explorer
- A dedicated, searchable interactive table accounting for **every single one of the 265 discovered files**.
- Filter by extension (`.xlsx`, `.docx`, `.pdf`, `.mp4`, `.psd`, `.png`, `.jpg`, `.ods`, `.zip`).
- Real-time search by filename with file sizes and one-click preview/download.

### 3. Complete Bilingual Arabic & English Architecture
- **Instant Language Switcher (`EN | AR`)** in the navigation header.
- Full RTL (Right-to-Left) layout for Arabic and LTR for English.
- Optimized typography: **Cairo** for Arabic, **Outfit** and **Plus Jakarta Sans** for English.
- 100% translated UI, project descriptions, marketing aims, highlights, categories, and metrics.
- Preserves natural LTR direction for emails, phone numbers, file names, and technical terms.
- Remembers user preference across sessions.

### 4. Ambient Music & Audio Experience
- Subtle, calming ambient soundscape with gentle chords and warm pads.
- Custom navigation controls: Play/Pause, Mute/Unmute, and Volume Slider.
- Animated multi-bar audio visualizer pulsing dynamically to playback.
- Initialized paused to respect browser autoplay policies, with a tasteful invitation banner.
- **Smart Video Coordinator**: Automatically pauses ambient music when a project video starts playing so audio never clashes.
- Built-in Web Audio API synthesizer fallback ensuring 100% offline reliability.

### 5. Verified Professional Identity & Metrics
- All personal details, experience, metrics, and education strictly derived from **Nada's official CV and project documentation**:
  - **24+** Client Social Media Pages Managed across 7 industries.
  - **114,000+** Verified Video Views.
  - **265** Project Assets mapped and preserved.
  - **16** Content Calendars & Campaign Spreadsheets.
  - **7** Video Productions.
  - **23** Photoshop Masterfiles.
  - **Vice President**, Rally Society at Beni Suef University.
  - **Bachelor of Science (Zoology)**, Faculty of Science, Beni Suef University (Graduation: 2028).

---

## 📁 Repository Structure

```
d:\projects\nada\
│
├── index.html                           # Main portfolio application entry point
├── package.json                         # Node scripts for local serving and data rebuild
│
├── css\
│   └── styles.css                       # Design system, glassmorphism, responsive & RTL styles
│
├── js\
│   ├── app.js                           # Bilingual switcher, canvas background, project filters, modal
│   ├── audio-player.js                  # Ambient music controller, visualizer, volume & video pauses
│   └── inventory-viewer.js              # Live spreadsheet viewer, docx reader, PDF embed, PSD gallery
│
├── data\
│   ├── portfolio-database.js            # Unified JavaScript database (works via file:// and http://)
│   ├── portfolio-inventory.json         # Complete structured metadata for all 265 files
│   └── extracted-content.json          # Pre-parsed spreadsheets, docx paragraphs, and PDF texts
│
├── assets\
│   ├── audio\
│   │   └── ambient_calm.mp3             # Synthesized 60s loopable peaceful ambient soundtrack
│   └── previews\
│       └── psd\                         # 23 High-resolution WebP previews generated from PSDs
│
├── scripts\
│   ├── build_portfolio_data.py          # Scans repository, extracts XLSX, ODS, DOCX, and PDF text
│   └── build_full_database.py           # Compiles project metadata and bilingual translations
│
├── NADA NASSER MOHAMED con.pdf          # Official 4-page Curriculum Vitae (Untouched original)
├── WhatsApp Image 2026-10-23...jpeg     # Professional Portrait Photograph (Untouched original)
└── Nada_Portfolio\                      # Original project folder containing all 263 client files (Untouched)
```

---

## 🚀 How to Run the Portfolio Locally

### Option 1: Using Python (Recommended - No install needed)
Run the following command in the project directory:
```bash
python -m http.server 3000
```
Then open your browser at:
`http://localhost:3000`

### Option 2: Using Node.js / npm
```bash
npm start
```
or
```bash
npx serve -l 3000 .
```
Then navigate to:
`http://localhost:3000`

### Option 3: Direct File Opening
You can also directly double-click `index.html` to open it in Chrome, Edge, or Firefox! Because the dataset is bundled in `data/portfolio-database.js`, all interactive features, tables, scripts, audio, and galleries work without CORS blocks.

---

## 🌐 How to Deploy Online

### Deploying to GitHub Pages:
1. Push this directory to a GitHub repository.
2. Go to **Repository Settings** > **Pages**.
3. Under **Branch**, select `main` (or `master`) and folder `/ (root)`.
4. Click **Save**. Your portfolio will be live at `https://<username>.github.io/<repo>/`!

### Deploying to Vercel or Netlify:
- Drag and drop the `nada` folder into the Netlify dashboard or import via Vercel.
- Framework Preset: **Other / Static Site**.
- Build command: leave empty or `npm run build:data`.
- Output directory: `.` (root).

---

## 🧪 Verification & Quality Assurance Summary

| Test Category | Test Description | Result |
| :--- | :--- | :--- |
| **File Integrity** | Recursive check confirming all 265 original files remain untouched and unmodified | **PASSED (100%)** |
| **JavaScript Syntax** | Node.js syntax compilation of `app.js`, `audio-player.js`, `inventory-viewer.js`, and `portfolio-database.js` | **PASSED (Zero errors)** |
| **Local Server HTTP** | Status 200 verified on HTML, CSS, JS, Audio MP3, WebP previews, and original assets | **PASSED (Status 200)** |
| **Bilingual Toggle** | Seamless dynamic EN ↔ AR toggle, RTL/LTR layout switch, font family change without reload | **PASSED** |
| **Spreadsheet Viewer** | Multi-sheet tab switching, row search, Table View & Post Cards View, original file download | **PASSED** |
| **DOCX Script Reader** | Hook callout rendering, dialogue quotes, scene cues, and typography styling | **PASSED** |
| **PDF Viewer** | Embedded iframe viewing, extracted full-text search, direct download | **PASSED** |
| **PSD Galleries** | 23 WebP previews loaded with zoom lightbox and direct PSD download | **PASSED** |
| **Video Player** | Native HTML5 MP4 video playback with volume and script integration | **PASSED** |
| **Ambient Audio** | Ambient MP3 playback, visualizer pulse, volume slider, auto-pause on video play | **PASSED** |
| **Accessibility & Motion**| `prefers-reduced-motion` media queries, semantic HTML, visible focus states | **PASSED** |
