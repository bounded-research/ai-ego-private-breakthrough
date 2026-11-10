# Rebuilding and checking

Install requirements.txt in a suitable Python environment, plus system DejaVu Serif fonts and Poppler (`pdftotext`, `pdfinfo`, `pdftoppm`).

```sh
python3 scripts/build_pdf.py
python3 scripts/check_publication.py
python3 scripts/check_links.py
```

The PDF renderer reads ARTICLE.md; it never rewrites prose. Its metadata timestamp is fixed to the candidate's date for reproducibility. Remove the editorial-candidate footer only as part of an approved release.

The content checker can fail on a broken reference, missing text, bad local link or leaked filesystem path. Passing does not establish factual truth or quality. Network checks retain HTTP failures and do not infer full-text access from200 responses.
