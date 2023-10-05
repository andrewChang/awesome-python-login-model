import requests
from bs4 import BeautifulSoup
import http.cookies
import json

def cookie2json():
        # 原始Cookie字符串，替换成你的实际Cookie字符串
    cookie_string = '__uuid=1694992852177.68; _uetvid=d8067d5055b011eea134bb55d32e10bb; _ga=GA1.1.927517050.1694992853; _gcl_aw=GCL.1694992853.Cj0KCQjwx5qoBhDyARIsAPbMagBcdom8zp_y6X9K_EdKlNBnZOkGWU85WY_lVs2FX3ZrGm2r5eGNqXYaAmPUEALw_wcB; _gcl_au=1.1.1468646778.1694992853; _clck=tk78ik|2|ff3|0|1355; XSRF-TOKEN=TAJIwzOIS7qUzXVzxC_Gsw; __gc_id=f6a4873bb4f14d95981276b93ac0f697; _ga_Q11MZCVPQN=GS1.1.1694992852.1.1.1694992927.0.0.0; Hm_lvt_a2647413544f5a04f00da7eee0d5e200=1694992947; hpo_role-sec_project=sec_project_liepin; hpo_sec_tenant=0; fe_se=-1694994740118; _e_ld_auth_=81d0f56a01a17e74c67c0abaa3186f48; imApp_2=1; imId=3fbdaff53ab4b8eccb8db5f39dbf4c7c; imId_2=3fbdaff53ab4b8eccb8db5f39dbf4c7c; imClientId=3fbdaff53ab4b8ec77ef34c9feaddba4; imClientId_2=3fbdaff53ab4b8ec77ef34c9feaddba4; inited_user=201f67c6b0003067c82dd6c229a5072a; user_roles=1; new_user=false; c_flag=b26e4782ff3f60c18f498e420be9290d; Hm_lpvt_a2647413544f5a04f00da7eee0d5e200=1695683869; _ga_54YTJKWN86=GS1.1.1695683864.3.1.1695684858.0.0.0; __tlg_event_seq=80; fe_im_connectJson_2=%7B%222_9906f2ffad1da2bba9dba665e9526a14%22%3A%7B%22socketConnect%22%3A%221%22%2C%22connectDomain%22%3A%22liepin.com%22%7D%7D; Qs_lvt_442519=1695771687; Qs_pv_442519=2831944532065899000; __tlog=1694992852179.96%7C00000000%7CR000241555%7Cgg_pc_02%7Cs_00_pz0; acw_tc=276077cd16957718517344563e6382b969aa64f71d29382d3f305bfd8a3859; UniqueKey=9906f2ffad1da2bba9dba665e9526a14; liepin_login_valid=0; lt_auth=7%2B9bO3JUnQjw7SXf22JYsfpJit2uUG7PoCwEjRwD1oW9U%2FPi4P%2FgSw2Pp7AD%2FioIq0wmJqgzMLb3MO%2F5yHtD7EcR%2BVGnn52uv%2Fq4z30ER%2FpnIsW2vezHg%2FXUQpgnlkAA8nFbpEIL%2BVzO; b-u-category=2; fe_im_socketSequence_new_2=14_11_12; __session_seq=47; __uv_seq=8; fe_im_opencontactlist=0_2; fe_im_openchatwin=fastProcess_1; fe_im_opened_pages=_1695685099571'

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
    print(f"------->{soup}<---------")
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


