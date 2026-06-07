# Design Contract

## Product feel

Clean, technical dashboard — think GitHub Actions run page meets Vercel deployment status. Dark-on-light, structured data, status badges. Designed for quick scanning by technical operators and Feishu mobile review.

## Colors (hex)

| Token | Hex | Usage |
|-------|-----|-------|
| `--bg` | `#f8f9fa` | Page background |
| `--card-bg` | `#ffffff` | Card/container background |
| `--text-primary` | `#1a1a2e` | Headings, body text |
| `--text-secondary` | `#6c757d` | Labels, timestamps |
| `--accent` | `#4361ee` | Links, active elements |
| `--success` | `#2ec4b6` | Pass / complete / done |
| `--warning` | `#ff9f1c` | Running / pending |
| `--danger` | `#e63946` | Fail / blocked |
| `--border` | `#e9ecef` | Card borders, dividers |

## Typography

- **Font stack:** `-apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif`
- **Headings:** 600 weight, `--text-primary`
- **Body:** 400 weight, 16px base, `--text-primary`
- **Meta/labels:** 13px, `--text-secondary`
- **Status badges:** 12px, 600 weight, uppercase

## Component notes

- **Status badges:** Pill-shaped (border-radius: 12px), colored background with white text
- **Stage cards:** White card with left border color matching gate status (green=pass, red=fail, gray=pending)
- **Progress bar:** Horizontal bar at top showing stage completion ratio
- **Prototype iframe:** Full-width embed with fallback message

## Out of scope for prototype

- Real-time polling or WebSocket updates
- User authentication
- Dark mode
- Interactive charts (stage timing graphs)
