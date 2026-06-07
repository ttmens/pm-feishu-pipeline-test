# PM Pipeline Dashboard MVP — Implementation Plan

**Goal:** Build a single-page static HTML dashboard that displays pipeline run status, stage cards, detail views, and prototype embed.

**Architecture:** Single HTML file (docs/index.html) with embedded CSS and vanilla JS. No build step, no framework, no backend. Data is static (stageData array). Deploys to GitHub Pages.

**Tech Stack:** HTML5, CSS3 (custom properties), vanilla JS.

---

## Tasks

### Task 1: Create 04-mvp/DESIGN.md
**Files:** Create `04-mvp/DESIGN.md`
- Copy design tokens from 02b-prototype/DESIGN.md as base
- Ensure all CSS variables documented

### Task 2: Build docs/index.html (T1.1–T6.2)
**Files:** Create `04-mvp/docs/index.html`
- HTML skeleton with viewport meta (T1.1)
- CSS variables per DESIGN.md tokens in :root only (T6.1)
- Run status header with slug, badge, stage count (T1.2)
- Progress bar (T1.3)
- 7 stage cards with status/gate badges, timestamps, hover effects, touch targets ≥44px (T2.1, T2.2)
- Screen navigation: click card → detail, back button → overview (T3.1)
- Gate results table in detail view (T3.2)
- Artifact links list (T3.3)
- Footer with Pipeline Index, GitHub Repo, Prototype Preview links (T4.1)
- Prototype preview screen with embedded mini-dashboard (T5.1)
- No hardcoded hex outside :root (T6.1)

### Task 3: Write 04-mvp/README.md (T6.3)
**Files:** Create `04-mvp/README.md`
- Purpose, file structure, deploy steps, known limitations

### Task 4: Smoke test (T6.2)
- Open in browser, verify all screens render, links work, no console errors
