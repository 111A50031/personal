from docx import Document
from pathlib import Path

doc_path = Path('doc/intro.docx')
out_path = Path('doc/intro_text.html')

print(f"Checking: {doc_path.absolute()}")
if not doc_path.exists():
    print('doc not found')
else:
    print('doc found, loading...')
    doc = Document(doc_path)
    paras = [p.text.strip() for p in doc.paragraphs if p.text.strip()]
    print(f"Found {len(paras)} paragraphs")
    
    # Wrap paragraphs in <p>
    html = '\n'.join(f'<p>{p}</p>' for p in paras)
    out_path.write_text(html, encoding='utf-8')
    print(f'Wrote {out_path}')
    
    # Print first few paragraphs for verification
    for i, p in enumerate(paras[:3]):
        print(f"  [{i}]: {p[:80]}...")
