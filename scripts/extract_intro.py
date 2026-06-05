from docx import Document
from pathlib import Path

def main():
    doc_path = Path('doc/intro.docx')
    out_path = Path('doc/intro_text.html')
    if not doc_path.exists():
        print('doc not found:', doc_path)
        return
    doc = Document(doc_path)
    paras = [p.text.strip() for p in doc.paragraphs if p.text.strip()]
    # Wrap paragraphs in <p>
    html = '\n'.join(f'<p>{p}</p>' for p in paras)
    out_path.write_text(html, encoding='utf-8')
    print('Wrote', out_path)

if __name__ == '__main__':
    main()
