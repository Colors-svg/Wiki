import os
import re
import pymupdf
from PIL import Image

PDF_DIR = "fuentes_pdf"
OUTPUT_BASE = "docs/assets/figuras"

os.makedirs(OUTPUT_BASE, exist_ok=True)

# List all official PDFs (VI-GU-*, VI-IN-*)
pdf_files = sorted([f for f in os.listdir(PDF_DIR) if f.startswith("VI-") and f.endswith(".pdf")])
print(f"Total PDFs a procesar: {len(pdf_files)}")

global_extracted = 0

def rects_overlap(r1, r2):
    # Intersection check
    intersect = r1 & r2
    if intersect.is_empty:
        return False
    # If intersection area is > 40% of smaller rect, they are overlapping layers
    area_int = intersect.width * intersect.height
    area_r1 = r1.width * r1.height
    area_r2 = r2.width * r2.height
    min_area = min(area_r1, area_r2)
    return (area_int / min_area) > 0.4 if min_area > 0 else False

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

    # First pass: identify repetitive header/footer/logo images across pages
    image_usage_count = {}
    for page in doc:
        seen_on_page = set()
        for img in page.get_images(full=True):
            xref = img[0]
            if xref not in seen_on_page:
                seen_on_page.add(xref)
                image_usage_count[xref] = image_usage_count.get(xref, 0) + 1

    repetitive_xrefs = {xref for xref, count in image_usage_count.items() if count > 2}

    fig_idx = 1
    extracted_doc_count = 0

    for page_idx, page in enumerate(doc):
        # We find meaningful images on this page
        page_imgs = page.get_images(full=True)
        valid_rects = []

        for img in page_imgs:
            xref = img[0]
            if xref in repetitive_xrefs:
                continue

            try:
                base_img = doc.extract_image(xref)
            except Exception:
                continue

            w = base_img["width"]
            h = base_img["height"]
            if w < 100 or h < 50:
                continue

            # Skip extreme aspect ratios
            if w / h > 18 or h / w > 18:
                continue

            rects = page.get_image_rects(xref)
            for r in rects:
                # Skip header/footer positions (e.g. y < 80 or y > 720 on standard letter)
                if r.y1 < 75 or r.y0 > 710:
                    continue
                valid_rects.append(r)

        if not valid_rects:
            continue

        # Group overlapping rects into composite clusters (merging background + green highlight layer)
        clusters = []
        for r in valid_rects:
            merged = False
            for c in clusters:
                if rects_overlap(c, r):
                    c |= r  # union bounding box
                    merged = True
                    break
            if not merged:
                clusters.append(pymupdf.Rect(r))

        # Sort clusters by vertical position on the page (top to bottom)
        clusters.sort(key=lambda r: (round(r.y0 / 20) * 20, r.x0))

        for cluster_rect in clusters:
            # Check cluster size
            if cluster_rect.width < 80 or cluster_rect.height < 40:
                continue

            # Render the composite area directly from the page at 200 DPI
            # This captures the base UI + any highlight boxes or green overlays merged with 100% fidelity
            pix = page.get_pixmap(clip=cluster_rect, dpi=200)

            fig_filename = f"figura-{fig_idx:02d}.png"
            fig_path = os.path.join(doc_out_dir, fig_filename)
            pix.save(fig_path)

            fig_idx += 1
            extracted_doc_count += 1
            global_extracted += 1

    print(f"[{doc_code}] Extraídas y renderizadas {extracted_doc_count} figuras nítidas.")

print(f"\nPROCESO COMPLETADO: {global_extracted} figuras extraídas y compuestas correctamente.")
