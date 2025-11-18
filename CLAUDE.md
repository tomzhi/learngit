# CLAUDE.md - AI Assistant Guide for learngit Repository

**Repository:** tomzhi/learngit
**Owner:** tomzhi
**License:** MIT License (Copyright 2021)
**Last Updated:** 2025-11-18
**Purpose:** Git learning and tutorial repository

---

## Repository Overview

This repository serves as a practice environment for learning and testing basic Git commands and workflows. It contains simple sample code files and a trial directory used for experimenting with various Git operations.

### Key Characteristics
- **Educational Purpose**: Designed for learning Git fundamentals
- **Simple Structure**: Minimal codebase with focus on Git workflow practice
- **Active Learning**: Contains artifacts from various Git operations (staging, commits, amendments, branching)
- **Multi-platform Development**: History shows work from both Windows (terminal/VSCode) and other environments

---

## Repository Structure

```
learngit/
├── .git/                  # Git repository metadata
├── trial/                 # Practice directory for Git operations
│   ├── branch_file        # File created in branch trial_dev
│   └── hello              # Multi-stage commit example file
├── LICENSE                # MIT License file
├── README.md              # Basic repository description
├── jsSample.js            # Simple JavaScript console.log sample
├── pythonSample.py        # Simple Python print sample
└── CLAUDE.md              # This file - AI assistant guide
```

### File Purposes

#### Root Directory Files
- **LICENSE**: MIT License, Copyright 2021 tomzhi
- **README.md**: Simple description: "trial out basic git command here"
- **jsSample.js**: Basic JavaScript file with console.log statements
- **pythonSample.py**: Basic Python file with print statements

#### trial/ Directory
- **branch_file**: Created in branch `trial_dev`, demonstrates branch-merge workflow
- **hello**: Demonstrates multi-stage commits (stage1-4) and amend operations

---

## Development Workflows

### Git Branching Strategy

#### Branch Naming Conventions
1. **Claude AI Assistant Branches**: Must follow pattern `claude/claude-md-{sessionId}`
   - Example: `claude/claude-md-mi4b74t65vm8nwc1-01AeSqmpaRTjCgfNwrNujhry`
   - **CRITICAL**: Branches MUST start with `claude/` and end with matching session ID
   - Pushing to branches not matching this pattern will result in 403 HTTP errors

2. **Feature/Practice Branches**: Used for learning exercises
   - Example: `trial_dev` (historical branch used for practice)

### Git Operations Best Practices

#### Commit Workflow
Based on repository history, typical workflow includes:
1. Make changes to files
2. Stage changes: `git add <files>`
3. Commit with descriptive messages
4. Amend commits when needed: `git commit --amend`
5. Push to remote: `git push -u origin <branch-name>`

#### Historical Commit Patterns
- **Early commits** (4+ years ago): Learning stages (stage1, stage2, stage4_amend)
- **Recent commits** (8 months ago): Platform-specific development trials
  - "submission trial from vscode in Windows"
  - "2nd submission trial from terminal in Windows"
  - "sample from tutorial"

### Remote Repository

- **Remote Name**: origin
- **Fetch URL**: `http://local_proxy@127.0.0.1:48193/git/tomzhi/learngit`
- **Push URL**: `http://local_proxy@127.0.0.1:48193/git/tomzhi/learngit`

#### Network Operations
- **Push Strategy**: Always use `git push -u origin <branch-name>`
- **Retry Logic**: If network errors occur, retry up to 4 times with exponential backoff (2s, 4s, 8s, 16s)
- **Fetch Strategy**: Prefer fetching specific branches: `git fetch origin <branch-name>`

---

## Code Conventions

### File Naming
- Use descriptive names with clear purpose
- Python files: `*.py`
- JavaScript files: `*.js`
- Documentation: `*.md`

### Code Style

#### Python (pythonSample.py)
- Simple print statements for testing
- Clear output formatting with separators (dashes)

#### JavaScript (jsSample.js)
- Console.log for output
- String formatting with separators

**Note**: This is a learning repository; code style is intentionally simple and focused on Git operations rather than production-quality code.

---

## Development Environment

### Platforms Used
- Windows (VSCode, Terminal)
- Linux environment (current)

