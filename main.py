from dotenv import load_dotenv
import os
import argparse
from src.utils import sum_two_squares
from src.figure import Figure
import numpy
from src.Circle import Circle
def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--len",
        required=False,
        type=int,
        help="len for figure"
    )
    return parser.parse_args()

def main():
    c1 = Circle(6)
    c2 = Circle(3)
    print(sum_two_squares(c1, c2))

if __name__ == "__main__":
    load_dotenv()
    args = parse_args()
    main()

