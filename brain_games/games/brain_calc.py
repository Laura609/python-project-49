# brain_games/games/brain_calc.py
import random
import operator
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


def play_game():
    """Основная логика игры"""
    rounds = 3

    # Приветствие
    print("Welcome to the Brain Games!")
    name = input("May I have your name? ")
    print(f"Hello, {name}!")

    # Сообщение о начале игры
    print("What is the result of the expression?")

    # Вопросы генерируются после приветствия
    for _ in range(rounds):
        # Генерация и вывод вопроса
        question, correct_answer = generate_question()
        print(f"Question: {question}")  # Это должно быть первым выводом

        user_answer = input("Your answer: ")

        if user_answer == correct_answer:
            print("Correct!")
        else:
            print(f"'{user_answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {name}!")
            return

    print(f"Congratulations, {name}!")
