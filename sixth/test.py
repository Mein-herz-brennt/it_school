import json

dct = {"hello world": True, "hi": "bye"}

# {key : value}

print(dct)
dct["hello world"] = False
print(dct["hello world"])
print(dct["hi"])

# file = open("test.txt", "w", encoding="utf-8")  # r - reading, w - writing, a - дозапис, b - bytes
# file.close()

with open("test.json", "w", encoding="utf-8") as file:
    json.dump(dct, file, indent=3)

with open("test.json", "r", encoding="utf-8") as file:
    text = json.load(file)
print("text += ", text)


