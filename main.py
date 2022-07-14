#Тестовое задание на вакансию Junior python developer. Онлайн-школа Тетрика.
import bs4, requests

'''
Решение 1-го задания
'''


def task(array: str) -> int:
    '''
    :param array: Строка из цифр 1 и 0.
    :return: Номер первого символа 0.
    '''
    return array.find('0')


#print(task("111111111110000000000000000"))

'''
Решение 2-го задания
'''


def get_animals_from(link: str) -> bs4.BeautifulSoup:
    responce = requests.get(url=link)
    soup = bs4.BeautifulSoup(responce.text, 'lxml')
    return soup


def pars_wiki_animals() -> None:
    '''
    Функция собирает названия всех животных с Википедии.
    '''
    link = 'https://inlnk.ru/jElywR'
    parsing = True
    with open('animals.txt', 'w', encoding='utf-8') as file:
        while parsing:
            page = get_animals_from(link)
            tag_a = page.find(id='mw-pages').find_all('a')
            old_link = link

            for elem in tag_a:
                content = elem.text

                if content not in ('Предыдущая страница', 'Следующая страница'):
                    file.write(content + '\n')
                elif content == 'Следующая страница':
                    link = 'https://ru.wikipedia.org' + elem.get('href')

            if link == old_link:
                parsing = False


def count_animals(file_name: str) -> dict:
    '''
    Функция подсчитывает количество животных начинающихся на одинаковую букву.
    :param file_name: Строка содержащая имя файла.
    :return: Словарь с парами буква - количество букв.
    '''
    first_letters = {}

    with open(file_name, encoding='utf-8') as file:
        content = file.readlines()
        for elem in content:
            first_letters[elem[0]] = first_letters[elem[0]] + 1 if elem[0] in first_letters else 1
    return dict(sorted(first_letters.items(), key=lambda x: x[0].lower()))


# pars_wiki_animals()
# for elem in count_animals('animals.txt').items():
#     print('{}: {}'.format(*elem))

'''
Решение 3-го задания
'''

tests = [
    {'data': {'lesson': [1594663200, 1594666800],
             'pupil': [1594663340, 1594663389, 1594663390, 1594663395, 1594663396, 1594666472],
             'tutor': [1594663290, 1594663430, 1594663443, 1594666473]},
     'answer': 3117
    },
    {'data': {'lesson': [1594702800, 1594706400],
             'pupil': [1594702789, 1594704500, 1594702807, 1594704542, 1594704512, 1594704513, 1594704564, 1594705150,
                       1594704581, 1594704582, 1594704734, 1594705009, 1594705095, 1594705096, 1594705106, 1594706480,
                       1594705158, 1594705773, 1594705849, 1594706480, 1594706500, 1594706875, 1594706502, 1594706503,
                       1594706524, 1594706524, 1594706579, 1594706641],
             'tutor': [1594700035, 1594700364, 1594702749, 1594705148, 1594705149, 1594706463]},
    'answer': 3577
    },
    {'data': {'lesson': [1594692000, 1594695600],
             'pupil': [1594692033, 1594696347],
             'tutor': [1594692017, 1594692066, 1594692068, 1594696341]},
    'answer': 3565
    },
]


def appearance(intervals: dict) -> int | float:
    '''

    :param intervals: Словарь из интервалов времени урока, ученика и учителя.
    :return: Время совместного нахождения ученика и учителя на уроке.
    '''
    flags = dict.fromkeys(intervals, 0)
    events = sorted((elem, (-1) ** i, name)
                    for name in intervals
                    for i, elem in enumerate(intervals[name]))
    start, result = 0, 0
    for event in events:
        flags[event[2]] += event[1]
        if all(flags.values()) and start == 0:
            start = event[0]
        elif not all(flags.values()) and start > 0:
            result += event[0] - start
            start = 0
    return result


# if __name__ == '__main__':
#    for i, test in enumerate(tests):
#        test_answer = appearance(test['data'])
#        print(test_answer)
#        assert test_answer == test['answer'], f'Error on test case {i}, got {test_answer}, expected {test["answer"]}'
