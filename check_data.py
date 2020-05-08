class NotEmailError(Exception):
    pass

class NotNameError(Exception):
    pass

def check_data(line):
    if len(line) != 3:
        raise ValueError('НЕ присутсвуют все три поля')
    if not line[0].isalpha():
        raise NotNameError('поле имени содержит НЕ только буквы')
    if ('@' not in line[1]) or ('.' not in line[1]):
        raise NotEmailError('поле email НЕ содержит @ и .(точку)')
    if int(line[2]) < 10 or int(line[2]) > 99:
        raise ValueError('поле возраст НЕ является числом от 10 до 99')
    else:
        return line

wf = open('C:/Users/olivi/skills/HW9/registrations_good.log', 'ta', encoding = 'utf-8')
badf = open('C:/Users/olivi/skills/HW9/registrations_bad.log', 'ta', encoding = 'utf-8')
with open('C:/Users/olivi/skills/HW9/registrations_.txt', 'r', encoding='utf-8') as rf:
    for line in rf:
        if not line.isspace():
            try:
                data = check_data(line.split())
                wf.write(' '.join((data[0], data[1], data[2], '\n')))
            except ValueError as exc:
                print(f'Поймано исключение: {exc}')
                badf.write(line)
            except NotNameError as exc:
                print(f'Поймано исключение: {exc}')
                badf.write(line)
            except NotEmailError as exc:
                print(f'Поймано исключение: {exc}')
                badf.write(line)
wf.close()
badf.close()
