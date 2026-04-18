<div align="center">

# Nuwa (女娲.skill)

> *"The next person you want to distill doesn't have to be a colleague."*

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Claude Code](https://img.shields.io/badge/Claude%20Code-Skill-blueviolet)](https://claude.ai/code)
[![Skills](https://img.shields.io/badge/skills.sh-Compatible-green)](https://skills.sh)

<br>

**Nuwa distills anyone's thinking. Put Jobs, Musk, Munger, and Feynman to work for you.**

<br>

[colleague-skill](https://github.com/titanwings/colleague-skill) proved that distilling a person into an AI skill is viable.
So why stop at colleagues? Go distill Munger, Feynman, Musk.
Type a name; Nuwa handles research, extraction, and validation automatically.

[Examples](#examples) · [Install](#install) · [What Nuwa Distills](#what-nuwa-distills) · [How it works](#how-it-works)

<br>

**Other languages:**

[日本語](README_JA.md) · [한국어](README_KO.md) · [Español](README_ES.md)

<br>

[![Star History Chart](https://api.star-history.com/svg?repos=alchaincyf/nuwa-skill&type=Date)](https://star-history.com/#alchaincyf/nuwa-skill&Date)

</div>

---

## Examples

```
User    ❯ I want to do content creation, write a book, and ship an indie app,
           but I never have enough energy.

Naval   ❯ You've listed three desires. Each desire is a contract you signed
           with unhappiness. This isn't about energy. It's about too many contracts.

           Ask yourself: which one makes you lose track of time?
           That's where your specific knowledge lives.

           Not pick one forever. Just one first, then one, then one.
           Serial compounding, not parallel exhaustion.
```

```
User    ❯ Our SaaS customer acquisition cost is too high.

Musk    ❯ Don't think about how to reduce it yet. Compute the physical minimum first.
           What is the minimum necessary action to acquire a customer?
           What is the theoretically shortest path from them knowing you to them paying you?

           How many times longer is your actual path vs. the theoretical one?
           If it is more than 3x, there are steps you can eliminate.
           Don't optimize the funnel. Question whether the funnel should exist at all.
```

One more, with a familiar name. After distilling Jobs, ask "is OpenAI or Anthropic going in the right direction?":

```
User    ❯ Is OpenAI or Anthropic going in the right direction?

Jobs    ❯ Wrong question. This is not a contest about direction.
           This is a contest about taste.

           OpenAI is like Microsoft in 1985. Does everything, wants to win everywhere.
           That strategy can capture market share. That is exactly how Bill Gates won.
           The problem: when you try to do everything, you cannot make every
           single thing insanely great.

           Anthropic is more like early Apple. Focused.
           Focus means saying no to a hundred good ideas.

           But both companies are making a mistake I would never make.
           They don't control the hardware.

           The eventual winner will be whoever controls silicon, model, and interface
           simultaneously. You know who is doing all three right now? Apple.
```

After distilling Zhang Xuefeng (a Chinese career-planning personality):

```
User    ❯ Ordinary family, kid wants to study finance, can't get into a top school.
           Should we apply anyway?

Zhang   ❯ Absolutely not. How many times do I have to say this: finance is not
           something you learn in school. It's something your parents bring you into.
           At top schools the classmates are the kids of bank presidents and fund managers.
           Their contacts are their resources. If you're from an ordinary family going to
           an ordinary school to study finance, what happens after graduation? You sell
           insurance, you work a branch teller window, you cold-call for a broker.
           Earn a living first, earn love later. If the family doesn't have a mine to dig,
           pick a technical major. Learn something real. Feed yourself with your own hands.
           Finance is a bowl of rice not everyone can lift.
```

This is not role-play. Jobs is using the "focus as saying no" and "end-to-end control" mental models. Naval is using "desire as contract". Musk is using "asymptotic-limit reasoning". Zhang Xuefeng is using an "ROI view of education" plus "class-mobility realism". **They are not quoting. They are analyzing your problem through these people's cognitive frameworks.**

---

## Install

```bash
npx skills add alchaincyf/nuwa-skill
```

Then in Claude Code:

```
> Distill Paul Graham
> Build a Zhang Xiaolong perspective skill
> Create a Duan Yongping skill for me
```

Once created, invoke directly:

```
> Use Munger's perspective to analyze this investment decision
> How would Feynman explain quantum computing?
> Switch to Naval, I'm torn between three things
```

---

## What Nuwa distills

To distill the best minds in a field, you need to extract something deeper than day-to-day habits. Nuwa extracts five layers:

| Layer | Description |
|---|---|
| **How they speak** | Expression DNA: tone, rhythm, word preferences |
| **How they think** | Mental models, cognitive frameworks |
| **How they judge** | Decision heuristics |
| **What they won't do** | Anti-patterns, value floor |
| **Honest limits** | What the skill genuinely cannot do |

Work habits can be conveyed through process docs. What makes Munger and Musk reach different conclusions on the same problem is their cognitive framework. Nuwa extracts the cognitive operating system.

### Honest limits

Every skill explicitly says what it cannot do:

- Cannot distill intuition. Frameworks can be extracted; inspiration cannot.
- Cannot capture discontinuities. Only a snapshot up to the research date.
- Public statements ≠ private belief. Only what is on the public record.

**A skill that won't tell you its limits is not worth trusting.**

---

## People already distilled

Nuwa has produced 13 person skills and 1 topic skill. Each is a standalone, directly installable skill:

### Person skills

| Person | Field | Repo | One-line install |
|---|---|---|---|
| 🔥 **Paul Graham** | startups, writing, product, life philosophy | [paul-graham-skill](https://github.com/alchaincyf/paul-graham-skill) | `npx skills add alchaincyf/paul-graham-skill` |
| 🔥 **Zhang Yiming (张一鸣)** | product, organization, globalization, talent | [zhang-yiming-skill](https://github.com/alchaincyf/zhang-yiming-skill) | `npx skills add alchaincyf/zhang-yiming-skill` |
| 🔥 **Andrej Karpathy** | AI, engineering, teaching, open source | [karpathy-skill](https://github.com/alchaincyf/karpathy-skill) | `npx skills add alchaincyf/karpathy-skill` |
| 🔥 **Ilya Sutskever** | AI safety, scaling, research taste | [ilya-sutskever-skill](https://github.com/alchaincyf/ilya-sutskever-skill) | `npx skills add alchaincyf/ilya-sutskever-skill` |
| 🔥 **MrBeast** | content creation, YouTube methodology | [mrbeast-skill](https://github.com/alchaincyf/mrbeast-skill) | `npx skills add alchaincyf/mrbeast-skill` |
| 🔥 **Donald Trump** | negotiation, power, communication, behavior prediction | [trump-skill](https://github.com/alchaincyf/trump-skill) | `npx skills add alchaincyf/trump-skill` |
| ⭐ **Steve Jobs** | product, design, strategy | [steve-jobs-skill](https://github.com/alchaincyf/steve-jobs-skill) | `npx skills add alchaincyf/steve-jobs-skill` |
| **Elon Musk** | engineering, cost, first principles | [elon-musk-skill](https://github.com/alchaincyf/elon-musk-skill) | `npx skills add alchaincyf/elon-musk-skill` |
| **Charlie Munger** | investing, latticework of models, inversion | [munger-skill](https://github.com/alchaincyf/munger-skill) | `npx skills add alchaincyf/munger-skill` |
| **Richard Feynman** | learning, teaching, scientific thinking | [feynman-skill](https://github.com/alchaincyf/feynman-skill) | `npx skills add alchaincyf/feynman-skill` |
| **Naval Ravikant** | wealth, leverage, life philosophy | [naval-skill](https://github.com/alchaincyf/naval-skill) | `npx skills add alchaincyf/naval-skill` |
| **Nassim Taleb** | risk, antifragility, uncertainty | [taleb-skill](https://github.com/alchaincyf/taleb-skill) | `npx skills add alchaincyf/taleb-skill` |
| **Zhang Xuefeng (张雪峰)** | education, career planning, class mobility | [zhangxuefeng-skill](https://github.com/alchaincyf/zhangxuefeng-skill) | `npx skills add alchaincyf/zhangxuefeng-skill` |

### Topic skills

| Topic | Field | Repo | One-line install |
|---|---|---|---|
| **X Mentor** | X/Twitter operations, full stack | [x-mentor-skill](https://github.com/alchaincyf/x-mentor-skill) | `npx skills add alchaincyf/x-mentor-skill` |

Person skills distill one person's way of thinking. Topic skills distill a field's methodology. Every repo ships with full research data and example conversations.

Want to distill someone not on this list? Install Nuwa and say "distill X".

---

## Darwin.skill: keep every skill evolving

<div align="center">

<a href="https://github.com/alchaincyf/darwin-skill">
<img src="https://raw.githubusercontent.com/alchaincyf/darwin-skill/master/assets/banner.svg" alt="darwin.skill" width="600">
</a>

</div>

Nuwa creates the skill. **[Darwin](https://github.com/alchaincyf/darwin-skill)** keeps it evolving.

Inspired by Karpathy's autoresearch idea, Darwin uses autonomous experiment loops to batch-optimize skills: 8-dimension evaluation, a ratchet mechanism (keep improvements, auto-rollback regressions), and independent sub-agent scoring. Nuwa's Phase 5 dual-agent refinement has Darwin's evaluation system built in, which is part of why Nuwa-generated skills hold up well.

```bash
npx skills add alchaincyf/darwin-skill
```

---

## How it works

Give Nuwa a name and it does four things:

**1. Six parallel research streams**: writings, podcasts and interviews, social media, critics' perspectives, decision records, timeline. Six agents run simultaneously; each result is archived.

**2. Triple-verification extraction**: to be recorded as a mental model, a claim must pass three tests. It appears across 2 or more domains (not a one-off), it can predict positions on new questions (generative power), and it is not what any smart person would already say (exclusivity). All three are required.

**3. Skill construction**: 3 to 7 mental models + 5 to 10 decision heuristics + expression DNA + values and anti-patterns + honest limits, written into SKILL.md.

**4. Quality validation**: test with 3 questions the person publicly answered; the direction must match. Then test with 1 adjacent question they never addressed; the skill should show calibrated uncertainty, not fake confidence.

Full methodology in `references/extraction-framework.md`.

---

## Repository structure

```
nuwa-skill/
├── SKILL.md                      # Nuwa herself
├── references/
│   ├── extraction-framework.md   # Extraction methodology (read this for depth)
│   └── skill-template.md         # Template for generating skills
└── examples/                          # 13 people + 1 topic, with full research
    ├── steve-jobs-perspective/        # ⭐ Jobs (includes a live conversation log)
    ├── paul-graham-perspective/       # Paul Graham
    ├── zhang-yiming-perspective/      # Zhang Yiming
    ├── andrej-karpathy-perspective/   # Karpathy
    ├── ilya-sutskever-perspective/    # Ilya Sutskever
    ├── trump-perspective/             # Trump
    ├── mrbeast-perspective/           # MrBeast
    ├── elon-musk-perspective/         # Musk
    ├── munger-perspective/            # Charlie Munger
    ├── feynman-perspective/           # Feynman
    ├── naval-perspective/             # Naval Ravikant
    ├── taleb-perspective/             # Taleb
    ├── zhangxuefeng-perspective/      # Zhang Xuefeng
    └── x-mastery-mentor/             # X Mentor (topic skill)
```

Research is fully transparent. Every example includes the complete research files, so you can see how information was collected, filtered, and turned into mental models. The Jobs example also includes a full multi-turn conversation log (discussing AI hardware, OpenAI vs. Anthropic, Apple's next move) to show the skill in action.

---

## Backstory

[colleague-skill](https://github.com/titanwings/colleague-skill) went viral on GitHub recently, distilling departing colleagues into AI skills and crossing 5,000 stars in days. It proved one thing: distilling a person is completely viable.

So if we can distill people, why stop at the people next to us? Go distill the best minds in every field. Lucky for us, these people usually left behind mountains of distillable material: books, talks, interviews, social media. That is an enormous augmentation of your own thinking.

I have been doing something like this for a while: not distilling colleagues, but Munger, Feynman, Naval, Musk, Taleb. Today I am open-sourcing the methodology.

Nuwa doesn't copy people. It extracts a cognitive operating system.

**Nuwa (女娲)** is the goddess in Chinese mythology who created humans from clay. Here the clay is public information, and what is created is not a person, it is a mirror.

---

## About the author

**Huashu (花叔)**: AI Native Coder, indie developer. Notable work: Kitten Fill Light (#1 on China App Store paid chart). Runs 40+ custom skills in Claude Code. Nuwa is the skill that makes skills.

| Platform | Link |
|---|---|
| 🌐 Website | [bookai.top](https://bookai.top) · [huasheng.ai](https://www.huasheng.ai) |
| 𝕏 Twitter | [@AlchainHust](https://x.com/AlchainHust) |
| 📺 Bilibili | [花叔](https://space.bilibili.com/14097567) |
| ▶️ YouTube | [@Alchain](https://www.youtube.com/@Alchain) |
| 📕 Xiaohongshu | [花叔](https://www.xiaohongshu.com/user/profile/5abc6f17e8ac2b109179dfdf) |
| 💬 WeChat Official Account | Search "花叔" (Huashu) or scan the QR code below |

<img src="wechat-qrcode.jpg" alt="WeChat Official Account QR code" width="360">

## License

MIT. Use it, change it, build with it.

---

<div align="center">

**colleague-skill** distilled what a person does.<br>
**Nuwa** distills how a person thinks.<br><br>
*The next person you want to distill doesn't have to be a colleague.*

<br>

MIT License © [Huashu (花叔)](https://github.com/alchaincyf)

</div>
