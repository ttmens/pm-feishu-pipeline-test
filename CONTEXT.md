# Context — feishu-pipeline-test

## Glossary

| Term | Definition |
|------|------------|
| **PM Pipeline v3** | The 7-stage gated workflow (brief → align → research → analysis → spec → MVP → retro) for taking a product idea to a working MVP, orchestrated via Hermes Kanban with specialist profiles per stage. |
| **Gate** | A validation checkpoint between pipeline stages. Each stage must pass its gate (verified by `validate-gates.py`) before the next stage's Kanban task promotes from `todo` to `ready`. Gate failure blocks promotion and triggers Feishu notification. |
| **Kanban Fan-out** | The decomposition pattern where an orchestrator creates child tasks (`kanban_create`) with explicit `parents` arrays, forming a DAG. Child tasks stay in `todo` until all parents reach `done`, then auto-promote to `ready`. |
| **Superpowers Chain** | The mandatory skill sequence in the MVP stage: `plan` → `test-driven-development` → `opencode` → `requesting-code-review` → `dogfood`. Each skill must complete before the next starts. |
| **Self-Evolution** | The pipeline's feedback loop: each run's retro produces `skill_patch_proposals` that improve pipeline skills, `pipeline-knowledge` docs that capture patterns/anti-patterns, and `feedback.jsonl` entries for cross-run tracking. |
| **Slug** | A URL-safe identifier for a pipeline run (e.g., `feishu-pipeline-test`). Used in project directory path (`pm-{slug}`), GitHub repo name, and GitHub Pages URL. |

## Project Context

This is an **end-to-end validation run** of the PM pipeline v3. The "product" is the pipeline's own correctness — confirming that a Feishu-triggered idea flows through all stages, produces required artifacts, passes gates, and deploys to GitHub Pages.

**Parent idea:** Idea: PM pipeline v3 e2e test
**Project directory:** `D:/workspace/projects/pm-feishu-pipeline-test/`
**GitHub:** `https://github.com/ttmens/pm-feishu-pipeline-test`
**Pages:** `https://ttmens.github.io/pm-feishu-pipeline-test/`

## Key Stakeholders

- **Pipeline operator:** Runs and monitors the pipeline, reviews gate results
- **Feishu user:** Triggers the pipeline via `/goal` command
- **Downstream consumers:** Future pipeline runs that depend on validated stage behavior
