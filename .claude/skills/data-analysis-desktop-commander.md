---
description: Analyze CSV, Excel, and JSON data files using Desktop Commander MCP
---

Use Desktop Commander MCP to analyze the data file: {{file}}

## Process

### Phase 1 - Understand Structure
1. Get file info with `get_file_info` to see sheets/structure
2. Read the data with `read_file`
3. Parse into usable format (2D arrays for Excel)

### Phase 2 - Explore Data
4. Identify columns and data types
5. Check for missing values
6. Calculate basic statistics

### Phase 3 - Deep Analysis
7. Find trends and patterns
8. Identify outliers or anomalies
9. Group and aggregate as needed
10. Use `execute_code` for Python analysis if needed

### Phase 4 - Report
11. Present findings with:
    - Data overview
    - Key metrics
    - Trends and insights
    - Recommendations

## File Type Handling

### Excel Files (.xlsx, .xls, .xlsm)
- Read returns 2D JSON arrays per sheet
- Use get_file_info to see sheet names
- Read each sheet separately for large files

### CSV Files
- Parse as text or use read_file directly
- Identify delimiter automatically
- Handle headers and data rows

### JSON Files
- Parse structure (array vs object)
- Identify nested structures
- Flatten for analysis if needed

## Available Tools
- `read_file` - Read Excel, CSV, JSON directly
- `get_file_info` - Check file metadata and sheet structure
- `write_file` - Write analysis results
- `execute_code` - Run Python for complex analysis
