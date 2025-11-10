def solve(S: str, K: int) -> int:
    """
    Return the score of S amplified K times

    S: string to amplify
    K: integer for number of times to amplify
    """

    # YOUR CODE HERE
    def char_score(c):
        if "a" <= c <= "z":
            return ord(c) - ord("a") + 1
        else:
            return ord(c) - ord("A") + 27

    letters = list(S)
    for _ in range(K):
        new_letters = []
        for c in letters:
            if c.islower():
                new_letters.append(c.upper())
            else:
                new_letters.append(c)
                new_letters.append(c.lower())
        letters = new_letters

    total = 0
    for c in letters:
        total += char_score(c)
    return total


def main():
    T = int(input())
    for _ in range(T):
        temp = input().split()
        S, K = temp[0], int(temp[1])
        print(solve(S, K))


if __name__ == "__main__":
    main()
