from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC

# nextHref = input("Please enter your link: ")
# nextHref = "https://gplinks.co/wPvSLr"

with open('links.txt', 'r') as file:
    for line in file:
        nextHref = line.strip()
        print(f"visit link: {nextHref}")

        options = Options()
        options.add_argument("--enable-notifications")
        options.accept_insecure_certs = True
        options.assume_untrusted_cert_issuer = True
        options.add_argument("--no-sandbox")
        options.add_argument("--allow-http-screen-capture")
        options.add_argument("--disable-impl-side-painting")
        options.add_argument("--disable-setuid-sandbox")
        options.add_argument("--disable-seccomp-filter-sandbox")

        # options.add_experimental_option("detach", True)
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),
                                  options=options)

        driver.maximize_window()

        isLoop = True
        while isLoop:
            try:
                driver.get(nextHref)
                verifyBtn = WebDriverWait(driver, 60).until(
                    EC.visibility_of_element_located((By.ID, 'VerifyBtn'))
                )
                verifyBtn.click()
                sleep(10)
                nextBtn = driver.find_element(By.ID, 'NextBtn')
                nextHref = nextBtn.get_attribute('href')
                print(nextHref)
                if nextHref.find('gplinks.co') != -1:
                    isLoop = False
                    driver.get(nextHref)
                    getLink = WebDriverWait(driver, 60).until(
                        EC.visibility_of_element_located((By.CSS_SELECTOR, '#link-btn a'))
                    )
                    sleep(15)
                    isGetLink = True
                    while isGetLink:
                        if getLink.get_attribute('innerHTML') == 'Get Link':
                            getLink.click()
                            isGetLink = False
                        else:
                            sleep(5)

            except:
                print("Something else went wrong")
                isLoop = False

        driver.quit()
