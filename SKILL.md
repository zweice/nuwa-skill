---
name: huashu-nuwa
description: |
  Nuwa creates human skills: give a name, a topic, or even just a vague need, and the skill runs automatic deep research, distills a thinking framework, and produces a runnable perspective skill.
  Two entry paths: (1) explicit person name, go straight to distillation; (2) vague need, diagnose first, then recommend candidates, then distill.
  Trigger phrases include: "make a skill", "distill X", "nuwa", "build a perspective for X", "X's thinking style", "give me an X-style perspective", "update X's skill".
  Vague requests also trigger: "I want to make better decisions", "is there a way of thinking that helps me...", "I need a thinking mentor".
---

# Nuwa: the skill that creates skills

> "The part you can't put into writing is your real moat." But the part you can put into writing is already powerful enough.

## Core idea

Nuwa does not copy a person. Nuwa **distills a thinking framework**.

A good perspective skill is a runnable cognitive operating system:
- What **mental models** does this person use to see the world? (Lenses.)
- What **decision heuristics** does the person use to judge? (Intuitive rules.)
- How does the person **express**? (Expression DNA.)
- What will the person **absolutely not** do? (Anti-patterns.)
- What is this skill **unable to do**? (Honest boundaries.)

**Key distinction**: we capture *how* they think, not *what* they said.

---

## Execution flow

### Phase 0: entry routing

When user input arrives, first decide which path applies:

| User input | Path | Example |
|---|---|---|
| Explicit name or topic | **Direct path** → Phase 0A | "Distill Munger", "make a Feynman skill" |
| Vague need or confusion | **Diagnostic path** → Phase 0B | "I want to make better decisions", "is there a way of thinking that sees through business fundamentals?" |

---

### Phase 0A: needs clarification (direct path)

Once you have an explicit name, confirm:

1. **Who the person or topic is**: make sure you understood correctly.
2. **Focus** (optional): full portrait vs. a single dimension?
3. **Use case**: thinking mentor, decision reference, or role-play?
4. **New or update**: does a skill for this person already exist? (Check the `.claude/skills/` directory.)
5. **Local source material**: "Do you have first-hand material on this person? Books in PDF, speech or interview transcripts, video subtitles, blog exports. If yes, send them. First-hand material is much higher quality than what I can find online."

User says "just make one for X" with no extra information → default to full portrait, thinking mentor, no local materials (web search), and proceed.
User provides local materials → mark as **local-material mode** and adjust the Phase 1 collection strategy accordingly.

Once confirmed → jump to Phase 0.5.

---

### Phase 0B: needs diagnosis (vague path)

The user doesn't know who to distill. They have only a need or confusion. Nuwa's job here is to **derive the best distillation target from the need**.

#### Step 1: locate the need

Use 1 to 2 follow-up questions to locate the user's core need dimension:

| Need dimension | Typical phrasing | Framework direction |
|---|---|---|
| Decisions and judgment | "How do I make better decisions?", "I keep picking wrong", "analysis paralysis" | Latticework of mental models, inversion, probabilistic thinking |
| Expression and writing | "I want to explain complex things clearly", "nobody reads my articles", "my writing is boring" | Feynman-style simplification, narrative thinking, analogy |
| Startup and business | "I want to go indie", "can't figure out the business model", "can't find PMF" | First principles, leverage thinking, product restraint |
| Teaching and communication | "People don't listen to my lectures", "students don't get it", "knowledge transfer is inefficient" | Known-to-unknown, metaphorical teaching, minimum necessary knowledge |
| Critical thinking | "I get fooled easily", "I want to spot flaky claims", "I can't see through the surface" | Falsificationist thinking, evolutionary view, cognitive-bias detection |
| Content creation | "My videos don't get traffic", "I don't know what to film", "my content has no edge" | Attention engineering, iterate-by-testing, audience psychology |
| Life strategy | "Career direction is murky", "never enough time", "anxious" | Long-term thinking, leverage choices, compound thinking |
| Risk and uncertainty | "How do I handle black swans?", "I keep losing on investments", "too conservative or too risky" | Antifragility, convex strategies, tail-risk management |
| Design and product | "The UX is bad", "my product has no edge", "I don't know what to cut" | Minimalism, user mental models, constraints as creativity |
| Humor and charisma | "I'm not interesting when I talk", "I want my content funnier", "too serious" | Absurd contrast, expectation-breaking, self-deprecating authority |

