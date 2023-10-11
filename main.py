from argparse import ArgumentParser
import os
import json

parser = ArgumentParser()
parser.add_argument("command", help="要执行的功能，可选列表：add, modify")
parser.add_argument("-id", help="群号")
parser.add_argument("-name", help="群名称")
parser.add_argument("-tags", help="群标签")
parser.add_argument("-url", help="加群链接")
args = parser.parse_args()


def url_correct(url: str) -> str:
    params = url.split("//")[-1].split("?")[-1].split("&")
    param_dict = {i.split("=")[0]: i.split("=")[1] for i in params}
    return f"https://qm.qq.com/cgi-bin/qm/qr?_wv={param_dict['_wv']}&k={param_dict['k']}"


def correct():
    with open("groups.json", 'r', encoding="UTF-8") as f:
        groups = json.load(f)['groups']
    for i in groups:
        try:
            i['url'] = url_correct(i['url'])
        except IndexError:
            print("加群链接不正确:", i['url'])
            exit(1)
    groups.sort(key=lambda x: x['id'])
    with open("groups.json", 'w+', encoding="UTF-8") as f:
        json.dump({"groups": groups}, f, indent=4, ensure_ascii=False)


def build():
    with open("groups.json", 'r', encoding="UTF-8") as f:
        groups = json.load(f)['groups']
    if not os.path.exists("./src/groups"):
        os.mkdir("./src/groups")
    with open("./src/groups/README.md", 'w+', encoding="UTF-8") as f:
        f.writelines(["---\nicon: ri:qq-fill\neditLink: false\n---\n\n",
                      "# 总览\n\n可以在右上角的搜索框处搜索群，电脑端点击群名称可以直接加群\n\n",
                      "| 群名称/群头像 | 主要内容 | 群号 |\n| ---- | ---- | ---- |\n"])
        for i in groups:
            f.write(
                f'''| <figure><img src="http://p.qlogo.cn/gh/{i['id']}/{i['id']}/100" height="100" width="100" /><figcaption>[{i['name']}]({i['url']})</figcaption></figure> | {i['tags']} | {i['id']} |\n''')


def modify(id: str, name: str, tags: str, url: str):
    url = url_correct(url)
    with open("info.md", 'w+', encoding="UTF-8") as f:
        f.write(f"群名称：{name}\n群号：{id}\n群标签：{tags}\n加群链接：{url}")
    print(f"正在添加：\n群名称：{name}\n群号：{id}\n群标签：{tags}\n加群链接：{url}")
    with open("groups.json", 'r', encoding="UTF-8") as f:
        groups = json.load(f)['groups']
    for i in groups:
        if i['id'] == id:
            i['name'] = name
            i['tags'] = tags
            i['url'] = url
            break
    else:
        groups.append({"id": id, "name": name, "tags": tags, "url": url})
    with open("groups.json", 'w+', encoding="UTF-8") as f:
        json.dump({"groups": groups}, f, indent=4, ensure_ascii=False)
    print("添加成功")
    correct()


if __name__ == "__main__":
    if args.command == "build":
        build()
    elif args.command == "modify":
        if not all([args.id, args.name, args.tags, args.url]):
            parser.error("请输入 id, name, tags, and url 全部四个参数")
        modify(args.id, args.name, args.tags, args.url)
    else:
        parser.error("无效的指令")
