# scanner/config.py

SUSPECT_PATTERNS = {
    "Keylogger": [
        r"onKey",
        r"onKeyDown",
        r"KeyEvent",
        r"TextWatcher",
        r"InputMethodManager",
        r"getText\(",
    ],
    "Data Exfiltration": [
        r"HttpURLConnection",
        r"URLConnection",
        r"Socket",
        r"OutputStreamWriter",
        r"PrintWriter",
        r"BufferedWriter",
    ],
    "Encryption/Obfuscation": [
        r"AES",
        r"Cipher",
        r"Base64\.decode",
        r"javax\.crypto",
    ],
    "Sensitive Permissions": [
        r"ACCESS_FINE_LOCATION",
        r"RECORD_AUDIO",
        r"READ_CONTACTS",
        r"READ_SMS",
        r"CAMERA",
    ]
}
