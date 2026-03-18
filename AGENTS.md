# Agent roster — DevOps, IT, CTO & CRM data ops

Use these agents in Cursor/Claude by name or by opening the matching file under `.github/agents/`.

| Agent | Role | Primary tools / surfaces |
|-------|------|---------------------------|
| **devops-platform** | CI/CD, containers, deploy scripts, env/secrets hygiene | Shell, Docker, AWS task defs, repo scripts |
| **it-integrations** | OAuth, MCP connectors, token/scopes, redirect URIs | HubSpot, Attio, Auth0 MCPs; vendor consoles |
| **cto-advisor** | Architecture, vendor fit, risk, build-vs-buy | Read-only guidance + repo patterns |
| **crm-data-ops** | Merge/dedupe contacts & companies across HubSpot, Attio, Airtable, Excel/CSV | HubSpot, Attio, Airtable MCPs; pandas/CSV in code |

## Invocation hints

- **“Run as DevOps”** → devops-platform agent.
- **“HubSpot OAuth broken / scopes / redirect”** → it-integrations agent.
- **“Should we use X or Y for CRM?”** → cto-advisor.
- **“Merge these spreadsheets with HubSpot contacts”** → crm-data-ops.

## HubSpot OAuth note

Browser history cannot be read from this workspace. For **real** OAuth audit data, use:

- HubSpot: **Settings → Integrations → Private Apps / Connected Apps** (tokens, scopes).
- Your app’s **redirect URI** and **client_id** in the developer project.
- MCP: `user-hubspot` after OAuth — validate with a simple API call (e.g. contacts read).

## Files

| File | Purpose |
|------|---------|
| [.github/agents/devops-platform.agent.md](.github/agents/devops-platform.agent.md) | Pipelines, Docker, deploy, secrets |
| [.github/agents/it-integrations.agent.md](.github/agents/it-integrations.agent.md) | OAuth, MCP, IT ops |
| [.github/agents/cto-advisor.agent.md](.github/agents/cto-advisor.agent.md) | Technical leadership patterns |
| [.github/agents/crm-data-ops.agent.md](.github/agents/crm-data-ops.agent.md) | HubSpot + Attio + Airtable + Excel/CSV |

Claude Code plugin entries: `.claude-plugin/plugins/desktop-commander-agents/plugin.json` (agents `devops-platform`, `it-integrations`, `cto-advisor`, `crm-data-ops`).
