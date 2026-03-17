# Audit Report — Scripts & Homebrew Compatibility

**Date:** 2025-03-16  
**Scope:** Homebrew formulae/casks, project npm dependencies, install scripts, Node/engine compatibility.

---

## Summary

| Area | Status | Action Taken |
|------|--------|--------------|
| Homebrew | ✅ Updated | `brew update && brew upgrade` — 5 formulae + 3 casks upgraded |
| npm (safe fixes) | ✅ Applied | `npm audit fix` — 14 vulnerabilities fixed |
| npm (remaining) | ⚠️ 12 left | See "Remaining npm vulnerabilities" below |
| install.sh | ✅ Compatible | Node 22.14.0 URL verified; script is compatible |
| install-docker.sh | ✅ No brew | Uses Docker + python3 only |
| Node engine | ✅ Compatible | `package.json` engines `>=18`; system has Node 25.8.1 |

---

## 1. Homebrew

### Completed
- **`brew update`** — Already up-to-date.
- **`brew upgrade`** — Upgraded:
  - **Formulae:** simdjson, gh, qwen-code, sqlite, **node** (25.8.0 → 25.8.1)
  - **Casks:** claude-code, codex, gitkraken-cli

### Warnings (optional to address)
- **PowerShell cask:** Deprecated/disabled — consider replacing or removing if unused (`brew uninstall --cask powershell` if not needed).
- **Command Line Tools:** `brew doctor` reports:
  - No Cask quarantine support (Swift/Command Line Tools).
  - A newer Command Line Tools release is available (Xcode 26.3).
  - **Optional fix:** `xcode-select --install` or install from [developer.apple.com/download/all](https://developer.apple.com/download/all/).
- **Tier 2 configuration:** Your setup is Tier 2 for Homebrew; see [Support Tiers](https://docs.brew.sh/Support-Tiers#tier-2).
- **powershell-lts tap:** Formula uses deprecated `depends_on macos: :high_sierra`. Report to [powershell/homebrew-tap](https://github.com/powershell/homebrew-tap) if you use it.

### Project-related brew
- **PUBLISH.md** references `brew install mcp-publisher` — no change needed; ensure it’s installed when publishing.
- **Testcontainers Desktop** — Already installed and up to date (`atomicjar/tap/testcontainers-desktop`).

---

## 2. npm Dependencies

### Safe fixes applied
- **`npm audit fix`** (no `--force`) was run:
  - Updated/resolved multiple packages (e.g. hono, @hono/node-server, @modelcontextprotocol/sdk, file-type, markdown-it, minimatch, qs, serialize-javascript, tar, lodash, diff, ajv, basic-ftp).
  - **Before:** 26 vulnerabilities (7 low, 6 moderate, 12 high, 1 critical).
  - **After (safe fix):** 12 vulnerabilities remaining (5 low, 2 moderate, 5 high).

### Remaining npm vulnerabilities (12)

1. **nexe / download / got / http-cache-semantics** (high)  
   - **Fix:** `npm audit fix --force` would downgrade **nexe** to 1.1.6 (breaking change).  
   - **Recommendation:** Leave as-is unless you need to build binaries with nexe; nexe is a devDependency for packaging. If you do packaging, consider moving to a different builder or accepting the risk in a dev-only tool.

2. **tar** (high) — via **@mapbox/node-pre-gyp**  
   - **Fix:** `npm audit fix` may update tar in the tree; run again or bump **sharp** (or other deps that use node-pre-gyp) when updates are available.  
   - **Recommendation:** Re-run `npm audit fix` after dependency updates; if still present, track [node-tar](https://github.com/npm/node-tar) and [@mapbox/node-pre-gyp](https://github.com/mapbox/node-pre-gyp) for fixes.

3. **tmp** (no fix available) — via **external-editor → @inquirer/editor → @inquirer/prompts → @anthropic-ai/mcpb**  
   - **Recommendation:** No upstream fix; risk is in **@anthropic-ai/mcpb** (dev tool). Keep mcpb updated; consider reporting to Anthropic if they depend on a vulnerable tmp.

### Do not run (without explicit decision)
- **`npm audit fix --force`** — Would downgrade **nexe** and may break the build/packaging pipeline. Only use after testing.

### Deprecation warnings (informational)
- **inflight**, **npmlog**, **rimraf**, **lodash.isequal**, **glob@7**, **are-we-there-yet**, **gauge**, **fstream** — Come from transitive dependencies (e.g. nexe, nodemon, serve-handler). No change required for compatibility; consider when upgrading those deps.

---

## 3. Scripts & compatibility

### install.sh
- **Node check:** Requires Node ≥ 18; offers to install Node **v22.14.0** if missing.
- **Node URL:** `https://nodejs.org/dist/v22.14.0/node-v22.14.0.pkg` was verified (still valid).
- **Compatibility:** ✅ Script is compatible; no edits required for current Node or Homebrew.

### install-docker.sh
- Uses **Docker**, **python3** (for JSON config), and standard shell. No Homebrew or Node required.
- **Compatibility:** ✅ No changes needed.

### package.json
- **engines:** `"node": ">=18.0.0"` — ✅ Satisfied by Node 25.8.1 (Homebrew).
- **postinstall:** Runs `dist/track-installation.js` and `dist/npm-scripts/verify-ripgrep.js`; **dist** is created by `prepare`/`build`, so first install may fail postinstall until after first build (known pattern for this project).

---

## 4. Recommended ongoing commands

```bash
# Homebrew: update and upgrade (periodically)
brew update && brew upgrade

# Optional: upgrade casks that use 'version :latest' or auto_updates
brew update && brew upgrade --cask --greedy

# npm: re-check and apply safe fixes after dependency changes
npm audit
npm audit fix

# Optional: list outdated packages
npm outdated
```

---

## 5. Optional next steps

1. **Command Line Tools:** Run `xcode-select --install` or install the latest from Apple if you use Xcode/CLT heavily.
2. **PowerShell:** If you don’t use it, `brew uninstall --cask powershell` to clear the deprecated cask warning.
3. **nexe:** If you don’t build binaries, consider removing **nexe** from devDependencies to drop the got/http-cache-semantics chain; otherwise leave as-is or plan a move to another packager.
4. **Major upgrades:** Some packages have newer major versions (e.g. **glob** 13, **zod** 4, **open** 11, **isbinaryfile** 6). Test thoroughly before upgrading; current set is compatible.

---

*Report generated from audit run on 2025-03-16.*
