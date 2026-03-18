# Zapier MCP — audit & integration playbook (beta)

**Disclaimer:** OAuth connections and “which tools appear in chat” are controlled by **Zapier’s MCP dashboard** and each **host** (Mistral Le Chat, Claude, Cursor, etc.). Scripts here **audit readiness** and **inventory 1Password**; they do **not** complete OAuth or add Zaps for you.

## Zapier MCP constants

| Item | Value |
|------|--------|
| MCP server URL (Mistral / generic HTTP MCP) | `https://mcp.zapier.com/api/v1/connect` |
| Auth mode (Mistral admin connector) | OAuth 2.1 |

## What can be scripted vs manual

| Action | Scriptable? | Notes |
|--------|-------------|--------|
| Verify `op` (1Password CLI) signed in | Yes | `scripts/zapier-mcp-audit.sh` |
| List vault items (dev/API tags) | Yes | `scripts/zapier-mcp-1password-report.sh` |
| Map item → “you still must add this app in Zapier MCP” | Doc + report | 1Password stores **secrets**; Zapier MCP exposes **actions** you enable per integration |
| Mistral admin: Add Connector → Zapier → OAuth 2.1 | Manual | Admin UI |
| Mistral user: chat.mistral.ai/connections → Connect | Manual | Per-user OAuth |
| Claude Desktop / Cursor `mcp.json` for Zapier | Manual | Paste server URL + OAuth flow per product docs |
| “Add all dev tools from 1Password” to Zapier | **Not fully automatable** | Each Zapier app/action is configured in **Zapier**; use inventory report as a **checklist** |

## Mistral Le Chat (admin)

1. Copy server address: `https://mcp.zapier.com/api/v1/connect`
2. Mistral admin → **Connectors** → **Add Connector** → **Zapier**
3. Paste URL → Authentication **OAuth 2.1** → **Connect**
4. Org-wide connector; **actions you add** on the Zapier side are what the assistant can use.

## Mistral Le Chat (user)

1. `https://chat.mistral.ai/connections`
2. Find Zapier → **Connect** → complete OAuth
3. Manage via **Tools** in chat

## Audit commands (repo root)

```bash
# Full audit (1Password + env presence checks)
./scripts/zapier-mcp-audit.sh

# 1Password-only inventory (configure vault/tag via env)
ZAPIER_MCP_1P_VAULT="YourVault" ZAPIER_MCP_1P_TAG="dev-api" ./scripts/zapier-mcp-1password-report.sh

# Several tags (e.g. dev, api, mcp) in one go
ZAPIER_MCP_1P_VAULT="Private" ZAPIER_MCP_1P_TAGS="dev,api,mcp,work" ./scripts/zapier-mcp-1password-multi-tag.sh
```

## Security

- Never commit OAuth tokens or API keys; use **1Password** + `op run` or `op://` references where your stack supports it.
- Zapier MCP executes **real** actions; review **which Zaps** are exposed and use least privilege.
- Beta products: re-run audits after host (Mistral/Anthropic/OpenAI) doc changes.

## Relevant API keys in 1Password (typical labels)

Use the 1Password report script output as a checklist to ensure items exist; then in **Zapier**, connect the same apps (Slack, Gmail, HubSpot, etc.) and enable only the actions you want on the MCP server.

- Mistral / OpenAI / Anthropic API keys (for **API** MCP servers — separate from Zapier MCP)
- OAuth apps: Google, Microsoft, Atlassian, etc. (often **per-Zapier** connection, not copied from 1Password)

## Standards note (oversight)

Treat Zapier MCP like any privileged integration: document **who enabled which tools**, **periodic access review**, and **human approval** for high-risk actions (ABA/Sedona-style oversight for legal-adjacent workflows).
