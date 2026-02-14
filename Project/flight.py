
class Flight:
    def __init__(self, route, passengers, plane):
        self.route = route
        self.passengers = passengers
        self.plane = plane

    def show_info(self):
        return(
            f' {self.route} | Пассажиров: {self.passengers} | '
            f' Мест: {self.plane.total_capacity()} | Секции: {len(self.plane.sections)} | '
        )

    def full_info(self):
        lines = []
        lines.append('=== РЕЙС ===')
        lines.append(f'Маршрут: {self.route}')
        lines.append(f'Пассажиры: {self.passengers}')
        lines.append(f'Секции: {self.plane.sections}')
        lines.append(f'Мест: {self.plane.total_capacity()}')
        lines.append('--- СЕКЦИИ ---')

        for i in range(len(self.plane.sections)):
            free = self.plane.sections[i].capacity - self.plane.sections[i].occupied
            lines.append(f'{i + 1}. {self.plane.sections[i].name}: вместимость = {self.plane.sections[i].capacity}, занято = {self.plane.sections[i].occupied}, свободно: {free}')

        return '\n'.join(lines)

