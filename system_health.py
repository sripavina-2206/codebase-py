import shutil

def check_disk():
    # Checks disk usage of the root directory
    total, used, free = shutil.disk_usage("/")
    free_percent = (free / total) * 100
    
    print("--- System Storage Health ---")
    print(f"Total Space: {total // (2**30)} GB")
    print(f"Free Space: {free // (2**30)} GB ({free_percent:.1f}%)")

    if free_percent < 20:
        print("Warning: Low disk space!")
    else:
        print("Disk space is healthy.")

if __name__ == "__main__":
    check_disk()
