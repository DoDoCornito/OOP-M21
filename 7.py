class BoundingRectangle:
    def __init__(self):
        self.min_x = float('inf')
        self.max_x = float('-inf')
        self.min_y = float('inf')
        self.max_y = float('-inf')

    def add_point(self, x, y):
        self.min_x = min(self.min_x, x)
        self.max_x = max(self.max_x, x)
        self.min_y = min(self.min_y, y)
        self.max_y = max(self.max_y, y)

    def width(self):
        return self.max_x - self.min_x

    def height(self):
        return self.max_y - self.min_y

    def bottom_y(self):
        return self.min_y

    def top_y(self):
        return self.max_y

    def left_x(self):
        return self.min_x

    def right_x(self):
        return self.max_x

# Пример использования
rect = BoundingRectangle()
rect.add_point(1, 3)
rect.add_point(4, 5)
print(rect.width())  # Вывод: 3
print(rect.height())  # Вывод: 2
print(rect.bottom_y())  # Вывод: 3
print(rect.top_y())  # Вывод: 5
print(rect.left_x())  # Вывод: 1
print(rect.right_x())  # Вывод: 4
