import requests
from bs4 import BeautifulSoup
import json
from datetime import datetime
import time

# Keywords to search for
KEYWORDS = ["crypto", "bitcoin", "ethereum", "blockchain", "t.me"]

# Output file
OUTPUT_FILE = "keyword_matches.jsonl"

# Function to fetch paste IDs from Pastebin archive
def get_paste_ids():
    url = "https://pastebin.com/archive"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    links = soup.find_all("a", href=True)
    paste_ids = []

    for link in links:
        href = link['href']
        if href.startswith('/') and len(href[1:]) == 8:  # paste IDs are 8 characters
            paste_ids.append(href[1:])
    
    return list(set(paste_ids))[:30]  # unique & only latest 30

# Function to check keywords in a paste
def check_keywords(paste_id):
    raw_url = f"https://pastebin.com/raw/{paste_id}"
    try:
        response = requests.get(raw_url, timeout=10)
        content = response.text.lower()
    except Exception as e:
        print(f"Failed to fetch {paste_id}: {e}")
        return

    found = [word for word in KEYWORDS if word in content]
    if found:
        result = {
            "source": "pastebin",
            "context": f"Found crypto-related content in Pastebin paste ID {paste_id}",
            "paste_id": paste_id,
            "url": raw_url,
            "discovered_at": datetime.utcnow().isoformat() + "Z",
            "keywords_found": found,
            "status": "pending"
        }
        with open(OUTPUT_FILE, "a") as f:
            f.write(json.dumps(result) + "\n")
        print(f"[+] Match found in {paste_id}: {found}")
    else:
        print(f"[-] No match in {paste_id}")

# Main process
def main():
    paste_ids = get_paste_ids()
    print(f"[*] Found {len(paste_ids)} pastes. Checking them...")

    for paste_id in paste_ids:
        check_keywords(paste_id)
        time.sleep(2)  # basic rate limiting

if __name__ == "__main__":
    main()
