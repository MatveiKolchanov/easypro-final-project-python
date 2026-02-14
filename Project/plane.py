
class Plane:
    def __init__(self):
        self.sections = []

    def total_capacity(self):
        total = 0

        for section in self.sections:
            total += section.capacity

        return total

    def distribute(self, passengers):
        remaining = passengers

        for section in self.sections:
            if remaining <= 0:
                section.occupied = 0
            else:
                take = section.capacity if remaining >= section.capacity else remaining
                section.occupied = take
                remaining -= take