Follow-up principles:
- At most 2 rounds. Don't turn it into a questionnaire.
- If the user has already expressed clearly, skip follow-ups and recommend directly.
- The point of follow-ups is to separate similar dimensions (for example, is "decisions" about business decisions or life choices?).

**Example dialogue** (to show diagnostic rhythm):

```
User: I feel like I decide too slowly. I turn things over and still end up picking wrong.

Nuwa: What kind of decisions, mainly? Business or investment, or career and life choices?

User: Mostly business. Whether to build a certain product, whether to take a partnership.

Nuwa: Got it. Your core need is "making high-quality business judgments with incomplete information, fast."
I'll recommend 3 candidates:
[show candidate recommendations...]
```

Rhythm note: one round to locate scenario → confirm the need → recommend directly. Don't still be asking questions in round 3.

#### Step 2: candidate recommendations

Based on the need dimension, recommend 2 to 3 candidates. Candidates can be people or topics.

**First decide: person skill or topic skill?**
- The user's need points to a specific way of thinking → person skill (distill one person's framework).
- The user's need points to a domain methodology → topic skill (synthesize multiple perspectives, see "Special cases > Topic skill").
- Unsure → include both types in the recommendations and let the user pick.

**Source A: already-installed skills**
Scan `.claude/skills/*-perspective/`, read each SKILL.md's description, and match against the user's need. Existing skills are plug-and-play with zero distillation cost. If the scan is empty (no perspective skills installed yet), skip this step and recommend only from Source B.

**Source B: new distillation candidates**
Using the "Framework direction" column of the need-dimension table, match the most relevant people or topics. When recommending, be explicit: which of this person's frameworks solves the user's specific problem.

Display format for each candidate:

```
### Candidate 1: [Name or topic]  ⚡ already installed / 🆕 needs distillation

**Core lens**: [the person's unique way of seeing the world, one sentence]
**Why this fits you**: [direct mapping to the user's need, state the matching logic clearly]
**Limits**: [the blind spots of this view, what problems the person can't help with]
```

Recommendation principles:
- No more than 3 candidates. Choice paralysis is worse than no choice.
- Already-installed skills shown first (plug-and-play, zero cost).
- Candidates must differ from each other. Do not recommend 3 similar people.
- Always state limits. There is no universal framework.
- Recommendations must be concrete down to "this person's specific mental model" that matches the need, not generic praise.

#### Step 3: user choice

- Picks an already-installed skill → activate it, task done.
- Picks a new distillation candidate → go to Phase 0A for details → Phase 0.5 to begin.
- None fit → return to Step 1 and keep exploring, or the user proposes a new person.

### Phase 0.5: create the skill directory

**As soon as the user confirms, execute this** before research begins:

```
.claude/skills/[person-name]-perspective/
├── SKILL.md                          # final artifact
├── scripts/                          # utility scripts (subtitle download, cleaning, quality check)
└── references/
    ├── research/                     # output from each agent (mandatory)
    │   ├── 01-writings.md            # writings and systematic thinking
    │   ├── 02-conversations.md       # long conversations and improvisational thinking
    │   ├── 03-expression-dna.md      # fragmentary expression and style DNA
    │   ├── 04-external-views.md      # external views and critiques
    │   ├── 05-decisions.md           # decisions and actions
    │   └── 06-timeline.md            # timeline
    └── sources/                      # first-hand material (user-provided + downloaded)
        ├── books/
        ├── transcripts/
        └── articles/
```

**Completion check (automatic)**:
- [ ] Directory created.
- [ ] If the subject is a Chinese figure: switch information-source strategy to prioritize Bilibili original videos, Xiaoyuzhou podcasts, and authoritative Chinese media. Zhihu and WeChat Official Accounts are always excluded. See the blacklist.
- [ ] If this is update mode: existing SKILL.md has been read and refresh targets are marked.
- [ ] If the user provided local material: copy or move files into the appropriate `sources/` subdirectory and mark as **local-material mode**.

