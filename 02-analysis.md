# 02 — Analysis Report: PM Pipeline v3 Strategic Direction

**Project:** feishu-pipeline-test
**Stage:** Analysis (Stage 3)
**Date:** 2026-06-07

---

## 1. Problem Statement

Product managers spend 15+ hours per week across 5-8 disconnected tools (Jira, Notion, Slack, analytics, feedback platforms) to move an idea from conception to implementation. Each handoff between stages — research → analysis → spec → prototype → code — involves manual context transfer, document re-authoring, and alignment meetings. AI tools on the market (Productboard, ChatPRD, Builder.io) each solve one stage well, but no single platform orchestrates the full lifecycle with quality gates between stages. The result is a fragmented process where insights from research are lost during spec-writing, and specs drift during implementation.

The PM Pipeline v3 must decide: **build a standalone end-to-end pipeline vs. integrate into existing PM toolchains vs. focus on a differentiating wedge.**

---

## 2. Options Matrix

### Option A / 方案A: Standalone End-to-End Pipeline (Recommended)

Build pm-idea-to-mvp as a fully self-contained pipeline that owns every stage from brief to retro, using Kanban-orchestrated specialist agents, OpenSpec for spec-driven development, and GitHub Pages for artifact publishing.

| Dimension | Assessment |
|---|---|
| **Scope** | Full 7-stage pipeline, zero dependency on external PM tools |
| **Build effort** | High — must build research, analysis, spec, MVP, retro capabilities from scratch |
| **Time to value** | Medium (3-6 months for production-ready) |
| **Differentiation** | Highest — no competitor covers all 7 stages with self-evolution |
| **Risk** | High — competing against entrenched tools by doing everything well |
| **Cost** | Low marginal cost per run (open-source skills, free GitHub Pages) |
| **Fit for this test** | Exact match — this IS the validation run |

### Option B / 方案B: Integration-First Pipeline

Position pm-idea-to-mvp as an orchestration layer that delegates stages to best-in-class tools: Dovetail for research, ChatPRD for PRD drafting, Builder.io for prototyping, and the pipeline only handles coordination, gates, and the retro loop.

| Dimension | Assessment |
|---|---|
| **Scope** | Orchestration + gate management; delegates 4-5 stages to external tools |
| **Build effort** | Medium — API integrations, but less original capability building |
| **Time to value** | Fast (1-3 months for MVP orchestration) |
| **Differentiation** | Medium — orchestration is n8n/Activepieces' turf; gate-driven self-evolution is the differentiator |
| **Risk** | Medium — vendor lock-in, API cost accumulation, integration fragility |
| **Cost** | Medium-high — per-seat API costs ($20-$29/mo per tool × team size) |
| **Fit for this test** | Poor — would require credentials and API keys not available |

### Option C / 方案C: Wedge-First (Self-Evolution as the Hook)

Build only the retro → skill_patch → evolution loop as the initial product, positioning it as a "pipeline improvement engine" that can sit on top of any existing PM workflow. Once users adopt the evolution loop, expand backward into earlier stages.

| Dimension | Assessment |
|---|---|
| **Scope** | Retro + evolution only initially; expand to full pipeline over time |
| **Build effort** | Low — focused scope, can be validated quickly |
| **Time to value** | Fastest (2-4 weeks for retro MVP) |
| **Differentiation** | High — zero competitors offer automated self-improvement |
| **Risk** | High — retro without the upstream pipeline context may not produce meaningful patches |
| **Cost** | Low — minimal infrastructure needed |
| **Fit for this test** | Poor — ADR-001 commits to full 7-stage validation |

### Option D / 方案D: AI-Augmented PM Copilot

Build a single-agent assistant that PMs interact with conversationally (like ChatPRD but broader), which can trigger sub-skills for research, analysis, and spec-writing on demand. No gates, no orchestration — one agent, one conversation.

