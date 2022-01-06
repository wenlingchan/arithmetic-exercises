import argparse
import math
import random


def _generate_exercises(args):
    largest_number = args["largest_number"]
    largest_factor = math.floor(largest_number ** 0.5)

    # Exhaustive analyze all numbers <= largest_number
    numbers_1_or_2_factors = []  # store all numbers with 1 or 2 factors, e.g. [{"number": 7, "factors": [1, 7]}, ...]
    numbers_3_or_4_factors = []
    numbers_5_or_6_factors = []
    numbers_7_or_8_factors = []
    numbers_ge_9_factors = []

    for number in range(1, largest_number + 1):
        factors = set()
        for factor1 in range(1, largest_factor + 1):
            if number % factor1 == 0:
                # factor1 is a factor
                factor2 = number // factor1
                factors = factors.union({factor1, factor2})
        
        factors = sorted(factors)
        len_factors = len(factors)

        if len_factors <= 2:
            numbers_1_or_2_factors.append({"number": number, "factors": factors})
        elif len_factors <= 4:
            numbers_3_or_4_factors.append({"number": number, "factors": factors})
        elif len_factors <= 6:
            numbers_5_or_6_factors.append({"number": number, "factors": factors})
        elif len_factors <= 8:
            numbers_7_or_8_factors.append({"number": number, "factors": factors})
        else:
            numbers_ge_9_factors.append({"number": number, "factors": factors})

    # Randomly pick numbers from the exhaustive list
    results = random.choices(numbers_1_or_2_factors, k=args["questions_per_topic"])
    results += random.choices(numbers_3_or_4_factors, k=args["questions_per_topic"])
    results += random.choices(numbers_5_or_6_factors, k=args["questions_per_topic"])
    results += random.choices(numbers_7_or_8_factors, k=args["questions_per_topic"])
    results += random.choices(numbers_ge_9_factors, k=args["questions_per_topic"])

    random.shuffle(results)

    # Write questions file
    with open(args["questions_file"], "w") as f:
        f.write("Questions:\n\n")
        for i, result in enumerate(results):
            number = result["number"]
            f.write(f"{i + 1}.  Find all factors of {number}: _______________________________________________\n")

    # Write answers file
    with open(args["answers_file"], "w") as f:
        f.write("Answers:\n\n")
        for i, result in enumerate(results):
            factors = result["factors"]
            f.write(f"{i + 1}.  {factors}\n")


def _get_parser():
    parser = argparse.ArgumentParser(description="Generator of arithmetic exercises: factorization")
    parser.add_argument("questions_file", help="output exercise questions file path, e.g. ./questions.txt")
    parser.add_argument("answers_file", help="output exercise answers file path, e.g. ./answers.txt")
    parser.add_argument("--largest_number", type=int, default=400, help="largest number to be factorized, default is 400")
    parser.add_argument("--questions_per_topic", type=int, default=2, help="number of questions per topic, default is 2")
    return parser


if __name__ == "__main__":
    parser = _get_parser()
    args = vars(parser.parse_args())
    
    _generate_exercises(args)