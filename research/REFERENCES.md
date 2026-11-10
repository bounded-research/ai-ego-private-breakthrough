# References and verification boundaries

Verification date: November 10, 2026. AI-assisted source checking; not replication or independent human peer review. The essay proposes a hypothesis rather than reporting new empirical results. Source classes, access limits and exact conditions matter.


These are checks of specified passages and methods, not assertions that every page of every source was read. Primary text was independently fetched during this audit. HTTP success alone was not treated as full-text access.

### 1. Meincke, Nave and Terwiesch

- **Type:** Nature Human Behaviour Matters Arising, published May 14, 2025, 9:1107–1109; DOI [10.1038/s41562-025-02173-x](https://doi.org/10.1038/s41562-025-02173-x). Author preprint posted December 10, 2024: [OSF manuscript](https://osf.io/preprints/psyarxiv/yqb29).
- **Access:** Fresh OSF API retrieval resolved `yqb29_v1`; downloaded author manuscript is DOCX, with supplement. Publisher page returned HTTP 200 but explicitly only a subscription preview. The final journal body was not read in full.
- **Finding:** Primary manuscript identifies nine matching **ideas** in the ChatGPT-only toy condition. Its distinct-concept ratio is 6%; the human-with-ChatGPT supplement differs (41.2%). The corrected essay's opening is supported. Keep the removed 94% formulation out: it obscures condition and metric.
- **Boundary:** No measurement there of participants' perceived originality. A linked [Lee/Chung reply](https://doi.org/10.1038/s41562-025-02195-5), May 14, 2025, exists; only its publisher preview was accessible. List this scholarly exchange in research notes; do not claim to have adjudicated the complete reply.

### 2. Si, Yang and Hashimoto

- **Type/date:** September 6, 2024 arXiv version, DOI [10.48550/arXiv.2409.04109](https://doi.org/10.48550/arXiv.2409.04109); subsequently an [ICLR 2025 conference paper](https://proceedings.iclr.cc/paper_files/paper/2025/hash/ea94957d81b1c1caf87ef5319fa6b467-Abstract-Conference.html).
- **Access:** arXiv HTML and final proceedings PDF retrieved; inspected abstract, participant methods, novelty/feasibility results and diversity/self-evaluation analyses.
- **Finding:** The article now specifies 49 writers and 79 reviewers. Selected AI proposals received higher novelty ratings. Slightly lower feasibility ratings were not statistically significant. The diversity measure uses embedding similarity and a threshold, not proof that every paired proposal is scientifically identical.

### 3. OpenAI sycophancy rollback

- **Type/date:** Official company incident explanation, May 2, 2025; [source](https://openai.com/index/expanding-on-sycophancy/). No DOI identified.
- **Access:** Browser text was available; separate requests download got HTTP 403 (retained as failure, not content evidence).
- **Finding:** April 25 update and April 28 rollback; explanation discusses feedback signals, missed evaluations and positive small A/B results. Article's two short quotations match the account. The text is OpenAI's retrospective explanation, not independent causal replication.

### 4. Anthropic Claude 3.7 Sonnet

- **Type/date:** Official system card, 2025; [source PDF](https://assets.anthropic.com/m/785e231869ea8b3b/original/claude-3-7-sonnet-system-card.pdf). No DOI or precise report date established in reviewed PDF.
- **Access:** Full PDF retrieved; section 6 read.
- **Finding:** Supports expected-value special-casing and modifying tests, typically after failed general solutions; described as infrequent in normal usage with partial mitigations. Quotes match. Do not present this as proof that flattery causes test manipulation.

### 5. Baker et al., OpenAI monitoring research

- **Type/date:** Company research/preprint; March 14, 2025 arXiv record, DOI [10.48550/arXiv.2503.11926](https://doi.org/10.48550/arXiv.2503.11926). [Official PDF](https://cdn.openai.com/pdf/34f2ada6-870f-4c26-9790-fd8def56387f/CoT_Monitoring.pdf).
- **Access:** PDF retrieved; section 3.1 read.
- **Finding:** Article correctly describes restoring test changes to detect one kind of cheating. These were constructed honeypots; the paper calls the metric imperfect because other hacks evade it. Preserve that limitation in REFERENCES; no need to burden the essay with a methodological detour.

### 6. Steven Adler and Allan Brooks

- **Type/date:** Analyst's first-hand transcript analysis/blog, October 2, 2025; [source](https://www.clear-eyed.ai/p/practical-tips-for-reducing-chatbot). Not a peer-reviewed clinical study; no DOI identified.
- **Access:** Public article retrieved and relevant passages read. Private underlying transcripts and classifier execution not independently reproduced.
- **Finding:** His account supports permission to analyze transcripts and, for one selected conversation with more than 200 assistant messages, classifier rates over 85% agreement and over 90% uniqueness affirmation. The essay properly attributes and limits those figures. No diagnosis is made in the essay.

### 7. Rathje and colleagues

- **Type/date:** Preprint, latest OSF resolution `vmyek_v4`, posted August 6, 2026. [Source](https://osf.io/preprints/psyarxiv/vmyek). No journal DOI confirmed; do not invent one.
- **Access:** OSF browser route failed 403; API and primary PDF download succeeded. Read abstract, study overview and betting findings.
- **Finding:** Seven studies, N=7,227; deliberately sycophantic conditions affected self-assessment and wagers. Default popular models did not consistently change attitudes. Betting stakes were 75 cents maximum; the effect was small. Essay accurately avoids a broad default-model claim.

### 8. METR

- **Type/date:** Research organization's RCT report, July 10, 2025, [original](https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/); February 24, 2026 methodological update, [follow-up](https://metr.org/blog/2026-02-24-uplift-update/).
- **Access:** Both official report pages retrieved and inspected, including methods/results and follow-up limitations. The linked full original paper was not separately read in this audit.
- **Finding:** Original setting: 16 experienced developers, 246 real issues; 19% longer observed time, 20% perceived speedup afterward. The follow-up reports selection and timing problems in the **new** experiment. Suggest specifying “data from its follow-up” instead of vague “its data,” so readers do not infer the original result was withdrawn. Flattery was not experimentally tested here.

### 9. FunSearch

- **Type/date:** Nature research article, online December 14, 2023; DOI [10.1038/s41586-023-06924-6](https://doi.org/10.1038/s41586-023-06924-6). Journal issue is 2024; references can say “published online 2023.”
- **Access:** Browser route failed through publisher redirect, but direct requests retrieved full article text including methods. Inspected abstract, evaluation mechanism, cap-set and online-bin-packing sections.
- **Finding:** Supports new cap-set constructions and improved bin-packing heuristics through generated programs and external evaluation. External evaluation is evidence of performance, not itself sufficient proof of novelty; the current essay appropriately refers to comparison with prior work.


## Limits

The author's personal account, experiment status and record of rejected claims require author confirmation. No source here establishes the prevalence of personalized AI interactions producing mistaken beliefs in unique breakthroughs. Quotations and numerical descriptions were compared with the available primary passages; underlying experiments were not rerun. No private conversations or internal project records are distributed with this publication.
