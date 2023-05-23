import os
import json
import requests

def build():
    with open ("groups.json", 'r', encoding="UTF-8") as f:
        groups = json.load(f)['groups']
    groups.sort(key=lambda x: x['id'])
    if not os.path.exists("./src/groups"):
        os.mkdir("./src/groups")
    with open ("./src/groups/README.md", 'w+', encoding="UTF-8") as f:
        f.writelines(["---\neditLink: false\n---\n",
        "# 总览\n可以在右上角的搜索框处搜索群，点击群号可以直接加群\n",
        "| 群名称/群头像 | 主要内容 | 群号 |\n| ---- | ---- | ---- |\n"])
        for i in groups:
            f.write(f'''| <figure><img src="http://p.qlogo.cn/gh/{i['id']}/{i['id']}/100" height="100" width="100" /><figcaption>{i['name']}</figcaption></figure> | {i['tags']} | [{i['id']}]({i['url']}) |\n''')


def check():
    with open ("groups.json", 'r', encoding="UTF-8") as f:
        groups = json.load(f)['groups']

    for i in groups:
        params = {j.split('=')[0]: j.split('=')[1] for j in i['url'].split('?')[-1].split('&')}
        if ["authKey", "noverify", "group_code"] in list(params.keys()):
            raise Exception(f"群{i['id']}({i['name']})的加群链接未经脱敏处理，请检查")


def main():
    check()
    build()


if __name__ == "__main__":
    main()