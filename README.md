# Directory Bruteforcer (Python)

A multi-threaded directory brute-forcing tool with retry logic, response fingerprinting, and intelligent throttling.  
Built for educational pentesting and reconnaissance automation.

## Features
- 🚀 Multi-threaded (20 threads default)
- 🔁 Retry logic for unstable targets
- 🧠 Response fingerprinting (status + content length)
- ⚙️ Intelligent throttling to avoid false positives
- 📄 Wordlist support
- 📊 Ranked output for reporting

## Usage

```bash
python3 src/dir_bruteforcer.py https://example.com wordlists/common.txt
```

## Example Output
- 200 - 5321 bytes - /admin
- 301 - 0 bytes - /login
- 403 - 124 bytes - /backup

## Notes

For ethical use only.

Do not run on targets without permission.
