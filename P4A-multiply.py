import random
from random import randint

QUESTIONS_PER_TOPIC = 3
questions = []

for _ in range(QUESTIONS_PER_TOPIC):
    # 2-digits * 1-digit
    first = randint(10, 99)
    second = randint(0, 9)
    ans = first * second
    questions.append({"question": f"{first} x {second} = __________",
                      "answer": str(ans)})
    # 2-digits * 2-digits
    first = randint(10, 99)
    second = randint(10, 99)
    ans = first * second
    questions.append({"question": f"{first} x {second} = __________",
                      "answer": str(ans)})
    # 3-digits * 2-digits
    first = randint(100, 999)
    second = randint(10, 99)
    ans = first * second
    questions.append({"question": f"{first} x {second} = __________",
                      "answer": str(ans)})
    # 2-digits * 1-digits * 2-digit
    first = randint(10, 99)
    second = randint(0, 9)
    third = randint(10, 99)
    ans = first * second * third
    questions.append({"question": f"{first} x {second} x {third} = __________",
                      "answer": str(ans)})

random.shuffle(questions)

for i, question in enumerate(questions):
    q = question["question"]
    print(f"{i + 1}.  {q}\n\n")

for i, question in enumerate(questions):
    a = question["answer"]
    print(f"{i + 1}. {a}")