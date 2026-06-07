# Spec: Dashboard Stage Overview

## ADDED

### Capability: Stage Status Display

The dashboard MUST display all 7 pipeline stages with their current status and gate results.

**Requirements:**
- Each stage card shows: stage name, status badge (pending/running/done/failed), gate result badge (pass/fail/N/A), completion timestamp
- Stages are displayed in pipeline order (0 Brief → 6 Retro)
- Overall run status is shown at the top (in-progress / complete / failed)
- Progress bar shows stage completion ratio (N/7)

**Source:** 03-prd.md — US-1 (View Pipeline Run Overview)

**Verification:**
- Dashboard renders 7 stage cards with correct names
- Status badges match gates.json data
- Progress bar width equals (completed_stages / 7) * 100%
- Mobile layout (≤480px) shows all stage info without horizontal scroll

### Capability: Run Metadata

The dashboard MUST display run-level metadata.

**Requirements:**
- Project slug displayed in header
- Overall stage count (X/7 complete)
- Overall gate count (Y/Z passed)
- Run date/timestamp
