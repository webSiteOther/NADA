import os
import sys
import json
import zipfile
import xml.etree.ElementTree as ET
import openpyxl
import docx
import pypdf
from PIL import Image

sys.stdout.reconfigure(encoding='utf-8')

ROOT_DIR = '.'

def read_ods(filepath):
    try:
        with zipfile.ZipFile(filepath, 'r') as z:
            content = z.read('content.xml')
            root = ET.fromstring(content)
            sheets = {}
            for table in root.iter('{urn:oasis:names:tc:opendocument:xmlns:table:1.0}table'):
                tname = table.attrib.get('{urn:oasis:names:tc:opendocument:xmlns:table:1.0}name', 'Sheet1')
                rows = []
                for tr in table.iter('{urn:oasis:names:tc:opendocument:xmlns:table:1.0}table-row'):
                    row_cells = []
                    for tc in tr.iter('{urn:oasis:names:tc:opendocument:xmlns:table:1.0}table-cell'):
                        txt = ''.join(tc.itertext()).strip()
                        rep = int(tc.attrib.get('{urn:oasis:names:tc:opendocument:xmlns:table:1.0}number-columns-repeated', 1))
                        if rep > 25:
                            continue
                        for _ in range(rep):
                            row_cells.append(txt)
                    # Check if row has any non-empty cell
                    if any(c != '' for c in row_cells):
                        rows.append(row_cells)
                if rows:
                    sheets[tname] = rows
            return sheets
    except Exception as e:
        print(f"Error reading ODS {filepath}: {e}")
        return {}

def read_xlsx(filepath):
    try:
        wb = openpyxl.load_workbook(filepath, data_only=True)
        sheets = {}
        for sname in wb.sheetnames:
            ws = wb[sname]
            rows = []
            for r in range(1, min(ws.max_row + 1, 200)): # Max 200 rows per sheet for web perf
                row_vals = []
                for c in range(1, min(ws.max_column + 1, 30)):
                    val = ws.cell(r, c).value
                    row_vals.append('' if val is None else str(val).strip())
                if any(v != '' for v in row_vals):
                    rows.append(row_vals)
            if rows:
                sheets[sname] = rows
        return sheets
    except Exception as e:
        print(f"Error reading XLSX {filepath}: {e}")
        return {}

def read_docx(filepath):
    try:
        doc = docx.Document(filepath)
        paragraphs = []
        for p in doc.paragraphs:
            txt = p.text.strip()
            if txt:
                paragraphs.append({
                    "text": txt,
                    "style": p.style.name if p.style else "Normal"
                })
        return paragraphs
    except Exception as e:
        print(f"Error reading DOCX {filepath}: {e}")
        return []

def read_pdf(filepath):
    try:
        reader = pypdf.PdfReader(filepath)
        pages = []
        for i, page in enumerate(reader.pages):
            pages.append({
                "page": i + 1,
                "text": (page.extract_text() or '').strip()
            })
        return pages
    except Exception as e:
        print(f"Error reading PDF {filepath}: {e}")
        return []

def get_file_info(full_path):
    rel_path = os.path.relpath(full_path, ROOT_DIR).replace('\\', '/')
    filename = os.path.basename(full_path)
    ext = os.path.splitext(filename)[1].lower()
    size = os.path.getsize(full_path)
    
    # Formatted size
    if size < 1024:
        fsize = f"{size} B"
    elif size < 1024 * 1024:
        fsize = f"{size / 1024:.1f} KB"
    else:
        fsize = f"{size / (1024*1024):.2f} MB"
        
    return {
        "filename": filename,
        "path": rel_path,
        "ext": ext,
        "size_bytes": size,
        "size_formatted": fsize
    }

