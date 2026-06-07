# Proposal: Standalone End-to-End PM Pipeline v3

## Why

Product managers spend 15+ hours/week across 5-8 disconnected tools moving an idea from conception to implementation. AI tools on the market (Productboard, ChatPRD, Builder.io, Dovetail) each solve one stage well, but **no single platform orchestrates the full lifecycle with quality gates between stages**. Context is lost at every handoff: research insights don't inform specs, specs drift during implementation, and lessons from completed projects aren't captured systematically.

The PM Pipeline v3 addresses this by providing a fully automated, 7-stage gated workflow (brief → align → research → analysis → spec → MVP → retro) where each stage is executed by a specialist AI agent, with structured handoffs and validation gates ensuring quality at every step.

## What changes

The pipeline introduces five capabilities that do not exist in any single competitor:

1. **Full-stage automation** — Idea to MVP in one automated pipeline, with no manual handoffs between stages. Each stage reads the previous stage's artifacts and produces structured output for the next.

2. **Kanban-orchestrated specialist agents** — Each stage is a separate Kanban task assigned to a specialist profile (pm-aligner, pm-researcher, pm-analyst, pm-planner, pm-builder), with parent-child dependencies forming a DAG. Tasks auto-promote when parents complete.

3. **Gate-driven quality control** — Every stage must pass a validation gate (enforced by `validate-gates.py`) before the next stage can begin. Gate failures block promotion and notify the operator via Feishu.

4. **OpenSpec integration** — Structured spec-driven development: the analyst drafts a proposal, the planner writes delta specs and task checklists, and the builder implements against tasks.md. Requirements are version-controlled in-repo.

5. **Self-evolution loop** — The retro stage produces skill patch proposals that improve the pipeline's own skills, knowledge docs, and feedback tracking. Each run makes the next run better.

## Impact

| Metric | Current state (manual PM workflow) | With PM Pipeline v3 |
|---|---|---|
| Time from idea to MVP artifact | Days to weeks | Hours (pipeline runtime) |
| Context loss between stages | High (manual re-authoring) | Low (structured handoffs) |
| Quality consistency | Variable (depends on individual PM) | Consistent (gate-enforced) |
| Process improvement | Ad hoc (retros rarely happen) | Automatic (every run produces patches) |
| Tool licensing cost | $50+/mo per user (4-5 tools) | LLM API costs only |

## Acceptance scenarios

1. **End-to-end run**: A Feishu user types `/goal 产品想法：{描述}`. Within one pipeline execution, all 7 stages complete, gates pass, and a GitHub Pages site is published showing the full run report.

2. **Gate enforcement**: If the research stage produces fewer than 5 source URLs, the gate fails, the analysis task does not promote, and the operator receives a Feishu notification with the specific failure reason.

3. **Self-evolution**: After a pipeline run completes, the retro stage produces at least one `skill_patch_proposal` that, when approved and merged, improves a pipeline skill's instructions, pitfalls, or verification steps.

4. **Artifact traceability**: Every stage's output can be traced back to specific inputs from prior stages. The PRD cites research findings; the MVP implements against OpenSpec tasks; the retro references gate results.
