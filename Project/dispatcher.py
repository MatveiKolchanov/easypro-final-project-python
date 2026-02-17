
from Project.cabinSection import CabinSection
from Project.plane import Plane
from Project.flight import Flight
from Project.route import Route

import random

class Dispatcher:
    def __init__(self):
        self.flights = []

    def run(self):
        while True:
            self.print_flights()

            self.print_menu()
            choice = input('Выберете пункт: ')

            if choice == '2':
                print('Завершение работы')
                break

            if choice != '1':
                print('Неверный пункт меню')
                continue

    def print_flights(self):
        print('\n' + '=' * 50)

        if len(self.flights) == 0:
            print('Запланированных рейсов пока нет')
        else:
            print('Запланированные рейсы: ')

        for i in range(len(self.flights)):
            print(f'{i + 1}. {self.flights[i].show_info()}')

        print('=' * 50)

    def print_menu(self):
        print('\nМеню:')
        print('1. Запланировать рейс')
        print('2. Выход')

    def create_flight(self):
        route = self.create_route()
        passengers = self.sell_tickets(route)

    def create_route(self):
        print('\n [Шаг 1] Создание маршрута')
        from_city = input('Город вылета: ').strip()
        to_city = input('Город прилета: ').strip()

        return Route(from_city, to_city)

    def sell_tickets(self, route):
        print('\n[Шаг 2] Продажа билетов')
        passengers = random.randint(20, 420)
        print(f'На маршрут {route} купили ьилеты: {passengers} пассажиров.')

        return passengers

    def form_plane(self, passengers):
        print('\n[Шаг 3] Формирование самолета')
        mode = self.choose_plane_mode()

        plane = Plane()

        if mode == '1':
            capacity = int(input('Вместимость одной секции от 10 до 70'))
            name = input('Название секции (эконом): ')

    def choose_plane_mode(self):
        print('1. Все секции одинаковой вместимости')
        print('2. Секции разной вместимости (случайно)')
        mode = input('Выберете вариант: ').strip()

        return mode







