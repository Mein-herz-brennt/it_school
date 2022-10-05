import cgi
import json


def reader():
    with open("hi.json", "r", encoding='utf-8') as file:
        info = json.load(file)
    return info


def writer(info):
    inf = reader()
    inf.append(info)
    with open("hi.json", "w", encoding="utf-8") as file:
        json.dump(inf, file, indent=3)
    return "Вас успішно додано"


def if_in(password):
    info = reader()
    if int(password) in info:
        return True
    else:
        return False


if __name__ == '__main__':
    words = cgi.FieldStorage()
    words = words.getfirst("get_word")
    if words == "1111":
        with open("admin.html", "r", encoding="utf-8") as file:
            html_content = file.read()
        print('Content-Type: text/html; charset=utf-8\n')
        print(html_content)
    elif if_in(words):
        with open("user.html", "r", encoding="utf-8") as file:
            html_content = file.read()
        print('Content-Type: text/html; charset=utf-8\n')
        print(html_content)
    else:
        with open("out.html", "r", encoding="utf-8") as file:
            html_content = file.read()
        html_content = html_content.replace("result", "Вибачте та ви не маєте доступу до функцій")
        print('Content-Type: text/html; charset=utf-8\n')
        print(html_content)
