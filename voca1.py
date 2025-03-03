import random

# Vocabulary list with Korean translations
vocabulary = {
    'Honored': '영광인',
    'Commencement': '졸업식',
    'Drop out': '중퇴하다',
    'Adopted': '입양된',
    'Relented': '양보하다',
    'Stumbled into': '우연히 만나다',
    'Curiosity': '호기심',
    'Subtle': '미묘한',
    'Serif': '세리프 (서체)',
    'Trust': '신뢰하다'
}


# Matching exercise
def matching_exercise():
    print("\n--- Matching Exercise ---")
    english_words = list(vocabulary.keys())
    korean_words = list(vocabulary.values())
    random.shuffle(korean_words)

    for i, word in enumerate(english_words):
        print(f"{i + 1}. {word} : ___________")

    print("\nMatch the correct Korean translation to each English word:")
    for i, word in enumerate(english_words):
        answer = input(f"{word}: ")
        correct_answer = vocabulary[word]

        if answer.strip() == correct_answer:
            print("Correct!\n")
        else:
            print(f"Incorrect! The correct answer is: {correct_answer}\n")


# Fill-in-the-blank exercise
def fill_in_the_blank():
    print("\n--- Fill-in-the-Blank Exercise ---")

    sentences = [
        ("After much persuasion, my mother finally __________ and agreed to sign the papers.", 'Relented'),
        ("I could never have imagined that learning about __________ would be so important later on.", 'Typography'),
        ("He __________ college after just one semester because he didn’t see the point of staying.", 'Dropped out'),
        ("His __________ in believing that everything would work out was one of his greatest strengths.", 'Trust'),
        ("The artwork on the flyer was so __________ that it caught everyone's attention.", 'Subtle')
    ]

    random.shuffle(sentences)

    for sentence, correct_answer in sentences:
        print(sentence)
        answer = input("Fill in the blank: ")
        if answer.strip().lower() == correct_answer.lower():
            print("Correct!\n")
        else:
            print(f"Incorrect! The correct answer is: {correct_answer}\n")


# Multiple choice exercise
def multiple_choice():
    print("\n--- Multiple Choice Exercise ---")

    questions = [
        ("What does 'Serif' refer to?",
         ['a) A type of food', 'b) A style of font', 'c) A place of study', 'd) A philosophical concept'], 'b'),
        ("What does 'Curiosity' mean?",
         ['a) Being afraid of new things', 'b) A strong desire to learn or know something', 'c) A plan for the future',
          'd) A sudden change in behavior'], 'b'),
        ("What is the meaning of 'Relented'?",
         ['a) To resist something', 'b) To agree after initial refusal', 'c) To create something new',
          'd) To feel regret'], 'b')
    ]

    random.shuffle(questions)

    for question, options, correct_answer in questions:
        print(question)
        for option in options:
            print(option)
        answer = input("Choose the correct option (a, b, c, or d): ")
        if answer.strip().lower() == correct_answer.lower():
            print("Correct!\n")
        else:
            print(f"Incorrect! The correct answer is: {correct_answer}\n")


# Main function to run the program
def main():
    print("Welcome to the Vocabulary Practice Program!\n")
    while True:
        print("Choose an exercise:")
        print("1. Matching Exercise")
        print("2. Fill-in-the-Blank Exercise")
        print("3. Multiple Choice Exercise")
        print("4. Exit\n")

        choice = input("Enter the number of your choice: ")

        if choice == '1':
            matching_exercise()
        elif choice == '2':
            fill_in_the_blank()
        elif choice == '3':
            multiple_choice()
        elif choice == '4':
            print("Goodbye! Keep learning!")
            break
        else:
            print("Invalid choice! Please choose again.\n")


# Run the program
if __name__ == "__main__":
    main()