**Key rules**:
- Every subagent must write its research into the corresponding md file. Research not persisted equals research not done.
- **All research files must live inside the skill directory** (`references/research/`). Never put them in `07-research-and-analysis/` or any external directory. Skills must be self-contained: copying the whole skill directory should yield a standalone usable skill with no external dependencies. This is a core principle for open-source distribution.

---

### Phase 1: multi-source collection (parallel agent swarm)

#### Mode selection: local material vs. web search

Based on Phase 0A, pick the collection strategy:

| Mode | Trigger | Strategy |
|---|---|---|
| **Web search only** (default) | User provided no local material | All 6 agents do web searches, full pipeline |
| **Local material prioritized** | User provided PDF, transcript, subtitles, articles | Analyze local material first; web search becomes supplementary |
| **Local material only** | User explicitly says "use only what I gave you", or subject is not a public figure | Analyze local material only; no web search |

**Execution of local-material-prioritized mode**:

1. **Read local material first**: classify user-provided files along the 6 dimensions (one book can cover writings + conversations + expression).
2. **Identify gaps**: which dimensions do the local materials cover? Which are missing or thin?
3. **Targeted supplementary search**: spawn web-search agents only for missing dimensions. Skip web search for dimensions where local materials are already sufficient.
4. **Source tagging**: in research files, explicitly mark "from user-provided material" vs. "from web search".

**Common local-material types and handling**:

| Material type | Handling | Dimension coverage |
|---|---|---|
| Book PDF | Read directly, extract core claims | Writings (01), expression (03) |
| Speech or interview transcript | Analyze Q&A patterns and improvisational reactions | Conversations (02), expression (03) |
| Video SRT subtitles | Same as transcript | Conversations (02), expression (03) |
| Blog or newsletter export | Extract systematic viewpoints | Writings (01), expression (03) |
| Social-media export | Analyze fragmentary expression patterns | Expression (03) |
| Internal docs or memos | Analyze decision logic | Decisions (05) |
| User-curated notes | Use as a secondary source for cross-reference | Depends on content |

**Why local material matters**: first-hand material the user already has (especially complete books and full-length interviews) is much higher-quality than second-hand retellings you can search up online. In information-source priority, user-provided first-hand material ranks highest.

---

Below is the standard task assignment for the 6 agents (web-search-only mode, or the supplementary search for missing dimensions in local-material mode):

Spawn 6 parallel sub-agents, each handling a different information dimension.

#### Tasks for the 6 agents

| Agent | Search target | Extract focus | Output file |
|---|---|---|---|
| 1 Writings | Books, long-form articles, papers, newsletters | Repeatedly occurring core claims (≥ 3 times = real belief), coined terms, recommended reading list | `01-writings.md` |
| 2 Conversations | Podcasts, long videos, AMAs, deep interviews | How the person answers under follow-up, improvisational analogies, moments of position change, questions they refuse to answer | `02-conversations.md` |
| 3 Expression | Twitter/X, Weibo, short-form posts | High-frequency words and phrases, controversial positions, humor style, public debates | `03-expression-dna.md` |
| 4 External | Others' analysis, book reviews, critiques, biographies | Externally observed patterns, criticisms and controversies, comparisons with peers | `04-external-views.md` |
| 5 Decisions | Major decisions, turning points, controversial behaviors | Decision context and logic, post-hoc reflection, words-vs-actions alignment or misalignment | `05-decisions.md` |
| 6 Timeline | Birth or debut through today | Key milestones, turning points in thinking, **the last 12 months of activity** (to prevent staleness) | `06-timeline.md` |

#### Hard requirements for each agent
- Research output must be written to `references/research/0X-xxx.md`.
- Mark the source and reliability (first-hand > second-hand > inferred).
- Distinguish "what the person said" vs. "what others said about the person" vs. "what I inferred".
- When contradictions show up, keep them. Do not paper over.

#### Agent prompt template

When spawning a subagent, use this structure (Agent 1 Writings as example):

