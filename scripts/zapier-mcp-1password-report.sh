#!/usr/bin/env bash
# Inventory 1Password items for mapping to Zapier MCP checklist.
# Set ZAPIER_MCP_1P_VAULT and/or ZAPIER_MCP_1P_TAG (optional).
# Output: titles and IDs only — no secret field values.

set -euo pipefail

if ! command -v op &>/dev/null; then
  echo "ERROR: 1Password CLI (op) not installed."
  exit 1
fi

if ! op whoami &>/dev/null; then
  echo "ERROR: Not signed in. Run: eval \"\$(op signin)\""
  exit 1
fi

VAULT="${ZAPIER_MCP_1P_VAULT:-}"
TAG="${ZAPIER_MCP_1P_TAG:-}"

echo "=========================================="
echo "1Password inventory (Zapier MCP checklist)"
echo "Vault filter: ${VAULT:-(all accessible)}"
echo "Tag filter:   ${TAG:-(none)}"
echo "=========================================="
echo ""

ARGS=(item list --format=json)
if [[ -n "$VAULT" ]]; then
  ARGS+=(--vault "$VAULT")
fi
if [[ -n "$TAG" ]]; then
  ARGS+=(--tags "$TAG")
fi

JSON=$(op "${ARGS[@]}" 2>/dev/null) || {
  echo "WARN: item list failed (check vault name / permissions). Trying all vaults without tag..."
  JSON=$(op item list --format=json 2>/dev/null) || { echo "ERROR: op item list failed"; exit 1; }
}

if command -v jq &>/dev/null; then
  COUNT=$(echo "$JSON" | jq 'length')
  echo "Items: $COUNT"
  echo ""
  echo "$JSON" | jq -r '.[] | "\(.id)\t\(.title)\t\(.vault.name // "—")"' | while IFS=$'\t' read -r id title vname; do
    echo "  - $title  [vault: $vname]  id=$id"
  done
else
  echo "$JSON" | python3 -c "
import json, sys
data = json.load(sys.stdin)
print(f'Items: {len(data)}')
for it in data:
    vid = it.get('vault', {}) or {}
    vname = vid.get('name', '—') if isinstance(vid, dict) else '—'
    print(f\"  - {it.get('title','?')}  [vault: {vname}]  id={it.get('id','')}\")
" 2>/dev/null || echo "Install jq or use Python3 for formatted list. Raw JSON available via: op item list --format=json"
fi

echo ""
echo "Use this list as a checklist: for each app you rely on, add/enable the matching"
echo "integration in Zapier MCP (Zapier UI). 1Password holds credentials; Zapier wires actions."
