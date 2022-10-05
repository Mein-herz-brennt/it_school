from wsgiref.simple_server import make_server
import cgi
import json
from random import randint

HOST = ""
port = 9000


# start_response("200 OK", [("Content-Type:", "text/html;  cherset=utf-8")])
# return [bytes(text, encoding="utf-8")]

def reader(filename: str) -> str:
    with open(filename, "r", encoding="utf-8") as file:
        text = file.read()
    return text


def reader1():
    with open("hi.json", "r", encoding='utf-8') as file:
        info = json.load(file)
    return info


def writer(info):
    inf = reader1()
    inf.append(info)
    with open("hi.json", "w", encoding="utf-8") as file:
        json.dump(inf, file, indent=3)
    return "Вас успішно додано"


def if_in(password):
    info = reader1()
    if int(password) in info:
        return True
    else:
        return False


def password():
    new_password = randint(10 * 4, 10 * 6)
    writer(new_password)
    return str(new_password)


def web_app(env, start_response):
    form = cgi.FieldStorage(fp=env["wsgi.input"], environ=env)
    path = env.get("PATH_INFO", "")
    if path == "/":
        words = form.getfirst("get_word")
        if words:
            if words == "1111":
                with open("admin.html", "r", encoding="utf-8") as file:
                    html_content = file.read()
                start_response("200 OK", [("Content-Type:", "text/html;  cherset=utf-8")])
                return [bytes(html_content, encoding="utf-8")]
            elif if_in(words):
                with open("user.html", "r", encoding="utf-8") as file:
                    html_content = file.read()
                start_response("200 OK", [("Content-Type:", "text/html;  cherset=utf-8")])
                return [bytes(html_content, encoding="utf-8")]
            else:
                with open("out.html", "r", encoding="utf-8") as file:
                    html_content = file.read()
                html_content = html_content.replace("result", "Вибачте та ви не маєте доступу до функцій")
                start_response("200 OK", [("Content-Type:", "text/html;  cherset=utf-8")])
                return [bytes(html_content, encoding="utf-8")]
        else:
            text = reader("index.html")
            start_response("200 OK", [("Content-Type:", "text/html;  cherset=utf-8")])
            return [bytes(text, encoding="utf-8")]

    elif path == '/create_password':
        with open("out.html", "r", encoding="utf-8") as file:
            text = file.read()
        html_content = text.replace("result", password())
        start_response("200 OK", [("Content-Type:", "text/html;  cherset=utf-8")])
        return [bytes(html_content, encoding="utf-8")]


if __name__ == '__main__':
    print(f'Starting server in http://localhost:{port}')
    httpd = make_server(HOST, port, web_app)
    httpd.serve_forever()
