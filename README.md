# 🔨 Claude Project Forge

A scaffolding system for creating clean, well-configured Claude Code projects. Extract configurations from your existing projects into reusable templates, then use those templates to spin up new projects instantly.

## 🎯 What This Does

**Claude Project Forge** helps you:

1. **Harvest** - Extract Claude Code configurations from your existing projects (CLAUDE.md, commands, MCP configs, AI docs)
2. **Template** - Organize those configurations into reusable templates
3. **Forge** - Create new projects from templates with all configurations in place

No more manually copying files between projects or recreating your Claude Code setup from scratch!

## 📋 Prerequisites

- Python 3.7+
- Existing Claude Code projects to harvest from (optional for first-time setup)

## 🚀 Quick Start

### Step 1: Harvest from Existing Projects

Extract Claude Code configurations from your best projects:

```bash
# Harvest everything from a project into the "base" template
python scripts/harvest.py ../obsidian-ai-agent --template base

# Harvest from a PRP-based project into "agentic-workflow" template
python scripts/harvest.py ../PRPs-agentic-eng --template agentic-workflow

# Harvest specific commands only
python scripts/harvest.py ../aiengine --template workshop \
  --commands generate-prp.md execute-prp.md
```

### Step 2: Create New Projects

Use your templates to create new projects:

```bash
# Create a new project with the "base" template
python scripts/forge.py my-new-project --template base

# Create with AI docs included
python scripts/forge.py api-project --template python-fastapi

# Create in a specific location
python scripts/forge.py webapp --template base --destination ~/projects
```

### Step 3: Start Working

```bash
cd my-new-project
claude
```

Your new project already has:
- ✅ CLAUDE.md with project guidelines
- ✅ Custom slash commands in `.claude/commands/`
- ✅ Permission settings in `.claude/settings.local.json`
- ✅ MCP configurations (if harvested)
- ✅ AI documentation (if included)
- ✅ Project structure (src/, tests/, docs/, PRPs/)
- ✅ .gitignore configured for Claude Code

---

## 📖 Complete Usage Guide

### 🌾 Harvest Script

The **harvest script** extracts Claude Code files from existing projects into templates.

#### Basic Usage

```bash
python scripts/harvest.py <source-project> [options]
```

#### Options

| Flag | Description | Default |
|------|-------------|---------|
| `--template`, `-t` | Template name to create/update | `base` |
| `--commands`, `-c` | Specific command files to copy | All commands |
| `--no-ai-docs` | Skip copying AI documentation | Include AI docs |
| `--ai-docs-subdir` | Subdirectory for AI docs | `general` |

#### What Gets Harvested

The script looks for and copies these files:

- ✅ `CLAUDE.md` - Project guidelines and instructions
- ✅ `.claude/commands/` - All custom slash commands
- ✅ `.claude/settings.local.json` - Permission configurations
- ✅ `.mcp.json` - MCP server configurations
- ✅ `.gitignore` - Git ignore patterns
- ✅ `PRPs/templates/` - PRP templates (if exist)
- ✅ `PRPs/ai_docs/`, `ai_docs/`, or `docs/ai/` - AI documentation

#### Examples

**Example 1: Harvest Everything**

```bash
python scripts/harvest.py ../obsidian-ai-agent --template python-fastapi
```

Output:
```
🌾 Harvesting from: obsidian-ai-agent
📦 Template: python-fastapi

✅ Copied CLAUDE.md
✅ Copied command: generate-prp.md
✅ Copied command: execute-prp.md
✅ Copied settings.local.json
✅ Copied .mcp.json
✅ Copied .gitignore
✅ Copied AI doc: claude-code/cc_base.md
✅ Copied AI doc: pydantic-ai/tools.md

✨ Harvest complete!
   Commands: 2
   PRP templates: 0
   AI docs: 2
```

**Example 2: Harvest Specific Commands**

```bash
python scripts/harvest.py ../PRPs-agentic-eng --template agentic \
  --commands generate-prp.md execute-prp.md prime-core.md
```

This copies only CLAUDE.md, settings, and the three specified commands.

**Example 3: Harvest Without AI Docs**

```bash
python scripts/harvest.py ../aiengine --template workshop --no-ai-docs
```