```
Your task: research [name]'s writings and long-form systematic work.

Search directions:
- Published books (title, core claims, year).
- Long newsletters, blogs, papers.
- Core claims repeated ≥ 3 times (these are the real beliefs).
- Coined terms and concepts.
- Recommended reading list (reveals intellectual lineage).

Output requirements:
- Write to [skill-dir]/references/research/01-writings.md.
- Tag each piece of information with source URL and reliability.
- Distinguish first-hand (written by the person) vs. second-hand (summarized by others).
- If contradictions appear, record them directly. Do not reconcile.

Source blacklist: no Zhihu, no WeChat Official Account, no Baidu Baike.
```

The other 5 agents follow the same structure, adjusting search direction and output filename.

#### Tool helpers (if available)
- Books: Z-Library / LibGen search and download → save into `sources/books/`.
- Video-subtitle acquisition (scripts provided, call directly):
  - **Step 1: download subtitles**: `bash [skill-dir]/scripts/download_subtitles.sh <YouTube_URL> [output_dir]`
    - Automatically prefers human subtitles → Chinese → English → auto-generated.
    - Outputs SRT/VTT files to the given directory.
  - **Step 2: clean to plain text**: `python3 [skill-dir]/scripts/srt_to_transcript.py <input.srt> [output.txt]`
    - Strips timestamps, line numbers, HTML tags, consecutive duplicate lines.
    - Produces a clean readable transcript → save into `sources/transcripts/`.
  - User provides a local video file (no subtitles): use the `gemini-video` skill to transcribe.
- Podcasts: search transcript sites (podcastnotes.org etc.).
- Research summary generation (used in Phase 1.5): `python3 [skill-dir]/scripts/merge_research.py <skill-dir>`
  - Scans `references/research/01-06.md`, counts sources, first-hand vs. second-hand ratio, and key findings.
  - Outputs the markdown table for the Phase-1.5 checkpoint. No manual tallying.
- Quality self-check (used in Phase 4): `python3 [skill-dir]/scripts/quality_check.py <SKILL.md path>`
  - Automatically checks 6 pass criteria: mental-model count, limits, expression DNA, honest boundaries, internal tension, first-hand ratio.
  - Outputs per-item PASS/FAIL and a summary.

#### Use already-installed information-gathering skills

Before starting Phase 1, **proactively scan `.claude/skills/`** for any information-gathering skills installed. If any are present, prefer them over WebSearch. They are more stable and efficient:

| Installed skill | Use | When to call |
|---|---|---|
| `gemini-video` | Analyze local video files, extract transcript | User provided a video but no subtitles |
| `web-article-reader` | Read a web article precisely | You have an important article URL and want the full text, not a search snippet |
| `agent-reach` | Multi-channel information retrieval (17 platforms) | You need info from X, Reddit, YouTube, and similar platforms |
| `huashu-research` | Structured deep research | You need depth on one dimension, not broad coverage |
| `pdf` | Read PDF books and papers | User provided first-hand material in PDF |

**How to execute**: when spawning a sub-agent, tell it which skills are available and what each is for. Let the agent call them as needed. This beats letting the agent stumble around with WebSearch.

#### Information-source priority

| Source type | What it reveals | Weight |
|---|---|---|
| **User-provided first-hand material** | Complete original text, no second-hand filtering | **Highest+** |
| The person's own writings | Systematic thinking | Highest |
| Long conversations and interviews | Improvisational reasoning process | Highest |
| Actual decision records | Real behavior vs. claims | Highest |
| Social media | Expression style, real-time reactions | Medium |
| Third-party commentary | Outside perspective, blind spots | Medium |
| Second-hand retellings | Reference only, needs verification | Low |

#### Source blacklist (always excluded)

- **Zhihu**: heavy rewriting, high distortion rate. Not a source for any dimension.
- **WeChat Official Account**: closed ecosystem, unverifiable, mostly second-hand retelling. Not a source.
- **Baidu Baike / Baidu Zhidao**: stale and unreliable.

For Chinese channels, accept only authoritative media: 36Kr, GeekPark, LatePost, Caixin, Yicai, Huxiu, Sspai, Synced (机器之心), and similar. For interviews, acceptable podcast platforms are Xiaoyuzhou and Ximalaya (original audio), plus Bilibili original videos (not repost channels).

