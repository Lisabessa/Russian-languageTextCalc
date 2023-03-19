import math

NUMS = {
    'ноль': 0, 'один': 1, 'два': 2, 'три': 3, 'четыре': 4, 'пять': 5, 'шесть': 6, 'семь': 7, 'восемь': 8, 'девять': 9,
    'десять': 10, 'одиннадцать': 11, 'двенадцать': 12, 'тринадцать': 13, 'четырнадцать': 14, 'пятнадцать': 15,
    'шестнадцать': 16, 'семнадцать': 17, 'восемнадцать': 18, 'девятнадцать': 19, 'двадцать': 20, 'тридцать': 30,
    'сорок': 40, 'пятьдесят': 50, 'шестьдесят': 60, 'семьдесят': 70, 'восемьдесят': 80, 'девяносто': 90, 'сто': 100,
    'двести': 200, 'триста': 300, 'четыреста': 400, 'пятьсот': 500, 'шестьсот': 600, 'семьсот': 700, 'восемьсот': 800,
    'девятьсот': 900, 'тысяча': 1000, 'две тысячи': 2000, 'три тысячи': 3000, 'четыре тысячи': 4000, 'пять тысяч': 5000,
    'шесть тысяч': 6000, 'семь тысяч': 7000, 'восемь тысяч': 8000, 'девять тысяч': 9000, 'десять тысяч': 10000
}
NUMERATORS = {
    'одна': 1, 'две': 2
}
DENOMINATORS = {
    'первых': 1, 'вторых': 2, 'третьих': 3, 'четвёртых': 4, 'пятых': 5, 'шестых': 6, 'седьмых': 7, 'восьмых': 8,
    'девятых': 9, 'десятых': 10, 'одиннадцатых': 11, 'двенадцатых': 12, 'тринадцатых': 13, 'четырнадцатых': 14,
    'пятнадцатых': 15, 'шестнадцатых': 16, 'семнадцатых': 17, 'восемнадцатых': 18, 'девятнадцатых': 19, 'двадцатых': 20,
    'тридцатых': 30, 'сороковых': 40, 'пятидесятых': 50, 'шестидесятых': 60, 'семидесятых': 70, 'восьмидесятых': 80,
    'девяностых': 90, 'сотых': 100, 'двухсотых': 200, 'трёхсотых': 300, 'четырёхсотых': 400, 'пятисотых': 500,
    'шестисотых': 600, 'семисотых': 700, 'восьмисотых': 800, 'девятисотых': 900, 'тысячных': 1000,
    'двухтысячных': 2000, 'трёхтысячных': 3000, 'четырёхтысячных': 4000, 'пятитысячных': 5000, 'шеститысячных': 6000,
    'семитысячных': 7000, 'восьмитысячных': 8000, 'девятитысячных': 9000, 'десятитысячных': 10000
}
DENOMINATORS1 = {
    'вторая': 2, 'третья': 3, 'четвёртая': 4, 'пятая': 5, 'шестая': 6, 'седьмая': 7, 'восьмая': 8,
    'девятая': 9, 'десятая': 10, 'одиннадцатая': 11, 'двенадцатая': 12, 'тринадцатая': 13, 'четырнадцатая': 14,
    'пятнадцатая': 15, 'шестнадцатая': 16, 'семнадцатая': 17, 'восемнадцатая': 18, 'девятнадцатая': 19, 'двадцатая': 20,
    'тридцатая': 30, 'сороковая': 40, 'пятидесятая': 50, 'шестидесятая': 60, 'семидесятая': 70, 'восьмидесятая': 80,
    'девяностая': 90, 'сотая': 100, 'двухсотая': 200, 'трёхсотая': 300, 'четырёхсотая': 400, 'пятисотая': 500,
    'шестисотая': 600, 'семисотая': 700, 'восьмисотая': 800, 'девятисотая': 900, 'тысячная': 1000,
    'двухтысячная': 2000, 'трёхтысячная': 3000, 'четырёхтысячная': 4000, 'пятитысячная': 5000, 'шеститысячная': 6000,
    'семитысячная': 7000, 'восьмитысячная': 8000, 'девятитысячная': 9000, 'десятитысячная': 10000
}