| Dimension | Assessment |
|---|---|
| **Scope** | Single conversational agent with tool access |
| **Build effort** | Medium — agent framework, tool definitions, prompt engineering |
| **Time to value** | Medium (2-3 months) |
| **Differentiation** | Low — crowded space (ChatPRD, Notion AI, Cursor, Copilot) |
| **Risk** | Medium — hard to differentiate from existing AI assistants |
| **Cost** | Medium — LLM API costs scale with usage |
| **Fit for this test** | Poor — contradicts the multi-agent Kanban architecture |

### Option E / 方案E: Open-Source Pipeline Framework (Platform Play)

Publish the pm-idea-to-mvp pipeline as an open-source framework with pluggable stages. Users install via pip/npm, define their own stage configurations (YAML), and plug in custom skills. The framework provides the orchestration engine, gate system, and GitHub Pages reporting; users supply the domain-specific skills.

| Dimension | Assessment |
|---|---|
| **Scope** | Framework + core stages; users plug in custom skills per domain |
| **Build effort** | High — need plugin architecture, SDK, documentation, example pipelines |
| **Time to value** | Slow (4-6 months for stable framework) |
| **Differentiation** | Medium — open-source frameworks exist, but none with Kanban + gates + self-evolution |
| **Risk** | High — requires community adoption to be valuable; framework without users is just code |
| **Cost** | Low — open-source distribution; community contributes skills |
| **Fit for this test** | Partial — this test run validates the core, but framework features need more runs |

### Option F / 方案F: Enterprise SaaS Pipeline

Build a hosted, multi-tenant SaaS version of the pipeline with a web UI, team collaboration, role-based access, audit logs, and SLA-backed execution. The pipeline logic is the same as Option A, but delivered as a managed service.

| Dimension | Assessment |
|---|---|
| **Scope** | Full pipeline + web UI + multi-tenancy + billing + support |
| **Build effort** | Very high — infrastructure, auth, billing, monitoring, customer support |
| **Time to value** | Slow (6-12 months to production SaaS) |
| **Differentiation** | Medium — same pipeline logic as Option A, just packaged differently |
| **Risk** | Very high — SaaS requires significant capital, customer acquisition, and uptime guarantees |
| **Cost** | High — cloud infrastructure, support team, compliance |
| **Fit for this test** | Poor — premature; validate the pipeline logic first (Option A), then consider SaaS packaging |

### Option G / 方案G: VS Code / IDE Extension Pipeline

Embed the pipeline directly into the developer's IDE (VS Code, JetBrains) as an extension. PMs and engineers trigger stages from within their editor, see artifacts inline, and get real-time feedback. The pipeline runs locally or via a remote agent.

| Dimension | Assessment |
|---|---|
| **Scope** | IDE extension + local/remote pipeline execution |
| **Build effort** | Medium — IDE SDK, extension UI, local execution engine |
| **Time to value** | Medium (2-4 months) |
| **Differentiation** | Medium — IDE-native AI extensions exist (Copilot, Cursor), but none with gated PM pipelines |
| **Risk** | Medium — IDE adoption is fragmented; PMs may not use the same IDE as engineers |
| **Cost** | Low — extension distribution is free; LLM API costs per use |
| **Fit for this test** | Poor — IDE extension requires UI development outside this pipeline's scope |

---

## 3. SWOT Analysis — Option A (Standalone End-to-End Pipeline)

### Strengths
- **No competitor covers all 7 stages** — the research surveyed 8 tools; none span brief → retro
- **Self-evolution loop is unique** — retro produces skill patches that improve future runs; zero competitors
- **Open-source and free to run** — skills, gates, and pipeline logic are all open; only infra cost is LLM API calls
- **Structured handoffs** — Kanban tasks with metadata ensure context survives between stages; no information loss
- **GitHub Pages as single source of truth** — every run produces a browsable, shareable artifact index

### Weaknesses
- **High build complexity** — must be good at research, analysis, spec-writing, AND coding to be credible
- **No existing user base** — starting from zero; no network effects or data advantage
- **Rigid stage boundaries** — the gate system may feel bureaucratic for small teams that want flexibility
- **LLM quality ceiling** — all stages depend on LLM reasoning; model limitations become product limitations

