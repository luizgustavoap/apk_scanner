# scripts/apk_inspector.py

import os
import sys
from scanner.core import scan_folder

def main():
    if len(sys.argv) < 2:
        print("Use: python apk_inspector.py <folder_sources>")
        sys.exit(1)

    folder_sources = sys.argv[1]

    if not os.path.isdir(folder_sources):
        print(f"[!] Invalid folder: {folder_sources}")
        sys.exit(1)

    results = scan_folder(folder_sources)

    if not results:
        print("\n No suspicious pattern found.")
    else:
        print("\n Suspicious patterns detected:\n")
        for found in results:
            print(f"[!] File: {found['file']}")
            print(f"    Category: {found['category']}")
            print(f"    Pattern: {found['pattern']}")
            print("-" * 80)

if __name__ == "__main__":
    main()
