# Desktop Commander MCP - Claude Code Plugin

> Extend Claude Code with terminal control, file operations, and AI-powered development workflows.

## Overview

This plugin integrates [Desktop Commander MCP](https://github.com/wonderwhy-er/DesktopCommanderMCP) with Claude Code, providing:

- **Terminal Control** - Run and manage processes, SSH sessions, dev servers
- **File Operations** - Read, write, search, and edit files with surgical precision
- **Document Support** - Native Excel, PDF, and DOCX handling
- **Data Analysis** - Analyze CSV/Excel/JSON files with Python execution
- **Specialized Agents** - Pre-configured AI agents for common tasks

## Installation

### Option 1: Install from Local Path (Development)

```bash
# From the DesktopCommanderMCP directory
claude plugin install ./DesktopCommanderMCP
```

### Option 2: Install from GitHub (When Published)

```bash
claude plugin marketplace add wonderwhy-er/DesktopCommanderMCP
claude plugin install desktop-commander@desktop-commander-plugins
```

### Option 3: Direct MCP Server Setup

Add to your Claude Code configuration:

```bash
claude mcp add desktop-commander -- npx -y @wonderwhy-er/desktop-commander@latest
```

## Available Commands

After installation, use these commands in Claude Code:

| Command | Shortcut | Description |
|---------|----------|-------------|
| `/dc:analyze <file>` | `/dca` | Analyze a file - read content, get metadata, provide insights |
| `/dc:search <pattern>` | `/dcs` | Search codebase using ripgrep-powered search |
| `/dc:excel <file>` | `/dcx` | Analyze Excel or CSV data files |
| `/dc:run <command>` | `/dcr` | Run terminal commands and capture output |
| `/dc:explore <directory>` | `/dce` | Explore and map unfamiliar directory structures |

## Available Agents

Invoke these specialized agents for specific tasks:

### Code Explorer Agent
```
@code-explorer Explore this codebase
```
Explores and maps unfamiliar codebases. Identifies key files, architecture, and conventions.

### Data Analyst Agent
```
@data-analyst Analyze this spreadsheet
```
Analyzes CSV, Excel, and JSON data files. Extracts insights, calculates statistics, finds trends.

### File Organizer Agent
```
@file-organizer Organize my Downloads folder
```
Organizes, renames, and restructures files. Creates logical directory hierarchies.

### Test Runner Agent
```
@test-runner Run the test suite
```
Runs tests, captures output, reports results with pass/fail counts and failure analysis.

### PDF Processor Agent
```
@pdf-processor Extract content from this PDF
```
Extracts, analyzes, and creates PDF documents. Summarizes content and finds specific sections.

## Available Skills

Skills are reusable instruction templates that guide Claude's behavior:

### `analyze-with-desktop-commander`
Systematic file analysis workflow:
1. Discovery - Get metadata
2. Content Analysis - Read with pagination
3. Insights - Find patterns and issues
4. Report - Structured summary

### `search-codebase-desktop-commander`
Comprehensive codebase search:
1. Plan - Identify patterns and file types
2. Execute - Search content and filenames
3. Analyze - Group and contextualize results
4. Report - Organized findings

### `data-analysis-desktop-commander`
Data analysis workflow:
1. Understand Structure - Sheets, columns, types
2. Explore Data - Statistics, missing values
3. Deep Analysis - Trends, patterns, anomalies
4. Report - Metrics and insights

## Configuration

Edit `.claude/settings.json` to customize:

```json
{
  "plugins": {
    "desktop-commander": {
      "config": {
        "allowedDirectories": ["/your/project/path"],
        "defaultShell": "zsh",
        "fileReadLineLimit": 2000,
        "fileWriteLineLimit": 100,
        "telemetryEnabled": true
      }
    }
  }
}
```

### Configuration Options

| Option | Type | Default | Description |
|--------|------|---------|-------------|
| `allowedDirectories` | array | `[]` | Directories accessible for file operations |
| `defaultShell` | string | `bash` | Shell for command execution |
| `fileReadLineLimit` | number | `1000` | Maximum lines to read at once |
| `fileWriteLineLimit` | number | `50` | Maximum lines to write at once |
| `telemetryEnabled` | boolean | `true` | Enable usage telemetry |

## Usage Examples

### Analyze a Code File
```
/dca src/main.ts
```

### Search for a Pattern
```
/dcs interface UserRepository
```

### Analyze Sales Data
```
/dcx Q1_Sales_Report.xlsx
```

### Run Tests
```
/dcr npm test
```

### Explore a New Project
```
/dce ../new-project
```

### Use an Agent
```
@code-explorer Map out the architecture of this repository
```

### Use a Skill
```
Use the analyze-with-desktop-commander skill to examine package.json
```

## MCP Server Tools

Desktop Commander provides these tools to Claude:

### Terminal Tools
- `start_process` - Start programs with smart detection
- `interact_with_process` - Send commands to running programs
- `read_process_output` - Read output from processes
- `force_terminate` - Terminate sessions
- `list_sessions` - List active sessions
- `list_processes` - List running processes
- `kill_process` - Terminate by PID

### Filesystem Tools
- `read_file` - Read files, URLs, Excel, PDFs
- `read_multiple_files` - Read multiple files at once
- `write_file` - Write file contents
- `write_pdf` - Create/modify PDFs
- `create_directory` - Create directories
- `list_directory` - List with depth control
- `move_file` - Move/rename files
- `start_search` - Streaming search
- `get_more_search_results` - Paginated results
- `get_file_info` - File metadata

### Text Editing
- `edit_block` - Surgical text replacements

### Configuration
- `get_config` - Get server configuration
- `set_config_value` - Update settings

### Analytics
- `get_usage_stats` - Usage statistics
- `get_recent_tool_calls` - Recent tool call history

## Troubleshooting

### Plugin Not Loading
```bash
# Reload plugins
/reload-plugins

# Check for errors
/plugin errors
```

### MCP Server Not Found
Ensure Desktop Commander is installed:
```bash
npm install -g @wonderwhy-er/desktop-commander
```

### Permission Issues
Check `allowedDirectories` in settings includes your project path.

### Search Not Working
Ensure ripgrep is available (bundled with Desktop Commander).

## Development

### Local Testing

1. Make changes to `.claude-plugin/plugin.yaml`
2. Test with:
   ```bash
   claude plugin install ./DesktopCommanderMCP --scope local
   ```
3. Reload in Claude:
   ```
   /reload-plugins
   ```

### Publishing

To publish as a marketplace plugin:

1. Create a GitHub release
2. Ensure `.claude-plugin/marketplace.json` is committed
3. Share the marketplace URL:
   ```bash
   claude plugin marketplace add wonderwhy-er/DesktopCommanderMCP
   ```

## Security Notes

⚠️ **Important**: This plugin can execute arbitrary commands and modify files.

- Only install from trusted sources
- Review `allowedDirectories` configuration
- Commands run with your user permissions
- Sensitive operations are logged in audit trail

## Links

- [Desktop Commander MCP](https://github.com/wonderwhy-er/DesktopCommanderMCP)
- [NPM Package](https://www.npmjs.com/package/@wonderwhy-er/desktop-commander)
- [Claude Code Plugins Documentation](https://docs.anthropic.com/en/docs/claude-code/plugins)

## License

MIT License - See [LICENSE](../LICENSE) for details.
