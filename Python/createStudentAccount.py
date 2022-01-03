import sys
import json
import requests

class __Autonomy__(object):
    """
    自定义变量的write方法
    """
    def __init__(self):
        """
        init
        """
        self._buff = ""

    def write(self, out_stream):
        """
        :param out_stream:
        :return:
        """
        self._buff += out_stream


api_url = "http://tinywebdb.appinventor.space/api"

def request_data(url, idx):
    req = requests.post(url,
                        data={"user": "bbc123", "secret": "fb3b5e2c", "action": "search","tag":idx})  # 请求连接
    return dict(eval(req.text))

def update_data(url, idx, data):
    req = requests.post(url,
                        data={"user": "bbc123", "secret": "fb3b5e2c",
                              "action": "update","tag":idx,"value":data})  # 写入

if __name__ == "__main__":
    r = request_data(api_url, "students")
    studentList= list(r["students"])
    #print(studentList)
    print("(为省略输入班级编号一次只能录入一个班级，录入完成请结束重新运行)")
    classNumber = input("请输入班级编号:")
    while True:
        name = input("请输入学生姓名(输入结束停止):")
        if name=="结束":
            break
        card = input("请输入积分:")
        studentInfo = []
        studentInfo.append(["name",name])
        studentInfo.append(["password","123456"]) 
        studentInfo.append(["classNumber",classNumber])
        studentInfo.append(["card",card])
        studentInfo.append(["school",""])
        studentList.append(studentInfo)


    current = sys.stdout
    a = __Autonomy__()
    # 会调用a的write方法, 和self._buff的内容拼接
    sys.stdout = a
    print(studentList,end="")
    sys.stdout = current

    # 输出捕获的内容
    student_data = a._buff.replace("'",'"')
    print(student_data)
    update_data(api_url,"students",student_data)
    print("写入成功")

