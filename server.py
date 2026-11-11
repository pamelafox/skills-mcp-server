"""Local FastMCP server that serves every skill folder under ./skills.

Each skill is a folder containing a SKILL.md (with name/description frontmatter)
plus any supporting files. Skills are re-read on every request, so edits show up
without restarting the server.
"""

import argparse
from pathlib import Path

from fastmcp import FastMCP, Skill
from fastmcp.skills.provider import SkillCatalogProvider

SKILLS_DIR = Path(__file__).parent / "skills"


class LocalSkills(SkillCatalogProvider):
    def __init__(self, root: Path) -> None:
        super().__init__([])
        self.root = root

    async def load_skills(self) -> list[Skill]:
        return [
            Skill.from_directory(path)
            for path in sorted(self.root.iterdir())
            if (path / "SKILL.md").is_file()
        ]


mcp = FastMCP("Local Skills")
mcp.add_provider(LocalSkills(SKILLS_DIR))


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--http", action="store_true", help="Serve over HTTP instead of stdio")
    parser.add_argument("--port", type=int, default=8001)
    args = parser.parse_args()
    if args.http:
        mcp.run(transport="http", host="127.0.0.1", port=args.port)
    else:
        mcp.run()
