int()  # всі цілі числа
str()  # строки, слова і тд.
float()  # дроби, числа з плаваючою комою.
bool()  # булеві значення 1/0 , True or False
list()  # Список з довільних елементів
tuple()  # кортеж, як список тільки не можна міняти
dict()  # словник дозволяє звертатися до значення за умовним ключем

int_ = 4345
str_ = 'hgfjhdret088768'
float_ = 435245.87655
bool_ = True
list_ = [123, 'hfhfdf', 9876564]
tuple_ = (1212, 'hghdg', 876544)
dict_ = {'key': 'value', '1': 1, "ghdfhf": "fdfghg", "bool": True, "dict": {'key': 'value1', '1': 1}}

# for i in
# while
counter = 1
while counter < 1000:
    print(counter)
    counter /= 0.1

for keys, values in dict_.items():
    print(keys, "--->", values)


def piramid(n: int):
    counter = 1
    n_ = n
    star = '-'
    while counter <= n:
        if counter % 2 != 0:
            passed = n_//2
            # print(1, "-->", passed)
            print(" " * passed + star * counter + " " * passed)
            n_ -= 1
            counter += 1
        else:
            passed = n_//2
            # print(2, "-->", passed)
            print(" " * passed + star * counter + " " * passed)
            n_ -= 1
            counter += 1

        # print(n_)


piramid(120)