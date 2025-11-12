#!/usr/bin/env python3
"""
Harvest script to copy Claude Code files from existing projects into templates.

This script helps you extract CLAUDE.md, commands, MCP configs, and AI docs
from your existing projects to build reusable templates.
"""

import argparse
import shutil
from pathlib import Path
from typing import List, Optional


class Harvester:
    """Harvest Claude Code assets from existing projects."""

    def __init__(self, source_project: Path, template_name: str):
        """
        Initialize harvester.

        Args:
            source_project: Path to the source project to harvest from
            template_name: Name of the template to create/update
        """
        self.source = Path(source_project).resolve()
        self.forge_root = Path(__file__).parent.parent
        self.template_dir = self.forge_root / "templates" / template_name
        self.ai_docs_dir = self.forge_root / "ai_docs_sources"

        if not self.source.exists():
            raise ValueError(f"Source project does not exist: {self.source}")

    def harvest_claude_md(self) -> bool:
        """Copy CLAUDE.md file if it exists."""
        source_file = self.source / "CLAUDE.md"
        if source_file.exists():
            dest = self.template_dir / "CLAUDE.md"
            dest.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(source_file, dest)
            print(f"✅ Copied CLAUDE.md")
            return True
        else:
            print(f"⚠️  No CLAUDE.md found")
            return False

    def harvest_commands(self, command_names: Optional[List[str]] = None) -> int:
        """
        Copy .claude/commands/ directory or specific commands.

        Args:
            command_names: Optional list of specific command filenames to copy

        Returns:
            Number of commands copied
        """
        source_commands = self.source / ".claude" / "commands"
        if not source_commands.exists():
            print(f"⚠️  No .claude/commands/ directory found")
            return 0

        dest_commands = self.template_dir / ".claude" / "commands"
        dest_commands.mkdir(parents=True, exist_ok=True)

        copied = 0
        if command_names:
            # Copy specific commands
            for cmd_name in command_names:
                source_file = source_commands / cmd_name
                if source_file.exists():
                    shutil.copy2(source_file, dest_commands / cmd_name)
                    print(f"✅ Copied command: {cmd_name}")
                    copied += 1
                else:
                    print(f"⚠️  Command not found: {cmd_name}")
        else:
            # Copy all commands
            for cmd_file in source_commands.glob("**/*.md"):
                relative_path = cmd_file.relative_to(source_commands)
                dest_file = dest_commands / relative_path
                dest_file.parent.mkdir(parents=True, exist_ok=True)
                shutil.copy2(cmd_file, dest_file)
                print(f"✅ Copied command: {relative_path}")
                copied += 1

        return copied

    def harvest_settings(self) -> bool:
        """Copy .claude/settings.local.json if it exists."""
        source_file = self.source / ".claude" / "settings.local.json"
        if source_file.exists():
            dest = self.template_dir / ".claude" / "settings.local.json"
            dest.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(source_file, dest)
            print(f"✅ Copied settings.local.json")
            return True
        else:
            print(f"⚠️  No settings.local.json found")
            return False

    def harvest_mcp_config(self) -> bool:
        """Copy .mcp.json if it exists."""
        source_file = self.source / ".mcp.json"
        if source_file.exists():
            dest = self.template_dir / ".mcp.json"
            dest.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(source_file, dest)
            print(f"✅ Copied .mcp.json")
            return True
        else:
            print(f"⚠️  No .mcp.json found")
            return False

    def harvest_ai_docs(self, target_subdir: str = "general") -> int:
        """
        Copy AI documentation to ai_docs_sources.

        Args:
            target_subdir: Subdirectory name in ai_docs_sources

        Returns:
            Number of files copied
        """
        # Common AI docs locations
        possible_locations = [
            self.source / "PRPs" / "ai_docs",
            self.source / "ai_docs",
            self.source / "docs" / "ai",
        ]

        source_dir = None
        for loc in possible_locations:
            if loc.exists():
                source_dir = loc
                break

        if not source_dir:
            print(f"⚠️  No AI docs directory found")
            return 0

        dest_dir = self.ai_docs_dir / target_subdir
        dest_dir.mkdir(parents=True, exist_ok=True)

        copied = 0
        for doc_file in source_dir.glob("**/*.md"):
            relative_path = doc_file.relative_to(source_dir)
            dest_file = dest_dir / relative_path
            dest_file.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(doc_file, dest_file)
            print(f"✅ Copied AI doc: {relative_path}")
            copied += 1

        return copied

    def harvest_gitignore(self) -> bool:
        """Copy .gitignore if it exists."""
        source_file = self.source / ".gitignore"
        if source_file.exists():
            dest = self.template_dir / ".gitignore"
            dest.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(source_file, dest)
            print(f"✅ Copied .gitignore")
            return True
        else:
            print(f"⚠️  No .gitignore found")
            return False

    def harvest_prp_templates(self) -> int:
        """Copy PRP templates if they exist."""
        source_dir = self.source / "PRPs" / "templates"
        if not source_dir.exists():
            print(f"⚠️  No PRP templates found")
            return 0

        dest_dir = self.template_dir / "PRPs" / "templates"
        dest_dir.mkdir(parents=True, exist_ok=True)

        copied = 0
        for template_file in source_dir.glob("*.md"):
            shutil.copy2(template_file, dest_dir / template_file.name)
            print(f"✅ Copied PRP template: {template_file.name}")
            copied += 1

        return copied

    def harvest_all(self, include_ai_docs: bool = True, ai_docs_subdir: str = "general") -> dict:
        """
        Harvest all available assets from the source project.

        Args:
            include_ai_docs: Whether to copy AI documentation
            ai_docs_subdir: Subdirectory for AI docs

        Returns:
            Dictionary with counts of what was copied
        """
        print(f"\n🌾 Harvesting from: {self.source.name}")
        print(f"📦 Template: {self.template_dir.name}\n")

        results = {
            "claude_md": self.harvest_claude_md(),
            "commands": self.harvest_commands(),
            "settings": self.harvest_settings(),
            "mcp_config": self.harvest_mcp_config(),
            "gitignore": self.harvest_gitignore(),
            "prp_templates": self.harvest_prp_templates(),
            "ai_docs": 0,
        }

        if include_ai_docs:
            results["ai_docs"] = self.harvest_ai_docs(ai_docs_subdir)

        print(f"\n✨ Harvest complete!")
        print(f"   Commands: {results['commands']}")
        print(f"   PRP templates: {results['prp_templates']}")
        print(f"   AI docs: {results['ai_docs']}")

        return results