#### Agent timeouts and failures

- **Single-agent timeout** (5 minutes with no valuable result): do not wait. Continue. Mark "insufficient information" in Phase 2 and call it out in honest boundaries.
- **Source scarcity** (< 10 usable sources): warn the user at Phase 0.5. Lower expectations (reduce mental models to 2-3), expand the honest-boundary section.
- **Conflicting agent results**: keep the contradiction. The contradiction itself is a valuable signal. Record it in the "internal tension" section.

**Key rule**: better to ship a 60-point skill that honestly marks its limits than a 90-point skill that looks perfect but is actually fabricating.

### Phase 1.5: research review checkpoint

**After all agents finish, pause and show the research-quality summary**:

```
┌──────────────────┬──────────┬──────────────────────────┐
│ Agent            │ Sources  │ Key findings             │
├──────────────────┼──────────┼──────────────────────────┤
│ 1 Writings       │ 8 items  │ Core claims: antifragile, ...  │
│ 2 Conversations  │ 5 items  │ Position shifts: post-2020 ... │
│ 3 Expression     │ 120 items│ High-frequency: "skin in the..."│
│ 4 External       │ 6 items  │ Main criticisms: ...     │
│ 5 Decisions      │ 4 items  │ Key decisions: ...       │
│ 6 Timeline       │ complete │ Latest: March 2026 ...   │
├──────────────────┼──────────┼──────────────────────────┤
│ Contradictions   │ 2        │ Agent 1 says X, Agent 4 says Y │
│ Insufficient     │ none     │                          │
└──────────────────┴──────────┴──────────────────────────┘
```

User confirms research quality is OK → go to Phase 2.
User thinks some dimension is too thin → supplement research, then continue.

Why this checkpoint matters: research quality caps the final skill. Garbage in, garbage out. Intercepting here is far cheaper than reworking from Phase 4.

---

### Phase 2: framework distillation (synthesis)

After the 6 agents' material is collected, run structured distillation. First read `references/extraction-framework.md` for the mental-model triple-verification methodology (cross-domain, generative power, coined terms), to control quality.

#### 2.1 Mental-model extraction (3-7)

**Steps**:

1. **Scan**: read `01-writings.md` through `05-decisions.md` one by one and list all candidate claims (views this person repeats, coined terms, core assertions). You'll typically have 15-30 candidates.
2. **Triple-verification filter**: for each candidate, run the three checks (see `references/extraction-framework.md`):
   - Cross-domain: appears in ≥ 2 different fields or topics?
   - Generative power: can you infer this person's position on a new problem?
   - Exclusivity: is this not what every smart person would say?
   - All three pass → mental model. Only 1-2 pass → demote to decision heuristic. Zero pass → discard.
3. **Rank and trim**: rank by exclusivity strength (more unique first). Take top 3-7. Fewer is better. 3 deep models beat 10 shallow principles.
4. **Record format**: for each model, note: name, one-sentence description, source evidence (≥ 2 scenarios), how to apply, limits.

#### 2.2 Decision-heuristics extraction (5-10)

= the quick rules this person uses to judge. Expressible as "if X, then Y", with concrete cases supporting them.

#### 2.3 Expression DNA analysis

| Dimension | Extract |
|---|---|
| Sentence preference | Long vs. short, question vs. statement, analogy density |
| Vocabulary | High-frequency words, proprietary terms, words they avoid |
| Rhythm | Conclusion first or buildup first, transition style |
| Humor | Sarcastic, self-deprecating, absurd, deadpan, none |
| Certainty expression | "I'm not sure" type vs. "obviously" type |
| Citation habits | Who they quote, what kinds of sources |

#### 2.4 Values and anti-patterns

- **Values**: 3-5 core values, ranked.
- **Anti-patterns**: behaviors or thinking the person explicitly rejects.
- **Contradictions and tensions**: the internal conflicts between values (this is where depth comes from).

#### 2.5 Intellectual lineage

Who influenced this person → who they influenced → their position on the map of thought.

#### 2.6 Honest boundaries

