"""Задание состоит из двух частей:
1 часть – написать программу в соответствии со своим вариантом задания.
2 часть – усложнить написанную программу, введя по своему усмотрению в условие минимум одно ограничение
на характеристики объектов и целевую функцию для оптимизации решения.

Вариант 13:
Фирма закупает К компьютеров. В магазине компьютеры N типов. Сформировать все возможные варианты покупки.

Требуется для своего варианта второй части л.р. №6 (усложненной программы) написать объектно-ориентированную реализацию.
В программе должны быть реализованы минимум один класс, три атрибута, два метода."""

from random import choice, randrange


def product(*args, repeat=1):
    # если нет аргументов, возвращаем пустой список
    pools = list(map(tuple, args)) * repeat
    result = [[]]
    for pool in pools:
        result = [x + [y] for x in result for y in pool]
    for prod in result:
        yield tuple(prod)


class buying_laptops:
    def __init__(self):
        self.combr = []
        self.maxstr = []
        self.exception = []
        self.purchases = []
        self.combinations = []
        self.maxs = self.cntcomps = self.cnttips = self.dm = 0
        self.BRANDS = ['Apple', 'Asus', 'Dell', 'HP', 'Lenovo', 'Acer', 'MSI', 'Samsung']

        self.cntcomps = int(input('\nВведите кол-во покупаемых компьютеров: '))
        while self.cntcomps < 0:
            self.cntcomps = int(input('\nПринимаются только положительные числа: '))
        if not self.cntcomps:
            print('\nОчень умно! Вы решили сэкономить деньги и не купили ни одного компьютера.')
            quit()

        self.cnttips = int(input('\nВведите кол-во типов компьютеров: '))
        while self.cnttips < 0:
            self.cnttips = int(input('\nПринимаются только положительные числа: '))
        if not self.cnttips:
            print('\nКажется, сегодня мы остались без покупок.')
            quit()

        try:
            self.switch = int(input('\nЗапустить усложнённую версию программы? ( Нет = 0 | Да = 1 ): '))
            while self.switch != 0 and self.switch != 1:
                self.switch = int(input('\nПринимаются только значения "0" и "1": '))
        except ValueError:
            self.switch = 0

    def calculations(self):

        if not self.switch:
            self.computers = [f'№ {i}: {choice(self.BRANDS)}' for i in range(1, self.cnttips + 1)]

        if self.switch:
            print('\nУсложнением будет являться качество производителя.\nЕсли качество производителя низкое, то данный'
                  ' производитель не будет учитываться в рассмотрении его к покупке.\nТак же у каждого компьютера есть '
                  'своя стоимость. Вывести вариант покупки с максимальной суммарной стоимостью.')

            self.computers = [f'{choice(self.BRANDS)} ({randrange(10999, 99999, 1000)} р.)' for i in
                          range(1, self.cnttips + 1)]

            self.сomp1 = str(self.computers)[2:-1].replace("'", '')

            self.d = 0
            if len(self.computers) > 1:
                b = len(self.computers)
                while (b - len(self.computers)) <= (b // 2 - 1):
                    r = choice(self.BRANDS)
                    if r not in self.exception:
                        self.exception.append(r)

                    for i, varu in enumerate(self.computers):
                        for j in self.exception:
                            if j in varu:
                                self.computers.pop(i)
                else:
                    for i in self.exception:
                        self.d = f'{self.d}, {i}'

            else:
                while len(self.exception) < 3:
                    r = choice(self.BRANDS)
                    if r not in self.exception:
                        self.exception.append(r)

                for i, varu in enumerate(self.computers):
                    for j in self.exception:
                        if j in varu:
                            self.computers.pop(i)
                for i in self.exception:
                    self.d = f'{self.d} {i}'

        if self.computers:
            self.comp2 = str(self.computers)[2:-1].replace("'", '')
        else:
            print('\nКажется, сегодня мы остались без покупок.')
            quit()

        for i, varu in enumerate(product(self.computers, repeat=self.cntcomps)):
            s = 0
            b = {}

            if ((self.cntcomps > 4 and len(self.computers) > 8) or (self.cntcomps > 9 or len(self.computers) > 12)) and not self.dm:
                self.dm = int(input(f'\nВы ввели большие значения K или N, работа программы может занять существенное '
                              f'время. Хотите дождаться вывода? ( Да = 1 | Нет = 0 ): '))
                while not self.dm and self.dm:
                    self.dm = int(input('Принимаются только значения "0" и "1": '))
                if not self.dm:
                    quit()
                print('\nПодождите...')

            for j in sorted(varu):
                if j in b:
                    b[j] = b[j] + 1
                else:
                    b[j] = 1
                if self.switch == 1:
                    s += int(j[-9:-4])

            if b not in self.combr:
                self.combinations.append(varu)

            if self.switch == 1:
                if s >= self.maxs:
                    self.maxs = s
                    self.maxstr = varu

            self.combr.append(b)

        if self.switch:
            self.results = (str(self.maxstr[::-1])[2:-2].replace("'", '').replace(', ', ' | '))

    def result_window(self):
        if not self.switch:
            print(f'\nКомпьютеры в магазине:')
            print(str(self.computers)[2:-1].replace("'", ''))
        else:
            print(f'\nКомпьютеры в магазине:\n{self.сomp1}')
            print(f'\nНекачественные производители:\n{self.d[3::]}')
            print(f'\nКомпьютеры подлежащие выбору:\n{self.comp2}')
            print(f'\nВариант самой дорогой покупки:')
            print(f'{self.results} - Сумма покупки: {self.maxs} руб.')

        self.b = 1
        if len(self.combinations) > 30:
            self.b = int(input(f'\nКолличество возможных покупок равно {len(self.combinations)}.\n'
                               f'Вывести их на экран? ( Да = 1 | Нет = 0 ): '))
            while not self.b and self.b:
                self.b = int(input('\nПринимаются только значения "0" и "1": '))

        if self.b:
            print('\nВозможные варианты покупок:')
            for i, var in enumerate(sorted(self.combinations, key=len)):
                h = str(var)[1:-2].replace("'", '').replace(', ', ' | ')
                print(f'{i + 1}. {h}')

    def update(self):
        self.calculations()
        self.result_window()


laptop = buying_laptops()
laptop.update()
