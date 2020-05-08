def sumOfPairs(L1, L2):
    sum = 0
    sumOfPairs = []
    for i in range(len(L1)):
        sumOfPairs.append(L1[i]+L2[i])

    print("sumOfPairs = ", sumOfPairs)

try:
    sumOfPairs('п')
except TypeError as exc:
    print('Функция работает только со строками!', exc)
except NameError as exc:
    print('Переменные не определены!', exc)
except IndexError as exc:
    print('Первое слово не должно быть больше второго!', exc)
except Exception as exc:
    print('Непредвиденная ошибка!', exc)
except SyntaxError as exc:
    print('Синтаксическая ошибка!', exc)