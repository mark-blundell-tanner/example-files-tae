import os
import re
from collections import defaultdict

def lint_md_files_for_warning(folder_path):
    file_messages = defaultdict(lambda: {"warning": []})
    allowed_filename_pattern = re.compile(r'^[A-Za-z0-9\-_\.]+$')

    for root, _, files in os.walk(folder_path):
        for file in files:
            if file.endswith('.md'):
                file_path = os.path.join(root, file)
                
                # Check for disallowed characters in filenames
                if not allowed_filename_pattern.match(file):
                    file_messages[file_path]["warning"].append(
                        f"{file_path}:\nFilename contains characters other than ASCII letters (a-zA-Z), digits (0-9), dashes(-), underscores(_), or dots(.). Please rename the file."
                    )

    return file_messages

if __name__ == "__main__":
    folder_to_check = '.'  # Current directory
    messages = lint_md_files_for_warning(folder_to_check)
    
    for file, msg_dict in messages.items():
        for warning in msg_dict["warning"]:
            print(f"\033[91mWARNING:\033[0m {warning}\n")