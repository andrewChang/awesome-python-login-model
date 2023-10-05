from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from pyvirtualdisplay import Display
import logging

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

if __name__=='__main__':
    init_display()
    # test_baidu()
    print('Success!')