# Quiz Game

import random

def Data_for_quiz_game():
    Questions = [
        {"question": "What keyword we use for creating a functon: ", "choices": ["A. import", 
    "B. class", "C. def"], "answer": "C"},
        {"question": "Which one is not an integer: ", "choices": ["A. 30", "B. 40.0", "C. int"], "answer": "C"},
        {"question": "For addition we use __ sign in python.", "choices": ["A. *", "B. +", "C. -"], "answer": "B"},
        {"question": "Python is ____ sensitive.", "choices": ["A. case", "B. variable", "C. string"], "answer": "A"},
        {"question": "At which field of AI, python is very useful:", "choices": ["A. Data Modling", 
    "B. Building Electric Robots", "C. Hardware for AI use"], "answer": "A"}
    ]
    return Questions

def showing_question(Question):
    print(Question["question"])
    for choice in Question["choices"]:
        print(choice)
    user_answer = input("Your answer: ")
    return user_answer.upper()

def checking_answer(user_answer,answer):
    return user_answer == answer

def display_feedback(is_correct,answer):
    if is_correct:
        print("Correct!\n")
    else:
        print("Incorrect. The correct answer is: {}\n".format(answer))

def quiz_game():
    print("Welcome to the Quiz Game!")
    print("Rules: Don't cheat\n Answer to the questions by typing the letter corresponding to your choice.")

    Questions = Data_for_quiz_game()
    random.shuffle(Questions)

    score = 0

    for Question in Questions:
        user_answer = showing_question(Question)
        is_correct = checking_answer(user_answer,Question["answer"])
        display_feedback(is_correct,Question["answer"])

        if is_correct:
            score += 1

    print("Quiz Completed!")
    print("\nYour score is {}/{}".format(score, len(Questions)))

    play_again = input("\nDo you want to play again? \n Yes/No:")
    if play_again.upper() == "Yes":
        quiz_game()
    else:
        print("Thanks for playing\n")

quiz_game()
