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
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import concurrent.futures
import requests


class ResumeCrawl:
    def __init__(self) -> None:
        self.driver = self.init_drive()
        self.cookies = None
    
    def set_cookies(self, cookies):
        self.cookies = cookies

    def init_drive(self):
        options = Options()
        options.add_argument('--no-sandbox')
        # options.add_argument('--headless')
        options.add_argument('--disable-gpu')
        # options.add_argument('--remote-debugging-port=3332')
        driver = webdriver.Chrome(options=options)
        return driver
    
    def init_display(self):
        # display = Display(visible=0, size=(900, 800))
        # display.start()
        # driver = init_drive()
        # driver.get(url="https://www.baidu.com")
        # print(driver.title)
        # driver.quit()
        # display.stop()
        pass
    def step_one_query_resume_lists(self, url, query):
        driver = self.driver
        driver.get(url=url)
        # assert "在线沟通" in driver.title
        wait = WebDriverWait(driver, 500)
        wait.until(EC.title_contains("在线沟通"))
        self.cookies = driver.get_cookies()
        # 点击search_link
        search_link = driver.find_element(By.XPATH, "//li[@data-selector='search']/a")
        search_link.click()
        # 等待页面加载完成
        wait = WebDriverWait(driver, 10)  # 设置最长等待时间为10秒
        input = wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@class='search-input']")))
        # input = driver.find_element(By.XPATH, "//input[@class='search-input']")
        # 输入搜索内容
        input.send_keys(query)
        # 点击按钮
        button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@class='ant-btn search-btn ant-btn-primary']")))
        # button = driver.find_element(By.XPATH, "//button[@class='ant-btn search-btn ant-btn-primary']")
        button.click()

        resume_urls = []
        # 等待简历列表加载完成
        # resume_elements = driver.find_elements(By.XPATH, "//ul[@class='resume-list']/li")
        resume_elements = wait.until(EC.visibility_of_all_elements_located((By.XPATH, "//ul[@class='resume-list']/li")))
        for resume_element in resume_elements:
            resume_url = resume_element.get_attribute("data-resumeurl")
            resume_urls.append(resume_url)
        for index, resume_url in enumerate(resume_urls):
            print(f"resume_url[{index}]={resume_url}")
        return resume_urls

    def step_two_get_every_resume_content(self, resume_urls):
        # 打开新标签页
        self.driver.execute_script("window.open('{}', '_blank')".format(resume_urls[0]))
        print("未完待续")

# 配置日志记录
# logging.basicConfig(level=logging.DEBUG,  # 设置日志级别（DEBUG、INFO、WARNING、ERROR、CRITICAL）
                    # format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
# 创建一个日志记录器
# logger = logging.getLogger('my_logger')

# 多线程打开多个网页，并且返回网页内容
def get_resume_content_from_urls_request(urls):
    with concurrent.futures.ThreadPoolExecutor() as executor:
        # executor.map(open_url, urls)
        # 使用能够带返回值回来的线程方法
        futures = [executor.submit(open_url, url) for url in urls]
        resume_contents = []
        for future in concurrent.futures.as_completed(futures):
            result = future.result()
            resume_contents.append(result)
    
    with open("./resume_content.text", "+a", encoding="utf-8") as file:
        for content in resume_contents:
            file.write(content)
        print(f"总共找到{resume_contents.count}个简历")


def open_url(url):
    # 设置浏览器头信息
    headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36'
    }
    response = requests.get(url,headers=headers, cookies=cookies)
    resume_content = response.text
    print(f"简历详情页--------------->{resume_content}<-------------------")
    return resume_content
        
    


if __name__ == '__main__':
    # init_display()
    # test_baidu()
    #test_liepin()
    #print('Success!')
    url = r"https://lpt.liepin.com/user/login"
    qurey = "嵌入式开发"
    resume_crawl = ResumeCrawl()
    resume_urls = resume_crawl.step_one_query_resume_lists(url, qurey)
    resume_crawl.step_two_get_every_resume_content(resume_urls)
                                            

