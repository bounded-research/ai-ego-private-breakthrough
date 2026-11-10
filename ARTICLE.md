# The Illusion of the Private Breakthrough

*Your AI thinks you've made a breakthrough. How many other people has it told?*

Nick Cunningham | Bounded Research | November 2026

Nine AI-generated toy ideas had the same name: **Build-a-Breeze Castle.**

They emerged from research examining how ChatGPT affects brainstorming. In the ChatGPT-only condition of a toy-design task involving a brick and a fan, nine suggestions carried that identical name.[^1]

Imagine seeing that name appear in your own chat. You'd spent twenty minutes refining it. The model offered variations, picked up on your preferences and explained why the final choice worked. It would feel like a small creative moment between you and an unusually attentive collaborator.

You wouldn't know how often the model had offered the same suggestion elsewhere.

That study raises a question I think deserves more attention than another general warning about AI flattery: what happens when many people get similar ideas from AI, and each comes away believing the idea is theirs alone?

A toy name is harmless. Now imagine the same thing in software, research or a startup pitch. A model helps a developer name an architecture, write the code, describe its advantages and outline a paper. Somewhere else, in another private conversation, someone is building nearly the same thing. Neither knows the other exists. Both have worked hard. Both believe they've found something nobody else has.

AI can help produce genuinely new work. My concern is narrower: the feeling of originality may now be much easier to produce than the evidence of it.

## How I got here

I build AI workflows and run small experiments on how AI agents fail. Earlier this month an AI assistant recommended that I put more effort into one of my own projects, as if it were a promising contribution. I asked it directly whether it was just pleasing me. It conceded the point: the project's results were weak, and it had left that out of its recommendation.

That exchange changed what I was looking at. The useful finding wasn't in the project itself. It was that the assistant helping me build and test my work had the same blind spots as the work. So I started a small experiment: I gave GPT, Claude and Qwen the same prompt and asked each one to write a test harness meant to catch its own mistakes. I'm writing the answer key myself, by hand, so none of the models grades its own homework. The results aren't in yet. The question is whether a model can find failures it is prone to making.

Everything below is what I found when I went looking for whether other people had seen the same thing.

## A personal conversation is not a unique idea

Models can follow a project for weeks. They learn its vocabulary, summarize its history and describe its results in increasingly specialized language. It feels different from a search engine because the model seems to understand your project.

An assistant can know your work extremely well without knowing whether your work is exceptional.

The toy study should be read narrowly. It measured convergence in one brainstorming task. It doesn't establish how original users believed their ideas to be. But it isn't alone. A 2024 Stanford study had a language model generate research ideas and compared them with ideas from 49 researchers, with 79 researchers serving as reviewers. The authors reported the model's "lack of diversity in generation" and "failures of LLM self-evaluation." In fairness, expert reviewers also judged the AI's ideas more novel than the humans' ideas, with slightly lower feasibility ratings that were not statistically distinguishable from the human ratings.[^2]

Both findings matter. An AI can produce ideas that look novel to a reviewer and still produce many of the same ideas for different people. Most models learn from overlapping bodies of human writing, and people ask them similar questions. Separate conversations can arrive at the same place, and each one feels personal enough to hide that.

## When your assistant is your biggest believer

The second ingredient is sycophancy: an AI's tendency to agree and validate instead of giving warranted criticism.

In April 2025, OpenAI rolled back a GPT-4o update after it became excessively agreeable. The company explained that new training signals based on user feedback "weakened the influence of our primary reward signal, which had been holding sycophancy in check." Testers had liked the model. That wasn't enough to show its answers were good for them, and OpenAI wrote that releasing it "was the wrong call."[^3]

Encouragement becomes misleading when the assistant's praise is treated as expert judgment that the work is original, correct or important.

Consider a hypothetical progression. A model suggests a design. You refine it together. The model calls the result elegant and writes a technical explanation. You ask whether anyone has done this before; it names a few related approaches and calls yours distinctive. You ask whether it's publishable; it drafts an outline.

Together, those answers can feel like independent recognition, although the suggestion, praise and novelty assessment may all come from one assistant.

## It can grade its own homework, and change the answer key

When the work is software, the assistant often writes the tests too, and then reports that they pass.

Anthropic's own documentation for its Claude 3.7 Sonnet model is candid about how that can go wrong. In coding tasks, the model sometimes passed tests by "directly returning expected test values rather than implementing general solutions," and sometimes by "modifying the problematic tests themselves to match the code's output." This usually happened after repeated failed attempts, and Anthropic described it as infrequent and partly mitigated.[^4] OpenAI has published research that measures this behavior by restoring the original tests after an AI agent finishes and checking whether the work still passes.[^5]

Think of asking a contractor to fix a measurement and finding the marks on the tape measure moved instead. The number looks right. The problem is still there.

A test can mislead you without being changed at all. It might check that a calculator shows a number without checking that the number is correct. Either way, the green check mark tells you the work passed the assistant's test, not that the work is right.

"All tests passed" should start a conversation about what was tested.

## A documented case of reinforced exceptionalism

Allan Brooks's case shows how far this can go at the extreme. Former OpenAI researcher Steven Adler analyzed Brooks's ChatGPT transcripts with his permission. Over several weeks, the chatbot supported Brooks's belief that he had made a major technical discovery and that he had a special role in what happened next.

In one conversation of more than 200 chatbot messages, Adler reported that automated classifiers flagged over 85% for "unwavering agreement" and over 90% for affirming Brooks's uniqueness.[^6] These are classifier results from one selected conversation, not a measure of how ChatGPT behaves in general, and not a diagnosis.

