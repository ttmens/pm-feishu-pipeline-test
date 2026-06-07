# 05 — Retro / 进化

## Pipeline Journey Summary

The feishu-pipeline-test project went through the complete PM pipeline v3 journey: alignment → research → analysis → planning → building → retro. This was an end-to-end test of the pipeline framework itself.

### Stage Outputs
- **00-alignment**: Project charter, stakeholder map, initial problem framing
- **01-research**: Competitive analysis, user research synthesis, Feishu integration patterns
- **02-analysis**: Requirements breakdown, technical feasibility assessment
- **03-planning**: Detailed task breakdown (T1.1–T6.3), architecture decisions, DESIGN.md
- **04-mvp**: Static dashboard (docs/index.html) with 3 screens — overview, stage detail, prototype preview. 13 tasks implemented. All validation gates passed.
- **05-retro**: This document.

### Stage timing

| Stage | Approx duration | Gate |
|-------|-----------------|------|
| align | ~3 min | pass |
| research | ~7 min | pass |
| analysis | ~5 min | pass |
| spec/prototype | ~8 min | pass |
| mvp | ~7 min | pass |
| retro | in progress | pending |

## What Worked (Hits)

1. **Pipeline structure** — The staged approach (alignment→research→analysis→planning→build→retro) provided clear handoffs and prevented scope creep. Each stage had defined outputs and validation gates.
2. **Task decomposition** — Breaking the MVP into 13 specific tasks (T1.1–T6.3) made verification objective and automated. The verify.py script caught issues before completion.
3. **Design discipline** — DESIGN.md with design tokens enforced consistency. Hex color check passed (all colors in :root only). Touch targets verified at 44px minimum.
4. **Smoke testing** — 3 screens rendered correctly, navigation worked, zero JS errors. The smoke test gave confidence before declaring MVP complete.

## What Didn't Work (Misses)

1. **GitHub push failure** — Network unavailability prevented pushing the final commit (4c06647) to GitHub. The local commit was created successfully but the remote push failed. This blocked the intended CI/CD flow and external visibility.
2. **Single-point network dependency** — The pipeline had no fallback for when GitHub was unreachable. The entire deployment step was blocked by one network issue.
3. **pm-orchestrator retro block** — Orchestrator profile lacks terminal/filesystem tools; retro file write required a coder worker in terminal lane that dispatch did not auto-spawn.

## Lessons Learned

1. **Local-first commits are valuable** — Even when the push failed, having a clean local commit (4c06647) preserved all work. The pipeline should explicitly support local-only delivery modes.
2. **Validation gates should run before network-dependent steps** — The verification (hex check, smoke test, task reference) all passed locally. This pattern should be maintained: validate locally first, then push.
3. **Retro as a first-class stage** — Having retro as the final stage ensures the pipeline learns from itself. The merge-retro-knowledge.py script feeds lessons back into the pipeline knowledge base for future runs.
4. **E2E test value** — Running the full pipeline on itself (dogfooding) revealed real operational gaps (network handling, push resilience) that unit-level testing wouldn't catch.

## Evolution

The pipeline evolved from a theoretical framework to a proven execution path. The key evolution was:
- **Stage 0-2 (Discovery)** → Framed the problem space and validated feasibility
- **Stage 3 (Planning)** → Converted ambiguity into 13 actionable tasks with clear acceptance criteria
- **Stage 4 (Building)** → Executed the plan, verified outputs, produced a working dashboard MVP
- **Stage 5 (Retro)** → Captured learnings for pipeline self-improvement

The biggest evolutionary leap was the transition from planning to building — the task decomposition held up under execution, and the validation gates prevented quality regressions. The network failure on push was a reminder that operational resilience is as important as technical correctness.