### Opportunities
- **Agentic AI trend** — Productboard reports 10+ hours/week reclaimable with agent orchestration; market is moving in our direction
- **No-code/low-code movement** — PMs are building their own automations (n8n, Stackby); our pipeline is a pre-built automation
- **Enterprise PM tool fatigue** — Productboard ($20/maker/mo), Dovetail ($29/mo), Notion AI ($10/mo + AI) add up to $50+/mo; our pipeline costs a fraction
- **API-first PM tools** — most competitors have APIs; future integration is possible without changing core architecture

### Threats
- **Platform risk** — if major PM tools (Notion, Jira, Productboard) add AI agent orchestration, they could replicate our differentiation
- **LLM commoditization** — as LLM APIs become cheaper and more capable, single-agent solutions may close the gap on multi-agent orchestration
- **Adoption friction** — requires users to adopt a new workflow (Feishu → Kanban → Pages); switching costs from existing tools
- **Quality bar** — one bad MVP or inaccurate research report undermines trust in the entire pipeline

---

## 4. Explicit Recommendation (推荐方案)

**推荐：选择方案 A — 独立端到端流水线（Standalone End-to-End Pipeline）。**

Rationale:
1. **Alignment with ADR-001**: The pipeline has already committed to a full 7-stage validation run. Option A is the only choice that validates the complete architecture.
2. **Maximum whitespace**: Research confirms no competitor spans all 7 stages. This is a defensible position, not a feature chase.
3. **Self-evolution as moat**: The retro → skill_patch loop creates a compounding advantage — each run makes the pipeline smarter. Competitors would need to replicate the entire pipeline, not just a feature.
4. **Cost advantage**: Running on open-source skills + free GitHub Pages + LLM APIs is significantly cheaper than licensing 4-5 separate PM tools.
5. **This test run IS the proof**: The feishu-pipeline-test project exists to validate exactly this approach. Building anything else would invalidate the test.

---

## 5. Key Risks and Mitigations

| Risk | Likelihood | Impact | Mitigation |
|---|---|---|---|
| LLM produces low-quality research or analysis | Medium | High | Confidence tags on claims; gate validation requires ≥5 sources |
| Gate system is too rigid for real teams | Medium | Medium | Gates are configurable per project; future runs can relax criteria |
| GitHub Pages deploy latency blocks downstream stages | Low | Low | Pages deploy is async; pipeline gates check local artifacts, not Pages |
| Kanban orchestration overhead exceeds value | Low | Medium | Keep specialist profiles lean; merge stages if handoff cost > value |
| Self-evolution produces harmful skill patches | Medium | High | Human approval required before skill patches are merged (CHANGELOG.md) |
| Credential/push failures block stage completion | Medium | Low | Local commit succeeds even if push fails; artifacts are preserved |

---

## 6. Testable Hypotheses

1. **H1 — Full pipeline produces higher-quality output than individual tools**: A pipeline run that completes all 7 stages will produce more actionable and coherent artifacts than using 3 separate tools (e.g., ChatPRD + Notion + Builder.io) for the same idea.
   - *Measurement*: Compare artifact completeness scores and stakeholder satisfaction ratings.

2. **H2 — Self-evolution improves pipeline quality over time**: Pipeline runs 5+ will produce fewer gate failures and higher-confidence research claims than runs 1-4, due to skill patches accumulated from retros.
   - *Measurement*: Track gate failure rate and average confidence score across runs.

3. **H3 — Kanban-orchestrated handoffs preserve context better than manual handoffs**: Downstream stages will reference ≥80% of upstream findings without requiring re-research.
   - *Measurement*: Trace reference chains between stage artifacts (e.g., does the PRD cite specific research findings?).

4. **H4 — GitHub Pages as the artifact index is sufficient for stakeholder review**: Stakeholders can understand the full pipeline run's outcome by reviewing the Pages site alone, without accessing the git repo.
   - *Measurement*: Survey stakeholders after presenting only the Pages site.

5. **H5 — A single-page static dashboard (ADR-004) is sufficient to validate the MVP stage**: The builder stage's superpowers chain will succeed with a simple dashboard scope; complexity is not required for pipeline validation.
   - *Measurement*: Successful completion of the full superpowers chain (plan → TDD → opencode → review → dogfood) with the dashboard scope.