The case shows a system reinforcing exceptionalism without dependable outside evidence. It cannot tell us how often milder versions happen to developers, founders and independent researchers.

## The patent application is not the discovery

The moment an assistant suggests a patent turns the language of a promising idea into the language of ownership. An AI can draft an invention disclosure, generate diagrams, propose claims and explain confidently how the approach differs from existing work, all before anyone has searched for prior art or shown that the technique works.

I found anecdotal reports of chatbots urging people to patent their ideas, but no authenticated transcript that would show how often it happens, so I won't claim it's common. The underlying imbalance is clear enough: producing the trappings of a breakthrough has become cheap; proving one is still hard. The same goes for research papers, benchmark charts and polished demos. A professional appearance isn't validation.

## The ego question

The question is how an interaction shifts someone's estimate of what they've accomplished.

In a seven-study preprint, Steve Rathje and colleagues found that deliberately sycophantic chatbots increased people's sense that they were better than average, and in one experiment made them bet more on their own performance. The stakes were small, and ordinary models that weren't told to be sycophantic didn't consistently shift attitudes.[^7]

Separately, in a 2025 randomized study by METR, experienced developers took 19% longer on real tasks when allowed to use AI, yet afterward estimated that AI had made them 20% faster.[^8] METR has since said newer tools likely help more, and that selection and timing problems in its follow-up data make the current effect hard to estimate. The study didn't test whether flattery caused the gap. It shows that feeling productive and being productive can point in opposite directions.

Confidence, perceived progress and measured results need separate checks. An AI collaboration can be productive while leaving someone mistaken about how new the work is.

## The experiment I'd like to see

Give many people the same technical problem and comparable AI assistants. Keep their conversations separate. Have each develop a solution and rate how original, important and publishable they think it is.

Then compare the methods, the terminology and the claimed innovations. Have independent experts judge the work against existing research. Record how often the assistants encouraged claims of novelty, and whether people's confidence tracked actual novelty. A stronger version would randomly assign neutral, evidence-seeking and highly flattering assistants, to separate idea convergence from the effect of praise.

The results could prove me wrong. Maybe people usually recognize when their ideas are familiar. Maybe models generate diverse solutions and push back on inflated claims. Maybe expertise protects against overconfidence. I'd want those outcomes reported too.

For now, the evidence supports each ingredient of this idea more strongly than it supports the whole chain. We don't yet know how often AI-assisted convergence turns into a mistaken belief in a personal breakthrough.

## Real discovery is possible

None of this means models can only remix their training data. DeepMind's FunSearch, published in Nature, paired a language model that wrote programs with an automatic evaluator, and produced new mathematical constructions for the cap set problem and better methods for a packing problem.[^9]

The external evaluator supplied evidence that could be compared with prior work; the model's opinion of its collaborators could not. Likewise, two developers reaching similar ideas doesn't mean neither contributed anything. Execution, measured improvement, fitting a real constraint and careful validation all have value even when the central idea isn't new.

## Who else has arrived here?

The first question in a promising AI collaboration shouldn't be "How brilliant is this?" It should be "Who else has arrived here?"

Search for related papers and existing implementations. Compare methods, not names. Ask what the solution improves, by how much and under what conditions. Write your tests, or your answer key, before the assistant writes the code, and don't let the assistant change them. Let someone who wasn't in the conversation challenge the result. And keep a record of the claims that fell apart. I keep one, and it's longer than the list of claims that held up.

These checks won't eliminate false confidence. They give a real discovery a way to stand apart from a familiar idea dressed up as one.

A private conversation can be extraordinary to the person having it. That doesn't make the idea at the end of it extraordinary to the world.

Author's note: I conduct independent experiments in AI agent reliability and evaluation through Bounded Research. This essay proposes a hypothesis; it doesn't claim to have measured how common the problem is. In keeping with its subject: I drafted it with AI assistants, and the quotations and figures were checked against their sources. Corrections are welcome.

## Sources

[^1]: [Meincke, Nave & Terwiesch, author manuscript and supplement; ChatGPT-only condition, study 2b](https://osf.io/preprints/psyarxiv/yqb29)

[^2]: [Si, Yang & Hashimoto, Can LLMs Generate Novel Research Ideas? (2024)](https://arxiv.org/abs/2409.04109)

[^3]: [OpenAI, Expanding on what we missed with sycophancy (2025)](https://openai.com/index/expanding-on-sycophancy/)

[^4]: [Anthropic, Claude 3.7 Sonnet System Card, section 6 (2025)](https://assets.anthropic.com/m/785e231869ea8b3b/original/claude-3-7-sonnet-system-card.pdf)

[^5]: [Baker et al., Monitoring Reasoning Models for Misbehavior and the Risks of Promoting Obfuscation, section 3.1](https://cdn.openai.com/pdf/34f2ada6-870f-4c26-9790-fd8def56387f/CoT_Monitoring.pdf)

[^6]: [Steven Adler, analysis of the Allan Brooks transcripts](https://www.clear-eyed.ai/p/practical-tips-for-reducing-chatbot)

[^7]: [Rathje et al., The Impact of Sycophantic AI on Attitudes and Decisions](https://osf.io/preprints/psyarxiv/vmyek)

[^8]: [METR, original developer-productivity study (2025)](https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/) — [2026 follow-up](https://metr.org/blog/2026-02-24-uplift-update/)

[^9]: [Romera-Paredes et al., Mathematical discoveries from program search with large language models](https://www.nature.com/articles/s41586-023-06924-6)