def text_to_number(sp):  # принимает на вход список слов числа и возвращает целую часть, числитель и знаменатель
    NUM, DENOM, SEP = 0, 0, 0
    # обработка строки со знаменателя
    if sp[-1] in DENOMINATORS or sp[-1] in DENOMINATORS1:  # ЕСЛИ ЕСТЬ ДРОБИ
        DENOM_IND = len(sp) - 1  # индекс начала знаменателя
        # определяем знаменатель окончательно
        if len(sp) > 2 and sp[-2] not in NUMERATORS and NUMS[sp[-2]] >= 20:  # знаменатель составной
            DENOM += NUMS[sp[-2]]
            DENOM_IND -= 1
        if sp[-1] in DENOMINATORS:
            DENOM += DENOMINATORS[sp[-1]]
        else:
            DENOM += DENOMINATORS1[sp[-1]]
        SEP_FLAG = False  # показатель того, что дробь смешанная
        for i in range(DENOM_IND):  # составляем числитель
            if sp[i] == 'и':
                SEP_FLAG = True
            elif SEP_FLAG is False and sp[i] in NUMS:
                SEP += NUMS[sp[i]]
            elif SEP_FLAG is False and sp[i] in NUMERATORS:
                SEP += NUMERATORS[sp[i]]
            elif SEP_FLAG is True and sp[i] in NUMS:
                NUM += NUMS[sp[i]]
            elif SEP_FLAG is True and sp[i] in NUMERATORS:
                NUM += NUMERATORS[sp[i]]
        if SEP_FLAG is False:  # дробь не смешанная
            NUM = SEP
            SEP = 0
    else:  # ОБРАБОТКА ОБЫЧНОГО ЧИСЛА
        for elem in sp:
            SEP += NUMS[elem]
    return SEP, NUM, DENOM


def findNUM(number):  # ищет текстовое представление заданного числа
    for key in NUMS:
        if NUMS[key] == number:
            return key
    return -1


def findNUMERATOR(number):  # ищет текстовое представление ЧИСЛИТЕЛЯ
    for key in NUMERATORS:
        if NUMERATORS[key] == number:
            return key
    return -1


def findDENOMINATOR(number):  # ищет текстовое представление ЗНАМЕНАТЕЛЯ
    for key in DENOMINATORS:
        if DENOMINATORS[key] == number:
            return key
    return -1


def findDENOMINATOR1(number):  # ищет текстовое представление ЗНАМЕНАТЕЛЯ1
    for key in DENOMINATORS1:
        if DENOMINATORS1[key] == number:
            return key
    return -1


