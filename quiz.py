questions = [
    {
        "question": "What is the capital of India?",
        "options": ["A. Mumbai", "B. Delhi", "C. Pune", "D. Chennai"],
        "answer": "B"
    },
    {
        "question": "Which language is used in Python programming?",
        "options": ["A. English", "B. Hindi", "C. Python", "D. Java"],
        "answer": "C"
    },
    {
        "question": "2 + 2 = ?",
        "options": ["A. 3", "B. 4", "C. 5", "D. 6"],
        "answer": "B"
    }
]

score = 0

print("===== QUIZ APPLICATION =====\n")

for q in questions:
    print(q["question"])

    for option in q["options"]:
        print(option)

    user_answer = input("Enter your answer (A/B/C/D): ").upper()

    if user_answer == q["answer"]:
        print("Correct Answer!\n")
        score += 1
    else:
        print("Wrong Answer!\n")

print("===== QUIZ COMPLETED =====")
print("Your Final Score is:", score, "/", len(questions))