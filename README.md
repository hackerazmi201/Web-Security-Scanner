# 🛡️ Web Security Scanner  
### Automated Web Application Security Scanner (XSS & SQL Injection Detection)

---

## 📌 Overview

Web Security Scanner is a lightweight, CLI-based web vulnerability scanner built using **Python**.  
It helps security researchers and ethical hackers identify:

- Cross-Site Scripting (XSS)
- SQL Injection (SQLi)
- Vulnerable input forms

This tool is designed for **educational purposes** and **authorized security testing only**.

---

# 🚀 Features

- 🔍 Automatic form detection  
- 🧪 XSS payload testing  
- 💉 SQL Injection detection  
- 🎨 Colored CLI output (Linux & Windows supported)  
- 📄 JSON report generation  
- ⚡ Simple & fast scanning  
- 🖥️ Professional command-line interface  
- 🧾 Help menu (`-h` support)

---

# 🏗️ Project Structure

```
web-security-scanner/
│
├── scanner.py
├── core/
│   ├── crawler.py
│   ├── tester.py
│   └── payloads.py
│
├── reports/
├── requirements.txt
└── README.md
```

---

# 🛠️ Technologies Used

- Python 3
- Requests
- BeautifulSoup4
- Argparse
- Colorama

---

# 💻 Installation Guide

---

## 🔹 1️⃣ Windows Installation

### Step 1 – Install Python

Download Python from:  
https://www.python.org/downloads/

✔ Make sure to check: **“Add Python to PATH”**

---

### Step 2 – Clone the Repository

```bash
git clone https://github.com/hackerazmi201/web-security-scanner.git
cd web-security-scanner
```

---

### Step 3 – Install Requirements

```bash
pip install -r requirements.txt
```

---

### Step 4 – Run the Scanner

```bash
python scanner.py -u https://example.com
```

---

## 🐧 2️⃣ Linux Installation (Kali / Ubuntu / Parrot OS)

### Step 1 – Update System

```bash
sudo apt update
sudo apt install python3 python3-pip git -y
```

---

### Step 2 – Clone Project

```bash
git clone https://github.com/hackerazmi201/web-security-scanner.git
cd web-security-scanner
```

---

### Step 3 – Install Dependencies

```bash
pip3 install -r requirements.txt
```

---

### Step 4 – Run Scanner

```bash
python3 scanner.py -u https://example.com
```

---

## 🍎 3️⃣ macOS Installation

### Step 1 – Install Homebrew (if not installed)

```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

---

### Step 2 – Install Python & Git

```bash
brew install python git
```

---

### Step 3 – Clone Repository

```bash
git clone https://github.com/hackerazmi201/web-security-scanner.git
cd web-security-scanner
```

---

### Step 4 – Install Requirements

```bash
pip3 install -r requirements.txt
```

---

### Step 5 – Run Scanner

```bash
python3 scanner.py -u https://example.com
```

---

# 📌 Usage Guide

## 🔹 Help Menu

```bash
python scanner.py -h
```

Output:

```
usage: scanner.py [-h] -u URL [-o OUTPUT]

Web Security Scanner - XSS & SQLi Detection Tool

options:
  -h, --help            show help message
  -u, --url             Target URL to scan
  -o, --output          Custom output report file
```

---

## 🔹 Basic Scan

```bash
python scanner.py -u https://target.com
```

---

## 🔹 Custom Report Name

```bash
python scanner.py -u https://target.com -o myreport.json
```

---

# 📄 Report Output

After scanning, reports are automatically saved inside:

```
/reports/
```

Example:

```
reports/report_20260216_221530.json
```

---

# ⚠️ Disclaimer

This tool is intended for:

- Educational purposes  
- Security research  
- Authorized penetration testing  

⚠️ Do NOT scan websites without permission.  
Unauthorized testing is illegal.

---

# 🧠 Future Improvements

- Multi-thread scanning
- Directory fuzzing
- Subdomain enumeration
- HTML report dashboard
- Vulnerability severity rating
- Export to PDF

---

# 🤝 Contributing

Pull requests are welcome.  
For major changes, please open an issue first.

---

# 📜 License

MIT License

---

# 👨‍💻 Author

**HackerAzmi**  
Ethical Hacker | Bug Bounty Hunter | Security Researcher  

GitHub: https://github.com/hackerazmi201  

---

# ⭐ Support

If you like this project, please ⭐ star the repository.
