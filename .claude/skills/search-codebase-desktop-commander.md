---
description: Search codebase systematically using Desktop Commander's ripgrep-powered search
---

Use Desktop Commander MCP to search for: {{pattern}}

## Process

### Phase 1 - Plan
1. Understand what the user is looking for
2. Identify relevant file types and patterns

### Phase 2 - Execute Search
3. Use `start_search` for content search
4. Use `start_search` with `type:"file"` for filename search
5. Use `get_more_search_results` for pagination
6. Track all matches found

### Phase 3 - Analyze
7. Group results by file/relevance
8. Extract key context from matches
9. Identify patterns across files

### Phase 4 - Report
10. Present findings organized by:
    - File location
    - Match context
    - Relevance to query
    - Action items if any

## Search Tips

### Content Search
```
Use start_search with:
- pattern: The text/regex to find
- filePattern: Optional glob to filter files
```

### File Name Search
```
Use start_search with:
- type: "file"
- pattern: Filename pattern (glob or regex)
```

### Pagination
```
Use get_more_search_results with:
- searchId: From start_search response
- offset: Where to start fetching
- length: Number of results to fetch
```

## Available Tools
- `start_search` - Start streaming search
- `get_more_search_results` - Get paginated results
- `stop_search` - Stop active search
- `list_searches` - List active searches
