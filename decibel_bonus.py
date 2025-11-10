def solve(S: str, K: int) -> int:
    """
    Return the score of S amplified K times

    S: string to amplify
    K: integer for number of times to amplify
    """

    # YOUR CODE HERE
    MOD = 998244353

    def char_score(c):
        if "a" <= c <= "z":
            return ord(c) - ord("a") + 1
        return ord(c) - ord("A") + 27

    counts = {}
    for c in S:
        is_upper = c.isupper()
        counts[(is_upper, c)] = counts.get((is_upper, c), 0) + 1

    for _ in range(K):
        new_counts = {}
        for (is_upper, c), cnt in counts.items():
            if not is_upper:
                new_counts[(True, c.upper())] = (
                    new_counts.get((True, c.upper()), 0) + cnt
                ) % MOD
            else:
                new_counts[(True, c)] = (new_counts.get((True, c), 0) + cnt) % MOD
                new_counts[(False, c.lower())] = (
                    new_counts.get((False, c.lower()), 0) + cnt
                ) % MOD
        counts = new_counts

    total = 0
    for (is_upper, c), cnt in counts.items():
        total = (total + char_score(c) * cnt) % MOD

    return total


def main():
    T = int(input())
    for _ in range(T):
        temp = input().split()
        S, K = temp[0], int(temp[1])
        print(solve(S, K))


if __name__ == "__main__":
    main()
