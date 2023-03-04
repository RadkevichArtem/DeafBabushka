import random
import re


def random_year():
    return random.randint(1930, 1950)


answers = {'hello': 'ЧЕГО СКАЗАТЬ - ТО ХОТЕЛ, МИЛОК?!',
           'what': 'АСЬ?! ГОВОРИ ГРОМЧЕ, ВНУЧЕК!',
           'never_since': f'НЕТ, НИ РАЗУ С {random_year()} ГОДА!',
           'bye': 'ДО СВИДАНИЯ, МИЛЫЙ!'}


def run_conversation(n_goodbye=3):
    flag = 0
    pattern = re.compile(r"^ПОКА!+$")
    print(answers['hello'])

    while flag < n_goodbye:
        question = input('> ').strip()
        if pattern.match(question):
            flag += 1
            if flag < n_goodbye:
                print(answers['never_since'])
        elif question.isupper():
            print(answers['never_since'])
        else:
            print(answers['what'])
    print(answers['bye'])


if __name__ == "__main__":
    run_conversation()
