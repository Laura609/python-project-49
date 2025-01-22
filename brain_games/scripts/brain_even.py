import random
import prompt

# Константы
ROUNDS_COUNT = 3


def is_even(number):
    """Проверяет, чётное ли число."""
    return number % 2 == 0


def generate_question():
    """Генерирует случайный вопрос и правильный ответ."""
    number = random.randint(1, 100)
    correct_answer = "yes" if is_even(number) else "no"
    return number, correct_answer


def main():
    print("Welcome to the Brain Games!")
    name = prompt.string("May I have your name? ")
    print(f"Hello, {name}!")
    print('Answer "yes" if the number is even, otherwise answer "no".')

    correct_answers_count = 0
    while correct_answers_count < ROUNDS_COUNT:
        question, correct_answer = generate_question()
        print(f"Question: {question}")
        user_answer = prompt.string("Your answer: ").lower()

        if user_answer != correct_answer:
            print(f"'{user_answer}' is wrong answer ;(. Correct answer was "
                  f"'{correct_answer}'.")
            print(f"Let's try again, {name}!")
            return

        print("Correct!")
        correct_answers_count += 1

    print(f"Congratulations, {name}!")

