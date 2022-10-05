import cgi
from random import randint
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


def password():
    new_password = randint(10*4, 10*6)
    writer(new_password)
    return str(new_password)


if __name__ == '__main__':
    with open("out.html", "r", encoding="utf-8") as file:
        text = file.read()
    html_content = text.replace("result", password())
    print('Content-Type: text/html; charset=utf-8\n')
    print(html_content)
