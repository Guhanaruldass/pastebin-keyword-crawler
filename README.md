# Pastebin Keyword Crawler

A Python script that scrapes Pastebin’s public archive and extracts pastes containing crypto-related keywords and Telegram links.

---

## Features

- Scrapes the latest 30 pastes from [Pastebin Archive](https://pastebin.com/archive).
- Searches paste content for keywords such as:
  - `crypto`, `bitcoin`, `ethereum`, `blockchain`
  - Telegram links: `t.me`
- Saves matching pastes to `keyword_matches.jsonl` in JSONL format.
- Includes basic rate limiting to prevent blocking.

---

## Setup Instructions

1. **Clone the repository:**

   ```bash
   git clone https://github.com/Guhanaruldass/pastebin-keyword-crawler.git
   cd pastebin-keyword-crawler