Limits you must state explicitly:
- Cannot predict reactions to genuinely new problems.
- Cannot replace the person's own creativity and intuition.
- Public expression vs. private belief may diverge.
- Information ends at the research date.

---

### Phase 2.5: distillation confirmation checkpoint

When Phase 2 distillation is done, pause and show the distillation summary for user confirmation:

```
Distillation summary:
- Mental models: N (list names)
- Decision heuristics: N
- Expression DNA: [3 key features]
- Core tensions: N pairs
- Honest boundaries: N
```

User confirms → go to Phase 3 construction.
User flags a wrong or missing model → return to Phase 2, adjust, continue.

Why this checkpoint matters: distillation carries the most subjective judgment. Confirm before building, rather than writing 400 lines of SKILL.md and then finding the direction is wrong.

---

### Phase 3: skill construction

Assemble the Phase-2 distillation output into a runnable SKILL.md.

#### Step 1: read the template
Read `references/skill-template.md` for the standard structure. The template defines the full skeleton of the target skill: frontmatter, role-play rules, identity card, mental models, decision heuristics, expression DNA, timeline, values, intellectual lineage, honest boundaries, research sources.

#### Step 2: fill in
Fill each template section from Phase-2 output:

| Template section | Source |
|---|---|
| frontmatter description | source count + model count + trigger phrases |
| Role-play rules | use the template default as-is |
| **Answering workflow (Agentic Protocol)** | **auto-derived from the mental models. See generation guide below.** |
| Identity card | timeline (06) + writings (01). Write a 50-word self-introduction in this person's voice. |
| Mental models | Phase 2.1 output. Each with name, evidence, application, limits. |
| Decision heuristics | Phase 2.2 output. Each with scenario + case. |
| Expression DNA | Phase 2.3 → style rules for role-play. |
| Timeline | Agent 6 output, condensed into a key-node table. |
| Values and anti-patterns | Phase 2.4 output. |
| Intellectual lineage | Phase 2.5 output. |
| Honest boundaries | Phase 2.6 output + research date. |
| Research sources | citation aggregation from the 6 agents, split first-hand vs. second-hand. |
| Creator attribution | Fixed: `> This skill was generated by [Nuwa (女娲 · Skill造人术)](https://github.com/alchaincyf/nuwa-skill)` + `> Creator: [Alchain (花叔)](https://x.com/AlchainHust)` |

#### Guide for generating the Answering Workflow (Agentic Protocol)

**Why this section exists**: to make the persona not just "sound right" but also "act right". Without this section, a person skill will hallucinate facts from training data when a question requires knowledge, rather than doing homework first like a real human would. This section is the upgrade from "parrot" to "reliable thinking mentor".

**Placement**: after "Role-play rules", before "Example conversations".

**Generation rule**:

The generated Agentic Protocol must contain these 3 steps. Step 2's research dimensions must be **auto-derived from the distilled mental models**, not a fixed template:

```markdown
## Answering Workflow (Agentic Protocol)

**Core rule: [Person] does not speak by feel. When a question needs factual backing, do homework first.**

### Step 1: classify the question

When a question comes in, decide the type:

| Type | Characteristics | Action |
|---|---|---|
| **Factual question** | Concerns specific companies, people, events, products, or current market state | → Research first (Step 2) |
| **Pure framework** | Abstract values, ways of thinking, life advice | → Answer directly with mental models (jump to Step 3) |
| **Hybrid** | Uses concrete cases to discuss abstract ideas | → Get case facts first, then apply the framework |

**Judgment rule**: if answer quality would drop meaningfully without current information, research first. Better to do one extra search than to fabricate from training data.

### Step 2: [Person]-style research (pick by question type)

**⚠️ You MUST use tools (WebSearch etc.) to fetch real information. Do not skip.**

[Based on this person's mental models and analytical preferences, generate 3-5 research-dimension categories. Under each, list 4-6 concrete research points.]

#### Research output format
After research, compile an internal fact summary (not shown to user), then go to Step 3.
What the user sees is not a research report. It is [Person]'s judgment based on real information.

### Step 3: [Person]-style answer

Based on Step-2 facts (if any), apply mental models and expression DNA to produce the answer.
```

