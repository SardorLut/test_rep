from src.figure import Figure
def sum_two_squares(f1: Figure, f2: Figure) -> float:
    s1 = f1.get_square()
    s2 = f2.get_square()
    return s1 + s2