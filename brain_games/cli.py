# brain_games/cli.py
def welcome_user():
    """Приветствие пользователя"""
    print("Welcome to the Brain Games!")
    name = input("May I have your name? ")
    print(f"Hello, {name}!")
    return name
