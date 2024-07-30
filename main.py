import itertools
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

# combinations from 'aa' to 'zz'
def generate_alpha_combinations():
    for letters in itertools.product("abcdefghijklmnopqrstuvwxyz", repeat=2):
        yield ''.join(letters)

def generate_numeric_range():
    for number in range(0000, 10000):
        yield str(number)

# Create URLs
def generate_urls(base_url):
    urls = []
    for alpha in generate_alpha_combinations():
        for num in generate_numeric_range():
            url = base_url.replace('yy', alpha).replace('xxxx', num)
            urls.append(url)
    return urls

# Configure Chrome options
def configure_chrome_options(incognito):
    chrome_options = Options()
    chrome_options.add_argument("--disable-infobars")
    chrome_options.add_argument("--disable-extensions")
    chrome_options.add_argument("--disable-popup-blocking")
    if incognito:
        chrome_options.add_argument("--incognito")
    return chrome_options

# Open URLs in browser
def open_urls_in_browser(urls, delay, incognito):
    chrome_options = configure_chrome_options(incognito)
    
    # Create new instance of Chrome driver
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

    for url in urls:
        try:
            driver.get(url)
            print(f"Opened: {url}")
        except Exception as e:
            print(f"Failed to open {url}: {e}")
        time.sleep(delay)

    driver.quit()

if __name__ == "__main__":
    base_url = "https://www.example.com/yyxxxx"  #keep it yy and xxxx or change line 22 and generater
    delay = 5  # Delay in seconds
    incognito = True  # Incognito mode (Boolean)

    urls_list = [
        "http://example.com/01",
        "http:/example.com/02",
        # Add URLs here
    ]

    use_generated_urls = True  # Set to True to use generated URLs

    if use_generated_urls:
        urls = generate_urls(base_url)
        urls = urls[:10]  # number of URLs u wanna run
    else:
        urls = urls_list

    open_urls_in_browser(urls, delay, incognito)
