from quiz_questions import *
import random

def class_result_function(questions):
    results = []

    return results

def grouping_function():

    group_answer = ''
    totally_seperate_group_answer = ''
    while not(group_answer == 'AA' or group_answer == 'AB' or group_answer == 'BA' or group_answer == 'BB'):

        group_answer = str(input(first_group_questions).upper())
        if not (group_answer == 'A' or group_answer == 'B'):
            print('Invalid input, please try again:\n')
            continue


        while not(totally_seperate_group_answer == 'A' or totally_seperate_group_answer == 'B'):

            totally_seperate_group_answer = str(input(second_group_questions).upper())
            if not(totally_seperate_group_answer == 'A' or totally_seperate_group_answer == 'B'):
                print('Invalid input, please try again:\n')

        group_answer += totally_seperate_group_answer

    return group_answer

def roll_stats():
    roll_character = str(input('Would you like for me to roll stats for you using 4d6 dropping the lowest roll? (Y / N)').upper())
    while not(roll_character == 'Y' or roll_character == 'N'):
        print('Invalid input, please try again:\n')
        roll_character = str(input('Would you like for me to roll stats for you using 4d6 dropping the lowest roll? (Y / N)').upper())

    if (roll_character == 'Y'):
        for x in range(6):
            roll_1 = random.randint(1,6)
            roll_2 = random.randint(1,6)
            roll_3 = random.randint(1,6)
            roll_4 = random.randint(1,6)

            rolls = [roll_1, roll_2, roll_3, roll_4]
            smallest = min(rolls)
            rolls.remove(smallest)

            print(sum(rolls))