def main():
    all_files = []
    
    for dirpath, dirnames, filenames in os.walk(ROOT_DIR):
        # Skip node_modules, .git, etc.
        if 'node_modules' in dirpath or '.git' in dirpath or 'assets\\previews' in dirpath or 'assets/previews' in dirpath or 'assets\\audio' in dirpath or 'assets/audio' in dirpath:
            continue
        for f in filenames:
            full = os.path.join(dirpath, f)
            all_files.append(full)
            
    print(f"Discovered {len(all_files)} raw files in project folder.")
    
    # Process PSD previews map
    psd_previews = {}
    psd_preview_dir = os.path.join('assets', 'previews', 'psd')
    if os.path.exists(psd_preview_dir):
        for f in os.listdir(psd_preview_dir):
            if f.endswith('.webp'):
                psd_previews[f] = f"assets/previews/psd/{f}"

    # Extract contents for documents
    spreadsheets_data = {}
    documents_data = {}
    pdf_data = {}
    
    file_inventory = []
    
    for fpath in all_files:
        info = get_file_info(fpath)
        ext = info["ext"]
        rel = info["path"]
        
        # Categorize
        cat = "Other"
        proj_id = "general"
        
        if "01_Content_Plans" in rel:
            cat = "Content Plans"
            if "السيف" in rel:
                proj_id = "al_saif"
            elif "اللؤلؤه" in rel:
                proj_id = "al_loloa"
            elif "المركز المصري السعودي" in rel:
                proj_id = "egyptian_saudi_center"
            elif "اور" in rel:
                proj_id = "our_retail"
            elif "بلاتنيوم" in rel:
                proj_id = "platinum"
            elif "تهنئات اكتوبر" in rel:
                proj_id = "october_greetings"
            elif "توب لاند" in rel:
                proj_id = "top_land"
            elif "د.الملا" in rel:
                proj_id = "dr_mulla"
            elif "د.هادي" in rel:
                proj_id = "dr_hady"
            elif "رحال" in rel:
                proj_id = "rahhal"
            elif "مستشفي الزهراء" in rel:
                proj_id = "al_zahraa_hospital"
        elif "02_Campaigns" in rel:
            cat = "Campaigns"
            if "campaign El Mansour 6" in rel:
                proj_id = "al_mansour_6"
            elif "campaign med guide" in rel:
                proj_id = "med_guide"
            elif "campaign rashed" in rel:
                proj_id = "koshary_rashed"
            elif "campaign tameem" in rel:
                proj_id = "tameem"
        elif "designs" in rel:
            cat = "Creative Design"
            if "المركز العلمي" in rel:
                proj_id = "scientific_center_designs"
            elif "معمل الفا كير" in rel:
                proj_id = "alpha_care"
        elif "اسكريبتات لفيديوهات واخراج" in rel:
            cat = "Video Production & Direction"
            proj_id = "video_production"
        elif info["filename"].startswith("NADA NASSER MOHAMED"):
            cat = "Professional Profile"
            proj_id = "nada_profile"
        elif info["filename"].startswith("WhatsApp Image"):
            cat = "Professional Profile"
            proj_id = "nada_profile"
            
        info["category"] = cat
        info["project_id"] = proj_id
        
        # Parse content where appropriate
        if ext == '.xlsx':
            info["preview_type"] = "interactive_spreadsheet"
            sheets = read_xlsx(fpath)
            spreadsheets_data[rel] = {
                "filename": info["filename"],
                "path": rel,
                "sheets": sheets
            }
        elif ext == '.ods':
            info["preview_type"] = "interactive_spreadsheet"
            sheets = read_ods(fpath)
            spreadsheets_data[rel] = {
                "filename": info["filename"],
                "path": rel,
                "sheets": sheets
            }
        elif ext == '.docx':
            info["preview_type"] = "formatted_document"
            paragraphs = read_docx(fpath)
            documents_data[rel] = {
                "filename": info["filename"],
                "path": rel,
                "paragraphs": paragraphs
            }
        elif ext == '.pdf':
            info["preview_type"] = "pdf_reader"
            pages = read_pdf(fpath)
            pdf_data[rel] = {
                "filename": info["filename"],
                "path": rel,
                "num_pages": len(pages),
                "pages": pages
            }
        elif ext in ['.png', '.jpg', '.jpeg']:
            info["preview_type"] = "image_gallery"
        elif ext == '.mp4':
            info["preview_type"] = "video_player"
        elif ext == '.psd':
            info["preview_type"] = "psd_preview"
            # match webp
            base = os.path.splitext(info["filename"])[0]
            clean_name = base.replace(' ', '_').replace(',', '').replace('(', '').replace(')', '') + '.webp'
            if clean_name in psd_previews:
                info["preview_image"] = psd_previews[clean_name]
        elif ext == '.zip':
            info["preview_type"] = "zip_archive"
            
        file_inventory.append(info)
        
    print(f"Total inventory items processed: {len(file_inventory)}")
    print(f"Spreadsheets with live data: {len(spreadsheets_data)}")
    print(f"DOCX documents with live text: {len(documents_data)}")
    print(f"PDFs with extracted text: {len(pdf_data)}")
    
    # Save full inventory JSON
    inv_path = os.path.join('data', 'portfolio-inventory.json')
    with open(inv_path, 'w', encoding='utf-8') as f:
        json.dump(file_inventory, f, ensure_ascii=False, indent=2)
    print(f"Saved {inv_path}")
    
    # Save live extracted data
    extracted_path = os.path.join('data', 'extracted-content.json')
    with open(extracted_path, 'w', encoding='utf-8') as f:
        json.dump({
            "spreadsheets": spreadsheets_data,
            "documents": documents_data,
            "pdfs": pdf_data
        }, f, ensure_ascii=False, indent=2)
    print(f"Saved {extracted_path}")

if __name__ == '__main__':
    main()
