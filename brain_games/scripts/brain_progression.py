import random
import prompt

# Константы
ROUNDS_COUNT = 3


def progression_game():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print('What number is missing in the progression?')

    for _ in range(ROUNDS_COUNT):
        # Длина прогрессии (от 5 до 10)
        length = random.randint(5, 10)

        # Первый элемент прогрессии и шаг прогрессии
        start = random.randint(1, 20)
        step = random.randint(1, 5)

        # Создаем прогрессию
        progression = [start + step * i for i in range(length)]

        # Выбираем случайную позицию для пропущенного числа
        hidden_index = random.randint(0, length - 1)

        # Скрываем число в прогрессии
        correct_answer = progression[hidden_index]
        progression[hidden_index] = '..'

        # Печатаем вопрос
        progression_str = ' '.join(map(str, progression))
        print(f'Question: {progression_str}')

        # Получаем ответ пользователя
        user_answer = int(prompt.string('Your answer: '))

        # Проверяем ответ
        if user_answer == correct_answer:
            print('Correct!')
        else:
            print(f"'{user_answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {name}!")
            return

    print(f'Congratulations, {name}!')


def main():
    progression_game()
