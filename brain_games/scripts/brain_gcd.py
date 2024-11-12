# brain_games/scripts/brain_gcd.py

import random
import math
import prompt


def gcd_game():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print('Find the greatest common divisor of given numbers.')

    rounds = 3  # Количество раундов

    for _ in range(rounds):
        # Генерация двух случайных чисел
        num1 = random.randint(1, 100)
        num2 = random.randint(1, 100)

        # Вычисление НОД
        correct_answer = math.gcd(num1, num2)

        # Вывод вопроса
        print(f'Question: {num1} {num2}')

        # Получение ответа от пользователя
        user_answer = int(prompt.string('Your answer: '))

        # Проверка ответа
        if user_answer == correct_answer:
            print('Correct!')
        else:
            print(f"'{user_answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {name}!")
            return  # Если ответ неверный, игра завершается

    print(f'Congratulations, {name}!')


def main():
    gcd_game()

