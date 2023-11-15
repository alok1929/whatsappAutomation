from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup

# Replace 'your_username' with the Instagram username of the page you want to scrape
instagram_username = 'alokhedge'

# Set up the Chrome WebDriver
driver = webdriver.Chrome()

# Load Instagram profile page
url = f'https://www.instagram.com/{instagram_username}/'
driver.get(url)

try:
    # Wait for the dynamic content to load
    element_present = EC.presence_of_element_located((By.CLASS_NAME, 'v1Nh3'))
    WebDriverWait(driver, 10).until(element_present)

    # Get the page source after the content is loaded
    page_source = driver.page_source
    soup = BeautifulSoup(page_source, 'html.parser')

    # Find the URL of the most recent post
    post_link = soup.find('a', class_='v1Nh3')['href']
    post_url = f'https://www.instagram.com{post_link}'

    print(f"The most recent post URL: {post_url}")

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    # Close the WebDriver
    driver.quit()
