import cgi
import json


def palindrome(word):
    if word[::-1]:
        return f"{word} is palindrome"
    else:
        return f"{word} is not palindrome"


if __name__ == '__main__':
    words = cgi.FieldStorage()
    words = words.getfirst("get_word")
    with open("out.html", "r", encoding="utf-8") as file:
        html_content = file.read()
    html_content = html_content.replace("result", palindrome(words))
    print('Content-Type: text/html; charset=utf-8\n')
    print(html_content)
