from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from pyvirtualdisplay import Display
import logging
from bs4 import BeautifulSoup
import os


# 配置日志记录
# logging.basicConfig(level=logging.DEBUG,  # 设置日志级别（DEBUG、INFO、WARNING、ERROR、CRITICAL）
                    # format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
# 创建一个日志记录器
# logger = logging.getLogger('my_logger')
def test_baidu():
    driver = init_drive()
    driver.get("https://www.baidu.com")
    # logger.debug(f'--------{driver.title}--------')
    assert '百度一下' in driver.title
    time.sleep(5)
    # logger.debug('finishing sleep 5s')

    input = driver.find_element(By.ID, value='kw')

    print(input)
    input.send_keys("猎聘网")
    button = driver.find_element(By.ID, value='su')
    button.click()
    print(driver.title)


def init_display():
    # display = Display(visible=0, size=(900, 800))
    # display.start()
    driver = init_drive()
    driver.get(url="https://www.baidu.com")
    print(driver.title)
    driver.quit()
    # display.stop()


def init_drive():
    options = Options()
    options.add_argument('--no-sandbox')
    options.add_argument('--headless')
    options.add_argument('--disable-gpu')
    # options.add_argument('--remote-debugging-port=3332')
    driver = webdriver.Chrome(options=options)
    return driver


def test_liepin():
    driver = init_drive()
    url = r"https://lpt.liepin.com/user/login"
    driver.get(url=url)
    time.sleep(5)
    if driver.title == "在线沟通":
        soup = BeautifulSoup(driver.page_source, "lxml")
        file_name = "chat.txt"
        if os.path.exists(file_name):
            print(f"{file_name} is exists")
        else:
            with open(file_name, "w") as file:
                file.write(soup.prettify(driver.page_source))
                print(f"{file_name} has been updated")
    


if __name__ == '__main__':
    # init_display()
    # test_baidu()
    test_liepin()
    print('Success!')