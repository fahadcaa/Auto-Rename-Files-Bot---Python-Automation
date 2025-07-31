import os
import re
from datetime import datetime
import argparse

def auto_rename_files(directory, pattern=None, prefix=None, suffix=None, 
                     replace=None, with_str=None, add_counter=False, 
                     case_sensitive=False, dry_run=False):
    """
    Automatically rename files in a directory based on specified rules.
    
    Args:
        directory (str): Path to the directory containing files to rename
        pattern (str): Regex pattern to match in filenames
        prefix (str): Prefix to add to filenames
        suffix (str): Suffix to add before the file extension
        replace (str): Text to replace in filenames
        with_str (str): Replacement text
        add_counter (bool): Whether to add a sequential counter
        case_sensitive (bool): Whether pattern matching is case sensitive
        dry_run (bool): If True, only show what would be renamed without making changes
    """
    if not os.path.isdir(directory):
        print(f"Error: Directory '{directory}' does not exist.")
        return
    
    files = [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]
    if not files:
        print("No files found in the directory.")
        return
    
    counter = 1
    flags = 0 if case_sensitive else re.IGNORECASE
    
    print(f"Found {len(files)} files in '{directory}'")
    print("Renaming preview:" if dry_run else "Renaming files:")
    
    for filename in files:
        name, ext = os.path.splitext(filename)
        new_name = name
        
        # Apply pattern matching and replacement
        if pattern and with_str:
            new_name = re.sub(pattern, with_str, new_name, flags=flags)
        elif replace and with_str:
            new_name = new_name.replace(replace, with_str)
        
        # Apply prefix/suffix
        if prefix:
            new_name = f"{prefix}{new_name}"
        if suffix:
            new_name = f"{new_name}{suffix}"
        
        # Add counter if requested
        if add_counter:
            new_name = f"{new_name}_{counter:04d}"
            counter += 1
        
        # Add the extension back
        new_filename = f"{new_name}{ext}"
        
        # Skip if no change
        if new_filename == filename:
            continue
        
        # Show or perform the rename
        old_path = os.path.join(directory, filename)
        new_path = os.path.join(directory, new_filename)
        
        if dry_run:
            print(f"'{filename}' -> '{new_filename}'")
        else:
            try:
                os.rename(old_path, new_path)
                print(f"Renamed '{filename}' to '{new_filename}'")
            except OSError as e:
                print(f"Error renaming '{filename}': {e}")

def main():
    parser = argparse.ArgumentParser(
        description="Auto Rename Files Bot - Python Automation Tool",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    
    parser.add_argument("directory", help="Directory containing files to rename")
    parser.add_argument("--pattern", help="Regex pattern to match in filenames")
    parser.add_argument("--with", dest="with_str", help="Replacement text for pattern matches")
    parser.add_argument("--replace", help="Exact text to replace in filenames")
    parser.add_argument("--prefix", help="Prefix to add to filenames")
    parser.add_argument("--suffix", help="Suffix to add before file extension")
    parser.add_argument("--counter", action="store_true", help="Add sequential counter to filenames")
    parser.add_argument("--case", action="store_true", help="Case-sensitive pattern matching")
    parser.add_argument("--dry-run", action="store_true", help="Preview changes without renaming")
    
    args = parser.parse_args()
    
    auto_rename_files(
        directory=args.directory,
        pattern=args.pattern,
        prefix=args.prefix,
        suffix=args.suffix,
        replace=args.replace,
        with_str=args.with_str,
        add_counter=args.counter,
        case_sensitive=args.case,
        dry_run=args.dry_run
    )

if __name__ == "__main__":
    main()
