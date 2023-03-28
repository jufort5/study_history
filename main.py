
high_score = 0

while True:
    print("Welcome to My Game!")
    print("1. Start Game")
    print("2. High Scores")
    print("3. Exit Game")

    choice = input("Enter your choice: ")

    if choice == "1":
        # Start game logic goes here
        print("Starting game...")

        study()

    elif choice == "2":
        # Display high score logic goes here
        print(f"High score: {high_score}")
    elif choice == "3":
        # Exit game
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please enter a valid number (1-3).")