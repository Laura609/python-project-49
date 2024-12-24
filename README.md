# Brain Games

![Maintainability](https://api.codeclimate.com/v1/badges/58fe0208f7f25471a0f7/maintainability)
![CI](https://github.com/Laura609/python-project-49/workflows/Hexlet%20CI/badge.svg)

Добро пожаловать в проект **Brain Games**! Это набор логических игр для тренировки вашего мышления. Каждая игра ставит перед вами задачу, и ваша цель — ответить на вопросы как можно быстрее и правильнее.

## Установка и запуск

Для установки и запуска игры на вашем компьютере выполните следующие шаги:

1. Клонируйте репозиторий:

    ```bash
    git clone https://github.com/Laura609/python-project-49.git
    ```

2. Перейдите в директорию проекта:

    ```bash
    cd python-project-49
    ```

3. Установите зависимости с помощью Poetry:

    ```bash
    poetry install
    ```

4. Войдите в виртуальное окружение:

    ```bash
    poetry shell
    ```

5. Вы можете запускать любую игру, используя соответствующие команды:

    - Для игры «Проверка на чётность» — `brain-even`
    - Для игры «Наибольший общий делитель» — `brain-gcd`
    - Для игры «Калькулятор» — `brain-calc`
    - Для игры «Арифметическая прогрессия» — `brain-progression`
    - Для игры «Простое ли число?» — `brain-prime`

---

## Игра "Проверка на чётность"

В этой игре вам нужно будет отвечать **"yes"**, если число чётное, и **"no"**, если число нечётное.

### Запуск игры

Для запуска игры «Проверка на чётность» используйте команду:

```bash
brain-even


Welcome to the Brain Games!
May I have your name? Sam
Hello, Sam!
Answer "yes" if the number is even, otherwise answer "no".
Question: 15
Your answer: no
Correct!

Question: 6
Your answer: yes
Correct!

Question: 7
Your answer: no
Correct!
Congratulations, Sam!
```
Что происходит при неверном ответе:
```bash
Question: 15
Your answer: yes
'yes' is wrong answer ;(. Correct answer was 'no'.
Let's try again, Sam!
```
## Игра "Наибольший общий делитель (НОД)"
В этой игре вам нужно будет вычислить наибольший общий делитель двух чисел.

### Запуск игры
Для запуска игры «Наибольший общий делитель» используйте команду:
```bash
brain-gcd
```
Пример игры:
```bash
Welcome to the Brain Games!
May I have your name? Sam
Hello, Sam!
Find the greatest common divisor of given numbers.
Question: 25 50
Your answer: 25
Correct!

Question: 100 52
Your answer: 4
Correct!

Question: 3 9
Your answer: 3
Correct!
Congratulations, Sam!
```
Что происходит при неверном ответе:
```bash
Question: 25 50
Your answer: 1
'1' is wrong answer ;(. Correct answer was '25'.
Let's try again, Sam!
```
## Игра "Калькулятор"
В этой игре вам нужно будет решать простые математические выражения (сложение, вычитание, умножение).

## Запуск игры
Для запуска игры «Калькулятор» используйте команду:
```bash
brain-calc
```
Пример игры:
```bash
Welcome to the Brain Games!
May I have your name? Sam
Hello, Sam!
What is the result of the expression?
Question: 4 + 10
Your answer: 14
Correct!

Question: 25 - 11
Your answer: 14
Correct!

Question: 25 * 7
Your answer: 175
Correct!
Congratulations, Sam!
```
Что происходит при неверном ответе:
```bash
Question: 25 * 7
Your answer: 145
'145' is wrong answer ;(. Correct answer was '175'.
Let's try again, Sam!
```
## Игра "Арифметическая прогрессия"
В этой игре вам нужно будет находить пропущенные числа в арифметической прогрессии.

### Запуск игры
Для запуска игры «Арифметическая прогрессия» используйте команду:
```bash
brain-progression
```
Пример игры:
```bash
Welcome to the Brain Games!
May I have your name? Sam
Hello, Sam!
What number is missing in the progression?
Question: 5 7 9 11 13 .. 17 19 21 23
Your answer: 15
Correct!

Question: 2 5 8 .. 14 17 20 23 26 29
Your answer: 11
Correct!

Question: 14 19 24 29 34 39 44 49 54 ..
Your answer: 59
Correct!
Congratulations, Sam!
```
Что происходит при неверном ответе:
```bash
Question: 5 7 9 11 13 .. 17 19 21 23
Your answer: 1
'1' is wrong answer ;(. Correct answer was '15'.
Let's try again, Sam!
```
## Игра "Простое ли число?"
В этой игре вам нужно будет определить, является ли число простым.

### Запуск игры
Для запуска игры «Простое ли число?» используйте команду:
```bash
brain-prime
```
Пример игры:
```bash
Welcome to the Brain Games!
May I have your name? Sam
Hello, Sam!
Answer "yes" if given number is prime. Otherwise answer "no".
Question: 7
Your answer: yes
Correct!

Question: 4
Your answer: no
Correct!

Question: 11
Your answer: yes
Correct!
Congratulations, Sam!
```
Что происходит при неверном ответе:
```bash
Question: 4
Your answer: yes
'yes' is wrong answer ;(. Correct answer was 'no'.
Let's try again, Sam!
```