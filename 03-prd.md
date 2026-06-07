# 03 — Product Requirements Document: PM Pipeline Dashboard

**Project:** feishu-pipeline-test
**Stage:** Spec (Stage 4)
**Date:** 2026-06-07
**Scope:** Single-page static dashboard (per ADR-004)

---

## Vision

A browsable, shareable dashboard that lets any stakeholder understand the full status of a PM Pipeline run at a glance — what stages completed, which gates passed or failed, and where to find every artifact — without needing to clone the git repo or run CLI commands.

## Personas

| Persona | Role | Key Need |
|---------|------|----------|
| **Pipeline Operator** | DevOps/PM who runs and monitors the pipeline | See all stage statuses and gate results in one view; quickly identify failures |
| **Feishu User** | PM who triggered the pipeline via `/goal` | Know when their request is done; access the output without technical setup |
| **Stakeholder Reviewer** | Manager or team lead reviewing pipeline output | Browse artifacts and understand the run's outcome without reading raw markdown |

## User Stories

### US-1: View Pipeline Run Overview

作为 Pipeline Operator，我希望看到一个单页仪表盘列出所有 7 个流水线阶段及其状态（pending/running/done/failed）、门禁结果（pass/fail）和完成时间戳，以便我能在 10 秒内评估任意流水线运行的健康状况。

**Acceptance Criteria:**
- Dashboard displays all 7 stages: brief, align, research, analysis, spec, MVP, retro
- Each stage shows: status badge, gate result (if completed), timestamp
- Overall run status (in-progress / complete / failed) is visible at the top
- Works on mobile (Feishu phone review)

### US-2: Access Stage Artifacts

作为 Stakeholder Reviewer，我希望点击任意已完成阶段时能看到其输出产物（markdown 文件、原型、规格说明）的链接，以便我不需要浏览 git 仓库结构就能审查工作成果。

**Acceptance Criteria:**
- Each completed stage lists its output files with clickable links
- Links open in the browser (GitHub Pages or raw GitHub URLs)
- Prototype stage (02b-prototype) renders as an inline iframe preview
- At least the following artifacts are linked: 02-analysis.md, 03-prd.md, openspec/proposal.md, openspec/tasks.md

### US-3: Review Gate Results

作为 Pipeline Operator，我希望看到每个阶段的详细门禁验证结果，包括哪些检查通过、哪些失败，以便我不需要检查 CLI 输出或日志就能诊断和修复门禁失败。

**Acceptance Criteria:**
- Gate results show individual check names and pass/fail status
- Failed gates display the specific failure reason
- Overall gate summary (total pass / total fail / total checks) is visible
- Gate data is sourced from gates.json in the repo

### US-4: Navigate Between Pipeline Runs

作为 Feishu User，我希望在仪表盘上看到指向其他流水线运行的链接，以便我能跨不同产品想法比较输出结果。

**Acceptance Criteria:**
- Dashboard includes a link to the pipeline index (https://ttmens.github.io/pm-pipeline-index/)
- Dashboard shows the current project's GitHub repo link
- Links open in new tabs

### US-5: View the Interactive Prototype

作为 Stakeholder Reviewer，我希望能与嵌入在仪表盘中的可交互原型互动，以便在 MVP 构建完成前体验提议的产品。

**Acceptance Criteria:**
- Prototype from 02b-prototype/ is embedded as an iframe in the dashboard
- Prototype is navigable (clickable links/buttons work within the iframe)
- Falls back to a static preview if iframe loading fails

## Out of Scope

- Authentication or role-based access control
- Real-time status updates (dashboard is static, refreshed on each Pages deploy)
- Editing or modifying pipeline artifacts from the dashboard
- Backend API or dynamic data fetching
- Multi-run comparison within the dashboard itself

## Success Metrics

| Metric | Target | How Measured |
|--------|--------|-------------|
| Dashboard loads in < 2s on mobile | Yes | Lighthouse mobile performance score |
| All 7 stages and gates visible | 100% | Manual verification against gates.json |
| All artifact links work | 100% | Link validation during build |
| Stakeholder can understand run outcome from Pages alone | Yes | H4 hypothesis validation |
