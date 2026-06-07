# Spec: Mobile Responsiveness

## ADDED

### Capability: Mobile-First Layout

The dashboard MUST render correctly on mobile devices (Feishu phone review).

**Requirements:**
- Viewport meta tag set for mobile
- Cards and text scale to ≤480px width without horizontal scroll
- Touch targets (stage cards, buttons, links) ≥ 44px height
- Typography remains legible at mobile size (≥ 13px body text)
- Progress bar visible and proportional on mobile

**Verification:**
- Lighthouse mobile performance score ≥ 80
- No horizontal scroll at 375px viewport width
- All interactive elements tappable without zoom
- Page load time < 2s on simulated slow 4G
