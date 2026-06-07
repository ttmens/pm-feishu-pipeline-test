# PM Pipeline Dashboard MVP — feishu-pipeline-test

## Purpose

A browsable, shareable static dashboard that lets any stakeholder understand the full status of a PM Pipeline run at a glance — what stages completed, which gates passed or failed, and where to find every artifact — without needing to clone the git repo or run CLI commands.

## File Structure

```
04-mvp/
├── DESIGN.md          # Design contract: colors, typography, component notes
├── README.md          # This file
└── docs/
    └── index.html     # Single-page dashboard (deployed to GitHub Pages)
```

## Architecture

- **Single HTML file** with embedded CSS and vanilla JavaScript — no build step, no framework, no backend
- **CSS custom properties** (design tokens) defined in `:root` — all color values centralized per `DESIGN.md`
- **Static data** stored in a `stageData` JavaScript array — each stage has name, description, status, gate results, timestamps, and artifact links
- **Three screens** toggled via `showScreen()` function:
  1. **Dashboard Overview** — run status header, progress bar, 7 stage cards
  2. **Stage Detail** — gate results table, artifact links list
  3. **Prototype Preview** — embedded mini-dashboard with fallback

## Design Tokens

All colors are defined as CSS variables in `:root` (see `DESIGN.md`). No hardcoded hex values appear outside the `:root` block.

| Token | Value |
|-------|-------|
| `--bg` | `#f8f9fa` |
| `--card-bg` | `#ffffff` |
| `--text-primary` | `#1a1a2e` |
| `--text-secondary` | `#6c757d` |
| `--accent` | `#4361ee` |
| `--success` | `#2ec4b6` |
| `--warning` | `#ff9f1c` |
| `--danger` | `#e63946` |
| `--border` | `#e9ecef` |

## How to Deploy

1. Commit the `04-mvp/docs/` directory to the repository
2. Enable GitHub Pages on the repository settings (Settings → Pages → Source: main branch, `/docs` folder)
3. The dashboard will be available at `https://<username>.github.io/<repo>/`

Alternatively, open `docs/index.html` directly in any browser — no server required.

## MVP Flows (per openspec/tasks.md)

Three user flows implemented across 13 tasks (T1.1–T6.3):

1. **Dashboard Shell + Run Overview** (Slice 1, US-1) — T1.1–T1.3: viewport, status header, progress bar
2. **Stage Card List** (Slice 2, US-1) — T2.1–T2.2: 7 stage cards with badges, hover, touch targets
3. **Stage Detail View** (Slice 3, US-2/US-3) — T3.1–T3.3: navigation, gate table, artifact links
4. **External Navigation** (Slice 4, US-4) — T4.1: footer links to Pipeline Index, GitHub Repo, Prototype
5. **Prototype Embed** (Slice 5, US-5) — T5.1: embedded mini-dashboard with fallback
6. **Polish & Verification** (Slice 6) — T6.1–T6.3: design tokens, smoke test, this README

## Smoke Test

Open `docs/index.html` in a browser and verify:
- [ ] All 7 stages (Brief → Retro) render as cards with correct badges
- [ ] Clicking any card opens the detail view with gate table and artifact links
- [ ] Back button returns to overview
- [ ] Prototype Preview screen loads
- [ ] Footer links (Pipeline Index, GitHub Repo, Prototype Preview) open in new tabs
- [ ] No JavaScript errors in browser console
- [ ] Page is responsive at 375px viewport width (no horizontal scroll)

## Known Limitations

- **Static data only** — the dashboard displays hardcoded `stageData`; it does not fetch live data from APIs or parse `gates.json`
- **No authentication** — anyone with the URL can view the dashboard (by design, for shareability)
- **No real-time updates** — refresh the page to see updated status after a pipeline re-run
- **Single run only** — does not support multi-run comparison within the dashboard
- **No dark mode** — light theme only
