import random
import math
from brain_games.engine import run_game
from brain_games.cli import welcome_user

def get_rules():
    return "Find the greatest common divisor of given numbers."


def generate_question():
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)
    correct_answer = str(math.gcd(num1, num2))
    question = f"{num1} {num2}"
    return question, correct_answer


def main():
    name = input("May I have your name? ")
    run_game(generate_question, get_rules, name)


if __name__ == '__main__':
    main()
