# Bootstrap Spark Protocol

> A `.spark/` directory is the smallest self-describing unit of agent knowledge. 
> Drop it into any repo. Any agent that finds it knows what this project is, 
> what it's for, and how to work with it.

## What is this?

The Bootstrap Spark is a lightweight convention — a standard directory structure 
that lets any agent (or human) orient themselves in a codebase within seconds.

## The `.spark/` Directory

```
.spark/
├── SHELL.md       # Self-describing knowledge — what this repo IS
├── tasks.md       # Active work — what's being done right now
├── decisions.md   # Architectural choices — why things are this way
├── domains.md     # Concepts — the language of this project
├── lessons.md     # Learnings — what we've proven or disproven
└── questions.md   # Open questions — what we don't know yet
```

## Quick Start

```bash
# Copy the template into your repo
cp -r .spark-template/.spark ./

# Validate your .spark/ directory
python sparkcheck.py ./.spark
```

## Philosophy

- **Minimal**: Six files, no dependencies, no build step.
- **Portable**: Any agent that can read markdown can use this.
- **Living**: These files change as the project changes.
- **Self-describing**: A repo with `.spark/` explains itself.

## Files

| File | Purpose | Audience |
|------|---------|----------|
| `SHELL.md` | What this repo is, what it does, who owns it | New agents, new humans |
| `tasks.md` | Current work, blockers, priorities | Contributors, collaborators |
| `decisions.md` | Why we chose X over Y | Future maintainers |
| `domains.md` | Key terms, concepts, boundaries | Anyone learning the system |
| `lessons.md` | What's worked, what hasn't | Future decision-makers |
| `questions.md` | Unknowns, risks, research needed | Researchers, architects |
