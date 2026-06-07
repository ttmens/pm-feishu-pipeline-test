# Design — PM Pipeline Dashboard MVP

## Architecture

The MVP is a **single-page static HTML dashboard** deployed via GitHub Pages. It reads pipeline state from `gates.json` (embedded at build time) and renders a structured view of the 7-stage pipeline run.

```
docs/index.html          ← Dashboard entry point (GitHub Pages)
gates.json               ← Gate validation results (JSON)
02b-prototype/index.html ← Clickable prototype (iframe embed)
03-prd.md                ← PRD (linked from dashboard)
openspec/                ← Spec artifacts (linked from dashboard)
```

### Data Flow

1. Pipeline stages write artifacts to the repo
2. `validate-gates.py --write` produces/updates `gates.json`
3. `build-run-report.py` reads `gates.json` + stage artifacts and generates `docs/index.html`
4. `pm-git-publish` commits and pushes; GitHub Pages serves the result

### Tech Constraints

- **Static only**: No build step, no bundler, no framework
- **No backend**: All data is embedded at build time or linked to raw GitHub URLs
- **Mobile-first**: Must render well on Feishu mobile browser
- **Self-contained**: A single HTML file with inline CSS/JS

## Screen Layout

### Screen 1: Dashboard Overview (default)
- Header: project slug, overall status badge
- Run summary card: stages complete, gates passed, date
- Progress bar
- Scrollable list of 7 stage cards (name, status badge, gate badge, timestamp)
- External links footer (Pipeline Index, GitHub Repo, Prototype Preview)

### Screen 2: Stage Detail (on card tap)
- Back button + stage name header
- Stage description
- Gate results table (check name, pass/fail)
- Artifact links list (opens in new tab)

### Screen 3: Prototype Preview
- Back button
- Embedded prototype (inline mini-dashboard for this MVP)
- Fallback text if embed fails

## State Management

Simple JS `showScreen()` function toggles `.active` class on screen divs. Stage data is hardcoded in a `stageData` array. In the real MVP, this data would be read from `gates.json` via fetch.

## Future Considerations

- Replace hardcoded `stageData` with fetch(`gates.json`)
- Add stage timing visualization
- Multi-run comparison table
- Dark mode toggle
