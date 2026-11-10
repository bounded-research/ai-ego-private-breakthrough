"""Typeset ARTICLE.md; does not change article text or fetch sources."""
from pathlib import Path
import re
import os
from datetime import datetime, timezone
os.environ.setdefault("SOURCE_DATE_EPOCH", str(int(datetime(2026, 11, 10, tzinfo=timezone.utc).timestamp())))
from xml.sax.saxutils import escape
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.colors import HexColor
from reportlab.lib.enums import TA_LEFT
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak

ROOT = Path(__file__).resolve().parents[1]
FONT_DIR = Path('/usr/share/fonts/truetype/dejavu')
for name, file in [('Essay','DejaVuSerif.ttf'),('Essay-Bold','DejaVuSerif-Bold.ttf'),('Essay-Italic','DejaVuSerif-Italic.ttf')]:
    pdfmetrics.registerFont(TTFont(name,str(FONT_DIR/file)))
pdfmetrics.registerFontFamily('Essay',normal='Essay',bold='Essay-Bold',italic='Essay-Italic',boldItalic='Essay-Bold')
ink=HexColor('#1f2937'); blue=HexColor('#274c77')
styles={
 'body':ParagraphStyle('body',fontName='Essay',fontSize=10.6,leading=15.2,spaceAfter=10,textColor=ink,allowWidows=0,allowOrphans=0),
 'title':ParagraphStyle('title',fontName='Essay-Bold',fontSize=24,leading=29,spaceAfter=14,textColor=ink,keepWithNext=True),
 'head':ParagraphStyle('head',fontName='Essay-Bold',fontSize=13,leading=17,spaceBefore=13,spaceAfter=8,textColor=ink,keepWithNext=True),
 'ref':ParagraphStyle('ref',fontName='Essay',fontSize=8.5,leading=12,spaceAfter=9,textColor=ink),
}
def markup(text):
    text=escape(text)
    text=re.sub(r'\[([^\]]+)\]\((https?://[^\s)]+)\)',r'<a href="\2" color="#274c77">\1</a>',text)
    text=re.sub(r'\[\^(\d+)\]',r'<a href="#ref\1" color="#274c77">[\1]</a>',text)
    text=re.sub(r'\*\*(.+?)\*\*',r'<b>\1</b>',text)
    return re.sub(r'(?<!\*)\*([^*]+)\*(?!\*)',r'<i>\1</i>',text)
def footer(canvas, doc):
    canvas.saveState()
    canvas.setStrokeColor(HexColor('#d5dbe3'));canvas.line(54,43,558,43)
    canvas.setFont('Essay',7.3);canvas.setFillColor(HexColor('#64748b'))
    canvas.drawString(54,29,'Bounded Research · Editorial candidate · November 2026')
    canvas.drawRightString(558,29,str(doc.page))
    canvas.restoreState()
flow=[]
for block in (ROOT/'ARTICLE.md').read_text().split('\n\n'):
    block=block.strip()
    if not block:continue
    style=styles['body'];prefix=''
    if block.startswith('# '):block=block[2:];style=styles['title']
    elif block.startswith('## '):
        if block == '## Sources': flow.append(PageBreak())
        block=block[3:];style=styles['head']
    elif re.match(r'^\[\^\d+\]: ',block):
        number=re.match(r'^\[\^(\d+)\]: ',block).group(1)
        block=re.sub(r'^\[\^\d+\]: ',f'{number}. ',block)
        prefix=f'<a name="ref{number}"/>';style=styles['ref']
    flow.append(Paragraph(prefix+markup(block),style))
out=ROOT/'paper/The-Illusion-of-the-Private-Breakthrough.pdf'
SimpleDocTemplate(str(out),pagesize=letter,leftMargin=54,rightMargin=54,topMargin=48,bottomMargin=58,
 title='The Illusion of the Private Breakthrough',author='Nick Cunningham',subject='Independent research essay; editorial candidate',invariant=1).build(flow,onFirstPage=footer,onLaterPages=footer)
print('Built',out.name)
