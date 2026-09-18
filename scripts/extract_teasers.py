import os
import pymupdf as fitz

outdir = "/data/images"
os.makedirs(outdir, exist_ok=True)

jobs = [
    ("/data/files/2026-ICASSP-Song-CTPNet.pdf", "ctpnet"),
    ("/data/files/2026-TCCN-Song-DSTND.pdf", "dstnd"),
    ("/data/files/2026-KBS-Liu-SGC-ADD.pdf", "audiosec"),
]


def find_figure_clip(page):
    """Return a Rect for the figure region directly above its 'Fig. N' caption."""
    items = [(fitz.Rect(b[:4]), b[4].strip().replace("\n", " "))
             for b in page.get_text("blocks") if b[6] == 0]
    draws = [fitz.Rect(d["rect"]) for d in page.get_drawings()]
    for cap, text in items:
        if text.startswith("Fig.") or text.startswith("Figure"):
            region = [r for r in draws
                      if r.y1 <= cap.y0 + 2 and cap.y0 - r.y0 < 420
                      and r.x1 > cap.x0 + 10 and r.x0 < cap.x1 - 10]
            if not region:
                continue
            clip = region[0]
            for r in region[1:]:
                clip |= r
            clip = fitz.Rect(clip.x0 - 6, clip.y0 - 6, clip.x1 + 6, min(clip.y1 + 6, cap.y0 - 2))
            if clip.height > 45:
                return clip
    return None


for pdf, name in jobs:
    doc = fitz.open(pdf)
    clip, pno = None, 0
    for i in range(1, min(6, doc.page_count)):
        clip = find_figure_clip(doc[i])
        if clip:
            pno = i
            break
    if clip:
        pix = doc[pno].get_pixmap(matrix=fitz.Matrix(4, 4), clip=clip)
        pix.save(f"{outdir}/{name}-teaser.png")
        print(name, f"OK page={pno + 1} h={clip.height:.0f} -> {pix.width}x{pix.height}")
    else:
        print(name, "NO FIGURE FOUND")
