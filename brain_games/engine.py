import prompt

ROUNDS_COUNT = 3


def run_game(generate_question, get_rules, name):
    """Основная логика игры"""
    print("Welcome to the Brain Games!")
    print(f"Hello, {name}!")
    print(get_rules())

    for _ in range(ROUNDS_COUNT):
        question, correct_answer = generate_question()
        print(f"Question: {question}")

        user_answer = prompt.string("Your answer: ").lower()

        if user_answer != correct_answer:
            print(f"'{user_answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {name}!")
            return

        print("Correct!")

    print(f"Congratulations, {name}!")
