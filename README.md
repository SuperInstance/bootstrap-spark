# Bootstrap Spark Protocol

**Six markdown files. Any agent that finds them knows what this repo is, what it's for, and how to work with it.**

A `.spark/` directory is the smallest self-describing unit of agent knowledge. Drop it into any repo. Any agent — or any human — that finds it can orient themselves within seconds. No README parsing, no guessing at project structure, no training data required.

---

## The Problem

Every repo has a README. But READMEs are written for humans. They describe what the project *does* — not what it *is*, not what decisions shaped it, not what's currently being worked on, not what's still unknown.

When a new agent walks into a codebase, it needs answers to six questions:

1. What is this thing?
2. What are we doing right now?
3. Why did we make the choices we made?
4. What language does this project speak?
5. What have we already learned?
6. What don't we know?

The `.spark/` directory answers all six.

---

## The Directory

```
.spark/
├── SHELL.md       → What this repo IS (not just what it does)
├── tasks.md       → Active work, blockers, priorities
├── decisions.md   → Why we chose X over Y
├── domains.md     → Key terms, concepts, the project's language
├── lessons.md     → What we've proven and disproven
└── questions.md   → Unknowns, risks, research needed
```

## Quick Start

```bash
# Initialize a spark in any repo
cp -r .spark-template/.spark ./

# Validate it
python sparkcheck.py ./.spark
```

Six files. No dependencies. No build step. Any agent that can read markdown can use this.

---

## Philosophy

**Minimal.** Six files is the minimum viable self-description. Add more as the project grows, but start here.

**Portable.** Any agent from any vendor, any model, any runtime can read markdown. No schema, no parser, no API.

**Living.** These files change as the project changes. Out-of-date documentation is worse than no documentation. Keep the spark burning.

**Self-describing.** A repo with `.spark/` explains itself to any agent that encounters it. No handshake, no onboarding, no gatekeeping.

---

## How It Fits

The Bootstrap Spark is part of a suite of fleet survival protocols:

| Protocol | Purpose |
|----------|---------|
| **[bootstrap-spark](https://github.com/SuperInstance/bootstrap-spark)** | Agent discovers what a repo IS (this) |
| **[bottle-protocol](https://github.com/SuperInstance/bottle-protocol)** | Agents communicate via git |
| **[casting-call](https://github.com/SuperInstance/casting-call)** | Vessels know which model plays which role |
| **[baton-skill](https://github.com/SuperInstance/baton-skill)** | Agents hand off work to successors |
| **[agent-bootcamp](https://github.com/SuperInstance/agent-bootcamp)** | New agents level up through challenges |

---

## License

MIT
