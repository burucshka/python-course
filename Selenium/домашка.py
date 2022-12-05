from selenium import webdriver
import time
from selenium.webdriver.common.by import By
drriver = webdriver.Chrome(executable_path=r"C:\Users\Viktor\PycharmProjects\pythonProject1\Selenium\chromedriver.exe")
import os.path
try:
    ask = input("Enter name file: ")
    file = open(ask + ".txt", "w")
    drriver.get(url='https://www.marvel.com/characters')
    time.sleep(5)
    # drriver.get_screenshot_as_file("fablo.png")
    # drriver.save_screenshot("pablo.png")
    name = drriver.title
    # element = drriver.find_element(By.CLASS_NAME, "promo__title")
    # print(element.text)
    elements =drriver.find_elements(By.CLASS_NAME, "card-body__headline")
    listd = []
    for i in elements:
        if i.text:
            file.write(i.text + "\n")
            listd.append(i.text)
    print(listd)
    file.close()
except Exception as error:
    print(error)
finally:
    drriver.close()
    drriver.quit()