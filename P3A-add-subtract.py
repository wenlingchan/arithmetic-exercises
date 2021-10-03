import random
from random import randint


questions = []

# + +
for i in range(2):
    first = randint(10, 10000)
    second = randint(10, 10000 - first)
    third = randint(10, 10000 - (first + second))
    ans = first + second + third
    questions.append({"question": f"{first} + {second} + {third} = __________",
                      "answer": str(ans)})

# - -
for i in range(2):
    first = randint(10, 10000)
    second = randint(10, first)
    third = randint(10, first - second)
    ans = first - second - third
    questions.append({"question": f"{first} - {second} - {third} = __________",
                      "answer": str(ans)})

# + -
for i in range(2):
    first = randint(10, 10000)
    second = randint(10, 10000 - first)
    third = randint(10, first + second)
    ans = first + second - third
    questions.append({"question": f"{first} + {second} - {third} = __________",
                      "answer": str(ans)})

# - + (second < first)
for i in range(2):
    first = randint(10, 10000)
    second = randint(10, first)
    third = randint(10, 10000 - (first - second))
    ans = first - second + third
    questions.append({"question": f"{first} - {second} + {third} = __________",
                      "answer": str(ans)})

# - + (second > first)
for i in range(2):
    first = randint(10, 10000)
    second = randint(first, 10000)
    third = randint(10 + second - first, 10000)
    ans = first - second + third
    questions.append({"question": f"{first} - {second} + {third} = __________",
                      "answer": str(ans)})

random.shuffle(questions)

for i, question in enumerate(questions):
    q = question["question"]
    print(f"{i + 1}.  {q}\n\n")

for i, question in enumerate(questions):
    a = question["answer"]
    print(f"{i + 1}. {a}")