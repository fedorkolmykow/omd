
import steps


def start_story():
    step = steps.step1
    while True:
        print(step['intro'])
        if step['future'] is None:
            break
        choice = ''
        num = 0
        while choice not in step['choices']:
            print('Напишите номер выбранного варианта:')
            print('\n'.join(step['choices']))
            try:
                num = int(input())-1
                choice = step['choices'][num]
            except (ValueError, IndexError):
                choice = None
        step = step['future'][num]


if __name__ == '__main__':
    start_story()
