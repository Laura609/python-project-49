import random
from brain_games.engine import run_game


def get_rules():
    return 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(number):
    if number < 2:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True


def generate_question():
    number = random.randint(1, 100)
    correct_answer = "yes" if is_prime(number) else "no"
    return number, correct_answer


def main():
    name = input("May I have your name? ")
    run_game(generate_question, get_rules, name)


if __name__ == '__main__':
    main()