def number_to_text_SEP(SEPres):  # переводит полученное число в текст
    if SEPres not in NUMS.values():
        if len(str(SEPres)) == 4 and int(str(SEPres)[1]) == 0 and int(str(SEPres)[2]) == 0:  # обработка чисел 1001-1009
            first = int(str(SEPres)[0] + '000')
            second = int(str(SEPres)[3])
            return findNUM(first) + ' ' + findNUM(second)
        elif len(str(SEPres)) == 4 and int(str(SEPres)[1]) == 0 and int(str(SEPres)[2:]) in NUMS.values():  # 1010-1019.
            first = int(str(SEPres)[0] + '000')
            second = int(str(SEPres)[2:])
            return findNUM(first) + ' ' + findNUM(second)
        elif len(str(SEPres)) == 4 and int(str(SEPres)[1]) == 0 and int(str(SEPres)[2:]) not in NUMS.values():  # 1021..
            first = int(str(SEPres)[0] + '000')
            second = int(str(SEPres)[2] + '0')
            third = int(str(SEPres)[3])
            return findNUM(first) + ' ' + findNUM(second) + ' ' + findNUM(third)
        elif len(str(SEPres)) == 4 and int(str(SEPres)[2]) == 0 and int(str(SEPres)[3]) == 0:  # 1100, 1200, 1300..
            first = int(str(SEPres)[0] + '000')
            second = int(str(SEPres)[1] + '00')
            return findNUM(first) + ' ' + findNUM(second)
        elif len(str(SEPres)) == 4 and int(str(SEPres)[2]) == 0:  # 1101-1109
            first = int(str(SEPres)[0] + '000')
            second = int(str(SEPres)[1] + '00')
            third = int(str(SEPres)[3])
            return findNUM(first) + ' ' + findNUM(second) + ' ' + findNUM(third)
        elif len(str(SEPres)) == 4 and int(str(SEPres)[2:]) in NUMS.values():  # 1110-1119, 1120, 1130..
            first = int(str(SEPres)[0] + '000')
            second = int(str(SEPres)[1] + '00')
            third = int(str(SEPres)[2:])
            return findNUM(first) + ' ' + findNUM(second) + ' ' + findNUM(third)
        elif len(str(SEPres)) == 4 and int(str(SEPres)[2:]) not in NUMS.values():  # 1121-1129..
            first = int(str(SEPres)[0] + '000')
            second = int(str(SEPres)[1] + '00')
            third = int(str(SEPres)[2] + '0')
            forth = int(str(SEPres)[3])
            return findNUM(first) + ' ' + findNUM(second) + ' ' + findNUM(third) + ' ' + findNUM(forth)
        elif len(str(SEPres)) == 3 and int(str(SEPres)[1:]) in NUMS.values():  # обработка чисел 110 - 120, 130
            first = int(str(SEPres)[0] + '00')
            second = int(str(SEPres)[1:])
            return findNUM(first) + ' ' + findNUM(second)
        elif len(str(SEPres)) == 3 and int(str(SEPres)[1]) == 0:  # обработка чисел 101 - 109
            first = int(str(SEPres)[0] + '00')
            second = int(str(SEPres)[2])
            return findNUM(first) + ' ' + findNUM(second)
        elif len(str(SEPres)) == 3:  # обработка чисел 121 - 129, 131 - 139...
            first = int(str(SEPres)[0] + '00')
            second = int(str(SEPres)[1] + '0')
            third = int(str(SEPres)[2])
            return findNUM(first) + ' ' + findNUM(second) + ' ' + findNUM(third)
        else:  # обработка составных двузначных чисел
            first = int(str(SEPres)[0] + '0')
            second = int(str(SEPres)[1])
            return findNUM(first) + ' ' + findNUM(second)
    else:
        return findNUM(SEPres)


def number_to_text_DENOM(DENOMres):  # переводит полученный знаменатель в текст
    if DENOMres not in DENOMINATORS.values():
        if len(str(DENOMres)) == 4 and int(str(DENOMres)[1]) == 0 and int(str(DENOMres)[2]) == 0:  # 1001-1009
            first = int(str(DENOMres)[0] + '000')
            second = int(str(DENOMres)[3])
            return findNUM(first) + ' ' + findDENOMINATOR(second)
        elif len(str(DENOMres)) == 4 and int(str(DENOMres)[1]) == 0 and int(str(DENOMres)[2:]) in DENOMINATORS.values():
            # 1010-1020, 1030...
            first = int(str(DENOMres)[0] + '000')
            second = int(str(DENOMres)[2:])
            return findNUM(first) + ' ' + findDENOMINATOR(second)
        elif len(str(DENOMres)) == 4 and int(str(DENOMres)[1]) == 0 and int(str(DENOMres)[2:]) not in DENOMINATORS.values():
            # 1021-1029...
            first = int(str(DENOMres)[0] + '000')
            second = int(str(DENOMres)[2] + '0')
            third = int(str(DENOMres)[3])
            return findNUM(first) + ' ' + findNUM(second) + ' ' + findDENOMINATOR(third)
        elif len(str(DENOMres)) == 4 and int(str(DENOMres)[2]) == 0 and int(str(DENOMres)[3]) == 0:  # 1100, 1200..
            first = int(str(DENOMres)[0] + '000')
            second = int(str(DENOMres)[1] + '00')
            return findNUM(first) + ' ' + findDENOMINATOR(second)
        elif len(str(DENOMres)) == 4 and int(str(DENOMres)[2]) == 0:  # 1101-1109
            first = int(str(DENOMres)[0] + '000')
            second = int(str(DENOMres)[1] + '00')
            third = int(str(DENOMres)[3])
            return findNUM(first) + ' ' + findNUM(second) + ' ' + findDENOMINATOR(third)
        elif len(str(DENOMres)) == 4 and int(str(DENOMres)[2:]) in DENOMINATORS.values():  # 1110-1119, 1120, 1130..
            first = int(str(DENOMres)[0] + '000')
            second = int(str(DENOMres)[1] + '00')
            third = int(str(DENOMres)[2:])
            return findNUM(first) + ' ' + findNUM(second) + ' ' + findDENOMINATOR(third)
        elif len(str(DENOMres)) == 4 and int(str(DENOMres)[2:]) not in DENOMINATORS.values():  # 1121-1129..
            first = int(str(DENOMres)[0] + '000')
            second = int(str(DENOMres)[1] + '00')
            third = int(str(DENOMres)[2] + '0')
            forth = int(str(DENOMres)[3])
            return findNUM(first) + ' ' + findNUM(second) + ' ' + findNUM(third) + ' ' + findDENOMINATOR(forth)
        elif len(str(DENOMres)) == 3 and int(str(DENOMres)[1:]) in DENOMINATORS.values():  # обработка чисел 110 - 120..
            first = int(str(DENOMres)[0] + '00')
            second = int(str(DENOMres)[1:])
            return findNUM(first) + ' ' + findDENOMINATOR(second)
        elif len(str(DENOMres)) == 3 and int(str(DENOMres)[1]) == 0:  # обработка чисел 101 - 109
            first = int(str(DENOMres)[0] + '00')
            second = int(str(DENOMres)[2])
            return findNUM(first) + ' ' + findDENOMINATOR(second)
        elif len(str(DENOMres)) == 3:  # обработка чисел 121 - 129, 131 - 139...
            first = int(str(DENOMres)[0] + '00')
            second = int(str(DENOMres)[1] + '0')
            third = int(str(DENOMres)[2])
            return findNUM(first) + ' ' + findNUM(second) + ' ' + findDENOMINATOR(third)
        else:  # обработка составных двузначных чисел
            first = int(str(DENOMres)[0] + '0')
            second = int(str(DENOMres)[1])
            return findNUM(first) + ' ' + findDENOMINATOR(second)
    else:
        return findDENOMINATOR(DENOMres)


