import requests
import json
import os
import urllib.request
import threading
from tkinter import messagebox

# URL of the update information JSON file
UPDATE_JSON_URL = "https://pastebin.com/LiWc3GcH"

# Path to the directory where Pixel Parks is installed
INSTALLATION_DIR = "C:/Path/To/PixelParks"

def generate_update_json(version, update_url):
    update_info = {
        "version": version,
        "url": update_url
    }
    with open("update.json", "w") as update_file:
        json.dump(update_info, update_file)

def check_for_updates():
    try:
        # Download update information from the URL
        with urllib.request.urlopen(UPDATE_JSON_URL) as url:
            update_info = json.loads(url.read().decode())

        latest_version = update_info["version"]
        latest_update_url = update_info["url"]
        current_version = get_current_version()

        if latest_version != current_version:
            messagebox.showinfo("Update Available",
                                f"New version {latest_version} is available. Click OK to update.")
            download_update(latest_update_url)
    except Exception as e:
        print("Error checking for updates:", e)

def get_current_version():
    try:
        with open("update.json", "r") as update_file:
            data = json.load(update_file)
            return data["version"]
    except FileNotFoundError:
        return "0.0"

def download_update(update_url):
    try:
        update_file = os.path.join(INSTALLATION_DIR, "PixelParks.exe")
        urllib.request.urlretrieve(update_url, update_file)
        messagebox.showinfo("Update Downloaded", "Update downloaded successfully. Please restart the application to apply the update.")
    except Exception as e:
        print("Error downloading update:", e)

# Example usage:
latest_version = "1.1"
latest_update_url = "https://pastebin.com/LiWc3GcH"
generate_update_json(latest_version, latest_update_url)

# Check for updates in a separate thread
threading.Thread(target=check_for_updates, daemon=True).start()
