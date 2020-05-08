class NotEmailError(Exception):
    pass

class NotNameError(Exception):
    pass

def registration():
    i = 0
    data = {}
    with open('C:/Users/olivi/skills/HW9/registrations_.txt', 'r', encoding="utf-8") as rf:
        for line in rf:
            data[i] = line.split()
            i += 1

    for key, val in data.items():
        if len(val) == 3:
            if val[0].isalpha():
                if '@' in val[1] and '.' in val[1]:
                    if 10 < int(val[2]) < 99:
                        with open('C:/Users/olivi/skills/HW9/registrations_good.log', 'ta', encoding="utf-8") as wf:
                            wf.write(' '.join((val[0], val[1], val[2], '\n')))
                    else:
                        try:
                            with open('C:/Users/olivi/skills/HW9/registrations_bad.log', 'ta', encoding="utf-8") as badf:
                                badf.write(' '.join(('ValueError', val[0], val[1], val[2], '\n')))
                            raise ValueError('поле возраст НЕ является числом от 10 до 99')
                        except ValueError as exc:
                            print(f'Поймано исключение: {exc}')
                else:
                    try:
                        with open('C:/Users/olivi/skills/HW9/registrations_bad.log', 'ta', encoding="utf-8") as badf:
                            badf.write(' '.join(('NotEmailError', val[0], val[1], val[2], '\n')))
                        raise NotEmailError('поле email НЕ содержит @ и .(точку)')
                    except NotEmailError as exc:
                        print(f'Поймано исключение: {exc}')
            else:
                try:
                    with open('C:/Users/olivi/skills/HW9/registrations_bad.log', 'ta', encoding="utf-8") as badf:
                        badf.write(' '.join(('NotNameError', val[0], val[1], val[2], '\n')))
                    raise NotNameError('поле имени содержит НЕ только буквы')
                except NotNameError as exc:
                    print(f'Поймано исключение: {exc}')
        else:
            try:
                with open('C:/Users/olivi/skills/HW9/registrations_bad.log', 'ta', encoding="utf-8") as badf:
                    badf.write(' '.join(('ValueError', str(val).replace("[", "").replace("]", "").replace(",", "").replace("'", ""), '\n')))
                raise ValueError('НЕ присутсвуют все три поля')
            except ValueError as exc:
                print(f'Поймано исключение: {exc}')

try:
    registration()
except IOError:
    print('Произошла ошибка ввода-вывода!')
