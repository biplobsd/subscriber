from msedge.selenium_tools import Edge, EdgeOptions

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


def findopj(pattern: str, delay: int = 10):
    try:
        return WebDriverWait(driver, delay).until(
            EC.visibility_of_element_located((By.XPATH, pattern))
        )
    except TimeoutException:
        return False


def dataload():
    with open("data.txt") as r:
        return r.read().split("\n")


def subNow(objXpath):
    allOpe = findopj(objXpath)
    if allOpe:
        allOpe.click()
        return True
    return False


def main():
    for c in dataload():
        addSecure = "https://"
        driver.get(addSecure+c if addSecure not in c else c)
        if not findopj(subscribed, 2):
            if subNow(subbuttion):
                print("Done...", c)
            else:
                print("Unable to ...", c)
        else:
            print("Already subscribed : "+c)


if __name__ == "__main__":

    # Launch Microsoft Edge (EdgeHTML)
    driver = Edge("msedgedriver.exe")

    # Launch Microsoft Edge (Chromium)
    options = EdgeOptions()
    options.use_chromium = True
    
    # Hare your Edge user profile folder path. You can find in edge://version/ "Profile Path" section
    options.add_argument(
        r'--user-data-dir=C:\\Users\\alpha4d\\AppData\\Local\\Microsoft\\Edge\\User Data')
    
    driver = Edge(options=options)

    # click button
    allOperations = '//a[text()="All Operations"]'
    getDetails = '//td[@data-header="Details: "]'

    subbuttion = "//yt-formatted-string[text()='Subscribe']/../../../ytd-subscribe-button-renderer[@class='style-scope ytd-c4-tabbed-header-renderer']"
    subscribed = "//yt-formatted-string[text()='Subscribed']/../../tp-yt-paper-button"

    # landing = "https://www.youtube.com/c/TechWithTim"
    # driver.get(landing)

    main()
