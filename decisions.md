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

## ADR-005: Standalone end-to-end pipeline over integration-first or wedge approaches

**Status:** Accepted
**Context:** Three strategic options were evaluated: (A) standalone end-to-end pipeline, (B) integration-first orchestration layer delegating to external tools, (C) wedge-first self-evolution loop. Analysis in `02-analysis.md`.
**Decision:** Build pm-idea-to-mvp as a fully self-contained pipeline (Option A) that owns every stage from brief to retro, using Kanban-orchestrated specialist agents, OpenSpec for spec-driven development, and GitHub Pages for artifact publishing.
**Rationale:** (1) No competitor covers all 7 stages with self-evolution — this is defensible whitespace. (2) ADR-001 commits to a full 7-stage validation; Options B and C would invalidate the test. (3) Self-evolution creates a compounding moat — each run improves the pipeline. (4) Open-source skills + free GitHub Pages costs far less than licensing 4-5 separate PM tools.
**Consequences:** High build complexity — must be good at research, analysis, spec-writing, AND coding. Starting from zero user base. LLM quality ceiling constrains all stages.
**Date:** 2026-06-07
**Source:** `02-analysis.md` section 4 (Explicit Recommendation)

## ADR-006: Gate-driven quality with configurable criteria per project

**Status:** Accepted
**Context:** The gate system could be rigid (fixed criteria for all projects) or flexible (configurable per project). Rigid gates ensure consistency but may block valid runs; flexible gates risk inconsistent quality.
**Decision:** Gates are enforced with project-specific criteria defined in the gate validation script. Default criteria are strict (≥5 sources, ≥3 options, ≤5 stories) but can be overridden per project via gate configuration.
**Rationale:** This test run (feishu-pipeline-test) uses strict defaults to validate the gate mechanism itself. Future real-product runs can relax criteria based on scope and risk tolerance. The gate system's value is in its configurability, not in fixed thresholds.
**Consequences:** Gate configuration adds operational overhead; operators must understand criteria trade-offs. Inconsistent criteria across projects could make cross-run comparison harder.
**Date:** 2026-06-07
**Source:** `02-analysis.md` section 5 (Key Risks and Mitigations)

## ADR-007: LLM quality ceiling — confidence tags and source requirements as mitigation

**Status:** Accepted
**Context:** All pipeline stages depend on LLM reasoning, which means model limitations (hallucination, outdated knowledge, reasoning errors) become product limitations. Without mitigation, low-quality outputs could undermine trust in the entire pipeline.
**Decision:** Every research claim must carry a confidence tag (HIGH/MEDIUM/LOW) with explicit rationale, and the research gate requires ≥5 source URLs. The analysis gate requires ≥3 options with explicit recommendation. These requirements force the LLM to ground its outputs in verifiable sources and structured reasoning.
**Rationale:** Confidence tags make the LLM's uncertainty visible to downstream stages and human reviewers. Source requirements prevent fabricated claims. Together, they create a quality floor even when LLM capabilities vary. This approach is informed by the research findings: 8 of 10 sources confirmed tool sprawl as the #1 PM pain point, giving us HIGH confidence in the problem statement.
**Consequences:** Some stages may fail gates not because the analysis is wrong, but because the LLM didn't produce enough structured evidence. Operators may need to re-run stages or provide additional context to meet gate criteria.
**Date:** 2026-06-07
**Source:** `02-analysis.md` section 6 (Testable Hypotheses) — H1, H3
