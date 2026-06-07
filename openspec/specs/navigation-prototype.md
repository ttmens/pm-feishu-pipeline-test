# Spec: Navigation & External Links

## ADDED

### Capability: External Navigation

The dashboard MUST provide links to related resources.

**Requirements:**
- Link to Pipeline Index (https://ttmens.github.io/pm-pipeline-index/)
- Link to GitHub repo (https://github.com/ttmens/pm-{slug})
- Links open in new tabs

**Source:** 03-prd.md — US-4 (Navigate Between Pipeline Runs)

**Verification:**
- All external links present in footer
- Links have target="_blank"
- Links resolve to correct URLs

### Capability: Prototype Preview

The dashboard MUST provide access to the clickable prototype.

**Requirements:**
- Prototype accessible via link/button from dashboard
- Prototype is embedded inline or in iframe
- Prototype is navigable (clickable elements work)
- Falls back to static preview if iframe fails

**Source:** 03-prd.md — US-5 (View the Interactive Prototype)

**Verification:**
- Prototype screen loads without errors
- Interactive elements (buttons, links) respond to clicks
- Fallback content displays if primary embed fails
