# deliverable-engine

> 🇰🇷 [한국어 README](./README.ko.md)

**Central quality hub that automatically structures, formats, and QC-checks every `.md` deliverable — whether produced by a domain skill or written from scratch.**

## Prerequisites

- **Claude Cowork or Claude Code** environment
- Recommended: [design-skill](https://github.com/jasonnamii/design-skill) for visual grammar cascade

## Goal

Most LLM-generated documents suffer from flat structure: conclusions buried at the end, uniform density from start to finish, and axis-by-axis enumeration that readers skim past. The deliverable engine intercepts every `.md` output and reshapes it into an hourglass structure (conclusion-first → spine → detail expansion) with deliberate density alternation across blocks. The result is a document that installs its message in the reader's mind rather than asking them to excavate it.

## When & How to Use

The engine activates automatically whenever any skill generates a `.md` file — no explicit invocation needed. It also detects documentary intent during conversation (the "1% gate") and proactively suggests switching to document mode. For direct use, include format keywords like "보고서로", "진단서로", or "리포트로" in your prompt.

## Use Cases

| Scenario | Prompt | What Happens |
|---|---|---|
| Strategy report from biz-skill | `"전략 진단해줘, 보고서로"` | biz-skill runs 18-axis analysis → deliverable engine reshapes output into narrative with density alternation |
| Quick internal note | `"회의 내용 정리해줘"` | Detected as internal/short → passthrough tier (minimal overhead) |
| Team-facing deliverable | `"팀한테 공유할 분석 리포트 만들어줘"` | External + long → full pipeline with hourglass + block design + 4-axis QC + design cascade |

## Key Features

- **3-Tier Gate** — Routes documents through full/light/passthrough pipelines based on purpose (external vs. internal) × length (20/50 line thresholds)
- **Hourglass Structure (§2)** — Conclusion-first → spine (densest section) → detail expansion. Content not subordinate to spine gets cut
- **Block Design with 7 Rules (§3)** — Density alternation (high/mid/low), mandatory transition devices between blocks, single-purpose-per-block enforcement
- **Spine Extraction Fallback** — When spine extraction fails (pure data, list-only, multiple equal conclusions), auto-classifies as reference-type document
- **Tier-based QC** — Full: 4-axis (numerical consistency, logic, style, block compliance). Light: numbers + vocabulary only. Passthrough: skip
- **Cascade Architecture** — Interceptor pattern that transforms output form without touching analysis logic

## Works With

- **[design-skill](https://github.com/jasonnamii/design-skill)** — Visual grammar and formatting (sole design authority)
- **[biz-skill](https://github.com/jasonnamii/biz-skill)** — 18-axis strategy output → narrative reshaping
- **[risk-radar](https://github.com/jasonnamii/risk-radar)** — Risk matrix → density-alternated blocks
- **[research-frame](https://github.com/jasonnamii/research-frame)** — Axis-based research → integrated deliverable
- **[trigger-dictionary](https://github.com/jasonnamii/trigger-dictionary)** — 제출청소 (pre-submission cleanup)

## Installation

```bash
git clone https://github.com/jasonnamii/deliverable-engine.git ~/.claude/skills/deliverable-engine
```

## Update

```bash
cd ~/.claude/skills/deliverable-engine && git pull
```

Skills placed in `~/.claude/skills/` are automatically available in Claude Code and Cowork sessions.

## Part of Cowork Skills

This is one of 25+ custom skills. See the full catalog: [github.com/jasonnamii/cowork-skills](https://github.com/jasonnamii/cowork-skills)

## License

MIT License — feel free to use, modify, and share.
