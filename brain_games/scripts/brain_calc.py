from brain_games.games.brain_calc import play_game
from brain_games.cli import welcome_user


def main():
    name = welcome_user()
    play_game(name)


if __name__ == '__main__':
    main()