def number_to_text_DENOM1(DENOMres):  # переводит полученный знаменатель в текст (для дробей с числителем "одна")
    if DENOMres not in DENOMINATORS1.values():
        if len(str(DENOMres)) == 4 and int(str(DENOMres)[1]) == 0 and int(str(DENOMres)[2]) == 0:  # 1001-1009
            first = int(str(DENOMres)[0] + '000')
            second = int(str(DENOMres)[3])
            return findNUM(first) + ' ' + findDENOMINATOR1(second)
        elif len(str(DENOMres)) == 4 and int(str(DENOMres)[1]) == 0 and int(str(DENOMres)[2:]) in DENOMINATORS1.values():
            # 1010-1020, 1030...
            first = int(str(DENOMres)[0] + '000')
            second = int(str(DENOMres)[2:])
            return findNUM(first) + ' ' + findDENOMINATOR1(second)
        elif len(str(DENOMres)) == 4 and int(str(DENOMres)[1]) == 0 and int(str(DENOMres)[2:]) not in DENOMINATORS1.values():
            # 1021-1029...
            first = int(str(DENOMres)[0] + '000')
            second = int(str(DENOMres)[2] + '0')
            third = int(str(DENOMres)[3])
            return findNUM(first) + ' ' + findNUM(second) + ' ' + findDENOMINATOR1(third)
        elif len(str(DENOMres)) == 4 and int(str(DENOMres)[2]) == 0 and int(str(DENOMres)[3]) == 0:  # 1100, 1200..
            first = int(str(DENOMres)[0] + '000')
            second = int(str(DENOMres)[1] + '00')
            return findNUM(first) + ' ' + findDENOMINATOR1(second)
        elif len(str(DENOMres)) == 4 and int(str(DENOMres)[2]) == 0:  # 1101-1109
            first = int(str(DENOMres)[0] + '000')
            second = int(str(DENOMres)[1] + '00')
            third = int(str(DENOMres)[3])
            return findNUM(first) + ' ' + findNUM(second) + ' ' + findDENOMINATOR1(third)
        elif len(str(DENOMres)) == 4 and int(str(DENOMres)[2:]) in DENOMINATORS1.values():  # 1110-1119, 1120, 1130..
            first = int(str(DENOMres)[0] + '000')
            second = int(str(DENOMres)[1] + '00')
            third = int(str(DENOMres)[2:])
            return findNUM(first) + ' ' + findNUM(second) + ' ' + findDENOMINATOR1(third)
        elif len(str(DENOMres)) == 4 and int(str(DENOMres)[2:]) not in DENOMINATORS1.values():  # 1121-1129..
            first = int(str(DENOMres)[0] + '000')
            second = int(str(DENOMres)[1] + '00')
            third = int(str(DENOMres)[2] + '0')
            forth = int(str(DENOMres)[3])
            return findNUM(first) + ' ' + findNUM(second) + ' ' + findNUM(third) + ' ' + findDENOMINATOR1(forth)
        elif len(str(DENOMres)) == 3 and int(str(DENOMres)[1:]) in DENOMINATORS1.values():  # обработка чисел 110 - 120..
            first = int(str(DENOMres)[0] + '00')
            second = int(str(DENOMres)[1:])
            return findNUM(first) + ' ' + findDENOMINATOR1(second)
        elif len(str(DENOMres)) == 3 and int(str(DENOMres)[1]) == 0:  # обработка чисел 101 - 109
            first = int(str(DENOMres)[0] + '00')
            second = int(str(DENOMres)[2])
            return findNUM(first) + ' ' + findDENOMINATOR1(second)
        elif len(str(DENOMres)) == 3:  # обработка чисел 121 - 129, 131 - 139...
            first = int(str(DENOMres)[0] + '00')
            second = int(str(DENOMres)[1] + '0')
            third = int(str(DENOMres)[2])
            return findNUM(first) + ' ' + findNUM(second) + ' ' + findDENOMINATOR1(third)
        else:  # обработка составных двузначных чисел
            first = int(str(DENOMres)[0] + '0')
            second = int(str(DENOMres)[1])
            return findNUM(first) + ' ' + findDENOMINATOR1(second)
    else:
        return findDENOMINATOR1(DENOMres)


