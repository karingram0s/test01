#### This repo contains my solution to the problem below. It is written in Python. 

Files:

- `README.md`  - this readme
- `test.py`    - the solution
- `input.in`   - sample input
- `output.out` - result of running `test.py` given `input.in`



Some people have been studying the following problem: given two numbers, `A` and `B`, how many numbers from `A` to `B`, inclusive, 
are divisible by another number `K`. For example, if `A` is `1`, `B` is `10`, and `K` is `3`, then there are `3` numbers that satisfy this: `3`, `6`, and `9`. Help them by programming a solution to this problem!

Input:

The first line is the number of test cases `T`. Each test case has three numbers `A`, `B`, `K`, each on their own line given in that order.

Output:

For each test case, output one line of the form `Case C: X`, where `C` is the case number (starting from `1`), 
and `X` is the number of integers between `A` and `B`, inclusive, that are divisible by `K`.

Constraints:

```
1 ≤ T ≤ 100
1 ≤ A ≤ B < 10000
1 ≤ K < 10000
```

Sample Input:

```
2
1
10
3
8
20
4
```

Sample Output:

```
Case 1: 3
Case 2: 4
```
