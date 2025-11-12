#!/usr/bin/env python3
"""
Forge script to create new Claude Code projects from templates.

This script takes a template and creates a new project with all the
Claude Code configurations, commands, and documentation.
"""

import argparse
import shutil
from pathlib import Path
from typing import List, Optional
import json


class ProjectForge:
    """Create new projects from Claude Code templates."""

    def __init__(self, project_name: str, template_name: str, destination: Optional[Path] = None):
        """
        Initialize project forge.

        Args:
            project_name: Name of the new project
            template_name: Name of the template to use
            destination: Optional destination directory (default: current directory)
        """
        self.project_name = project_name
        self.template_name = template_name
        self.forge_root = Path(__file__).parent.parent
        self.template_dir = self.forge_root / "templates" / template_name
        self.ai_docs_dir = self.forge_root / "ai_docs_sources"

        if destination:
            self.dest = Path(destination).resolve() / project_name
        else:
            self.dest = Path.cwd() / project_name

        if not self.template_dir.exists():
            raise ValueError(f"Template does not exist: {template_name}")

        if self.dest.exists():
            raise ValueError(f"Project directory already exists: {self.dest}")

    def copy_template_files(self) -> int:
        """
        Copy all files from template to new project.

        Returns:
            Number of files copied
        """
        print(f"\n📋 Copying template files...")

        copied = 0
        for item in self.template_dir.rglob("*"):
            if item.is_file():
                relative_path = item.relative_to(self.template_dir)
                dest_file = self.dest / relative_path
                dest_file.parent.mkdir(parents=True, exist_ok=True)
                shutil.copy2(item, dest_file)
                print(f"   ✅ {relative_path}")
                copied += 1

        return copied

    def copy_ai_docs(self, doc_categories: Optional[List[str]] = None) -> int:
        """
        Copy AI documentation from ai_docs_sources.

        Args:
            doc_categories: Optional list of subdirectories to copy (default: all)

        Returns:
            Number of files copied
        """
        if not self.ai_docs_dir.exists():
            print(f"⚠️  No AI docs sources found")
            return 0

        dest_ai_docs = self.dest / "ai_docs"
        dest_ai_docs.mkdir(parents=True, exist_ok=True)

        print(f"\n📚 Copying AI documentation...")

        copied = 0
        if doc_categories:
            # Copy specific categories
            for category in doc_categories:
                source_dir = self.ai_docs_dir / category
                if source_dir.exists():
                    for doc_file in source_dir.rglob("*.md"):
                        relative_path = doc_file.relative_to(source_dir)
                        dest_file = dest_ai_docs / category / relative_path
                        dest_file.parent.mkdir(parents=True, exist_ok=True)
                        shutil.copy2(doc_file, dest_file)
                        print(f"   ✅ {category}/{relative_path}")
                        copied += 1
                else:
                    print(f"   ⚠️  Category not found: {category}")
        else:
            # Copy all AI docs
            for doc_file in self.ai_docs_dir.rglob("*.md"):
                relative_path = doc_file.relative_to(self.ai_docs_dir)
                dest_file = dest_ai_docs / relative_path
                dest_file.parent.mkdir(parents=True, exist_ok=True)
                shutil.copy2(doc_file, dest_file)
                print(f"   ✅ {relative_path}")
                copied += 1

        return copied

    def create_project_structure(self, include_dirs: Optional[List[str]] = None) -> None:
        """
        Create additional project directories.

        Args:
            include_dirs: Optional list of directories to create
        """
        default_dirs = ["src", "tests", "docs"]
        dirs_to_create = include_dirs if include_dirs else default_dirs

        print(f"\n📁 Creating project structure...")
        for dir_name in dirs_to_create:
            dir_path = self.dest / dir_name
            dir_path.mkdir(parents=True, exist_ok=True)
            print(f"   ✅ {dir_name}/")

    def create_gitignore(self) -> None:
        """Create or append to .gitignore with Claude Code specific entries."""
        gitignore_path = self.dest / ".gitignore"

        # Standard Claude Code entries
        claude_entries = [
            "# Claude Code",
            ".claude/settings.local.json",
            ".mcp.local.json",
            "",
            "# Python",
            "__pycache__/",
            "*.py[cod]",
            "*$py.class",
            "*.so",
            ".Python",
            "venv/",
            "venv_linux/",
            "ENV/",
            "env/",
            ".venv",
            "",
            "# IDEs",
            ".vscode/",
            ".idea/",
            "*.swp",
            "*.swo",
            "*~",
            "",
            "# OS",
            ".DS_Store",
            "Thumbs.db",
            "",
        ]

        if gitignore_path.exists():
            # Append if not already present
            existing_content = gitignore_path.read_text()
            if "# Claude Code" not in existing_content:
                with gitignore_path.open("a") as f:
                    f.write("\n" + "\n".join(claude_entries))
                print(f"   ✅ Updated .gitignore")
        else:
            gitignore_path.write_text("\n".join(claude_entries))
            print(f"   ✅ Created .gitignore")

    def create_readme(self) -> None:
        """Create a basic README.md for the new project."""
        readme_path = self.dest / "README.md"

        if readme_path.exists():
            print(f"   ⚠️  README.md already exists, skipping")
            return

        readme_content = f"""# {self.project_name}

Project created with claude-project-forge using the `{self.template_name}` template.

## Getting Started

1. Review and customize `CLAUDE.md` for project-specific guidelines
2. Explore available commands in `.claude/commands/`
3. Configure MCP servers if needed (see `.mcp.json`)
4. Check `ai_docs/` for reference documentation

## Development

[Add your development instructions here]

## Testing

[Add your testing instructions here]

## License

[Add your license here]
"""

        readme_path.write_text(readme_content)
        print(f"   ✅ Created README.md")

    def forge(
        self,
        include_ai_docs: bool = False,
        ai_doc_categories: Optional[List[str]] = None,
        extra_dirs: Optional[List[str]] = None,
    ) -> dict:
        """
        Create a complete new project from template.

        Args:
            include_ai_docs: Whether to copy AI documentation
            ai_doc_categories: Specific AI doc categories to copy
            extra_dirs: Additional directories to create

        Returns:
            Dictionary with counts of what was created
        """
        print(f"\n🔨 Forging project: {self.project_name}")
        print(f"📦 Template: {self.template_name}")
        print(f"📍 Location: {self.dest}\n")

        # Create project directory
        self.dest.mkdir(parents=True, exist_ok=True)

        results = {
            "template_files": self.copy_template_files(),
            "ai_docs": 0,
        }

        # Copy AI docs if requested
        if include_ai_docs:
            results["ai_docs"] = self.copy_ai_docs(ai_doc_categories)

        # Create project structure
        self.create_project_structure(extra_dirs)

        # Create/update .gitignore
        self.create_gitignore()

        # Create README
        self.create_readme()

        print(f"\n✨ Project forged successfully!")
        print(f"   Template files: {results['template_files']}")
        print(f"   AI docs: {results['ai_docs']}")
        print(f"\n📂 Next steps:")
        print(f"   cd {self.dest.name}")
        print(f"   claude")

        return results


