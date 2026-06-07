# Product Idea Brief

**Title:** PM Pipeline v3 E2E Test — feishu-pipeline-test

## Problem Statement

The PM pipeline v3 (align → research → analysis → spec → MVP → retro) needs end-to-end validation to confirm that all stages, gates, skills, and Kanban handoffs work correctly in production. This project serves as a living smoke test: run a complete idea through the pipeline, verify each gate passes, and confirm GitHub Pages deployment with a functional dashboard.

## Target User & Job-to-be-Done

**Primary user:** PM pipeline operators (developers/PMs running Hermes Agent for product ideation)
**Job-to-be-done:** Verify that a Feishu-triggered idea flows through all 7 pipeline stages without errors, producing deployable artifacts at each gate, so the team can trust the pipeline for real product ideas.

## Success Metrics

1. All 6 Kanban subtasks (align, research, analysis, spec, MVP, retro) complete without crash/block
2. `gates.json` shows `align: pass`, `research: pass`, `analysis: pass`, `spec: pass`, `mvp: pass`, `retro: pass`
3. GitHub Pages deploys successfully at `https://ttmens.github.io/pm-feishu-pipeline-test/`
4. `05-retro.md` contains at least 1 skill patch proposal for pipeline evolution
5. Total pipeline execution time < 24 hours end-to-end

## Constraints

- Must use pm-idea-to-mvp v3 stage definitions exactly (no custom stages)
- All artifacts must live under `D:/workspace/projects/pm-feishu-pipeline-test/`
- GitHub repo: `ttmens/pm-feishu-pipeline-test`
- No real product spend — this is a validation run, not a shipped product
- Each stage must produce its mandated artifacts before promoting

## Non-Goals

- Building a production-ready application
- User research with real customers
- Market validation or competitive positioning
- Revenue modeling or go-to-market strategy

## Open Assumptions

1. **[HIGH confidence]** The pipeline's Kanban decomposition (decompose-pm-pipeline) correctly creates child tasks with proper parent dependencies
2. **[MEDIUM confidence]** GitHub Pages auto-deploys on push to `main` branch (assumes repo is configured for Pages)
3. **[MEDIUM confidence]** Feishu notification routing is functional for this project's tenant
4. **[LOW confidence]** The MVP stage's OpenCode superpowers chain (plan → TDD → opencode → review → dogfood) will succeed without manual intervention on this test scope
5. **[MEDIUM confidence]** All required skills (grill-me, openspec, open-design, ui-ux-pro-max) are installed on their respective assignee profiles
