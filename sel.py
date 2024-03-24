from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def sel():
    options = Options()
    options.add_argument("--headless")
    options.binary_location = "/usr/bin/google-chrome"
    driver = webdriver.Chrome(options=options)

    return {"Ada": "QRCT"}