def list_templates():
    """List all available templates."""
    forge_root = Path(__file__).parent.parent
    templates_dir = forge_root / "templates"

    if not templates_dir.exists():
        print("No templates found.")
        return

    print("\n📦 Available Templates:\n")
    for template_dir in sorted(templates_dir.iterdir()):
        if template_dir.is_dir():
            # Count files in template
            file_count = sum(1 for _ in template_dir.rglob("*") if _.is_file())
            print(f"   • {template_dir.name} ({file_count} files)")
    print()


def main():
    """Main CLI entry point."""
    parser = argparse.ArgumentParser(
        description="Create new Claude Code projects from templates"
    )
    parser.add_argument(
        "project_name",
        nargs="?",
        help="Name of the new project",
    )
    parser.add_argument(
        "--template",
        "-t",
        default="base",
        help="Template to use (default: base)",
    )
    parser.add_argument(
        "--destination",
        "-d",
        help="Destination directory (default: current directory)",
    )
    parser.add_argument(
        "--list",
        "-l",
        action="store_true",
        help="List available templates",
    )
    parser.add_argument(
        "--ai-docs",
        nargs="+",
        help="AI doc categories to include from ai_docs_sources (enables AI docs copying)",
    )
    parser.add_argument(
        "--dirs",
        nargs="+",
        help="Additional directories to create (default: src tests docs)",
    )

    args = parser.parse_args()

    # Handle --list flag
    if args.list:
        list_templates()
        return 0

    # Require project name if not listing
    if not args.project_name:
        parser.error("project_name is required (unless using --list)")

    try:
        forge = ProjectForge(
            args.project_name,
            args.template,
            args.destination,
        )

        forge.forge(
            include_ai_docs=bool(args.ai_docs),
            ai_doc_categories=args.ai_docs,
            extra_dirs=args.dirs,
        )

    except Exception as e:
        print(f"❌ Error: {e}")
        return 1

    return 0


if __name__ == "__main__":
    exit(main())
