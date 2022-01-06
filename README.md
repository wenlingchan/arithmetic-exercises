# Arithmetic Exercises Generator

I wrote these Python scripts to auto generate math exercises for my primary school kids.


## Get started

* Only Python (version >=3.6) is required.
* Use GIT to pull this repository, or click Code --> Download ZIP and unzip it as a project folder ```arithmetic-exercises```.
* Open a terminal, change directory to the project folder ```arithmetic-exercises```.


## Run

There are several scripts. One script for one type of arithmetic exercise.

### Generate exercises (addition & subtraction)

Run:
```bash
python3 addition-subtraction.py ./questions.txt ./answers.txt
```
* ```./questions.txt``` and ```./answers.txt``` are output files. You may self-define the files' path and name.
* There are optional arguments. You may check with ```python3 addition-subtraction.py -h```

The output ```questions.txt``` looks like:
```
Questions:

1.  7232 - 7938 + 942 = __________
2.  9281 - 8551 + 7422 = __________
3.  1345 - 905 - 156 = __________
4.  3783 + 2828 - 3249 = __________
5.  2332 - 9920 + 9902 = __________
6.  3462 + 2210 + 695 = __________
7.  2729 + 2070 - 3725 = __________
8.  7684 - 5200 + 2352 = __________
9.  9172 + 678 + 76 = __________
10.  5918 - 1380 - 4001 = __________
```

The output ```answers.txt``` looks like:
```
Answers:

1.  236
2.  8152
3.  284
4.  3362
5.  2314
6.  6367
7.  1074
8.  4836
9.  9926
10.  537
```

### Generate exercises (multiplication)

Run:
```bash
python3 multiplication.py ./questions.txt ./answers.txt
```
* ```./questions.txt``` and ```./answers.txt``` are output files. You may self-define the files' path and name.
* There are optional arguments. You may check with ```python3 multiplication.py -h```

The output ```questions.txt``` looks like:
```
Questions:

1.  195 x 36 = __________
2.  62 x 6 x 27 = __________
3.  99 x 1 = __________
4.  89 x 46 = __________
5.  48 x 6 x 56 = __________
6.  32 x 21 = __________
7.  690 x 39 = __________
8.  24 x 3 = __________
```

The output ```answers.txt``` looks like:
```
Answers:

1.  7020
2.  10044
3.  99
4.  4094
5.  16128
6.  672
7.  26910
8.  72
```

### Generate exercises (division)

Run:
```bash
python3 division.py ./questions.txt ./answers.txt
```
* ```./questions.txt``` and ```./answers.txt``` are output files. You may self-define the files' path and name.
* There are optional arguments. You may check with ```python3 division.py -h```

The output ```questions.txt``` looks like:
```
Questions:

1.  68 / 23 = __________
2.  530 / 2 = __________
3.  53 / 5 = __________
4.  728 / 9 = __________
5.  172 / 99 = __________
6.  387 / 95 = __________
7.  98 / 10 = __________
8.  78 / 5 = __________
```

The output ```answers.txt``` looks like:
```
Answers:

1.  2...22
2.  265...0
3.  10...3
4.  80...8
5.  1...73
6.  4...7
7.  9...8
8.  15...3
```

### Generate exercises (factorization)

Run:
```bash
python3 factorization.py ./questions.txt ./answers.txt
```
* ```./questions.txt``` and ```./answers.txt``` are output files. You may self-define the files' path and name.
* There are optional arguments. You may check with ```python3 factorization.py -h```

The output ```questions.txt``` looks like:
```
Questions:

1.  Find all factors of 14: _______________________________________________
2.  Find all factors of 127: _______________________________________________
3.  Find all factors of 297: _______________________________________________
4.  Find all factors of 38: _______________________________________________
5.  Find all factors of 76: _______________________________________________
6.  Find all factors of 342: _______________________________________________
7.  Find all factors of 110: _______________________________________________
8.  Find all factors of 148: _______________________________________________
9.  Find all factors of 84: _______________________________________________
10.  Find all factors of 71: _______________________________________________
```

The output ```answers.txt``` looks like:
```
Answers:

1.  [1, 2, 7, 14]
2.  [1, 127]
3.  [1, 3, 9, 11, 27, 33, 99, 297]
4.  [1, 2, 19, 38]
5.  [1, 2, 4, 19, 38, 76]
6.  [1, 2, 3, 6, 9, 18, 19, 38, 57, 114, 171, 342]
7.  [1, 2, 5, 10, 11, 22, 55, 110]
8.  [1, 2, 4, 37, 74, 148]
9.  [1, 2, 3, 4, 6, 7, 12, 14, 21, 28, 42, 84]
10.  [1, 71]
```