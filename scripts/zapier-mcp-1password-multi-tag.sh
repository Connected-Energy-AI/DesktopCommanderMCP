#!/usr/bin/env bash
# Run 1Password inventory for each tag in ZAPIER_MCP_1P_TAGS (comma-separated).
# Example:
#   ZAPIER_MCP_1P_VAULT=Private ZAPIER_MCP_1P_TAGS=dev,api,mcp,work ./scripts/zapier-mcp-1password-multi-tag.sh

set -euo pipefail

DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
TAGS="${ZAPIER_MCP_1P_TAGS:-}"

if [[ -z "$TAGS" ]]; then
  echo "Set ZAPIER_MCP_1P_TAGS=comma,separated,tags (and optionally ZAPIER_MCP_1P_VAULT)."
  exit 1
fi

IFS=',' read -ra ARR <<< "$TAGS"
for tag in "${ARR[@]}"; do
  t="$(echo "$tag" | xargs)"
  [[ -z "$t" ]] && continue
  echo ""
  echo "########## tag: $t ##########"
  export ZAPIER_MCP_1P_TAG="$t"
  "$DIR/zapier-mcp-1password-report.sh"
done
