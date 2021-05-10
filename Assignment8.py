from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time


def Bai1():
    driver = webdriver.Chrome(executable_path='./drive/chromedriver.exe')
    driver.maximize_window()
    driver.get("http://www.practiceselenium.com/practice-form.html")

    Firstname = driver.find_element_by_name('firstname')
    Firstname.send_keys("Huong")
    
    Lastname = driver.find_element_by_name('lastname')
    Lastname.send_keys("Nguyen Thi")

    Sex = driver.find_element_by_id('sex-1')
    Sex.click()

    Year = driver.find_element_by_id('exp-6')
    Year.click()

    FavoBlack = driver.find_element_by_id('tea1')
    FavoBlack.click()
    FavoRed = driver.find_element_by_id('tea2')
    FavoRed.click()

    Excibreak = driver.find_element_by_id('tool-0')
    Excibreak.click()

    Excibreak = driver.find_element_by_id('tool-1')
    Excibreak.click()

    Continent = Select(driver.find_element_by_id('continents'))
    Continent.select_by_visible_text('Asia')

    Command = Select(driver.find_element_by_id('selenium_commands'))
    Command.select_by_visible_text('Browser Commands')

    driver.find_element_by_id('submit').click()

    time.sleep(2)
    print(driver.current_url)
    driver.quit()

def Bai2():
    driver = webdriver.Chrome(executable_path='./drive/chromedriver.exe')
    driver.maximize_window()
    driver.get("http://automationpractice.com/index.php")
    assert "My Store" in driver.title
    Signin = driver.find_elements_by_xpath('//*[contains(text(), "Sign in")]')
    Signin[0].click()
    
    assert "Login - My Store" in driver.title
    driver.find_element_by_id('SubmitLogin').click()

    alert_text = driver.find_element_by_css_selector(".alert.alert-danger").text
    
    assert 'An email address required' in alert_text

    time.sleep(2)
    driver.quit()





if __name__ == "__main__":
    Bai1()
    # Bai2()

        


