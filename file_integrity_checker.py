import hashlib
import os
import json

HASH_DB = 'hashes.json'

def calculate_hash(file_path):
    sha256 = hashlib.sha256()
    try:
        with open(file_path, 'rb') as f:
            while chunk := f.read(8192):
                sha256.update(chunk)
        return sha256.hexdigest()
    except FileNotFoundError:
        return None

def scan_directory(directory):
    hash_data = {}
    for root, _, files in os.walk(directory):
        for file in files:
            full_path = os.path.join(root, file)
            normalized_path = os.path.abspath(full_path)
            hash_data[normalized_path] = calculate_hash(normalized_path)
    return hash_data


def save_hashes(directory):
    hashes = scan_directory(directory)
    with open(HASH_DB, 'w') as f:
        json.dump(hashes, f, indent=4)
    print("Initial hashes saved.")

def verify_files(directory):
    if not os.path.exists(HASH_DB):
        print("No hash database found. Run save_hashes() first.")
        return

    with open(HASH_DB, 'r') as f:
        old_hashes = json.load(f)

    new_hashes = scan_directory(directory)

    for path, old_hash in old_hashes.items():
        new_hash = new_hashes.get(path)
        if new_hash is None:
            print(f"Deleted: {path}")
        elif new_hash != old_hash:
            print(f"Modified: {path}")

    for path in new_hashes:
        if path not in old_hashes:
            print(f"New file: {path}")


    with open(HASH_DB, 'r') as f:
        old_hashes = json.load(f)

    new_hashes = scan_directory(directory)

    for path, old_hash in old_hashes.items():
        new_hash = new_hashes.get(path)
        if new_hash is None:
            print(f"Deleted: {path}")
        elif new_hash != old_hash:
            print(f"Modified: {path}")

    for path in new_hashes:
        if path not in old_hashes:
            print(f"New file: {path}")

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="File Integrity Checker")
    parser.add_argument("mode", choices=["save", "check"], help="save = store hashes, check = verify")
    parser.add_argument("directory", help="Folder to check")
    args = parser.parse_args()

    if args.mode == "save":
        save_hashes(args.directory)
    elif args.mode == "check":
        verify_files(args.directory)
