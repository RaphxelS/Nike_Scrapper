import time
import sys
import validators
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.color import Color

chrome_options = Options()
chrome_options.add_argument('--headless')  # No window
chrome_options.add_argument('--log-level=3')
chrome_options.add_argument("--window-size=1920x1080")
# OLD CODE: driver = webdriver.Chrome(chrome_options=chrome_options)
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
action = ActionChains(driver)


def main(tailleA, lienA):
    if validators.url(lienA):
        rep = "\nSIZE FOUND \n" + nike(tailleA, lienA)
        driver.delete_all_cookies()
        return rep
    else:
        rep1 = "\nSIZE FOUND \n" + nike(tailleA, cherche(lienA))
        driver.delete_all_cookies()
        return rep1


def nike(taille, lien):
    # taille = input("Taille :")
    # lien = input("Lien Nike :")
    # delai = float(input("Delai :"))
    original_window = driver.current_window_handle
    driver.delete_all_cookies()
    driver.switch_to.new_window('window')
    driver.close()
    driver.switch_to.window(original_window)

    driver.get(lien)
    driver.implicitly_wait(20)
    driver.find_element(by=By.XPATH, value='//*[@id="gen-nav-commerce-header-v2"]/div[1]/div/div[2]/div/div[3]/div['
                                           '1]/div[1]').click()
    print("COOKIE BYPASS")
    size = driver.find_element(by=By.XPATH, value="//*[text()='EU %s']" % taille)
    color = driver.find_element(by=By.XPATH, value="//*[text()='EU %s']" % taille).value_of_css_property(
        'background-color')

    hax = Color.from_string(color).hex
    driver.save_screenshot("screenshot.png")

    print("SIZE FOUND" + "=" + size.get_attribute('innerHTML'))

    driver.maximize_window()
    driver.save_screenshot("screenshot.png")

    return size.get_attribute('innerHTML') + "=" + check(hax)


def check(hax):
    if hax == '#f7f7f7':
        return "HORS STOCK"
    else:
        return "EN STOCK"


def cherche(mot):
    if len(mot) != 1:
        s = mot.replace(" ", "")
        print(s)

    driver.get("https://www.nike.com/fr/w?q=%s" % mot)
    driver.implicitly_wait(20)
    driver.find_element(by=By.XPATH,
                        value='//*[@id="gen-nav-commerce-header-v2"]/div[1]/div/div[2]/div/div[3]/div[''1]/div[1]').\
        click()
    up = mot.title()
    print(up)
    driver.find_element(by=By.XPATH,
                        value='//*[@id="Wall"]/div/div[6]/div[2]/main/section/div/div[1]/div/figure/a[2]/div/div/img').\
        click()
    driver.implicitly_wait(20)
    s = driver.current_url
    return str(s)


if __name__ == "__main__":
    tailleA = sys.argv[1]
    lienA = sys.argv[2]
    main(tailleA, lienA)
