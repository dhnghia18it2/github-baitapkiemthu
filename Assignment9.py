from selenium import webdriver
from selenium.webdriver.common.by import By
import time


def Bai1():
    driver = webdriver.Chrome(executable_path='./drive/chromedriver.exe')
    driver.get("http://practice.automationtesting.in/")
    time.sleep(2)
    driver.quit()

def Bai2():
    driver = webdriver.Chrome(executable_path='./drive/chromedriver.exe')
    driver.maximize_window()
    driver.get("http://practice.automationtesting.in/")
    time.sleep(2)
    driver.quit()

def Bai3():
    driver = webdriver.Chrome(executable_path='./drive/chromedriver.exe')
    driver.set_window_size(1200, 768)
    driver.get("http://practice.automationtesting.in/")
    time.sleep(2)
    driver.quit()

def Bai4_va_5():
    driver = webdriver.Chrome(executable_path='./drive/chromedriver.exe')
    driver.maximize_window()
    driver.get("http://practice.automationtesting.in/")
    print(driver.title)
    print(driver.current_url)
    time.sleep(2)
    driver.quit()

def Bai6():
    driver = webdriver.Chrome(executable_path='./drive/chromedriver.exe')
    driver.maximize_window()
    driver.get("http://practice.automationtesting.in/")
    print(driver.page_source)
    time.sleep(2)
    driver.quit()

def Bai7():
    driver = webdriver.Chrome(executable_path='./drive/chromedriver.exe')
    driver.maximize_window()
    driver.get("http://practice.automationtesting.in/")

    clickMenu = driver.find_element(By.XPATH,"/html/body/div[1]/div[1]/header/div[2]/nav/ul/li[2]/a")
    clickMenu.click()

    email = driver.find_element(By.XPATH,"/html/body/div[1]/div[2]/div/div/div/div/div[1]/div/div[2]/form/p[1]/input")
    email.send_keys("vnakhoa.18it2@vku.udn.vn")

    password = driver.find_element(By.XPATH,"/html/body/div[1]/div[2]/div/div/div/div/div[1]/div/div[2]/form/p[2]/input")
    password.send_keys("anhkhoa121")

    Registration = driver.find_element(By.XPATH,"/html/body/div[1]/div[2]/div/div/div/div/div[1]/div/div[2]/form/p[3]/input[3]")
    Registration.click()

    time.sleep(2)
    driver.quit()

def Bai8():
    driver = webdriver.Chrome(executable_path='./drive/chromedriver.exe')
    driver.maximize_window()
    driver.get("https://the-internet.herokuapp.com")

    clickMenu = driver.find_element(By.XPATH,"/html/body/div[2]/div/ul/li[21]/a")
    clickMenu.click()

    email = driver.find_element(By.XPATH,"/html/body/div[2]/div/div/form/div[1]/div/input")
    email.send_keys("tomsmith")

    password = driver.find_element(By.XPATH,"/html/body/div[2]/div/div/form/div[2]/div/input")
    password.send_keys("SuperSecretPassword!")

    login = driver.find_element(By.XPATH,"/html/body/div[2]/div/div/form/button")
    login.click()

    print(driver.title)
    time.sleep(2)
    driver.quit()

def Bai9():
    driver = webdriver.Chrome(executable_path='./drive/chromedriver.exe')
    driver.maximize_window()
    driver.get("https://itmscoaching.herokuapp.com/form")

    fname = driver.find_element(By.XPATH,"/html/body/div[1]/form/div/div[1]/input")
    fname.send_keys("Binh")

    lname = driver.find_element(By.XPATH,"/html/body/div[1]/form/div/div[2]/input")
    lname.send_keys("Nguyen")

    job = driver.find_element(By.XPATH,"/html/body/div[1]/form/div/div[3]/input")
    job.send_keys("Tester")

    education = driver.find_element(By.XPATH,"/html/body/div[1]/form/div/div[4]/div[4]/input")
    education.click()

    sex = driver.find_element(By.XPATH,"/html/body/div[1]/form/div/div[5]/div[3]/input")
    sex.click()

    selectExperience = driver.find_element(By.XPATH,"/html/body/div[1]/form/div/div[6]/select/option[4]")
    selectExperience.click()

    date = driver.find_element(By.XPATH,"/html/body/div[1]/form/div/div[7]/input")
    date.send_keys("20/7/2011")

    submit = driver.find_element(By.XPATH,"/html/body/div[1]/form/div/div[8]/a")
    submit.click()

    print(driver.title)
    time.sleep(5)
    driver.quit()

if __name__ == "__main__":
    Bai1()
    # Bai2()
    # Bai3()
    # Bai4_va_5()
    # Bai6()
    # Bai7()
    # Bai8()
    # Bai9()
        


