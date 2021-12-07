import math
import random

QUESTION_NUMBER_RANGE = (1, 400)  # inclusive
QUESTIONS_PER_TOPIC = 2

largest_factor1 = math.floor(QUESTION_NUMBER_RANGE[1] ** 0.5)

# Exhaustive analyze all numbers in QUESTION_NUMBER_RANGE
numbers_ln2_factors = []
numbers_3n4_factors = []
numbers_5n6_factors = []
numbers_7n8_factors = []
numbers_ge9_factors = []

for q_num in range(QUESTION_NUMBER_RANGE[0], QUESTION_NUMBER_RANGE[1] + 1):
    factors = set()
    for factor1 in range(1, largest_factor1 + 1):
        if q_num % factor1 == 0:
            factor2 = q_num // factor1
            factors = factors.union({factor1, factor2})
    
    len_factors = len(factors)
    if len_factors <= 2:
        numbers_ln2_factors.append({"number": q_num, "factors": sorted(factors)})
    elif len_factors <= 4:
        numbers_3n4_factors.append({"number": q_num, "factors": sorted(factors)})
    elif len_factors <= 6:
        numbers_5n6_factors.append({"number": q_num, "factors": sorted(factors)})
    elif len_factors <= 8:
        numbers_7n8_factors.append({"number": q_num, "factors": sorted(factors)})
    else:
        numbers_ge9_factors.append({"number": q_num, "factors": sorted(factors)})

# Randomly pick questions
questions = random.choices(numbers_ln2_factors, k=QUESTIONS_PER_TOPIC)
questions += random.choices(numbers_3n4_factors, k=QUESTIONS_PER_TOPIC)
questions += random.choices(numbers_5n6_factors, k=QUESTIONS_PER_TOPIC)
questions += random.choices(numbers_7n8_factors, k=QUESTIONS_PER_TOPIC)
questions += random.choices(numbers_ge9_factors, k=QUESTIONS_PER_TOPIC)

random.shuffle(questions)

# Print questions
print("List all factors.\n")
for i, question in enumerate(questions):
    number = question["number"]
    print(f"{i + 1}.  {number}  Factors: _______________________________________________\n")

# Print answers
print("\nAnswers:")
for i, question in enumerate(questions):
    factors = question["factors"]
    print(f"{i + 1}.  {factors}")
