import argparse
from random import randint, shuffle


def _generate_exercises(args):
    results = []  # store results in the format as e.g. [{"question": "213 / 15 = __________", "answer": (14, 3)}, ...]

    for i in range(args["questions_per_topic"]):
        # 2-digits / 1-digit
        a = randint(10, 99)
        b = randint(2, 9)
        quotient = a // b
        remainder = a % b
        results.append({"question": f"{a} / {b} = __________",
                        "answer": (quotient, remainder)})
        # 2-digits / 2-digits
        a = randint(60, 99)
        b = randint(10, 30)
        quotient = a // b
        remainder = a % b
        results.append({"question": f"{a} / {b} = __________",
                        "answer": (quotient, remainder)})
        # 3-digits / 1-digits
        a = randint(100, 999)
        b = randint(2, 9)
        quotient = a // b
        remainder = a % b
        results.append({"question": f"{a} / {b} = __________",
                        "answer": (quotient, remainder)})
        # 3-digits / 2-digits
        a = randint(100, 999)
        b = randint(10, 99)
        quotient = a // b
        remainder = a % b
        results.append({"question": f"{a} / {b} = __________",
                        "answer": (quotient, remainder)})

    shuffle(results)

    # Write questions file
    with open(args["questions_file"], "w") as f:
        f.write("Questions:\n\n")
        for i, result in enumerate(results):
            question = result["question"]
            f.write(f"{i + 1}.  {question}\n")

    # Write answers file
    with open(args["answers_file"], "w") as f:
        f.write("Answers:\n\n")
        for i, result in enumerate(results):
            answer = result["answer"]
            f.write(f"{i + 1}.  {answer[0]}...{answer[1]}\n")


def _get_parser():
    parser = argparse.ArgumentParser(description="Generator of arithmetic exercises: division")
    parser.add_argument("questions_file", help="output exercise questions file path, e.g. ./questions.txt")
    parser.add_argument("answers_file", help="output exercise answers file path, e.g. ./answers.txt")
    parser.add_argument("--questions_per_topic", type=int, default=2, help="number of questions per topic, default is 2")
    return parser


if __name__ == "__main__":
    parser = _get_parser()
    args = vars(parser.parse_args())
    
    _generate_exercises(args)