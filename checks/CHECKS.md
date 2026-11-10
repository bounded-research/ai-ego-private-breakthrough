# Candidate checks — November 10, 2026

Mechanical validation is not source verification or editorial approval. Human release approval is still pending.

- `python3 scripts/check_publication.py`: PASS on the delivered candidate. Checks required files, footnote definitions/uses, corrected model decimal, removed opening errors, exact ending, local Markdown targets, basic CFF fields/YAML parsing, trailing whitespace, private-path/credential-like patterns, PDF paragraph text parity and source hyperlinks.
- Negative control: a temporary copy changed the first citation from 1 to99. The same checker returned exit1 for citation mismatch and PDF text mismatch. No delivered article, sources or expected results were changed for that test.
- Initial PDF parity check FAILED because superscript extraction moved citation6 before its sentence. Changed PDF citation rendering to baseline links, then the same checker passed. No assertions were removed or weakened.
- `python3 scripts/build_pdf.py`: deterministic repeat build produced the same SHA-256. Runtime versions are pinned in requirements.txt; DejaVu Serif fonts and Poppler tools must be installed separately.
- `pdftoppm`: rendered all six pages. Visual review inspected the title, body, ending and references; margins, page numbers and linked references are present. Widow/orphan handling was improved after visual inspection.
- `pdfinfo -url`: all ten distinct article source URLs are embedded as PDF hyperlinks.
- `python3 scripts/check_links.py`: nine of ten source URLs returned HTTP200; OpenAI's rollback page returned HTTP403 to the requests client. That failure is retained in LINK-CHECKS.json. The AI source reviewer accessed the page through the browser tool; do not call the automated link sweep fully passing. HTTP200 does not prove a paper is open access (see source report).
- CFF check validates YAML syntax and selected identity fields, not the complete official schema.
- Repository upload is an explicit allowlist of publication files. No private transcripts, source download archives, credentials or internal project records are included. Pattern scanning is not a guarantee that every sensitive fact can be detected.
- Git whitespace and staged-file review run before the publication commit. Private repository and PR verified through GitHub after upload.

Public URLs, a release asset and logged-out access are NOT verified because no public release has been authorized. No LinkedIn post, profile pin or Zenodo registration was performed.

Evaluation changes: none. No study data or grading criteria modified. The citation negative control was a disposable copy, not a repaired empirical result. Scaffolds: none; the proposed experiment is explicitly a proposal and contains no fabricated data.
