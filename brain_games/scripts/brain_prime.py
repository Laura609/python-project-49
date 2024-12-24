import random
import prompt

# Константы
ROUNDS_COUNT = 3


def is_prime(number):
    """Проверка, является ли число простым"""
    if number < 2:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True


def prime_game():
    """Основная игра: ответить на вопрос, простое ли число"""
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print('Answer "yes" if given number is prime. Otherwise answer "no".')

    for _ in range(ROUNDS_COUNT):
        # Генерация случайного числа
        number = random.randint(1, 100)

        # Определение правильного ответа
        correct_answer = "yes" if is_prime(number) else "no"

        # Печатаем вопрос
        print(f'Question: {number}')

        # Получаем ответ от пользователя
        user_answer = prompt.string('Your answer: ').lower()

        # Проверяем ответ
        if user_answer == correct_answer:
            print('Correct!')
        else:
            print(f"'{user_answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {name}!")
            return  # Если ответ неверный, игра завершается

    print(f'Congratulations, {name}!')


def main():
    prime_game()