def number_to_text_NUMERATOR(NUMres):  # переводит полученный числитель в текст с учётом окончания на 1 или 2
    if NUMres not in NUMERATORS.values():
        if len(str(NUMres)) == 4 and int(str(NUMres)[1]) == 0 and int(str(NUMres)[2]) == 0:  # обработка чисел 1001-1009
            first = int(str(NUMres)[0] + '000')
            second = int(str(NUMres)[3])
            if second == 2 or second == 1:
                return findNUM(first) + ' ' + findNUMERATOR(second)
            else:
                return findNUM(first) + ' ' + findNUM(second)
        elif len(str(NUMres)) == 4 and int(str(NUMres)[1]) == 0 and int(str(NUMres)[2:]) in NUMS.values():  # 1010-1019.
            first = int(str(NUMres)[0] + '000')
            second = int(str(NUMres)[2:])
            return findNUM(first) + ' ' + findNUM(second)
        elif len(str(NUMres)) == 4 and int(str(NUMres)[1]) == 0 and int(str(NUMres)[2:]) not in NUMS.values():  # 1021..
            first = int(str(NUMres)[0] + '000')
            second = int(str(NUMres)[2] + '0')
            third = int(str(NUMres)[3])
            if third == 2 or third == 1:
                return findNUM(first) + ' ' + findNUM(second) + ' ' + findNUMERATOR(third)
            else:
                return findNUM(first) + ' ' + findNUM(second) + ' ' + findNUM(third)
        elif len(str(NUMres)) == 4 and int(str(NUMres)[2]) == 0 and int(str(NUMres)[3]) == 0:  # 1100, 1200, 1300..
            first = int(str(NUMres)[0] + '000')
            second = int(str(NUMres)[1] + '00')
            return findNUM(first) + ' ' + findNUM(second)
        elif len(str(NUMres)) == 4 and int(str(NUMres)[2]) == 0:  # 1101-1109
            first = int(str(NUMres)[0] + '000')
            second = int(str(NUMres)[1] + '00')
            third = int(str(NUMres)[3])
            if third == 2 or third == 1:
                return findNUM(first) + ' ' + findNUM(second) + ' ' + findNUMERATOR(third)
            else:
                return findNUM(first) + ' ' + findNUM(second) + ' ' + findNUM(third)
        elif len(str(NUMres)) == 4 and int(str(NUMres)[2:]) in NUMS.values():  # 1110-1119, 1120, 1130..
            first = int(str(NUMres)[0] + '000')
            second = int(str(NUMres)[1] + '00')
            third = int(str(NUMres)[2:])
            return findNUM(first) + ' ' + findNUM(second) + ' ' + findNUM(third)
        elif len(str(NUMres)) == 4 and int(str(NUMres)[2:]) not in NUMS.values():  # 1121-1129..
            first = int(str(NUMres)[0] + '000')
            second = int(str(NUMres)[1] + '00')
            third = int(str(NUMres)[2] + '0')
            forth = int(str(NUMres)[3])
            if forth == 1 or forth == 2:
                return findNUM(first) + ' ' + findNUM(second) + ' ' + findNUM(third) + ' ' + findNUMERATOR(forth)
            else:
                return findNUM(first) + ' ' + findNUM(second) + ' ' + findNUM(third) + ' ' + findNUM(forth)
        elif len(str(NUMres)) == 3 and int(str(NUMres)[1:]) in NUMS.values():  # обработка чисел 110 - 120, 130
            first = int(str(NUMres)[0] + '00')
            second = int(str(NUMres)[1:])
            return findNUM(first) + ' ' + findNUM(second)
        elif len(str(NUMres)) == 3 and int(str(NUMres)[1]) == 0:  # обработка чисел 101 - 109
            first = int(str(NUMres)[0] + '00')
            second = int(str(NUMres)[2])
            if second == 1 or second == 2:
                return findNUM(first) + ' ' + findNUMERATOR(second)
            else:
                return findNUM(first) + ' ' + findNUM(second)
        elif len(str(NUMres)) == 3:  # обработка чисел 121 - 129, 131 - 139...
            first = int(str(NUMres)[0] + '00')
            second = int(str(NUMres)[1] + '0')
            third = int(str(NUMres)[2])
            if third == 2 or third == 1:
                return findNUM(first) + ' ' + findNUM(second) + ' ' + findNUMERATOR(third)
            else:
                return findNUM(first) + ' ' + findNUM(second) + ' ' + findNUM(third)
        elif len(str(NUMres)) == 2 and NUMres not in NUMS.values():  # обработка составных двузначных чисел
            first = int(str(NUMres)[0] + '0')
            second = int(str(NUMres)[1])
            if second == 1 or second == 2:
                return findNUM(first) + ' ' + findNUMERATOR(second)
            else:
                return findNUM(first) + ' ' + findNUM(second)
        else:  # обработка двузначных чисел из списка NUM
            return findNUM(NUMres)
    else:
        return findNUMERATOR(NUMres)