def main():
    """Main CLI entry point."""
    parser = argparse.ArgumentParser(
        description="Harvest Claude Code assets from existing projects"
    )
    parser.add_argument(
        "source",
        help="Path to source project (relative or absolute)",
    )
    parser.add_argument(
        "--template",
        "-t",
        default="base",
        help="Template name to create/update (default: base)",
    )
    parser.add_argument(
        "--commands",
        "-c",
        nargs="+",
        help="Specific command files to copy (default: all)",
    )
    parser.add_argument(
        "--no-ai-docs",
        action="store_true",
        help="Skip copying AI documentation",
    )
    parser.add_argument(
        "--ai-docs-subdir",
        default="general",
        help="Subdirectory for AI docs in ai_docs_sources (default: general)",
    )

    args = parser.parse_args()

    try:
        harvester = Harvester(args.source, args.template)

        if args.commands:
            # Harvest specific items
            print(f"\n🌾 Harvesting specific items from: {harvester.source.name}\n")
            harvester.harvest_claude_md()
            harvester.harvest_commands(args.commands)
            harvester.harvest_settings()
        else:
            # Harvest everything
            harvester.harvest_all(
                include_ai_docs=not args.no_ai_docs,
                ai_docs_subdir=args.ai_docs_subdir,
            )

    except Exception as e:
        print(f"❌ Error: {e}")
        return 1

    return 0


if __name__ == "__main__":
    exit(main())
