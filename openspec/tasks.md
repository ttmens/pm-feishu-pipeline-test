# Tasks — PM Pipeline Dashboard MVP

Vertical slices mapped to 03-prd.md user stories. Each task is independently verifiable.

## Slice 1: Dashboard Shell + Run Overview (US-1)

- [ ] **T1.1** Create `docs/index.html` with HTML skeleton, viewport meta, and CSS variables per `04-mvp/DESIGN.md` tokens.
  - Verify: Page loads with correct font stack, colors, and responsive viewport on mobile.
  - Done-when: Lighthouse mobile score ≥ 80; no horizontal scroll at 375px.

- [ ] **T1.2** Build run status header with project slug, overall status badge, and stage completion count.
  - Verify: Header shows "feishu-pipeline-test", "Complete" badge, "7 / 7 stages done".
  - Done-when: Static data renders correctly; badge colors match design tokens.

- [ ] **T1.3** Add progress bar showing stage completion ratio (N/7).
  - Verify: Bar fills to 100% for complete run; width updates with data change.
  - Done-when: CSS width property correctly calculated from completed stage count.

## Slice 2: Stage Card List (US-1)

- [ ] **T2.1** Render 7 stage cards in pipeline order with name, status badge, gate badge, and timestamp.
  - Verify: All 7 stages (brief → retro) displayed with correct badges (done/pending/running).
  - Done-when: Cards match gates.json data; left border color matches gate status.

- [ ] **T2.2** Style cards with hover effects and tap-friendly sizing (≥ 44px touch target).
  - Verify: Cards have visible hover shadow; tap targets measured ≥ 44px on mobile.
  - Done-when: Passes mobile touch target audit.

## Slice 3: Stage Detail View (US-2, US-3)

- [ ] **T3.1** Implement screen navigation: clicking a stage card shows detail view with back button.
  - Verify: Click on any stage card → detail view renders; back button → overview.
  - Done-when: Navigation works for all 7 stages; no JS errors in console.

- [ ] **T3.2** Render gate results table in detail view (check name + pass/fail).
  - Verify: Table shows all gate checks for the selected stage; pass=fail rendered with correct icons/colors.
  - Done-when: Gate data matches gates.json; visual distinction between pass and fail.

- [ ] **T3.3** Render artifact links list in detail view (file name + clickable URL).
  - Verify: Each artifact link opens correct GitHub Pages/raw URL in new tab.
  - Done-when: All links resolve (no 404); target="_blank" set.

## Slice 4: External Navigation (US-4)

- [ ] **T4.1** Add footer with links to Pipeline Index, GitHub Repo, and Prototype Preview.
  - Verify: All 3 links present, open in new tabs, resolve correctly.
  - Done-when: Links match configured URLs for the current slug.

## Slice 5: Prototype Embed (US-5)

- [ ] **T5.1** Create prototype preview screen with embedded mini-dashboard.
  - Verify: Prototype screen loads via navigation; interactive elements respond.
  - Done-when: Prototype is navigable within the dashboard; fallback text shown on error.

## Slice 6: Polish & Verification

- [ ] **T6.1** Apply `04-mvp/DESIGN.md` design tokens consistently (colors, typography, spacing).
  - Verify: All CSS variables match design contract; no hardcoded hex values outside :root.
  - Done-when: `grep -r '#' docs/index.html` only finds references in `:root` block.

- [ ] **T6.2** Smoke test: open `docs/index.html` in browser, verify all screens and links.
  - Verify: All 3 screens render; all links work; no console errors.
  - Done-when: Manual pass on desktop Chrome and mobile dev tools.

- [ ] **T6.3** Write `04-mvp/README.md` with usage instructions and architecture notes.
  - Verify: README explains what the dashboard is, how it's built, and how to deploy.
  - Done-when: README covers: purpose, file structure, deploy steps, known limitations.
