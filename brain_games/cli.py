def welcome_user():
    """Приветствие и запрос имени пользователя"""
    print("Welcome to the Brain Games!")
    name = input("May I have your name? ")
    print(f"Hello, {name}!")
    return name
