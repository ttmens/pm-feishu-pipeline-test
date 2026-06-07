# Spec: Stage Detail & Artifact Links

## ADDED

### Capability: Stage Detail View

When a user clicks/taps a stage card, the dashboard MUST show a detail view with gate results and artifact links.

**Requirements:**
- Detail view includes: stage name, description, gate results table, artifact links
- Gate results table shows each check name and pass/fail status
- Artifact links open in new browser tabs (target="_blank")
- Back button returns to the dashboard overview

**Source:** 03-prd.md — US-2 (Access Stage Artifacts), US-3 (Review Gate Results)

**Verification:**
- Clicking any stage card navigates to detail view
- Gate table renders all checks from gates.json for that stage
- All artifact links are valid URLs that resolve
- Back button restores the overview screen

### Capability: Gate Result Visibility

Each stage's gate results MUST be individually visible.

**Requirements:**
- Passed checks shown with green checkmark (✓ Pass)
- Failed checks shown with red cross (✗ Fail) with failure reason
- Gate summary (total pass / total checks) is visible
