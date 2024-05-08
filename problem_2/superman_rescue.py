# Time Complexity O(n)
# Space Complexity O(n)
# auxiliary space O(1)
def get_maximum_number_of_chicken_protected_by_superman(
    n: int, k: int, pos_chicken_list: list[int]
) -> int:
    max_help = 1
    start_help_index = 0

    for i in range(1, n):
        while pos_chicken_list[i] > pos_chicken_list[start_help_index] + k - 1:
            start_help_index += 1

        max_help = max(max_help, i - start_help_index + 1)

    return max_help


def main():
    n, k = map(int, input().split())
    pos_chicken_list = list(map(int, input().split()))

    print(get_maximum_number_of_chicken_protected_by_superman(n, k, pos_chicken_list))


if __name__ == "__main__":
    main()
