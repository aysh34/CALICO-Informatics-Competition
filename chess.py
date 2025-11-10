from collections import defaultdict


def check_specific_row(pieces, key_fn, move_types):
    groups = defaultdict(list)
    for t, x, y in pieces:
        groups[key_fn(x, y)].append((t, x, y))
    cnt = 0
    for line in groups.values():
        line.sort(key=lambda p: (p[1], p[2]))
        for i in range(len(line) - 1):
            ta, xa, ya = line[i]
            tb, xb, yb = line[i + 1]
            if ta in move_types:
                cnt += 1
            if tb in move_types:
                cnt += 1
    return cnt


def solve(N: int, M: int, K: int, P: list[tuple[str, int, int]]) -> int:
    """

    N: Number of rows of the board
    M: Number of columns of the board
    K: Number of pieces
    P: list of tuples. Each tuple contains (piece type, x position, y position)
    """
    # YOUR CODE HERE
    total = 0
    total += check_specific_row(P, lambda x, y: y, {"R", "Q"})  # same row
    total += check_specific_row(P, lambda x, y: x, {"R", "Q"})  # same column
    total += check_specific_row(P, lambda x, y: x - y, {"B", "Q"})  # main diagonal
    total += check_specific_row(P, lambda x, y: x + y, {"B", "Q"})  # anti diagonal
    return total


def main():
    T = int(input())
    for _ in range(T):
        temp = input().split()
        N, M = int(temp[0]), int(temp[1])
        K = int(input())
        P = []
        for _ in range(K):
            temp = input().split()
            temp_tuple = (str(temp[0]), int(temp[1]), int(temp[2]))
            P.append(temp_tuple)
        print(solve(N, M, K, P))


if __name__ == "__main__":
    main()
