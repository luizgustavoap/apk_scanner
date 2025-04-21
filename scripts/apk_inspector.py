# scripts/apk_inspector.py

import os
import sys
from scanner.core import scan_folder

def save_txt(results, output_path):
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(f"APK Inspector Report\n")
        f.write(f"Generated on: {datetime.now().strftime("%m-%d-%Y %H:%M:%S")}\n")
        f.write(f"-" * 80 + "\n\n")

        if not results:
            f.write("No suspicious pattern found.\n")
        else:
            for found in results:
                f.write(f"[!] File: {found['file']}\n")
                f.write(f"    Category: {found['category']}\n")
                f.write(f"    Pattern: {found['pattern']}\n")
                f.write("-" * 80 + "\n")

    print(f"[+] Report saved to {output_path}")

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

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    output_path = os.path.join(os.getcwd(), f"apk_inspector_report_{timestamp}.txt")
    save_txt(results, output_path)

if __name__ == "__main__":
    main()
