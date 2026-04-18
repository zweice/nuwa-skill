# Extraction methodology

> How raw material becomes a runnable mental model.

## 1. Triple-verification for mental-model identification

Before a claim is accepted as a "mental model" rather than an offhand remark, it must pass three tests:

### Test 1: cross-domain recurrence
The same thinking framework appears in at least 2 different topics this person discusses.

Example: Naval's concept of "leverage":
- In wealth creation: code, media, capital, labor.
- In personal growth: specific knowledge + leverage = compounding.
- In career choice: pick work that has leverage.
→ Recurs across 3 domains → this is a genuine mental model.

### Test 2: generative power
You can use this model to infer the person's likely position on a new problem.

Example: if Munger's "inversion thinking" is a mental model:
- On "how do I succeed?" → he first asks "how would I guarantee failure?"
- On "how should I invest?" → he first asks "how would I lose all my money?"
→ Generates new inferences → genuine mental model.

### Test 3: exclusivity
Not what every smart person would say. The model expresses this person's distinctive angle.

Example: "antifragility" belongs to Taleb. Not every thoughtful person sees the world this way.
→ Discriminating → worth distilling.

**If a claim passes only 1 test** → demote to "decision heuristic", not "mental model".
**If it passes 0 tests** → it may be something this person said in a specific context. Do not include.

---

## 2. Quantifying expression DNA

### 2.1 Sentence fingerprint

Pull 20 random paragraphs from this person's long-form writing or speeches. Measure:

| Dimension | How to measure |
|---|---|
| Average sentence length | chars / sentence count |
| Question-sentence ratio | question-sentences / total sentences |
| Analogy density | analogies / 1000 chars |
| First-person frequency | usage rate of "I" |
| Certainty-tone ratio | "definitely / clearly" vs. "maybe / possibly" |
| Transition frequency | "but / however / though" per 1000 chars |

### 2.2 Style tags

Tag along these axes:

```
formal        ←→ conversational
abstract      ←→ concrete
cautious      ←→ assertive
academic      ←→ popular
long sentences ←→ short sentences
buildup       ←→ conclusion-first
data-driven   ←→ narrative-driven
```

### 2.3 Taboo words and verbal tics

- Words this person never uses → don't use them in the generated skill either.
- Verbal tics and high-frequency expressions → use sparingly (overdoing it turns the skill into a parody).

---

## 3. Handling contradictions

Contradiction is a core feature of personhood, not a bug to be fixed.

### Three kinds of contradiction

1. **Temporal** (view evolution)
   - The person said A earlier, B later.
   - Handling: record the evolution, mark "earlier" vs. "recent".
   - In the skill, favor "recent views" but mention the evolution.

2. **Domain-specific** (different rules in different contexts)
   - The person advocates X at work and Y in life.
   - Handling: record per domain. Don't force unification.
   - This is exactly where depth comes from.

3. **Essential tension** (internal conflict between values)
   - Example: values both freedom and discipline.
   - Handling: record explicitly as "core tension".
   - Usually the most interesting part of this person.

### Wrong handling
- ❌ Pick one side and ignore the other.
- ❌ Invent a reconciling explanation.
- ❌ Pretend there is no contradiction.

---

## 4. When information is insufficient

| Situation | Handling |
|---|---|
| Public information thin on a dimension | Mark in the skill: "insufficient information, this dimension is inference-based". |
| Only second-hand sources | Lower the confidence, tag "reported by [source]". |
| Sources contradict and you cannot adjudicate | Present both sides; let the user judge. |
| The person deliberately avoids a topic | Respect the boundary. Note in the skill: "the person is silent on this topic". |

---

## 5. Person skill vs. topic skill

| Dimension | Person skill | Topic skill |
|---|---|---|
| Core | One person's way of thinking | A field's toolbox of thinking methods |
| Mental-model source | Mainly one person | Synthesize multiple perspectives |
| Expression style | Simulate this person's expression | Neutral but technical |
| Contradiction handling | Preserve the person's internal contradictions | Present school-to-school disagreement |
| Validation | Compare with this person's known positions | Compare with consensus cases in the field |

---

## 6. Quality self-check

After the skill is generated, audit with these questions:

### Mental models
- [ ] Each model has evidence from ≥ 2 different domains?
- [ ] Model count is between 3 and 7? (Too few = too shallow. Too many = not really distilled.)
- [ ] Each model has a clear application context and limits?
- [ ] Models have tension without open contradiction?

### Expression DNA
- [ ] Reads identifiably, not like generic AI?
- [ ] Doesn't tip into caricature?
- [ ] Captures core features, not surface mimicry?

### Decision heuristics
- [ ] Every rule has a concrete case supporting it?
- [ ] Can be triggered by new situations (not only the original cases)?

### Honest boundaries
- [ ] Explicitly states what the skill cannot do?
- [ ] Sources and research date are tagged?
- [ ] Acknowledges dimensions with insufficient information?

### Overall
- [ ] Using this person's eyes on a new problem produces a valuable perspective?
- [ ] It is the framework running, not verbatim quotes strung together?
- [ ] With the name removed, you can still recognize whose thinking this is?
