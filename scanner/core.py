# scanner/core.py

import re
from scanner.config import SUSPECT_PATTERNS
from scanner.utils import get_java_files

def scan_file(filepath):
    findings = []
    try:
        with open(filepath, 'r', encoding="utf-8", errors="ignore") as file:
            content = file.read()
            for category, patterns in SUSPECT_PATTERNS.items():
                for pattern in patterns:
                    if re.search(pattern, content):
                        findings.append({
                            "file": filepath,
                            "category": category,
                            "pattern": pattern
                        })
    except Exception as e:
        print(f"[!] Error reading {filepath}: {e}")
    return findings

def scan_folder(path):
    print(f"[+] Initializing folder scan: {path}\n")
    results = []
    for file in get_java_files(path):
        results.extend(scan_file(file))
    return results