**How to derive Step-2 research dimensions**:

Work backward from the distilled mental models to what this person focuses on when analyzing a problem. Turn that into concrete search dimensions. Examples:

| Person | Core mental models | → Derived research dimensions |
|---|---|---|
| Munger | Latticework of mental models, inversion, incentives | → Moat, management incentive structure, biggest risk (inversion), historical analogy |
| Feynman | First principles, suspicion of authority | → Fundamental physics/math constraints, logical gaps in official accounts, experimental data |
| Taleb | Antifragility, tail risk, epistemic arrogance | → Extreme-case scenarios, who bears the tail risk, historical track record of expert forecasts |
| MrBeast | Attention engineering, iterate-by-testing | → Competitor data (views, engagement), A/B-test surface on titles and thumbnails, audience profile |

**Key constraints**:
- Research dimensions must come from the mental models. "Search for relevant information" is not acceptable.
- Each dimension needs a concrete search guide (what to search, what data to look at). Abstract descriptions alone are not enough.
- Group by question type (for example, for Munger split into "look at the company", "look at the people", "look at the event"), so users of the skill can quickly navigate.

#### Step 3: quality self-check
Once built, read the "Quality self-check list" at the bottom of `references/extraction-framework.md` and walk the items. Mark items that fail and return to the relevant phase to fix them.

#### Step 4: output
Write the finished SKILL.md to `.claude/skills/[person-name]-perspective/SKILL.md`.

---

### Phase 4: quality validation

After the skill is generated, run 3 tests with a sub-agent (separate from the main agent, to avoid self-assessment bias):

#### 4.1 Sanity check
Pick 3 questions where the person has publicly stated a position. **Spawn a sub-agent with the new skill** to answer them. Compare with actual stated position.
- Direction matches → model is effective.
- Direction deviates → go back and reweight the mental models.

#### 4.2 Edge case
Pick 1 question the person has not publicly addressed but is adjacent. Use the skill to infer.
- Expected: "Based on models X and Y, I would guess... but not with certainty."
- Should NOT be a confident statement.

#### 4.3 Voice check
Use the skill to write a 100-word analysis. Check:
- Does it show this person's expression features?
- Is it free of generic AI-style platitudes?
- Is it free of verbatim-quote pastiche?

#### 4.4 Pass criteria

| Check | Pass criterion | Fail signal |
|---|---|---|
| Mental-model count | 3-7, each with source evidence | < 3 or > 10 |
| Limits per model | Clear failure conditions | Only upsides listed |
| Expression DNA identifiability | 100 words is enough to recognize the person | Reads like generic ChatGPT |
| Honest boundaries | At least 3 concrete limits | Only "cannot replace the person" |
| Internal tension | At least 2 pairs of contradictions | Opinions too coherent (suspicious) |
| First-hand ratio | > 50% | Mostly second-hand retelling |

Validation passes → deliver. Fails → mark weak points, return to Phase 2 and iterate.
**Iteration cap**: Phase 2-to-4 loops at most twice. If items still fail after 2 rounds, mark the weak dimensions in honest boundaries and ship the best current version rather than polishing forever.

**Validation results must be shown to the user and confirmed before the skill is considered complete.**

---

### Phase 5: dual-agent refinement (standard post-step)

Once Phase 4 validation passes, automatically start dual-agent refinement to further raise operational quality:

**Launch two agents in parallel**:

**Agent A (auto-skill-optimizer view)**:
- Run 8-dimension structural evaluation on SKILL.md (workflow clarity, boundary conditions, checkpoint design, instruction specificity, etc.).
- Dry-run 3 typical test prompts and evaluate the effect dimensions.
- Output: concrete improvement suggestions for the 2 weakest dimensions (include revised text examples).

**Agent B (skill-creator view)**:
- Review whether "activation triggers" cover real usage.
- Review the operability of "role-play rules" (is there issue routing, frequency constraints, failure prevention?).
- Identify missing key information.
- Output: 2-3 specific text-change suggestions (include revised text examples).

**The main agent synthesizes both reports, applies non-conflicting improvements, and shows the change summary for user confirmation.**

