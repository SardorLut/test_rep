from src.figure import Figure
class Circle(Figure):
    def __init__(self, r: int):
        super().__init__()
        self.r = r
    def get_square(self) -> float:
        return self.r * self.pi
    