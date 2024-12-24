from brain_games.cli import welcome_user
from brain_games.games.brain_calc import play_game


def main():
    welcome_user()
    play_game()


if __name__ == '__main__':
    main()
