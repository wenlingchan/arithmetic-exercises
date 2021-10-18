import random
from random import randint

QUESTIONS_PER_TOPIC = 3
questions = []

for _ in range(QUESTIONS_PER_TOPIC):
    # 2-digits / 1-digit
    first = randint(10, 99)
    second = randint(2, 9)
    ans1 = first // second
    ans2 = first % second
    questions.append({"question": f"{first} / {second} = __________",
                      "answer": (str(ans1), str(ans2))})
    # 2-digits / 2-digits
    first = randint(60, 99)
    second = randint(10, 30)
    ans1 = first // second
    ans2 = first % second
    questions.append({"question": f"{first} / {second} = __________",
                      "answer": (str(ans1), str(ans2))})
    # 3-digits / 1-digits
    first = randint(100, 999)
    second = randint(2, 9)
    ans1 = first // second
    ans2 = first % second
    questions.append({"question": f"{first} / {second} = __________",
                      "answer": (str(ans1), str(ans2))})
    # 3-digits / 2-digits
    for _ in range(2):
        first = randint(100, 999)
        second = randint(10, 99)
        ans1 = first // second
        ans2 = first % second
        questions.append({"question": f"{first} / {second} = __________",
                          "answer": (str(ans1), str(ans2))})

random.shuffle(questions)

for i, question in enumerate(questions):
    q = question["question"]
    print(f"{i + 1}.  {q}\n\n")

for i, question in enumerate(questions):
    a = question["answer"]
    print(f"{i + 1}.  {a[0]}...{a[1]}")