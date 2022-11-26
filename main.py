"""Задается функция атаки."""
from random import randint


# Новый импорт.
# Из модуля start_game_banner, который расположен в папке graphic_arts,
# импортируем функцию run_screensaver().
from graphic_arts.start_game_banner import run_screensaver


def attack(char_name: str, char_class: str) -> str:
    """Задается функция атаки."""
    if char_class == 'warrior':
        """Задается урон война."""
        return (f'{char_name} нанёс противнику урон, равный '
                f'{5 + randint(3, 5)}')
    if char_class == 'mage':
        """Задается урон мага."""
        return (f'{char_name} нанёс противнику урон, равный '
                f'{5 + randint(5, 10)}')
    if char_class == 'healer':
        """Задается урон хиллера."""
        return (f'{char_name} нанёс противнику урон, равный '
                f'{5 + randint(-3, -1)}')


def defence(char_name: str, char_class: str) -> str:
    """Задается функция защиты."""
    if char_class == 'warrior':
        """Возращается защита война."""
        return (f'{char_name} блокировал {10 + randint(5, 10)} ед. урона')
    if char_class == 'mage':
        """Возращается защита мага."""
        return (f'{char_name} блокировал {10 + randint(-2, 2)} ед. урона')
    if char_class == 'healer':
        """Возращается защита хиллера."""
        return (f'{char_name} блокировал {10 + randint(2, 5)} ед. урона')


def special(char_name: str, char_class: str) -> str:
    """Задается функция спец умения."""
    if char_class == 'warrior':
        """Возращается применение спец умения."""
        return (f'{char_name} применил специальное умение '
                f'«Выносливость {80 + 25}»')
    if char_class == 'mage':
        """Возращается применение спец умения."""
        return (f'{char_name} применил специальное умение «Атака {5 + 40}»')
    if char_class == 'healer':
        """Возращается применение спец умения."""
        return (f'{char_name} применил специальное умение «Защита {10 + 30}»')


def start_training(char_name: str, char_class: str) -> str:
    """Задается функция выбора типа персонажа."""
    if char_class == 'warrior':
        """Показывает кого игрок выбрал."""
        print(f'{char_name}, ты Воитель — великий мастер ближнего боя.')
    if char_class == 'mage':
        """Показывает кого игрок выбрал."""
        print(f'{char_name}, ты Маг — превосходный укротитель стихий.')
    if char_class == 'healer':
        """Показывает кого игрок выбрал."""
        print(f'{char_name}, ты Лекарь — чародей, способный исцелять раны.')
    print('Потренируйся управлять своими навыками.')
    print('Введи одну из команд: attack — чтобы атаковать противника, '
          'defence — чтобы блокировать атаку противника или '
          'special — чтобы использовать свою суперсилу.')
    print('Если не хочешь тренироваться, введи команду skip.')
    cmd: str = None
    while cmd != 'skip':
        """Функция задающая выход из игры."""
        cmd = input('Введи команду: ')
        if cmd == 'attack':
            """Функция задающая выход из игры."""
            print(attack(char_name, char_class))
        if cmd == 'defence':
            """Функция задающая выход из игры."""
            print(defence(char_name, char_class))
        if cmd == 'special':
            """Функция задающая выход из игры."""
            print(special(char_name, char_class))
    return 'Тренировка окончена.'


def choice_char_class() -> str:
    """Вычисляет квадратный корень."""
    approve_choice = None
    char_class = None
    while approve_choice != 'y':
        """Функция задающая выход из игры."""
        char_class: str = input('Введи название персонажа, '
                                'за которого хочешь играть:'
                                'Воитель — warrior, '
                                'Маг — mage, Лекарь — healer: ')
        """Функция задающая выход из игры."""                       
        if char_class == 'warrior':
            """Функция задающая выход из игры."""
            print('Воитель — дерзкий воин ближнего боя. '
                  'Сильный, выносливый и отважный.')
        if char_class == 'mage':
            """Функция задающая выход из игры."""
            print('Маг — находчивый воин дальнего боя. '
                  'Обладает высоким интеллектом.')
        if char_class == 'healer':
            """Функция задающая выход из игры."""
            print('Лекарь — могущественный заклинатель. '
                  'Черпает силы из природы, веры и духов.')
        approve_choice: str = input('Нажми (Y), чтобы подтвердить выбор, '
                                    'или любую другую кнопку, '
                                    'чтобы выбрать другого персонажа ').lower()
        """Функция задающая выход из игры."""
    return char_class


if __name__ == '__main__':
    run_screensaver()
    print('Приветствую тебя, искатель приключений!')
    print('Прежде чем начать игру...')
    char_name: str = input('...назови себя: ')
    print(f'Здравствуй, {char_name}! '
          'Сейчас твоя выносливость — 80, атака — 5 и защита — 10.')
    print('Ты можешь выбрать один из трёх путей силы:')
    print('Воитель, Маг, Лекарь')
    char_class: str = choice_char_class()
    print(start_training(char_name, char_class))
   