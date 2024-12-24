import random
import operator

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
    print("Welcome to the Brain Games!")  # Приветствие
    name = input("May I have your name? ")  # Запрос имени
    print(f"Hello, {name}!")  # Приветствие игрока
    print("What is the result of the expression?")

    # Начало игрового процесса: цикл вопросов
    for _ in range(rounds):
        question, correct_answer = generate_question()  # Генерация вопроса
        print(f"Question: {question}")  # Вопрос в нужном формате
        user_answer = input("Your answer: ")  # Ответ игрока

        if user_answer != correct_answer:
            print(f"'{user_answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {name}!")
            return

    # Единственное сообщение в конце игры
    print(f"Congratulations, {name}!")  # Финальный вывод
