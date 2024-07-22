# "Создание функций на лету"
first = 'Мама мыла раму'
second = 'Рамена мало было'
print(list(map(lambda x, y: x == y, first, second)))


# Результатом должен быть список совпадения букв в той же позиции:
# [False, True, True, False, False, False, False, False, True, False, False, False, False, False]

def get_advanced_writer(file_name):
    def write_everything(*data_set):
        with open(file_name, 'a', encoding='utf-8') as file:
            for elem in data_set:
                file.write(str(elem) + '\n')

    return write_everything


try:
    write = get_advanced_writer('example.txt')
except:
    with open('example.txt', 'w') as file:
        file.write('')
    write = get_advanced_writer('example.txt')

write('Это строчка', ['А', 'это', 'уже', 'число', 5, 'в', 'списке'])

# результат:
# Это строчка
# ['А', 'это', 'уже', 'число', 5, 'в', 'списке']

from random import choice


class MysticBall:
    def __init__(self, *word):
        self.word = word

    def __call__(self):
        return choice(self.word)


# Ваш код (количество слов для случайного выбора может быть другое):
first_ball = MysticBall('Да', 'Нет', 'Наверное')
print(first_ball())
print(first_ball())
print(first_ball())
