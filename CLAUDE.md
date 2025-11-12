### 🔄 Project Awareness & Context
- **Project Purpose**: This is a meta-project that creates clean Claude Code project setups from templates
- **Core Functionality**: Two main scripts - `harvest.py` (extract configs) and `forge.py` (create projects)
- **Use consistent naming conventions**: harvest, forge, template, ai_docs_sources
- **This is a tooling project**: Focus on usability, clarity, and reliability

### 🧱 Code Structure & Modularity
- **Never create a file longer than 500 lines of code.** Scripts are already modular with classes.
- **Organize code into clearly separated functions** with single responsibilities
- **Use clear, descriptive function and variable names**
- **Both scripts follow the same pattern**:
  - Class-based design (Harvester, ProjectForge)
  - CLI entry point in `main()`
  - Clear separation between file operations and user interaction

### 🧪 Testing & Reliability
- **Test manually before committing changes** - run both harvest and forge scripts
- **Test with different source projects** to ensure robustness
- **Verify file paths work on different systems** (macOS, Linux, Windows)
- **Check error handling** for missing files, invalid paths, etc.

### ✅ File Operations Best Practices
- **Always use pathlib.Path** for cross-platform compatibility
- **Use shutil.copy2** to preserve file metadata (timestamps, permissions)
- **Create parent directories** with `mkdir(parents=True, exist_ok=True)`
- **Resolve paths early** with `.resolve()` for clarity
- **Check existence before operations** to provide helpful error messages

### 📎 Style & Conventions
- **Use Python 3.7+** for compatibility
- **Follow PEP8** with clear, readable code
- **Use type hints** for function parameters and return values
- **Use descriptive variable names**: `source_project`, `template_name`, not `src`, `tmpl`
- **Print user-friendly output** with emojis for visual clarity:
  - ✅ for success
  - ⚠️  for warnings
  - ❌ for errors
  - 🌾 for harvesting
  - 🔨 for forging
  - 📦 for templates
  - 📚 for documentation

### 📚 Documentation & Explainability
- **README.md is critical** - it's the primary user documentation
- **Keep README up to date** when adding features or changing behavior
- **Use clear examples** in README with expected output
- **Docstrings for all functions** using Google style
- **Comment non-obvious file operations** especially path manipulations

### 🧠 AI Behavior Rules
- **Never assume file locations** - always check if files exist
- **Provide helpful error messages** that tell users what to do
- **Default to safe operations** - never overwrite without checking
- **Be explicit about what's being copied** - print every file operation
- **Handle edge cases gracefully**:
  - Missing source directories
  - Empty templates
  - Existing destination projects
  - Permission errors

### 🔧 Script Development Guidelines

#### For harvest.py:
- **Harvest methods should be independent** - each can work standalone
- **Use consistent return values** - bool for single items, int for counts
- **Print descriptive messages** so users know what's happening
- **Support both "all" and "specific" modes** for flexibility
- **Look in common locations** for files (e.g., multiple possible AI docs dirs)

#### For forge.py:
- **Create complete, working projects** - don't leave users with half-setup
- **Provide sensible defaults** - base template, current directory, common dirs
- **Be helpful with next steps** - print what to do after forging
- **Don't overwrite existing projects** - safety first
- **Support customization** - let users choose what to include

### 🎯 Feature Development Workflow

When adding new features:

1. **Update harvest.py if harvesting new file types**
   - Add new method following existing pattern
   - Call it in `harvest_all()` if appropriate
   - Update CLI arguments if needed

2. **Update forge.py if creating new project elements**
   - Add new method for creating the element
   - Call it in `forge()` if appropriate
   - Update CLI arguments if needed

3. **Update README.md**
   - Add examples showing the new feature
   - Update "What Gets Harvested" or "What Gets Created" sections
   - Add to "Complete Usage Guide"

4. **Test end-to-end**
   - Harvest from a real project
   - Forge a new project
   - Verify the new feature works

### 🚨 Common Pitfalls to Avoid

- **DON'T hardcode paths** - use Path operations for cross-platform support
- **DON'T assume directory structure** - check before copying
- **DON'T silently fail** - always inform users what went wrong
- **DON'T overwrite without warning** - check existence first
- **DON'T copy unnecessary files** - be selective about what to harvest

### 📦 Template Management

- **Templates live in `templates/`** - one subdirectory per template
- **Templates should be complete** - everything needed for a project type
- **Templates are versioned with the repo** - commit them to git
- **Templates can be updated** - re-harvest to refresh
- **Templates can be minimal or comprehensive** - support both styles

### 🎨 Output Formatting

User-facing output should be:
- **Clear and scannable** - use emojis and whitespace
- **Informative** - tell users what's happening
- **Actionable** - include next steps
- **Consistent** - use same emoji meanings throughout

Example good output:
```
🌾 Harvesting from: obsidian-ai-agent
📦 Template: python-fastapi

✅ Copied CLAUDE.md
✅ Copied command: generate-prp.md
⚠️  No .mcp.json found

✨ Harvest complete!
   Commands: 2
   AI docs: 5
```

### 🔐 Security Considerations

- **Don't copy sensitive files** - no .env, credentials, API keys
- **Respect .gitignore** - don't harvest files that should be ignored
- **Create .gitignore for new projects** - protect sensitive files by default
- **Warn about credentials in configs** - if MCP configs have API keys

### 🚀 Performance Considerations

- **File operations are fast** - no need to optimize unless copying thousands of files
- **Use pathlib for clarity** - not for speed (it's fast enough)
- **Print progress for large operations** - helps users understand what's happening
- **Don't recursively copy large directories** - be selective

### 📝 Maintenance Notes

- **This project is stable by design** - core functionality is simple
- **Extensions should be additive** - don't break existing workflows
- **Keep scripts independent** - harvest and forge don't depend on each other
- **Version control templates** - commit them so users have examples
- **Test with real projects** - use your own projects as test cases

### 🎓 Learning Resources

For understanding the code:
- Python pathlib: https://docs.python.org/3/library/pathlib.html
- argparse: https://docs.python.org/3/library/argparse.html
- shutil: https://docs.python.org/3/library/shutil.html

For understanding Claude Code:
- Claude Code docs: https://docs.anthropic.com/en/docs/claude-code
- PRP methodology: See PRPs-agentic-eng project

### 🎯 Success Criteria for Changes

Before committing changes, verify:
- ✅ Scripts run without errors
- ✅ Output is clear and helpful
- ✅ README reflects the changes
- ✅ Works on at least one real project
- ✅ Doesn't break existing functionality
- ✅ Follows the coding style
- ✅ Has appropriate error handling

### 🔮 Future Enhancement Ideas

Potential features to add (don't implement without user request):
- Interactive mode with prompts
- Template validation
- Template versioning
- Batch forging (create multiple projects)
- Template inheritance (base + extensions)
- Remote templates (from GitHub)
- Configuration file support
- Dry-run mode for both scripts
- Template marketplace/sharing

Keep it simple until users ask for more!
