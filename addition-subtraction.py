import argparse
from random import randint, shuffle


def _generate_exercises(args):
    min_value = 1
    max_value = 10 ** args["digits"] - 1

    results = []  # store results in the format as e.g. [{"question": "2345 + 345 + 4129 = __________", "answer": 6819}, ...]

    for i in range(args["questions_per_topic"]):
        # Generate exercise "a + b + c = ans"
        a = randint(min_value, max_value)
        b = randint(min_value, max_value - a)
        c = randint(min_value, max_value - (a + b))
        ans = a + b + c
        results.append({"question": f"{a} + {b} + {c} = __________",
                        "answer": ans})

        # Generate exercise "a - b - c = ans"
        a = randint(min_value, max_value)
        b = randint(min_value, a)
        c = randint(min_value, a - b)
        ans = a - b - c
        results.append({"question": f"{a} - {b} - {c} = __________",
                        "answer": ans})

        # Generate exercise "a + b - c = ans"
        a = randint(min_value, max_value)
        b = randint(min_value, max_value - a)
        c = randint(min_value, a + b)
        ans = a + b - c
        results.append({"question": f"{a} + {b} - {c} = __________",
                        "answer": ans})

        # Generate exercise "a - b + c = ans" and b < a
        a = randint(min_value, max_value)
        b = randint(min_value, a)
        c = randint(min_value, max_value - (a - b))
        ans = a - b + c
        results.append({"question": f"{a} - {b} + {c} = __________",
                        "answer": ans})

        # Generate exercise "a - b + c = ans" and b > a
        a = randint(min_value, max_value)
        b = randint(a, max_value)
        c = randint(min_value + b - a, max_value)
        ans = a - b + c
        results.append({"question": f"{a} - {b} + {c} = __________",
                        "answer": ans})

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
            f.write(f"{i + 1}.  {answer}\n")


def _get_parser():
    parser = argparse.ArgumentParser(description="Generator of arithmetic exercises: addition & subtraction")
    parser.add_argument("questions_file", help="output exercise questions file path, e.g. ./questions.txt")
    parser.add_argument("answers_file", help="output exercise answers file path, e.g. ./answers.txt")
    parser.add_argument("--digits", type=int, default=4, help="maximum number of digits of all numbers in questions and answers, default is 4")
    parser.add_argument("--questions_per_topic", type=int, default=2, help="number of questions per topic, default is 2")
    return parser


if __name__ == "__main__":
    parser = _get_parser()
    args = vars(parser.parse_args())
    
    _generate_exercises(args)