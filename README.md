# Auto-Rename-Files-Bot---Python-Automation
A Python script to automatically rename files in bulk based on customizable rules like patterns, prefixes, suffixes, text replacement, and sequential counters. Perfect for organizing photos, documents, or any messy file collection!
Here's a GitHub repository description (`README.md`) for your **Auto Rename Files Bot** Python automation script:

---

# Auto Rename Files Bot 🚀

A Python script to **automatically rename files** in bulk based on customizable rules like patterns, prefixes, suffixes, text replacement, and sequential counters. Perfect for organizing photos, documents, or any messy file collection!

[![Python Version](https://img.shields.io/badge/python-3.6%2B-blue)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

---

## Features ✨

- **Regex Pattern Matching**: Replace text in filenames using regex.
- **Text Replacement**: Swap specific substrings in filenames.
- **Prefix/Suffix**: Add text to the start or end of filenames.
- **Sequential Counter**: Append numbered counters (e.g., `_001`, `_002`).
- **Case-Sensitive Control**: Choose case-sensitive or case-insensitive matching.
- **Dry-Run Mode**: Preview changes before actually renaming files.
- **Lightweight**: No external dependencies—pure Python!

---

## Installation 📥

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/auto-rename-files-bot.git
   cd auto-rename-files-bot
   ```

2. Ensure you have Python 3.6+ installed.

---

## Usage 🛠️

Run the script from the command line:

```bash
python rename_bot.py /path/to/files [options]
```

### Examples:
| Command | Description |
|---------|-------------|
| `python rename_bot.py /photos --prefix "vacation_"` | Adds `vacation_` to all filenames. |
| `python rename_bot.py /docs --replace " " --with "_"` | Replaces spaces with underscores. |
| `python rename_bot.py /backups --suffix "_v1" --counter` | Appends `_v1_0001`, `_v1_0002`, etc. |
| `python rename_bot.py /files --pattern "\d{4}-\d{2}-\d{2}" --with "" --dry-run` | *Preview* removal of dates (YYYY-MM-DD). |

### All Options:
```
  --pattern TEXT    Regex pattern to match in filenames.
  --with TEXT       Replacement text for regex matches.
  --replace TEXT    Exact text to replace in filenames.
  --prefix TEXT     Add this prefix to filenames.
  --suffix TEXT     Add this suffix (before extension).
  --counter         Add a sequential counter (e.g., _0001).
  --case            Enable case-sensitive matching.
  --dry-run         Preview changes without renaming.
```

---

## Contributing 🤝

Pull requests are welcome! For major changes, open an issue first.

---

## License 📜

MIT © [Your Name](https://github.com/yourusername)

---

### Preview:
![Terminal Demo](https://i.imgur.com/placeholder.png) *(add a real screenshot later)*

---
