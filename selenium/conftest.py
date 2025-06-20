import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time

@pytest.fixture(scope="function")
def driver():
    # Configuration du driver Chrome
    options = Options()
    options.add_argument('--start-maximized')
    options.add_argument('--disable-gpu')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('--disable-extensions')
    options.add_argument('--disable-popup-blocking')
    options.add_argument('--disable-blink-features=AutomationControlled')
    options.add_experimental_option('excludeSwitches', ['enable-automation'])
    options.add_experimental_option('useAutomationExtension', False)
    
    try:
        # Initialisation du driver
        driver = webdriver.Chrome(options=options)
        driver.implicitly_wait(10)
        driver.set_page_load_timeout(30)
        
        yield driver
        
    except Exception as e:
        print(f"Une erreur s'est produite : {str(e)}")
        raise e
        
    finally:
        try:
            if driver:
                driver.quit()
        except Exception as e:
            print(f"Erreur lors de la fermeture du driver : {str(e)}") 