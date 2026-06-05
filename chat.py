
# ==============================
# PIXELBET AUTO CHAT BOT
# ==============================

import time
import random
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

# ==============================
# CONFIG
# ==============================

DELAY_PER_MESSAGE = 15

MESSAGES = [
    "good luck everyone!",
    "rain incoming 😂",
    "who hit jackpot today?",
    "lets gooooo!",
    "big win soon 🔥",
    "anyone from indonesia?",
    "pixelbet best site fr",
    "nice game 😎",
]

# ==============================
# CHROME OPTIONS
# ==============================

chrome_options = Options()

chrome_options.add_argument("--start-maximized")

# Anti basic detection
chrome_options.add_argument("--disable-blink-features=AutomationControlled")
chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
chrome_options.add_experimental_option('useAutomationExtension', False)

# ==============================
# DRIVER
# ==============================

driver = webdriver.Chrome(options=chrome_options)

# ==============================
# OPEN WEBSITE
# ==============================

driver.get("https://pixelbet.gg")

print("===================================")
print("LOGIN MANUALLY TO YOUR ACCOUNT")
print("After login press ENTER here")
print("===================================")

input()

print("Bot Started...")

# ==============================
# AUTO CHAT LOOP
# ==============================

while True:

    try:

        # RANDOM MESSAGE
        message = random.choice(MESSAGES)

        # ==========================
        # CHAT INPUT
        # ==========================

        # IMPORTANT:
        # You may need to inspect the website
        # and change this selector if needed.

        chat_input = driver.find_element(
            By.CSS_SELECTOR,
            "input"
        )

        # CLICK INPUT
        chat_input.click()

        # TYPE MESSAGE
        chat_input.send_keys(message)

        # SEND ENTER
        chat_input.send_keys(Keys.ENTER)

        print(f"[SENT] {message}")

        # RANDOM EXTRA DELAY
        extra_delay = random.randint(1, 5)

        total_delay = DELAY_PER_MESSAGE + extra_delay

        print(f"Waiting {total_delay} seconds...")

        time.sleep(total_delay)

    except Exception as e:

        print("ERROR:", e)

        print("Retrying in 10 seconds...")

        time.sleep(10)
