from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


def sel():
    try:
        options = Options()
        options.add_argument("--headless")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--remote-debugging-port=9222")
        options.add_argument("--user-data-dir=/root/code/fastapiping")
        options.add_argument("--disable-gpu")
        options.binary_location = "/usr/bin/google-chrome"
        service = Service(
            executable_path="/root/code/fastapiping/chromedriver-linux64/chromedriver"
        )

        driver = webdriver.Chrome(options=options, service=service)

        return {"Ada": "QRCT"}
    except Exception as e:
        return {"error": str(e)}