def number_to_text_NUM_DENOM(NUMres, DENOMres):  # переводит полученную дробь в текст
    RES = number_to_text_NUMERATOR(NUMres) + ' '
    if int(str(NUMres)[-1]) == 1:  # если числитель оканчивается на 1
        RES += number_to_text_DENOM1(DENOMres)
    else:
        RES += number_to_text_DENOM(DENOMres)
    return RES


def calc(request):
    sp = [elem for elem in request.split()]
    operation_index = 0
    if "умножить" in sp or "плюс" in sp or "минус" in sp and len(sp) >= 3:
        # делим список на представление 2 чисел
        sp1, sp2 = [], []
        if "умножить" in sp:
            operation_index = sp.index("умножить")
            if sp[operation_index + 1] == 'на':
                sp1 = sp[:operation_index]
                sp2 = sp[operation_index + 2:]
        elif "плюс" in sp:
            operation_index = sp.index("плюс")
        elif "минус" in sp:
            operation_index = sp.index("минус")
        if len(sp1) == 0 or len(sp2) == 0:
            sp1 = sp[:operation_index]
            sp2 = sp[operation_index + 1:]
        if len(sp1) == 0 or len(sp2) == 0:
            print('Похоже, вы допустили ошибку при вводе выражения')
            return -1
        SEP1, NUM1, DENOM1 = text_to_number(sp1)
        SEP2, NUM2, DENOM2 = text_to_number(sp2)
        RES = 0
        if sp[operation_index] == 'плюс':
            if NUM1 == 0 and NUM2 == 0 and DENOM1 == 0 and DENOM2 == 0:  # ЧИСЛА НЕДРОБНЫЕ
                SEPres = SEP1 + SEP2
                RES = number_to_text_SEP(SEPres)
            elif NUM1 == 0 and DENOM1 == 0:  # ВТОРОЕ ЧИСЛО - ДРОБЬ
                SEPres = SEP1 + SEP2
                RES = number_to_text_SEP(SEPres)
                RES += " и "
                NOD = math.gcd(NUM2, DENOM2)  # сокращение дроби
                NUM2 //= NOD
                DENOM2 //= NOD
                RES += number_to_text_NUM_DENOM(NUM2, DENOM2)
            elif NUM2 == 0 and DENOM2 == 0:  # ПЕРВОЕ ЧИСЛО - ДРОБЬ
                SEPres = SEP1 + SEP2
                RES = number_to_text_SEP(SEPres)
                RES += " и "
                NOD = math.gcd(NUM1, DENOM1)  # сокращение дроби
                NUM1 //= NOD
                DENOM1 //= NOD
                RES += number_to_text_NUM_DENOM(NUM1, DENOM1)
            else:  # все числа - дроби
                NUM1res = NUM1 + SEP1 * DENOM1  # перевод в неправильную дробь
                NUM2res = NUM2 + SEP2 * DENOM2
                if DENOM1 != DENOM2:  # приведение к общему знаменателю и сложение
                    DENOMres = DENOM1 * DENOM2
                    NUMres = NUM1res * DENOM2 + NUM2res * DENOM1
                else:
                    DENOMres = DENOM1
                    NUMres = NUM1res + NUM2res
                NOD = math.gcd(NUMres, DENOMres)  # сокращение дроби
                NUMres //= NOD
                DENOMres //= NOD
                SEPres = NUMres // DENOMres  # перевод дроби в смешанную
                NUMres -= SEPres * DENOMres
                if SEPres != 0 and NUMres != 0:
                    RES = number_to_text_SEP(SEPres) + " и " + number_to_text_NUM_DENOM(NUMres, DENOMres)
                elif SEPres == 0 and NUMres != 0:
                    RES = number_to_text_NUM_DENOM(NUMres, DENOMres)
                else:
                    RES = number_to_text_SEP(SEPres)
        if sp[operation_index] == 'минус':
            if NUM1 == 0 and NUM2 == 0 and DENOM1 == 0 and DENOM2 == 0:  # ЧИСЛА НЕДРОБНЫЕ
                SEPres = SEP1 - SEP2
                RES = number_to_text_SEP(SEPres)
                if SEPres < 0:
                    print('Похоже, вы допустили ошибку при вводе выражения')
                    return -1
            elif NUM1 == 0 and DENOM1 == 0:  # ВТОРОЕ ЧИСЛО - ДРОБЬ
                RES = ''
                SEPres = SEP1 - SEP2
                SEPres -= 1
                NUMres = DENOM2 - NUM2
                if SEPres != 0:
                    RES = number_to_text_SEP(SEPres)
                    RES += " и "
                NOD = math.gcd(NUMres, DENOM2)  # сокращение дроби
                NUMres //= NOD
                DENOM2 //= NOD
                RES += number_to_text_NUM_DENOM(NUMres, DENOM2)
                if SEPres < 0:
                    print('Похоже, вы допустили ошибку при вводе выражения')
                    return -1
            elif NUM2 == 0 and DENOM2 == 0:  # ПЕРВОЕ ЧИСЛО - ДРОБЬ
                RES = ''
                SEPres = SEP1 - SEP2
                if SEPres != 0:
                    RES = number_to_text_SEP(SEPres)
                    RES += " и "
                NOD = math.gcd(NUM1, DENOM1)  # сокращение дроби
                NUM1 //= NOD
                DENOM1 //= NOD
                RES += number_to_text_NUM_DENOM(NUM1, DENOM1)
                if SEPres < 0:
                    print('Похоже, вы допустили ошибку при вводе выражения')
                    return -1
            else:  # все числа - дроби
                NUM1res = NUM1 + SEP1 * DENOM1  # перевод в неправильную дробь
                NUM2res = NUM2 + SEP2 * DENOM2
                if DENOM1 != DENOM2:  # приведение к общему знаменателю и сложение
                    DENOMres = DENOM1 * DENOM2
                    NUMres = NUM1res * DENOM2 - NUM2res * DENOM1
                else:
                    DENOMres = DENOM1
                    NUMres = NUM1res - NUM2res
                if NUMres < 0:
                    print('Похоже, вы допустили ошибку при вводе выражения')
                    return -1
                NOD = math.gcd(NUMres, DENOMres)  # сокращение дроби
                NUMres //= NOD
                DENOMres //= NOD
                SEPres = NUMres // DENOMres  # перевод дроби в смешанную
                NUMres -= SEPres * DENOMres
                if SEPres != 0 and NUMres != 0:
                    RES = number_to_text_SEP(SEPres) + " и " + number_to_text_NUM_DENOM(NUMres, DENOMres)
                elif SEPres == 0 and NUMres != 0:
                    RES = number_to_text_NUM_DENOM(NUMres, DENOMres)
                else:
                    RES = number_to_text_SEP(SEPres)
        if sp[operation_index] == 'умножить':
            if NUM1 == 0 and NUM2 == 0 and DENOM1 == 0 and DENOM2 == 0:  # ЧИСЛА НЕДРОБНЫЕ
                SEPres = SEP1 * SEP2
                RES = number_to_text_SEP(SEPres)
            elif NUM1 == 0 and DENOM1 == 0:  # ВТОРОЕ ЧИСЛО - ДРОБЬ
                NUM2res = NUM2 + SEP2 * DENOM2
                NUMres = NUM2res * SEP1
                DENOMres = DENOM2
                NOD = math.gcd(NUMres, DENOMres)  # сокращение дроби
                NUMres //= NOD
                DENOMres //= NOD
                SEPres = NUMres // DENOMres  # перевод дроби в смешанную
                NUMres -= SEPres * DENOMres
                if SEPres != 0 and NUMres != 0:
                    RES = number_to_text_SEP(SEPres) + " и " + number_to_text_NUM_DENOM(NUMres, DENOMres)
                elif SEPres == 0 and NUMres != 0:
                    RES = number_to_text_NUM_DENOM(NUMres, DENOMres)
                else:
                    RES = number_to_text_SEP(SEPres)
            elif NUM2 == 0 and DENOM2 == 0:  # ПЕРВОЕ ЧИСЛО - ДРОБЬ
                NUM1res = NUM1 + SEP1 * DENOM1
                NUMres = NUM1res * SEP2
                DENOMres = DENOM1
                NOD = math.gcd(NUMres, DENOMres)  # сокращение дроби
                NUMres //= NOD
                DENOMres //= NOD
                SEPres = NUMres // DENOMres  # перевод дроби в смешанную
                NUMres -= SEPres * DENOMres
                if SEPres != 0 and NUMres != 0:
                    RES = number_to_text_SEP(SEPres) + " и " + number_to_text_NUM_DENOM(NUMres, DENOMres)
                elif SEPres == 0 and NUMres != 0:
                    RES = number_to_text_NUM_DENOM(NUMres, DENOMres)
                else:
                    RES = number_to_text_SEP(SEPres)
            else:  # все числа - дроби
                NUM1res = NUM1 + SEP1 * DENOM1  # перевод в неправильную дробь
                NUM2res = NUM2 + SEP2 * DENOM2
                NUMres = NUM1res * NUM2res
                DENOMres = DENOM1 * DENOM2
                NOD = math.gcd(NUMres, DENOMres)  # сокращение дроби
                NUMres //= NOD
                DENOMres //= NOD
                SEPres = NUMres // DENOMres  # перевод дроби в смешанную
                NUMres -= SEPres * DENOMres
                if SEPres != 0 and NUMres != 0:
                    RES = number_to_text_SEP(SEPres) + " и " + number_to_text_NUM_DENOM(NUMres, DENOMres)
                elif SEPres == 0 and NUMres != 0:
                    RES = number_to_text_NUM_DENOM(NUMres, DENOMres)
                else:
                    RES = number_to_text_SEP(SEPres)
        return RES
    else:
        print('Похоже, вы допустили ошибку при вводе выражения')
        return -1