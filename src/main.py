from urllib.parse import urljoin

from apify import Actor
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.common.by import By

# To run this Actor locally, you need to have the Selenium Chromedriver installed.
# https://www.selenium.dev/documentation/webdriver/getting_started/install_drivers/
# When running on the Apify platform, it is already included in the Actor's Docker image.


async def main():
    async with Actor:
        # Read the Actor input
        actor_input = await Actor.get_input() or {}
        start_urls = actor_input.get('start_urls')
        max_depth = actor_input.get('max_depth')

        if not start_urls:
            Actor.log.info('No start URLs specified in actor input, exiting...')
            await Actor.exit()

        # Launch a new Selenium Chrome WebDriver
        Actor.log.info('Launching Chrome WebDriver...')
        chrome_options = ChromeOptions()
        if Actor.config.headless:
            chrome_options.add_argument('--headless')
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--disable-dev-shm-usage')
        driver = webdriver.Chrome(options=chrome_options)
        
        try:
            # Open the URL in the Selenium WebDriver
            print(start_urls)
            print(type(start_urls))
            url = 'prueba_url'
            title = 3
            print('hola')
            print('hola2')
            await Actor.push_data({ 'url': url, 'title': title })
        except:
            Actor.log.exception(f'Cannot extract data from {url}.')

        driver.quit()
