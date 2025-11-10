def solve(W1: str, W2: str) -> str:
    """
    Return the string containing the word you should say

    W1: the second-to-last word said
    W2: the last word said
    """

    # YOUR CODE HERE
    def convert(n):
        if n % 15 == 0:
            return "bizzfuzz"
        if n % 3 == 0:
            return "bizz"
        if n % 5 == 0:
            return "fuzz"
        return str(n)

    possible = []
    if W1.isdigit():
        possible = [int(W1)]
    elif W1 == "bizz":
        possible = [i for i in range(3, 101, 3) if i % 5 != 0]
    elif W1 == "fuzz":
        possible = [i for i in range(5, 101, 5) if i % 3 != 0]
    elif W1 == "bizzfuzz":
        possible = [i for i in range(15, 101, 15)]

    answers = set()
    for n in possible:
        if convert(n + 1) == W2:
            answers.add(convert(n + 2))

    if len(answers) == 1:
        return list(answers)[0]
    else:
        return "crap"


def main():
    T = int(input())
    for _ in range(T):
        W1 = input()
        W2 = input()
        print(solve(W1, W2))


if __name__ == "__main__":
    main()