Copies everything except AI documentation (faster if you don't need docs).

**Example 4: Organize AI Docs by Category**

```bash
# Harvest AI docs into "fastapi" subdirectory
python scripts/harvest.py ../my-fastapi-project --template python-api \
  --ai-docs-subdir fastapi

# Harvest AI docs into "pydantic" subdirectory
python scripts/harvest.py ../ai-agent --template agent \
  --ai-docs-subdir pydantic-ai
```

This helps organize AI docs by technology/framework for reuse across projects.

#### After Harvesting

Your templates are stored in:
```
claude-project-forge/
├── templates/
│   ├── base/
│   │   ├── CLAUDE.md
│   │   ├── .claude/
│   │   │   ├── settings.local.json
│   │   │   └── commands/
│   │   │       ├── generate-prp.md
│   │   │       └── execute-prp.md
│   │   └── .gitignore
│   └── python-fastapi/
│       └── [similar structure]
└── ai_docs_sources/
    ├── general/
    ├── fastapi/
    └── pydantic-ai/
```

---

### 🔨 Forge Script

The **forge script** creates new projects from your templates.

#### Basic Usage

```bash
python scripts/forge.py <project-name> [options]
```

#### Options

| Flag | Description | Default |
|------|-------------|---------|
| `--template`, `-t` | Template to use | `base` |
| `--destination`, `-d` | Where to create project | Current directory |
| `--list`, `-l` | List available templates | - |
| `--no-ai-docs` | Skip copying AI docs | Include AI docs |
| `--ai-docs` | Specific AI doc categories | All categories |
| `--dirs` | Additional directories to create | `src tests docs PRPs` |

#### What Gets Created

The forge script creates:

- ✅ New project directory with your project name
- ✅ All files from the template
- ✅ AI documentation (from `ai_docs_sources/`)
- ✅ Standard project structure (`src/`, `tests/`, `docs/`, `PRPs/`)
- ✅ `.gitignore` with Claude Code entries
- ✅ `README.md` with getting started info

#### Examples

**Example 1: Create Basic Project**

```bash
python scripts/forge.py my-api --template base
```

Output:
```
🔨 Forging project: my-api
📦 Template: base
📍 Location: /Users/you/Projects/my-api

📋 Copying template files...
   ✅ CLAUDE.md
   ✅ .claude/commands/generate-prp.md
   ✅ .claude/commands/execute-prp.md
   ✅ .claude/settings.local.json

📚 Copying AI documentation...
   ✅ general/cc_base.md
   ✅ general/cc_best_practices.md

📁 Creating project structure...
   ✅ src/
   ✅ tests/
   ✅ docs/
   ✅ PRPs/

   ✅ Created .gitignore
   ✅ Created README.md

✨ Project forged successfully!
   Template files: 4
   AI docs: 2

📂 Next steps:
   cd my-api
   claude
```

**Example 2: List Available Templates**

```bash
python scripts/forge.py --list
```

Output:
```
📦 Available Templates:

   • base (7 files)
   • python-fastapi (12 files)
   • agentic-workflow (18 files)
```

**Example 3: Create with Specific AI Docs**

```bash
python scripts/forge.py fastapi-app --template python-fastapi \
  --ai-docs fastapi pydantic-ai
```

Only copies AI docs from the "fastapi" and "pydantic-ai" categories (not "general").

**Example 4: Create in Specific Location**

```bash
python scripts/forge.py new-agent --template agentic-workflow \
  --destination ~/workspace/agents
```

Creates project at `~/workspace/agents/new-agent/`.

**Example 5: Custom Directory Structure**

```bash
python scripts/forge.py ml-project --template base \
  --dirs src tests data models notebooks
```

Creates custom directories instead of the default `src tests docs PRPs`.

**Example 6: Skip AI Docs**

```bash
python scripts/forge.py quick-test --template base --no-ai-docs
```

Creates project without copying any AI documentation (faster setup).

---

## 🔄 Complete Workflow Example

Here's a real-world example of harvesting from multiple projects and creating a new one:

### 1. Harvest from Your Best Projects

```bash
# Get the core CLAUDE.md and commands from obsidian-ai-agent
python scripts/harvest.py ../obsidian-ai-agent --template base

# Add PRP-specific commands from PRPs-agentic-eng
python scripts/harvest.py ../PRPs-agentic-eng --template agentic \
  --commands create-base-prp.md execute-base-prp.md planning-create.md

# Get FastAPI-specific docs and configs
python scripts/harvest.py ../api-project --template python-fastapi \
  --ai-docs-subdir fastapi
```

### 2. Review Your Templates

```bash
# See what templates you have
python scripts/forge.py --list

# Check what's in a template
ls -R templates/base/
```

### 3. Create New Project

```bash
# Create a new FastAPI project with PRP workflow
python scripts/forge.py my-saas-api --template python-fastapi

cd my-saas-api
```

### 4. Customize and Start Working

```bash
# Edit CLAUDE.md for your specific project
vim CLAUDE.md

# Start Claude Code
claude
```

Now you have a clean project with:
- Your preferred CLAUDE.md guidelines
- Your favorite slash commands
- Your MCP configurations
- Your curated AI docs
- Clean project structure

---

## 📁 Project Structure

```
claude-project-forge/
├── README.md                    # This file
├── CLAUDE.md                    # Guidelines for working on the forge itself
├── scripts/
│   ├── harvest.py               # Extract configs from existing projects
│   └── forge.py                 # Create new projects from templates
├── templates/                   # Your reusable templates
│   ├── base/                    # Minimal template
│   ├── python-fastapi/          # Python/FastAPI template
│   └── agentic-workflow/        # Full PRP-based template
└── ai_docs_sources/             # Shared AI documentation
    ├── general/                 # General Claude Code docs
    ├── fastapi/                 # FastAPI-specific docs
    └── pydantic-ai/             # Pydantic AI docs
```

---

## 💡 Tips and Best Practices

### Harvesting

1. **Start with your best project** - Harvest from a project you're proud of
2. **Create multiple templates** - Different templates for different project types
3. **Organize AI docs by category** - Use `--ai-docs-subdir` to keep docs organized
4. **Iterate on templates** - Re-harvest to update templates as your practices evolve

### Forging

1. **Review templates first** - Use `--list` to see what's available
2. **Start minimal** - Use `--no-ai-docs` for quick experiments
3. **Customize after forging** - Templates are starting points, not rigid rules
4. **Version control your templates** - Commit the `templates/` directory to git

### Template Organization

**Recommended template structure:**

- **`base`** - Minimal CLAUDE.md + basic commands (for any project)
- **`python-fastapi`** - Python/FastAPI specific setup
- **`node-express`** - Node.js/Express specific setup
- **`agentic-workflow`** - Full PRP methodology with all commands
- **`ml-project`** - Machine learning project template
- **`workshop`** - Workshop/tutorial project setup

---

## 🔧 Customization

### Adding Custom Harvest Logic

Edit `scripts/harvest.py` to add methods for harvesting additional files:

```python
def harvest_docker_config(self) -> bool:
    """Copy docker-compose.yml if it exists."""
    source_file = self.source / "docker-compose.yml"
    if source_file.exists():
        dest = self.template_dir / "docker-compose.yml"
        shutil.copy2(source_file, dest)
        print(f"✅ Copied docker-compose.yml")
        return True
    return False
```

Then call it in `harvest_all()`.

### Adding Custom Forge Logic

Edit `scripts/forge.py` to create additional files or structure:

```python
def create_docker_files(self) -> None:
    """Create Dockerfile and docker-compose.yml."""
    dockerfile = self.dest / "Dockerfile"
    # ... create Dockerfile content
```

---

## 🤝 Contributing

Have ideas for improvements? Found a bug?

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

---

## 📄 License

MIT License - see LICENSE file for details

---

## 🙏 Acknowledgments

Built for the Claude Code community to make project setup faster and more consistent.

Inspired by tools like `create-react-app`, `cookiecutter`, and the PRP methodology from Rasmus Widing.

---

## 🆘 Troubleshooting

**"Template does not exist"**
- Run `python scripts/forge.py --list` to see available templates
- Make sure you've harvested from at least one project first

**"Source project does not exist"**
- Check your path to the source project
- Use absolute paths if relative paths aren't working

**"Project directory already exists"**
- Choose a different project name
- Or delete the existing directory if you're sure

**No files copied during harvest**
- Verify the source project has Claude Code configurations
- Check for `.claude/` directory in the source project
- Try running with just the source path to harvest everything

---

## 🚀 Next Steps

1. **Harvest from your best projects** to create templates
2. **Organize your AI docs** in `ai_docs_sources/`
3. **Create your first project** using `forge.py`
4. **Iterate and improve** your templates over time

Happy forging! 🔨✨
