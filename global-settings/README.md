# Global Claude Code Settings

This folder contains global Claude Code settings that apply to **all projects** on your machine.

## What's Included

- **CLAUDE.md** - Global rules and conventions for Claude Code
  - Python-focused best practices (PEP8, Pytest, type hints)
  - Code structure guidelines (500 line limit, modularity)
  - Testing requirements
  - Documentation standards
  - AI behavior rules

## Installation

### On a New Machine

1. **Clone or pull this repository:**
   ```bash
   cd ~/Documents/Projects
   git clone git@github.com:aureous1/claude-project-forge.git
   # OR if already cloned:
   cd claude-project-forge && git pull
   ```

2. **Ensure .claude directory exists:**
   ```bash
   mkdir -p ~/.claude
   ```

3. **Copy global settings:**
   ```bash
   cp ~/Documents/Projects/claude-project-forge/global-settings/CLAUDE.md ~/.claude/CLAUDE.md
   ```

4. **Verify installation:**
   ```bash
   ls -lh ~/.claude/CLAUDE.md
   ```

### Quick One-Liner

```bash
mkdir -p ~/.claude && cp ~/Documents/Projects/claude-project-forge/global-settings/CLAUDE.md ~/.claude/CLAUDE.md
```

## Keeping Multiple Machines in Sync

### Method 1: Manual Sync (Simple)

When you update global settings:

```bash
# On machine where you made changes
cd ~/Documents/Projects/claude-project-forge
cp ~/.claude/CLAUDE.md ./global-settings/CLAUDE.md
git add global-settings/CLAUDE.md
git commit -m "Update global Claude settings"
git push

# On other machines
cd ~/Documents/Projects/claude-project-forge
git pull
cp ./global-settings/CLAUDE.md ~/.claude/CLAUDE.md
```

### Method 2: Symlink (Advanced)

Create a symlink instead of copying (changes sync automatically with git pull):

```bash
# Backup existing file first
mv ~/.claude/CLAUDE.md ~/.claude/CLAUDE.md.backup

# Create symlink
ln -sf ~/Documents/Projects/claude-project-forge/global-settings/CLAUDE.md ~/.claude/CLAUDE.md

# Verify
ls -lh ~/.claude/CLAUDE.md
# Should show: .claude/CLAUDE.md -> ~/Documents/Projects/claude-project-forge/global-settings/CLAUDE.md
```

**Benefits of symlink:**
- ✅ Changes automatically sync when you `git pull`
- ✅ No need to manually copy after updates
- ⚠️ Be careful not to accidentally delete the source file

## How Global Settings Work

### Priority Order

Claude Code applies settings in this order:

1. **Project-specific** `CLAUDE.md` (in project root) - Highest priority
2. **Global** `~/.claude/CLAUDE.md` (this file) - Fallback
3. **Built-in** Claude Code defaults - Lowest priority

### Example

**Archon Project:**
- Project has Archon-specific `CLAUDE.md` with task management rules
- Global settings provide Python/testing conventions
- **Result:** Archon task management + Python best practices

**Non-Archon Project:**
- Project may have minimal or no `CLAUDE.md`
- Global settings provide all conventions
- **Result:** Python best practices + general guidelines

## What's NOT in Global Settings

These are **intentionally excluded** because they're project-specific:

- ❌ Task management systems (TASK.md, PLANNING.md, Archon)
- ❌ Project-specific workflows
- ❌ MCP server configurations
- ❌ Technology choices (frameworks, databases)

**Why?** These vary by project and should live in project-specific `CLAUDE.md` files.

## Modifying Global Settings

### When to Update

Update global settings when you want to change:
- Python conventions across all projects
- Testing standards
- Code style preferences
- Documentation requirements

### How to Update

1. Edit on one machine: `~/.claude/CLAUDE.md`
2. Copy back to repo:
   ```bash
   cp ~/.claude/CLAUDE.md ~/Documents/Projects/claude-project-forge/global-settings/CLAUDE.md
   ```
3. Commit and push:
   ```bash
   cd ~/Documents/Projects/claude-project-forge
   git add global-settings/CLAUDE.md
   git commit -m "Update global settings: [describe change]"
   git push
   ```
4. Sync other machines:
   ```bash
   cd ~/Documents/Projects/claude-project-forge
   git pull
   cp ./global-settings/CLAUDE.md ~/.claude/CLAUDE.md  # If not using symlink
   ```

## Troubleshooting

### Settings not applying

1. **Check file exists:**
   ```bash
   cat ~/.claude/CLAUDE.md
   ```

2. **Check file permissions:**
   ```bash
   chmod 644 ~/.claude/CLAUDE.md
   ```

3. **Restart Claude Code:**
   - Close and reopen your Claude Code session

### Conflicts between global and project settings

- Project-specific `CLAUDE.md` always takes priority
- Global settings act as **fallback** only
- Both can coexist peacefully if designed correctly

### Symlink broken

If symlink stops working:
```bash
# Remove broken symlink
rm ~/.claude/CLAUDE.md

# Recreate
ln -sf ~/Documents/Projects/claude-project-forge/global-settings/CLAUDE.md ~/.claude/CLAUDE.md
```

## Related Files

- **Project Template:** `../templates/base/CLAUDE.md` - Archon-specific project rules
- **Forge Scripts:** `../scripts/forge.py` - Creates new projects with templates
- **Main README:** `../README.md` - Full documentation for claude-project-forge

## Questions?

If you're setting this up on a new machine and run into issues:

1. Check that `~/.claude` directory exists and is writable
2. Verify the file path in your terminal matches your actual Projects location
3. Make sure you have git access to the claude-project-forge repository
4. Review the main README.md in the repository root

---

**Last Updated:** November 2025
**Repository:** https://github.com/aureous1/claude-project-forge
