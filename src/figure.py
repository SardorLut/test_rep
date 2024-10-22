class Figure:
    def __init__(self, x: int = 3,
                  y: int = 4,
                    pi: float=3.1415):
        self.x = x
        self.y = y
        self.pi = pi
    def get_square(self):
        raise NotImplementedError("implement me!")