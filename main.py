import csv
from quiz_functions import *
from quiz_questions import *
from collections import Counter as ctr
import matplotlib.pyplot as plt

print("="*50)
print("WELCOME TO THE D&D CLASS QUIZ!")
print("="*50)


input_file = 'total_results.csv'
first_column = []
int_second_column = []
total_results = []

# Get user group
user_group = grouping_function()

# Choose questions based on group
if user_group == 'AA':
    chosen_questions = physical_melee_questions
elif user_group == 'BA':
    chosen_questions = physical_range_questions
elif user_group == 'AB':
    chosen_questions = magical_melee_questions
else:
    chosen_questions = magical_range_questions

# Run quiz and get class results
class_results = class_result_function(chosen_questions)
class_tally = ctr(class_results)

# Finds most common class answered
most_common_classes = class_tally.most_common(2)

# Check if top two have same score (tie)
if len(most_common_classes) > 1 and most_common_classes[0][1] == most_common_classes[1][1]:
    most_common = 'Bard'  # fallback default for tie
else:
    most_common = most_common_classes[0][0]

# Prints the result of the quiz!
print("\n" + "="*50)
print(f"Congratulations! You are most likely a: {most_common}!")
print("="*50 + "\n")

# Read and update CSV
with open(input_file, mode='r', newline='') as infile:
    reader = csv.reader(infile)
    header = next(reader)
    reader_array = list(reader)

    for row in reader_array:
        if row[0] == most_common:
            row[1] = str(int(row[1]) + 1)
        total_results.append(row)
        first_column.append(row[0])
        int_second_column.append(int(row[1]))

# Write updated results into csv
with open(input_file, mode='w', newline='') as outfile:
    writer = csv.writer(outfile)
    writer.writerow(header)
    writer.writerows(total_results)

# Roll stats if requested
roll_stats()

# Ask if user wants graph
graph_results = input("\nShow total results graph? (Y/N):\n").strip().upper()
while graph_results not in ['Y', 'N']:
    print('Invalid input, please try again.\n')
    graph_results = input("\nShow total results graph? (Y/N):\n").strip().upper()

# Plot if requested
if graph_results == 'Y':
    print("Graphing...")

    plt.figure(figsize=(10, 6))
    plt.bar(first_column, int_second_column)
    plt.title('Total Class Results')
    plt.xlabel('Class')
    plt.ylabel('# of Results')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig("quiz_results.png")

    time.sleep(1)
    print("Done!\n")
    print("Graph saved as 'quiz_results.png'.\n")

print("\n" + "="*50)
print("Thanks for playing! May your rolls be ever in your favor.")
print("="*50 + "\n")
