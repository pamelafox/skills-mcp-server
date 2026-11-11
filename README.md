# Skills MCP server

A local [FastMCP](https://gofastmcp.com) server that serves every skill folder under `./skills`. Each skill is a folder containing a `SKILL.md` (with `name`/`description` frontmatter) plus any supporting files. Skills are re-read on every request, so edits show up without restarting the server.

## Configuration

Add the server to your MCP configuration, replacing the path with where you cloned this repo:

```json
"local-skills": {
  "tools": [
    "*"
  ],
  "type": "local",
  "command": "uv",
  "args": [
    "run",
    "--directory",
    "/Users/pamelafox/skills-mcp-server",
    "server.py"
  ]
},
```

> [!TIP]
> To use MCP skills in VS Code, enable this setting in your User Settings JSON:
>
> ```json
> "chat.agentHost.mcpSkills.enabled": true
> ```

## Running over HTTP

The server uses stdio by default. To serve over HTTP instead:

```shell
uv run server.py --http --port 8001
```

## Adding skills

Create a new folder under `skills/` with a `SKILL.md` file, for example `skills/release-notes/SKILL.md`.
