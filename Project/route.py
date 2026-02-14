
class Route:
    def __init__(self, from_city: str, to_city: str):
        self.from_city = from_city
        self.to_city = to_city

    def __str__(self):
        return self.from_city, self.to_city





