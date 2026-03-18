#!/usr/bin/env bash
# Zapier MCP readiness audit: 1Password CLI, optional env hints, static checklist.
# Does NOT perform OAuth or modify Zapier/Mistral. Repo root or any CWD.

set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
REPORT_DATE="$(date -u +"%Y-%m-%dT%H:%M:%SZ")"

echo "=========================================="
echo "Zapier MCP audit — $REPORT_DATE"
echo "=========================================="
echo ""

echo "## Zapier MCP endpoints"
echo "  Server URL (HTTP MCP): https://mcp.zapier.com/api/v1/connect"
echo "  Mistral admin: Connectors → Add Connector → Zapier → OAuth 2.1"
echo "  Mistral users: https://chat.mistral.ai/connections"
echo ""

echo "## 1Password CLI"
if ! command -v op &>/dev/null; then
  echo "  STATUS: op not found — install: https://developer.1password.com/docs/cli/"
else
  if op whoami &>/dev/null; then
    echo "  STATUS: signed in as $(op whoami 2>/dev/null | head -1)"
  else
    echo "  STATUS: not signed in — run: eval \"\$(op signin)\""
  fi
fi
echo ""

echo "## Optional env file (presence only, no values)"
ENV_FILE="${ROOT}/.env"
if [[ -f "$ENV_FILE" ]]; then
  for key in MISTRAL_API_KEY OPENAI_API_KEY ANTHROPIC_API_KEY ZAPIER_MCP_1P_VAULT ZAPIER_MCP_1P_TAG; do
    if grep -q "^${key}=" "$ENV_FILE" 2>/dev/null && ! grep -q "^${key}=$" "$ENV_FILE" 2>/dev/null && ! grep -q "^${key}=[[:space:]]*$" "$ENV_FILE" 2>/dev/null; then
      echo "  $key: set (value hidden)"
    else
      echo "  $key: missing or empty"
    fi
  done
else
  echo "  No .env at repo root (optional for this audit)"
fi
echo ""

echo "## Suggested next steps (manual)"
echo "  [ ] Zapier: MCP server → enable only needed actions (principle of least privilege)"
echo "  [ ] Mistral admin: connector installed with OAuth 2.1"
echo "  [ ] Each user: authorize at chat.mistral.ai/connections"
echo "  [ ] Run: ZAPIER_MCP_1P_VAULT=... ./scripts/zapier-mcp-1password-report.sh"
echo ""
echo "Docs: ${ROOT}/docs/ZAPIER_MCP_AUDIT.md"
echo "Done."
