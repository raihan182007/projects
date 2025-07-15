questions = [
        "Which is the longest river in the world?",
        "Who wrote the play 'Romeo and Juliet'?",
        "Which planet is known as the Red Planet?",
        "What is the smallest prime number?",
        "Who was the first person to walk on the Moon?",
        "What is the capital of Australia?",
        "In which year did World War II end?",
        "Which gas is most abundant in the Earth's atmosphere?",
        "Who painted the Mona Lisa?",
        "Which metal is liquid at room temperature?",
        "Which country is known as the Land of the Rising Sun?",
        "Which ocean is the largest?",
        "What is the hardest natural substance on Earth?",
        "Who is known as the father of computers?",
        "Which language has the most native speakers?"
    ]
answers = [
        "Nile",
        "William Shakespeare",
        "Mars",
        "2",
        "Neil Armstrong",
        "Canberra",
        "1945",
        "Nitrogen",
        "Leonardo da Vinci",
        "Mercury",
        "Japan",
        "Pacific Ocean",
        "Diamond",
        "Charles Babbage",
        "Mandarin Chinese"
    ]

def quiz():
    print("---- Welcome to the quiz game ----")
    print("-- Check your general knowlwdge --")
    m = len(questions)
    print(f"       Total question: {m}         ")

    score = 0
    currect_ans_question = []
    currect_ans = []
    wrong_ans_question = []
    wrong_ans = []

    n = len(questions)

    for i in range(n):
        question = questions[i]
        print(f"Question {i+1}: {question}")
        answer = input("Answer: ").lower()

        if answer == answers[i].lower():
            score += 1
            currect_ans_question.append(questions[i])
            currect_ans.append(answers[i])
        else:
            wrong_ans_question.append(questions[i])
            wrong_ans.append(answers[i])

    if score <= 5:
        gk_k = "Bad👎"
    elif score <= 10:
        gk_k = "Average👍"
    elif score <= 12:
        gk_k = "Good✅"
    else:
        gk_k = "Excellent🔥"

    print(f"Your total score is: {score}.")
    print(f"Wrong answer: {len(questions)-score}")
    print(f"Your currect percentage is: {(score/15)*100}%.")
    print(f"Your generan knowledge is {gk_k}.")

    input_1 = input("\nEnter yes to see all result: ").lower()

    if input_1 == "yes":
        print("Right answer:")
        for i in range(len(currect_ans_question)):
            print(f"Q{i+1}: {currect_ans_question[i]}")
            print(f"Answer: {currect_ans[i]}")

        print("\nWrong answer:")
        for i in range(len(wrong_ans_question)):
            print(f"Q{i+1}: {wrong_ans_question[i]}")
            print(f"Answer: {wrong_ans[i]}")           
    else:
        pass

    print("\nThank you for participating in the quiz game.👏")
    


def main():
    user_choice = input("Do you want to play the quiz game? [yes/no]: ").lower()
    if user_choice == "yes":
        quiz()
    elif user_choice == "no":
        print("No problem..Hope you will participate next!👋")
    else:
        print("Invalid input.You are out of the game.")

main()