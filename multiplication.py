import argparse
from random import randint, shuffle


def _get_n_digit_integer(digits):
    min_value = 10 ** (digits - 1)
    max_value = 10 ** digits - 1
    return randint(min_value, max_value)


def _generate_exercises(args):
    results = []  # store results in the format as e.g. [{"question": "213 x 15 = __________", "answer": 3195}, ...]

    for i in range(args["questions_per_topic"]):
        # 2-digits * 1-digit
        a = _get_n_digit_integer(2)
        b = _get_n_digit_integer(1)
        ans = a * b
        results.append({"question": f"{a} x {b} = __________",
                        "answer": ans})
        # 2-digits * 2-digits
        a = _get_n_digit_integer(2)
        b = _get_n_digit_integer(2)
        ans = a * b
        results.append({"question": f"{a} x {b} = __________",
                        "answer": ans})
        # 3-digits * 2-digits
        a = _get_n_digit_integer(3)
        b = _get_n_digit_integer(2)
        ans = a * b
        results.append({"question": f"{a} x {b} = __________",
                        "answer": ans})
        # 2-digits * 1-digits * 2-digit
        a = _get_n_digit_integer(2)
        b = _get_n_digit_integer(1)
        c = _get_n_digit_integer(2)
        ans = a * b * c
        results.append({"question": f"{a} x {b} x {c} = __________",
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
    parser = argparse.ArgumentParser(description="Generator of arithmetic exercises: multiplication")
    parser.add_argument("questions_file", help="output exercise questions file path, e.g. ./questions.txt")
    parser.add_argument("answers_file", help="output exercise answers file path, e.g. ./answers.txt")
    parser.add_argument("--questions_per_topic", type=int, default=2, help="number of questions per topic, default is 2")
    return parser


if __name__ == "__main__":
    parser = _get_parser()
    args = vars(parser.parse_args())
    
    _generate_exercises(args)