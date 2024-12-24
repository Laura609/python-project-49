# brain_games/engine.py
def run_game(generate_question, rounds=3):
    """Запуск игры, обработка раундов, проверка ответов."""
    print("Welcome to the Brain Games!")
    name = input("May I have your name? ")
    print(f"Hello, {name}!")

    for _ in range(rounds):
        question, correct_answer = generate_question()
        print(f"Question: {question}")
        user_answer = input("Your answer: ")

        if user_answer == correct_answer:
            print("Correct!")
        else:
            print(f"'{user_answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {name}!")
            return  # Завершаем игру при неверном ответе

    print(f"Congratulations, {name}!")
