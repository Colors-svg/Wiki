import os
import re
import hashlib
import pymupdf

PDF_DIR = "fuentes_pdf"
OUTPUT_BASE = "docs/assets/figuras"

os.makedirs(OUTPUT_BASE, exist_ok=True)

# List all official PDFs (VI-GU-*, VI-IN-*)
pdf_files = sorted([f for f in os.listdir(PDF_DIR) if f.startswith("VI-") and f.endswith(".pdf")])
print(f"Total PDFs a procesar: {len(pdf_files)}")

global_extracted = 0

for pdf_name in pdf_files:
    doc_code = os.path.splitext(pdf_name)[0]
    pdf_path = os.path.join(PDF_DIR, pdf_name)
    doc_out_dir = os.path.join(OUTPUT_BASE, doc_code)
    os.makedirs(doc_out_dir, exist_ok=True)

    try:
        doc = pymupdf.open(pdf_path)
    except Exception as e:
        print(f"Error abriendo {pdf_name}: {e}")
        continue

    # First pass: find all header/logo images that repeat across multiple pages
    image_usage_count = {}
    for page in doc:
        seen_on_page = set()
        for img in page.get_images(full=True):
            xref = img[0]
            if xref not in seen_on_page:
                seen_on_page.add(xref)
                image_usage_count[xref] = image_usage_count.get(xref, 0) + 1

    # Any image appearing on more than 2 pages is likely header/footer/logo
    repetitive_xrefs = {xref for xref, count in image_usage_count.items() if count > 2}

    fig_idx = 1
    extracted_doc_count = 0

    for page_idx, page in enumerate(doc):
        image_list = page.get_images(full=True)
        for img_info in image_list:
            xref = img_info[0]

            # Skip header/footer/logos
            if xref in repetitive_xrefs:
                continue

            try:
                base_img = doc.extract_image(xref)
            except Exception:
                continue

            w = base_img["width"]
            h = base_img["height"]
            img_bytes = base_img["image"]

            # Filter tiny icons, bullets, or separators (less than 80px or tiny size)
            if w < 100 or h < 60 or len(img_bytes) < 1200:
                continue

            # Aspect ratio sanity check: skip very thin divider lines
            if w / h > 18 or h / w > 18:
                continue

            fig_filename = f"figura-{fig_idx:02d}.png"
            fig_path = os.path.join(doc_out_dir, fig_filename)

            with open(fig_path, "wb") as f_out:
                f_out.write(img_bytes)

            fig_idx += 1
            extracted_doc_count += 1
            global_extracted += 1

    print(f"[{doc_code}] Extraídas {extracted_doc_count} figuras.")

print(f"\nPROCESO COMPLETADO: {global_extracted} figuras extraídas en total.")
