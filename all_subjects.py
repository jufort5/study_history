# Open the files for reading and writing
with open('subjects.txt', 'r') as a_file, open('all_subjects.txt', 'r+') as b_file:
    # Read the lines of b.txt and add them to a set
    existing_words = set()
    for line in b_file:
        #print(line)
        existing_words.add(line.strip())

    print (existing_words)
    # Loop through each line in a.txt
    for line in a_file:

        #print(line)
        # Get rid of any newline characters
        word = line.strip()

        # Check if the word already exists in b.txt
        if word not in existing_words:
            # Write the word to b.txt if it doesn't exist
            b_file.write(word + '\n')
            existing_words.add(word)