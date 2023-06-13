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
        prueba_input = actor_input.get('prueba_input')

        if not start_urls:
            Actor.log.info(
                'No start URLs specified in actor input, exiting...')
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
            print(actor_input)
            print(type(actor_input))
            url_texto = start_urls[0]['url']
            driver.get(url_texto)
            texto_boton = driver.find_elements(
                By.CSS_SELECTOR, "body > div.L3eUgb > div.o3j99.ikrT4e.om7nvf > form > div:nth-child(1) > div.A8SBwf > div.FPdoLc.lJ9FBc > center > input.gNO89b")
            print(f'texto botón: {texto_boton}')
            print(type(texto_boton))
            url = url_texto

            title = 3

            title2 = 4

            url2 = 'url'

            await Actor.push_data({'url': url, 'title': title, 'prueba': prueba_input})
            await Actor.push_data({'url': url2, 'title': title2, 'prueba': texto_boton})
        except:
            Actor.log.exception(f'Cannot extract data from {url}.')

        driver.quit()
