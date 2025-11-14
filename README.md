# 🔍 Directory Bruteforcer (Advanced Python Tool)

A **multi-threaded directory brute-forcing tool** built for offensive security labs and reconnaissance automation.
Designed to discover hidden directories such as `/admin`, `/backup`, `/config`, and undocumented API endpoints.

This tool includes:

* ⚡ High-speed multi-threading
* 🔁 Retry logic for unstable targets
* 🧠 Response fingerprinting (status + content length clusters)
* 🎯 Dynamic throttling to avoid WAF/IDS alerts
* 🖥️ Random User-Agent spoofing
* 📊 HTML, JSON, TXT reports
* 🟢 Clean, colorized console output
* 📈 Real-time progress bar

Developed as part of offensive security research and learning.

---

# 📂 Project Structure

```
dir-bruteforcer/
│── src/
│   └── dir_bruteforcer.py
│── wordlists/
│   └── common.txt
│── reports/
│   └── (generated reports here)
│── README.md
│── LICENSE
```

---

# 🚀 Features

### ✔ Multi-threaded (30 threads default)

Achieves fast enumeration without causing excessive server pressure.

### ✔ Intelligent Retry Logic

Handles timeouts, dropped packets, and unstable targets smoothly.

### ✔ Dynamic Throttling (0.05s – 0.20s)

Prevents false positives and avoids overwhelming production servers.

### ✔ Response Fingerprinting

Clusters responses using:

```
status-code + content-length
```

Example:

```
200-5120
403-124
301-0
```

Helps identify interesting or suspiciously long/short responses.

### ✔ Output Formats

Stored automatically under `/reports`:

| Format | Purpose                           |
| ------ | --------------------------------- |
| TXT    | Quick grep-friendly summary       |
| JSON   | Script automation / API pipelines |
| HTML   | Client reports, evidence-ready    |

---

# 🧪 Usage

### **Basic Scan**

```bash
python3 src/dir_bruteforcer.py https://example.com wordlists/common.txt
```

### **Example Output**

```
Progress: 45.83%
[FOUND] 200 | 5432 bytes | /admin
[FOUND] 403 | 124 bytes | /backup
[FOUND] 301 | 0 bytes | /login
```

### **Generated Reports**

Inside `/reports/`:

```
results-20251114-134530.txt
results-20251114-134530.json
results-20251114-134530.html
```

---

# 📸 Suggested Screenshot for GitHub (optional)

Open terminal and run:

```bash
python3 src/dir_bruteforcer.py https://testphp.vulnweb.com wordlists/common.txt
```

Then screenshot the green `[FOUND]` lines — looks excellent on GitHub.

---

# 🛠 How It Works (Internals)

### **1. Multi-thread Worker Pool**

Each worker:

* pulls a path from a shared queue
* builds full URL using `urljoin()`
* sends GET request
* fingerprints response
* saves result

### **2. Retry Mechanism**

If request fails:

```
retry → retry → retry → give up
```

### **3. Dynamic Throttling**

Each request sleeps for:

```
0.05s – 0.20s (random)
```

### **4. Fingerprinting Engine**

Fingerprint is generated using:

```
<status-code>-<content-length>
```

This helps detect:

* redirects
* forbidden directories
* suspiciously short responses
* WAF challenges

### **5. Real-time Progress Bar**

Updates every 0.2 seconds:

```
Progress: 78.12%
```

---

# 📈 Benchmarks (Local Lab Test)

Test target: DVWA (low security)
Wordlist: 200 lines
Threads: 30

| Mode                      | Time         |
| ------------------------- | ------------ |
| Single-thread             | ~18 seconds  |
| Multi-thread (30 threads) | ~1.4 seconds |

Speedup: **12x faster**

---

# 📌 Future Enhancements

* Recursive brute-forcing
* File extension scanning (`.php`, `.bak`, `.old`)
* Tor / proxy support
* WAF detection mode
* Burp Collaborator integration
* Visual clustering for fingerprints
* Ignore-length filter with thresholds

---

# 🧑‍⚖️ Ethical Disclaimer

This tool is intended **strictly for educational and authorized penetration testing** only.
Scanning any target without explicit permission is illegal and unethical.

The author is not responsible for misuse.

---

# 👨‍💻 Author

**Vignesh Mani**
Offensive Security Researcher
GitHub: [https://github.com/vigneshoffsec](https://github.com/vigneshoffsec)
LinkedIn: [https://linkedin.com/in/vignesh-m17](https://linkedin.com/in/vignesh-m17)