### Git Configuration
- Repository format version: 0
- File mode: true
- Auto garbage collection: disabled (`gc.auto = 0`)

---

## AI Assistant Guidelines

### When Working in This Repository

1. **Always Check Current Branch**
   - Verify you're on the correct Claude session branch
   - Branch name must match pattern: `claude/claude-md-{sessionId}`

2. **Commit Message Guidelines**
   - Keep messages descriptive and clear
   - Reference the purpose (e.g., "sample from tutorial", "trial from vscode")
   - Indicate platform/environment if relevant

3. **File Operations**
   - Maintain simple, educational code examples
   - Don't overcomplicate the codebase
   - Keep focus on Git learning, not advanced programming

4. **Branch Management**
   - Create feature branches for significant changes
   - Use descriptive branch names
   - Clean up branches after merging (if applicable)

5. **Push Operations**
   - **CRITICAL**: Only push to branches starting with `claude/` and ending with session ID
   - Always use `-u` flag for first push: `git push -u origin <branch-name>`
   - Implement retry logic for network failures
   - Never force push without explicit user request

6. **Documentation**
   - Keep CLAUDE.md updated with significant changes
   - Update README.md if repository purpose evolves
   - Document new conventions or patterns

### Common Tasks

#### Adding New Sample Code
1. Create file with clear, educational purpose
2. Keep code simple and well-commented
3. Add entry to this CLAUDE.md if it introduces new concepts

#### Testing Git Operations
- Use the `trial/` directory for experimental operations
- Document learnings in commit messages
- Don't delete historical learning artifacts unless requested

#### Updating Documentation
- Update dates and version information
- Keep structure clear and scannable
- Use markdown best practices

---

## Git History Summary

### Repository Timeline

- **Initial Commit** (e92480e): Repository creation
- **First GitHub Push** (7e9b0a2): "first submission to github for test"
- **Learning Stages** (e12b087, 0160cdc, afc91c0): Multi-stage commit practice
- **Branch Practice** (a4ba50e, 68a54e9): Branch creation and merging with trial_dev
- **Recent Activity** (7f8dbce, 0f25eed, acc2dc0): Platform-specific testing and tutorials

### Current State
- **HEAD**: `claude/claude-md-mi4b74t65vm8nwc1-01AeSqmpaRTjCgfNwrNujhry`
- **Commits**: 10 total commits
- **Active Branches**: 1 (current Claude session branch)
- **Working Directory**: Clean

---

## Troubleshooting

### Common Issues

1. **403 Error on Push**
   - **Cause**: Branch name doesn't match required pattern
   - **Solution**: Ensure branch starts with `claude/` and ends with session ID

2. **Network Failures**
   - **Cause**: Connection issues with local proxy
   - **Solution**: Implement exponential backoff retry (2s, 4s, 8s, 16s)

3. **Merge Conflicts**
   - **Note**: Unlikely in this simple repository
   - **Solution**: Standard Git conflict resolution if they occur

---

## Quick Reference

### Essential Commands

```bash
# Check current branch and status
git status
git branch

# Create and switch to new branch
git checkout -b <branch-name>

# Stage and commit changes
git add <files>
git commit -m "descriptive message"

# Push to remote (first time)
git push -u origin <branch-name>

# Push to remote (subsequent)
git push

# Fetch updates
git fetch origin <branch-name>

# View history
git log --oneline --graph --decorate
```

### File Locations
- Sample code: Root directory (`jsSample.js`, `pythonSample.py`)
- Practice files: `trial/` directory
- Documentation: `README.md`, `CLAUDE.md`
- License: `LICENSE` (MIT)

---

## Notes for AI Assistants

1. **Repository Purpose**: This is a learning environment - preserve its educational value
2. **Simplicity**: Maintain simple, clear code examples suitable for Git learning
3. **History**: Don't rewrite history unless explicitly requested
4. **Branching**: Always verify branch naming before pushing
5. **Documentation**: Keep this file updated with repository changes
6. **User Intent**: When in doubt about changes, ask the user for clarification

---

**End of CLAUDE.md**

_This document is maintained for AI assistants working with this repository. Keep it updated as the repository evolves._
