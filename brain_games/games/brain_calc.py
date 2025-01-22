import operator
import random
from brain_games.engine import run_game

# Операции для игры
OPERATIONS = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
}


def generate_question():
    """Генерация случайного математического выражения и правильного ответа"""
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)
    operation = random.choice(list(OPERATIONS.keys()))
    question = f"{num1} {operation} {num2}"
    correct_answer = OPERATIONS[operation](num1, num2)
    return question, str(correct_answer)


def get_rules():
    return "What is the result of the expression?"


def play_game(name):
    """Запуск игры с использованием общей логики"""
    run_game(generate_question, get_rules, name)
