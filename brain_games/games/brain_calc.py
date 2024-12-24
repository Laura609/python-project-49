import random
import operator

OPERATIONS = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
}


def generate_question():
    """Генерирует случайный вопрос и правильный ответ для игры 'Калькулятор'."""
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)
    operation = random.choice(list(OPERATIONS.keys()))
    question = f"{num1} {operation} {num2}"
    correct_answer = str(OPERATIONS[operation](num1, num2))
    return question, correct_answer


def brain_calc():
    """Запуск игры 'Калькулятор' с 3 раундами."""
    print("Welcome to the Brain Games!")  # Приветствие перед началом игры
    name = input("May I have your name? ")  # Получаем имя игрока
    print(f"Hello, {name}!")

    rounds = 3
    for _ in range(rounds):
        question, correct_answer = generate_question()
        print(f"Question: {question}")  # Печатаем вопрос в нужном формате
        user_answer = input("Your answer: ")

        if user_answer == correct_answer:
            print("Correct!")
        else:
            print(f"'{user_answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {name}!")
            return
    print(f"Congratulations, {name}!")