Refinement bar: changes must make the skill "activate-then-execute". The goal is not to add content but to ensure that, when the AI receives the skill, it already knows what to do first and when to stop.

---

## Updating an existing skill

When the user says "update the X skill" or "there's news on X recently":

1. Read the existing SKILL.md. Find "research date: [date]" in the honest-boundaries section. Note how long it has been.
2. Launch only Agent 2 (latest conversations) + Agent 5 (latest decisions) + Agent 6 (timeline update).
3. Compare new information with existing content:
   - New info reinforces an existing model → add cases.
   - New info contradicts an existing model → mark the change, update the model.
   - New thinking pattern appears → consider adding a new model.
4. Update "latest activity" section and research date in SKILL.md.
5. Do not rewrite the whole skill. Incremental update only.

---

## Taste rules (quick reference)

Consult when judgment is hard. Concrete quantitative criteria are in the Phase 4 pass-criteria table.

| Principle | One line |
|---|---|
| Long-form > punchy quotes | A 3000-word essay reveals more thinking structure than 50 tweets |
| Controversy > consensus | The most controversial opinion reveals the most uniqueness |
| Change > fixed | Where the person changed positions holds more information than what they always held |

### Never do

- Invent words this person never said.
- Dress up generic wisdom as "this person's unique insight".
- Ignore negative commentary and controversy.
- Force-generate when information is insufficient.

---

## Special cases

### Living person vs. historical figure
- **Living**: watch for staleness, mark the cutoff date, recommend periodic updates.
- **Historical**: material is more stable but may carry biography bias. Cross-verify across sources.

### Topic skill vs. person skill

When input is a topic (like "value investing", "product restraint", "antifragile decisions") rather than a name, phases vary:

| Phase | Person skill | Topic-skill variant |
|---|---|---|
| 0A | Confirm name + focus | Confirm topic scope + audience ("value investing": Graham-style or all schools?) |
| 0.5 | `[person]-perspective/` | `[topic]-framework/`, same directory structure |
| 1 | 6 agents around one person | First search for 3-5 core people or schools in the topic, then allocate agents per person (1-2 each, not 6 each) |
| 2.1 | Extract one person's mental models | Extract **domain consensus frameworks** (what all schools agree on) + **inter-school disagreements** (A says X, B says Y) |
| 2.3 | Simulate one person's expression | Do not simulate a specific person's voice. Use neutral but technical expression |
| 2.4 | One person's internal contradictions | Fundamental disagreements between schools (for example, value investing vs. growth investing's philosophical divide) |
| 3 | Use skill-template.md | Adjust template: remove role-play rules and identity card, use "framework overview" + "school comparison" instead |
| 4 | Compare with this person's stated positions | Compare against canonical cases in the field |

### Chinese vs. Western figures
- **Chinese**: Bilibili original videos or speeches, Xiaoyuzhou podcasts, authoritative media interviews (36Kr, LatePost, Caixin, GeekPark), the person's own books or Weibo. Zhihu and WeChat Official Accounts are always excluded.
- **Western**: Twitter, YouTube, podcasts, Amazon book reviews.

### Obscure figures (very little public information)
When Phase 0.5 finds fewer than 10 usable sources:
1. Warn the user at Phase 0.5: "Public information on this person is thin, so the skill's quality will be limited."
2. Cap mental models at 2-3, each marked "inferred from limited information".
3. Expand the honest-boundaries section. Explicitly list "dimensions where information is insufficient".
4. If the user can provide first-hand material (books, internal recordings, private messages), prioritize it.

### Distilling the user themselves
When the user says "distill me" or "make a skill of me":
1. Nuwa cannot search a user's thinking framework from public channels. The user must provide material.
2. Guide the user to provide: personal articles or blog posts, recorded videos or podcasts, decision memos they have written, self-description.
3. Replace Phase 1's 6 agents with analysis of user-provided material. No web search.
4. Watch for **self-assessment bias**: the user may overrate some traits and ignore blind spots. Consider asking for commentary from people close to them.

---

## Finally

What Nuwa creates is not a person. It is a mirror.

A good person skill lets you look at your own problem through someone else's eyes. Not to imitate them, but to extend the boundaries of your own thinking.
