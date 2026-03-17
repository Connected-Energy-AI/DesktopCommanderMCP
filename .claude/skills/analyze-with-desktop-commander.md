---
description: Analyze files using Desktop Commander MCP - read content, get metadata, and provide comprehensive insights
---

Use Desktop Commander MCP to analyze the file: {{file}}

## Process

### Phase 1 - Discovery
1. Get file metadata with `get_file_info`
2. Note file type, size, modification date

### Phase 2 - Content Analysis
3. Read file content with `read_file`
   - For large files, use offset/length pagination
   - For Excel files, read each sheet
   - For PDFs, extract text by pages
4. Identify the file's purpose and structure

### Phase 3 - Insights
5. Note any patterns, conventions, or anomalies
6. Identify potential issues or improvements
7. Summarize key findings

### Phase 4 - Report
8. Create a structured summary with:
   - **Overview**: What the file is
   - **Structure**: How it's organized
   - **Key Content**: Important details
   - **Recommendations**: If applicable

## Available Tools
- `get_file_info` - Get file metadata
- `read_file` - Read file content (supports Excel, PDF, text)
- `read_multiple_files` - Read multiple files at once
- `list_directory` - Explore directory structure
