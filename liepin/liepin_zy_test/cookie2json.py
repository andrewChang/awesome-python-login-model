import http.cookies
import json

# 原始Cookie字符串，替换成你的实际Cookie字符串
cookie_string = '__uuid=1694992852177.68; __tlog=1694992852179.96%7C00000000%7C00000000%7Cgg_pc_02%7Cgg_pc_02; _uetvid=d8067d5055b011eea134bb55d32e10bb; _ga=GA1.1.927517050.1694992853; _gcl_aw=GCL.1694992853.Cj0KCQjwx5qoBhDyARIsAPbMagBcdom8zp_y6X9K_EdKlNBnZOkGWU85WY_lVs2FX3ZrGm2r5eGNqXYaAmPUEALw_wcB; _gcl_au=1.1.1468646778.1694992853; _clck=tk78ik|2|ff3|0|1355; XSRF-TOKEN=TAJIwzOIS7qUzXVzxC_Gsw; __gc_id=f6a4873bb4f14d95981276b93ac0f697; _ga_Q11MZCVPQN=GS1.1.1694992852.1.1.1694992927.0.0.0; Hm_lvt_a2647413544f5a04f00da7eee0d5e200=1694992947; hpo_role-sec_project=sec_project_liepin; hpo_sec_tenant=0; fe_se=-1694994740118; _e_ld_auth_=81d0f56a01a17e74c67c0abaa3186f48; imApp_2=1; _h_ld_auth_=0d5f280151216c50c67c0abaa3186f48; imId=3fbdaff53ab4b8eccb8db5f39dbf4c7c; imId_2=3fbdaff53ab4b8eccb8db5f39dbf4c7c; imClientId=3fbdaff53ab4b8ec77ef34c9feaddba4; imClientId_2=3fbdaff53ab4b8ec77ef34c9feaddba4; inited_user=201f67c6b0003067c82dd6c229a5072a; user_roles=1; new_user=false; c_flag=b26e4782ff3f60c18f498e420be9290d; Hm_lpvt_a2647413544f5a04f00da7eee0d5e200=1695683869; _ga_54YTJKWN86=GS1.1.1695683864.3.1.1695684858.0.0.0; fe_im_socketSequence_new_2=11_11_11; __tlg_event_seq=80; fe_im_opencontactlist=0_0; fe_im_openchatwin=0_0; fe_im_opened_pages=; fe_im_connectJson_2=%7B%222_9906f2ffad1da2bba9dba665e9526a14%22%3A%7B%22socketConnect%22%3A%222%22%2C%22connectDomain%22%3A%22liepin.com%22%7D%7D; acw_tc=2760829516956850674045012e5f98069487133a04d3e31da55a799ff52c8a; UniqueKey=9906f2ffad1da2bba9dba665e9526a14; liepin_login_valid=0; lt_auth=uLxeOXJUnQjw7SXf22JYsfpJit2uUG7PoCwEjRwD1oW9U%2FPi4P%2FgSw2Pp7AD%2FioIqx4ncvQzMLb3MO72zHND7kEU8VGnn52uv%2Fq4z30ER%2FpnIsW2vezHg%2FXUQpgnlkAA8nFbpEIL%2BVzO; b-u-category=2; __session_seq=36; __uv_seq=15'

# 使用http.cookies解析Cookie字符串
cookie_parser = http.cookies.SimpleCookie()
cookie_parser.load(cookie_string)

# 将解析后的Cookie对象转换为JSON格式
cookie_json = {}
for key, morsel in cookie_parser.items():
    cookie_json[key] = morsel.value

# 将Cookie信息输出为JSON格式
json_cookie_string = json.dumps(cookie_json, indent=4)

# 打印JSON格式的Cookie信息
print(json_cookie_string)
