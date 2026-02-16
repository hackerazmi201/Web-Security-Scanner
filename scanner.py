import argparse
import sys
import os
from colorama import Fore, Style, init
from core.crawler import get_forms, get_form_details
from core.tester import test_xss, test_sqli
import json
from datetime import datetime

init(autoreset=True)

def banner():
    print(Fore.GREEN + r"""
  _    _            _                                     _ 
 | |  | |          | |                                   (_)
 | |__| | __ _  ___| | _____ _ __ __ _ _____ __ ___  _  _ 
 |  __  |/ _` |/ __| |/ / _ \ '__/ _` |_  / '_ ` _ \| || |
 | |  | | (_| | (__|   <  __/ | | (_| |/ /| | | | | | || |
 |_|  |_|\__,_|\___|_|\_\___|_|  \__,_/___|_| |_| |_|_||_|
    """)


def save_report(results, output_file=None):
    if not os.path.exists("reports"):
        os.makedirs("reports")

    if not output_file:
        output_file = f"reports/report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"

    with open(output_file, "w") as f:
        json.dump(results, f, indent=4)

    print(Fore.CYAN + f"[+] Report saved at {output_file}")

def scan(url):
    print(Fore.YELLOW + f"[+] Scanning Target: {url}")

    forms = get_forms(url)
    print(Fore.BLUE + f"[+] Found {len(forms)} forms")

    results = []

    for form in forms:
        details = get_form_details(form)
        print(Fore.MAGENTA + f"[*] Testing form action: {details['action']}")

        xss_vuln, xss_payload = test_xss(details, url)
        sqli_vuln, sqli_payload = test_sqli(details, url)

        result = {
            "form_action": details["action"],
            "xss_vulnerable": xss_vuln,
            "xss_payload": xss_payload,
            "sqli_vulnerable": sqli_vuln,
            "sqli_payload": sqli_payload
        }

        results.append(result)

        if xss_vuln:
            print(Fore.RED + f"[!] XSS Vulnerability Detected using payload: {xss_payload}")

        if sqli_vuln:
            print(Fore.RED + f"[!] SQL Injection Detected using payload: {sqli_payload}")

    save_report(results)

def main():
    parser = argparse.ArgumentParser(
        description="Web Security Scanner - XSS & SQLi Detection Tool"
    )

    parser.add_argument("-u", "--url", help="Target URL to scan", required=True)
    parser.add_argument("-o", "--output", help="Custom output file name")

    args = parser.parse_args()

    banner()
    scan(args.url)

if __name__ == "__main__":
    main()

