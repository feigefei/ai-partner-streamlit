import json
from pathlib import Path

#写入json数据文件
# user = {
#     "name":"示例用户",
#     "age":18,
#     "is_student":False,
#     "courses":["math","english"]
# }
# with open("resources/user.json","w",encoding="utf-8") as f:
#     # ensure_ascii=False  #确保中文不被转义
#     # indent=4 #缩进4个空格
#     json.dump(user,f,ensure_ascii=False,indent=4)

#读取json数据文件
resources = Path(__file__).resolve().parent / "resources"
user_file = resources / "user.json"
if not user_file.exists():
    user_file = resources / "user.example.json"
with open(user_file,"r",encoding="utf-8") as f:
    user = json.load(f)
    print(user)
    print(type(user))
