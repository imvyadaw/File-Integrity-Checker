import hashlib
import time

def get_file_hash(file_path):
    with open(file_path, 'rb') as f:
        file_data = f.read()
        return hashlib.sha256(file_data).hexdigest()

if __name__ == "__main__":
    file = input("Enter file name to monitor: ")
    baseline_hash = get_file_hash(file)
    print(f"[+] Monitoring started on {file}...")

    while True:
        current_hash = get_file_hash(file)
        if current_hash != baseline_hash:
            print("[!] ALERT: File has been modified!")
            break
        time.sleep(5)
