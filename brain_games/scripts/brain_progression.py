import random
from brain_games.engine import run_game


def generate_progression():
    """Генерация прогрессии"""
    length = random.randint(5, 10)
    start = random.randint(1, 20)
    step = random.randint(1, 5)
    progression = [start + step * i for i in range(length)]
    hidden_index = random.randint(0, length - 1)
    correct_answer = progression[hidden_index]
    progression[hidden_index] = '..'
    question = ' '.join(map(str, progression))
    return question, str(correct_answer)


def get_rules():
    return "What number is missing in the progression?"


def play_game(name):
    """Запуск игры с использованием общей логики"""
    run_game(generate_progression, get_rules, name)
