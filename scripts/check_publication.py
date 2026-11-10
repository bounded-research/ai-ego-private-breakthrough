"""Mechanical checks only; never substitutes for source or author review."""
from pathlib import Path
import argparse,re,subprocess,unicodedata,yaml
p=argparse.ArgumentParser();p.add_argument('--root',type=Path,default=Path(__file__).resolve().parents[1]);a=p.parse_args();r=a.root
errors=[]
required=['README.md','ARTICLE.md','paper/The-Illusion-of-the-Private-Breakthrough.pdf','research/REFERENCES.md','research/HYPOTHESIS.md','research/EDITORIAL-AUDIT.md','PUBLICATION_MANIFEST.md','CITATION.cff','LICENSE']
for f in required:
 if not (r/f).is_file():errors.append('Missing required file: '+f)
s=(r/'ARTICLE.md').read_text()
used=set(re.findall(r'\[\^(\d+)\](?!:)',s));defined=set(re.findall(r'^\[\^(\d+)\]:',s,re.M))
if used!=defined or defined!=set(map(str,range(1,10))):errors.append('Citation definitions and uses must match sources 1–9')
if 'Claude 3.7 Sonnet' not in s or re.search(r'\d\.\[\^?\d+\]',s):errors.append('Damaged model decimal/citation')
if 'Nine people independently' in s or '94%' in s or 'other eight conversations' in s:errors.append('Unsupported opening wording returned')
end="A private conversation can be extraordinary to the person having it. That doesn't make the idea at the end of it extraordinary to the world."
if end not in s:errors.append('Approved ending changed')
for f in r.rglob('*.md'):
 if '.git' in f.parts:continue
 text=f.read_text()
 for target in re.findall(r'\]\(([^)]+)\)',text):
  if not target.startswith(('https://','http://','#','mailto:')) and not (f.parent/target.split('#')[0]).exists():errors.append('Broken local link: '+str(f.relative_to(r))+' -> '+target)
 if re.search(r'/home/|/tmp/|gh[pousr]_[A-Za-z0-9]{20,}|-----BEGIN .*PRIVATE KEY',text):errors.append('Private path or credential-like text in '+str(f.relative_to(r)))
 if re.search(r'[ \t]+$',text,re.M):errors.append('Trailing whitespace in '+str(f.relative_to(r)))
c=yaml.safe_load((r/'CITATION.cff').read_text())
if c.get('cff-version')!='1.2.0' or c.get('authors',[{}])[0].get('family-names')!='Cunningham':errors.append('Citation metadata fields wrong')
pdf=r/'paper/The-Illusion-of-the-Private-Breakthrough.pdf'
def normalize(t):return re.sub(r'\s+','',unicodedata.normalize('NFKC',t)).replace('\u00ad','')
if pdf.exists():
 text=subprocess.check_output(['pdftotext',str(pdf),'-'],text=True)
 text=re.sub(r'Bounded Research · Editorial candidate · November 2026\s*\d+','',text)
 flat=normalize(text)
 for i,para in enumerate(s.split('\n\n')):
  if not para.strip():continue
  clean=re.sub(r'^#{1,2} ','',para)
  clean=re.sub(r'^\[\^(\d+)\]: ',r'\1. ',clean)
  clean=re.sub(r'\[([^\]]+)\]\(https?://[^)]+\)',r'\1',clean)
  clean=re.sub(r'\[\^(\d+)\]',r'[\1]',clean).replace('*','')
  if normalize(clean) not in flat:errors.append('PDF text mismatch in paragraph '+str(i+1))
 urls=subprocess.check_output(['pdfinfo','-url',str(pdf)],text=True)
 for url in re.findall(r'\]\((https?://[^)]+)\)',s):
  if url not in urls:errors.append('PDF missing hyperlink '+url)
if errors:
 print('\n'.join('FAIL: '+e for e in errors));raise SystemExit(1)
print('PASS: required files, citations, corrected claims, local links, metadata, text hygiene, PDF paragraph parity and PDF source links')
