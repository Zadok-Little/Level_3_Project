from quiz_questions import *
import random
import time

def class_result_function(questions):
    results = []

    for x in questions:
        print(f"\n{x['question']}")
        for key, value in x['options'].items():
            print(f'    {key}: {value}')
        time.sleep(0.5)  

        answer_check = True
        while answer_check:
            answer = input().strip().upper()
            if answer in x['options']:
                answer_check = False
            else:
                print('Invalid input, please try again:\n')
                time.sleep(0.5)

        class_result = x['class_map'][answer]
        results.append(class_result)

    return results



def grouping_function():
    group_answer = ''
    totally_seperate_group_answer = ''

    while group_answer not in ['AA', 'AB', 'BA', 'BB']:
        print(first_group_questions)
        first_input = input().strip().upper()

        if first_input not in ['A', 'B']:
            print('Invalid input, please try again:\n')
            continue

        while totally_seperate_group_answer not in ['A', 'B']:
            print(second_group_questions)
            second_input = input().strip().upper()

            if second_input not in ['A', 'B']:
                print('Invalid input, please try again:\n')
            else:
                totally_seperate_group_answer = second_input

        group_answer = first_input + totally_seperate_group_answer
        time.sleep(0.5)

    return group_answer


def roll_stats():
    print('Would you like for me to roll stats for you using 4d6 dropping the lowest roll? (Y/N):')
    roll_character = input().strip().upper()

    while not(roll_character == 'Y' or roll_character == 'N'):
        print('Invalid input, please try again:\n')
        print('Would you like for me to roll stats for you using 4d6 dropping the lowest roll? (Y/N):')
        roll_character = input().strip().upper()

    if (roll_character == 'Y'):

        print("Calculating your stats...")
        time.sleep(1)
        print("Done!\n")
        print("Your rolled stats:\n")

        for x in range(6):
            roll_1 = random.randint(1,6)
            roll_2 = random.randint(1,6)
            roll_3 = random.randint(1,6)
            roll_4 = random.randint(1,6)

            rolls = [roll_1, roll_2, roll_3, roll_4]
            smallest = min(rolls)
            rolls.remove(smallest)

            print(sum(rolls))