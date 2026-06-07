# Decisions — feishu-pipeline-test

## ADR-001: Pipeline test scope — full 7-stage run, not partial

**Status:** Accepted
**Context:** We could validate the pipeline with a subset of stages (e.g., align + research only) to save time, or run all 7 stages end-to-end.
**Decision:** Run all 7 stages (brief → align → research → analysis → spec → MVP → retro) to confirm the full handoff chain works, including the MVP builder stage and retro evolution feedback loop.
**Rationale:** A partial run would leave critical integration points untested (Kanban fan-in at MVP, superpowers chain, Pages deploy, retro skill patches). The cost of a full run (~24h) is acceptable for a one-time pipeline validation.
**Consequences:** Longer execution time; any single stage failure blocks the entire run.
**Date:** 2026-06-07

## ADR-002: GitHub Pages as the single source of truth for pipeline output

**Status:** Accepted
**Context:** Pipeline artifacts could be stored in multiple locations (local disk, cloud storage, GitHub wiki). We need one authoritative, shareable location.
**Decision:** All pipeline run reports, gate results, and stage artifacts are published to GitHub Pages at `https://ttmens.github.io/pm-{slug}/`. The Pages site is the single source of truth for pipeline output.
**Rationale:** Pages is free, auto-deploys on push, and provides a browsable index. It integrates with the existing pipeline index at `https://ttmens.github.io/pm-pipeline-index/`.
**Consequences:** Requires `pm-git-publish` to run after each stage; Pages deploy latency (~30s) between stage completion and visibility.
**Date:** 2026-06-07

## ADR-003: Fail-fast on gate rejection — no stage promotion on partial pass

**Status:** Accepted
**Context:** When a stage's gate check partially passes (e.g., research has 3/5 required URLs), we could promote with warnings or block entirely.
**Decision:** Block promotion entirely when any gate criterion fails. The blocked task surfaces on the Kanban board with the specific failure reason.
**Rationale:** Silent degradation would accumulate across stages, producing a final MVP built on incomplete research/analysis. Early failure is cheaper than late rework.
**Consequences:** Pipeline runs may stop mid-way, requiring human intervention to fix the upstream stage or adjust gate criteria.
**Date:** 2026-06-07

## ADR-004: Test project MVP scope — single-page static dashboard

**Status:** Accepted
**Context:** The MVP stage needs a concrete scope. We could build a complex multi-screen app or a minimal single-page dashboard.
**Decision:** The MVP is a single-page static HTML dashboard showing the pipeline run's status, gate results, and links to all artifacts. No backend, no authentication, no dynamic data.
**Rationale:** This scope is sufficient to validate the full superpowers chain (plan → TDD → opencode → review → dogfood) while keeping build time and complexity minimal. The goal is pipeline validation, not product features.
**Consequences:** The MVP will not demonstrate complex user flows or state management. Future real-product runs will need richer MVP scopes.
**Date:** 2026-06-07
