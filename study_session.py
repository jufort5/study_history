import time

# read subjects from subjects.txt file
with open('subjects.txt', 'r') as f:
    subjects = [line.strip() for line in f.readlines()]

# print numbered list of subjects
print("Choose a subject to study:")
for i, subject in enumerate(subjects):
    print(f"{i+1}. {subject}")

# prompt user for subject number
while True:
    try:
        subject_num = int(input("Enter the number of the subject you wish to study: "))
        if subject_num < 1 or subject_num > len(subjects):
            raise ValueError
        break
    except ValueError:
        print("Invalid input. Please enter a valid subject number.")

# record start time
start_time = time.time()
print(f"You are now studying {subjects[subject_num-1]}.")

# wait for user to finish studying
input("Press Enter when you are finished studying.")

# record end time and calculate elapsed time
end_time = time.time()
elapsed_time = end_time - start_time

# print elapsed time
print(f"You studied {subjects[subject_num-1]} for {elapsed_time:.2f} seconds.")

# write study history to file
with open('study_history.txt', 'a') as f:
    f.write(f"{time.strftime('%Y-%m-%d %H:%M:%S')},{subjects[subject_num-1]},{elapsed_time:.2f}\n")
