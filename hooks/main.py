# hooks/main.py

import sys
import os
import shutil
from pathlib import Path
from hooks.rules import rules

arr = []
'''
def find_word_in_files(root_dir, word):
    word_found = False
    for subdir, _, files in os.walk(root_dir):
        for file in files:
          if file.endswith(".yaml"):
            file_path = os.path.join(subdir, file)
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    for i, line in enumerate(f, start=1):
                        if word in line:
                            arr.append([file_path, i])
                            word_found = True
            except (UnicodeDecodeError, PermissionError) as e:
                print(f"Cannot read file {file_path}: {e}")

    if word_found:
        print(arr)
        sys.exit(1)
'''

def check_file(root_dir):
    for subdir,_, files in os.walk(root_dir):
        for file in files:
            file_path = os.path.join(subdir, file)
            if "__pycache__" in file_path or ".git" in file_path or ".github" in file_path:
                continue    
            try:
                with open(file_path, 'r', encoding='utf-8') as file:
                    content = file.read()

                for rule in rules:
                    if rule["file_filter"](Path(file_path)):
                        error = rule["check"](file_path, content)
                        if error:
                            arr.append([file_path])
                            #print(error) 
            except Exception as e:
                print(f"Error: {e}") 
                return False
    
    return True


def main():
    # Usage
    if not check_file('./'):
        print(arr)
        sys.exit(1)

    sys.exit(0)  

if __name__ == "__main__":
    main()  


          

