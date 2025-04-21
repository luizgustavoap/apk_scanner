import os
import subprocess
import re

# ============ CONFIG ============
JADX_PATH = "C:/jadx.bat" # Path to JADX .bat file
APK_PATH = "C:/apk.apk" # Path to the APK file to be scanned
# The APK file must be in the same directory as this script or provide the full path
OUTPUT_DIR = "decompiled_apk"
# =================================

# Suspected patterns to look for in the decompiled code
SUSPECT_PATTERNS = [
    r"ClipboardManager",
    r"getText\(",
    r"addTextChangedListener",
    r"Base64\.encodeToString",
    r"HttpURLConnection",
    r"OkHttpClient",
    r"Retrofit",
    r"new FileOutputStream",
    r"System\.exit",
    r"Runtime\.getRuntime\(\)\.exec",
    r"Log\.d",
    r"Log\.e",
    r"recordAudio",
    r"READ_SMS",
    r"SYSTEM_ALERT_WINDOW",
]

def decompile_apk():
    print(f"[+] Decompiling {APK_PATH} with jadx...")
    cmd = [JADX_PATH, "-d", OUTPUT_DIR, APK_PATH]
    try:
        subprocess.run(cmd, check=True)
        print(f"[+] Decompilation completed! Files saved in {OUTPUT_DIR}")
    except subprocess.CalledProcessError as e:
        print("[!] Error running JADX:")
        print(e)
        print("[!] Check if APK is corrupted or if JADX is correctly installed.")

def scan_for_malicious_code():
    print(f"[+] Scanning files in {OUTPUT_DIR} for suspected patterns...")
    suspected = []

    for root, _, files in os.walk(OUTPUT_DIR):
        for file in files:
            if file.endswith(".java"):
                path = os.path.join(root, file)
                with open(path, 'r', encoding="utf-8", errors="ignore") as f:
                    content = f.read()
                    for pattern in SUSPECT_PATTERNS:
                        if re.search(pattern, content):
                            suspected.append((path, pattern))

    if not suspected:
        print("[-] No suspected pattern found.")
    else:
        print(f"[!] Possible malicious patterns detected:")
        for path, pattern in suspected:
            print(f"  -> File: {path} | Pattern: {pattern}")

    return suspected

if __name__ == "__main__":
    decompile_apk()
    scan_for_malicious_code()
