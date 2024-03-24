from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def sel():
    try:
        options = Options()
        options.add_argument("--headless")
        options.add_argument("--remote-debugging-port=9222")
        options.binary_location = "/usr/bin/google-chrome"
        driver = webdriver.Chrome(options=options)

        return {"Ada": "QRCT"}
    except Exception as e:
        return {"error": str(e)}
