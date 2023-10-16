import requests
from bs4 import BeautifulSoup
import http.cookies
import json
import os


def cookie2json():
        # 原始Cookie字符串，替换成你的实际Cookie字符串
    cookie_string = '__uuid=1694992852177.68; _ga=GA1.1.927517050.1694992853; _gcl_au=1.1.1468646778.1694992853; XSRF-TOKEN=TAJIwzOIS7qUzXVzxC_Gsw; __gc_id=f6a4873bb4f14d95981276b93ac0f697; Hm_lvt_a2647413544f5a04f00da7eee0d5e200=1694992947; hpo_role-sec_project=sec_project_liepin; hpo_sec_tenant=0; fe_se=-1694994740118; _e_ld_auth_=81d0f56a01a17e74c67c0abaa3186f48; imApp_2=1; inited_user=201f67c6b0003067c82dd6c229a5072a; user_roles=1; new_user=false; c_flag=b26e4782ff3f60c18f498e420be9290d; Qs_lvt_442519=1695771687; Qs_pv_442519=2831944532065899000; fe_im_opencontactlist=0_3; fe_im_openchatwin=fastProcess_2; __tlog=1694992852179.96%7C00000000%7CR000241555%7Cgg_pc_02%7Cgg_pc_02; _uetvid=d8067d5055b011eea134bb55d32e10bb; _gcl_aw=GCL.1696981546.Cj0KCQjw7JOpBhCfARIsAL3bobfmZBUKtckoM4unzrqceqDMr_XVgxykA5KMs0pVyHUjO3RPyJyItLsaAuKiEALw_wcB; _clck=tk78ik|2|ffq|0|1355; _ga_Q11MZCVPQN=GS1.1.1696981545.2.0.1696981552.0.0.0; _ga_54YTJKWN86=GS1.1.1696981572.4.1.1696981587.0.0.0; Hm_lpvt_a2647413544f5a04f00da7eee0d5e200=1696981589; __tlg_event_seq=156; user_photo=5f8fa3a679c7cc70efbf444e08u.png; user_name=%E6%9C%B1%E6%88%90%E6%A3%AE; compar_id=2b411e91b8e021c57f53a634b68c31d1; _h_ld_auth_=0d5f280151216c50c67c0abaa3186f48; imId=47f3f33fe979b8d805cd690f9a5023eb; imId_2=47f3f33fe979b8d805cd690f9a5023eb; imClientId=47f3f33fe979b8d86d79489fc99791c0; imClientId_2=47f3f33fe979b8d86d79489fc99791c0; fe_im_socketSequence_new_2=18_18_18; fe_im_opened_pages=_1695685099571_1695771986531_1695771925424; fe_im_connectJson_2=%7B%222_94be455a5075a1141a667e00ad0d9493%22%3A%7B%22socketConnect%22%3A%222%22%2C%22connectDomain%22%3A%22liepin.com%22%7D%7D; acw_tc=276077d416970679517681102e13578ac93a4837ffe53484ffd3fb067f83d6; UniqueKey=9906f2ffad1da2bba9dba665e9526a14; liepin_login_valid=0; lt_auth=vedfOHJUnQjw7SXf22JYsfpJit2uUG7PoCwEjRwD1oW9U%2FPi4P%2FgSw2Pp7AD%2FioIqxx1cf8zMLb3Muj4znpC70MS%2FFGnn52uv%2Fq4z30ER%2FpnJ%2FiflMXuqtzpRpwhlns6yEpgn3ki0HXnig%3D%3D; b-u-category=2; __session_seq=67; __uv_seq=6'

    # 使用http.cookies解析Cookie字符串
    cookie_parser = http.cookies.SimpleCookie()
    cookie_parser.load(cookie_string)

    # 将解析后的Cookie对象转换为JSON格式
    cookie_json = {}
    for key, morsel in cookie_parser.items():
        cookie_json[key] = morsel.value
    return cookie_json
    # 将Cookie信息输出为JSON格式
    # json_cookie_string = json.dumps(cookie_json, indent=4)

    # 打印JSON格式的Cookie信息
    # print(json_cookie_string)
    # return json_cookie_string


# 设置浏览器头信息
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36'
}


def dump_html_file(file_name, html):
    if os.path.exists(file_name):
        path = os.path.abspath(file_name)
        print(f'{file_name} has existed...,and path is {path}')
    else:
        with open(file_name, "w") as file:
            file.write(html)
            print(f"{file_name} successed to write!")

# 设置登录后的cookie信息（替换成你的实际cookie）
#cookies = {
#   'cookie_name1': 'cookie_value1',
#    'cookie_name2': 'cookie_value2',
#    # 添加更多的cookie信息
#}


cookies = cookie2json()

# 发送GET请求获取猎聘网首页，并带上头信息和cookie信息
url = 'https://lpt.liepin.com/im/imresourceload?extendType=fastProcess'
response = requests.get(url, headers=headers, cookies=cookies)

# 检查请求是否成功
if response.status_code == 200:
    # 使用Beautiful Soup解析网页内容
    soup = BeautifulSoup(response.text, 'html.parser')
    dump_html_file("shouye.html", soup.prettify())
    # 示例：从网页中提取公司名称
    company_elements = soup.find_all('a', class_='company-name')
    for company in company_elements:
        print("公司名称:", company.text.strip())

    # 示例：从网页中提取职位信息
    job_elements = soup.find_all('div', class_='job-info')
    for job in job_elements:
        job_title = job.find('h3').text.strip()
        job_location = job.find('p', class_='location').text.strip()
        job_salary = job.find('p', class_='text-warning').text.strip()
        print(f"职位名称: {job_title}\n工作地点: {job_location}\n薪资待遇: {job_salary}\n")

else:
    print(f"请求失败，状态码：{response.status_code}")


