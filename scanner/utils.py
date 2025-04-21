# scanner/utils.py

import os

def get_java_files(root_path):
    for root, _, files in os.walk(root_path):
        for file in files:
            if file.endswith(".java"):
                yield os.path.join(root, file)
