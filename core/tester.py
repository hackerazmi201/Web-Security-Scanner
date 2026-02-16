import requests
from payloads import XSS_PAYLOADS, SQLI_PAYLOADS

def submit_form(form_details, url, payload):
    target_url = url + form_details["action"]
    data = {}

    for input in form_details["inputs"]:
        if input["name"]:
            data[input["name"]] = payload

    if form_details["method"] == "post":
        return requests.post(target_url, data=data)
    else:
        return requests.get(target_url, params=data)

def test_xss(form_details, url):
    for payload in XSS_PAYLOADS:
        response = submit_form(form_details, url, payload)
        if payload in response.text:
            return True, payload
    return False, None

def test_sqli(form_details, url):
    for payload in SQLI_PAYLOADS:
        response = submit_form(form_details, url, payload)
        if "sql" in response.text.lower() or "error" in response.text.lower():
            return True, payload
    return False, None
