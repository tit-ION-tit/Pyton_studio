c = input("введите пароль: ")
r = True
while r != False:
    if len(c) < 7:
        print("ваш пароль слишком короткий")
        c = input('введите пароль: ')
    else:
        if '123' in c:
            print("ваш пароль слишком легкий")
            c = input('введите пароль: ')
        else:
            r = False
            print('идеальный пароль')