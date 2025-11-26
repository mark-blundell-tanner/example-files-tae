import os
import json
import re

# Configurable paths
path_to_old_json_dir = 'json'
path_to_new_json_dir = 'json'
path_to_docs = 'docs'
begins_with_old = 'dev-'
begins_with_new = 'en-'

def extract_strings(obj, prefix=None):
    # Recursively extract all string values with their key paths
    if prefix is None:
        prefix = []
    results = []
    if isinstance(obj, dict):
        for k, v in obj.items():
            results.extend(extract_strings(v, prefix + [str(k)]))
    elif isinstance(obj, list):
        for i, v in enumerate(obj):
            results.extend(extract_strings(v, prefix + [str(i)]))
    elif isinstance(obj, str):
        results.append((".".join(prefix), obj))
    return results

def main():
    # Find all dev*.json and en*.json files
    old_files = [f for f in os.listdir(path_to_old_json_dir) if f.startswith(begins_with_old) and f.endswith(".json")]
    new_files = [f for f in os.listdir(path_to_new_json_dir) if f.startswith(begins_with_new) and f.endswith(".json")]

    # Match files by suffix after 'dev-' and 'en-'
    pairs = []
    unmatched = []
    dev_suffix_map = {f[4:]: f for f in old_files}
    en_suffix_map = {f[3:]: f for f in new_files}
    for suffix, dev_file in dev_suffix_map.items():
        en_file = en_suffix_map.get(suffix)
        if en_file:
            pairs.append((dev_file, en_file))
        else:
            unmatched.append(dev_file)

    # Find changed strings between matched JSON files
    changes = []
    for dev, en in pairs:
        with open(os.path.join(path_to_old_json_dir, dev), encoding="utf-8") as f1, \
            open(os.path.join(path_to_new_json_dir, en), encoding="utf-8") as f2:
            dev_json = json.load(f1)
            en_json = json.load(f2)
            dev_items = extract_strings(dev_json)
            en_items = dict(extract_strings(en_json))
            for key_path, old_value in dev_items:
                if key_path in en_items and old_value != en_items[key_path]:
                    changes.append((old_value, en_items[key_path]))

    # Remove any pairs where old == new (extra safety)
    changes = [(old, new) for old, new in changes if old != new]

    # Output unmatched files
    if unmatched:
        for dev in unmatched:
            print(f"No matching file for {dev}")

    # Search MD files for quoted strings and print matches
    COLOR_OLD = '\033[91m'
    COLOR_PATH = '\033[96m'
    COLOR_NEW = '\033[92m'
    COLOR_RESET = '\033[0m'
    found_old_texts = False
    if changes:
        for root, _, files in os.walk(path_to_docs):
            for file in files:
                if file.endswith(".md"):
                    path = os.path.join(root, file)
                    with open(path, encoding="utf-8") as f:
                        for i, line in enumerate(f, 1):
                            for match in re.finditer(r'"(.*?)"', line):
                                found = match.group(1)
                                col = match.start(1) + 1
                                for old, new in changes:
                                    if found == old:
                                        print(f"{COLOR_OLD}{found}{COLOR_RESET} found in {COLOR_PATH}{path}:{i}:{col}{COLOR_RESET}.\nFound changed text: {COLOR_NEW}{new}{COLOR_RESET}\n")
                                        found_old_texts = True
    if not found_old_texts:
        print(f"{COLOR_NEW}No old texts found in MD files.{COLOR_RESET}")

if __name__ == "__main__":
    main()