def welcome_user():
    """Функция для приветствия пользователя и получения его имени."""
    print("Welcome to the Brain Games!")
    name = input("May I have your name? ")
    print(f"Hello, {name}!")
    return name

