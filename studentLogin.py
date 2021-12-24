import json

import requests

api_url = "http://tinywebdb.appinventor.space/api"


def request_data(url, idx):
    req = requests.post(url,
                        data={"user": "bbc123", "secret": "fb3b5e2c", "action": "search", "tag": idx})  # 请求连接
    return dict(eval(req.text))


userName = input("请输入用户名:")
password = input("请输入密码:")
r = request_data(api_url, "cardAccount")
a = dict(r["cardAccount"])
# a = json.loads(r["cardAccount"])
account = dict(a["student"])
# print(account)
if userName in account:
    if account[userName][0] == password:
        print("登陆成功")
        class_num = account[userName][1]
        r = request_data(api_url, "studentInfo")
        # a = json.loads(r["studentInfo"])
        a = dict(r["studentInfo"])
        class_dict = dict(dict(a[class_num]))
        print(userName, dict(dict(class_dict["student"])[userName])["card"])
        # print(userName, a[class_num]["student"][userName]["card"])
    else:
        print("密码错误")
else:
    print("用户不存在")
# [["21020",[["courseType","App"],["ownerTeacher","白瑞琳"],["student",[["朱函妤",[["card","0"],["logs",[["2021-12-22","(积分变动原因)"]]],["school","未知"]]]]]]],["21061",[["courseType","PythonL2"],["ownerTeacher","白瑞琳"],["student",[["蒋汪毅",["school","未知","card","0","logs",["2021-12-22","(积分变动原因)"]]]]]]]]
# [["student",[["朱函妤",["123456","21020"]]]],["teacher",[["白瑞琳","abcd"],["刘鑫","abcd"]]]]
