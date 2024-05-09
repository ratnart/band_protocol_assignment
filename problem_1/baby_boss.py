# Time Complexity O(n)
# Space Complexity O(n)
def identify_baby_boss_habit(input_string: str) -> str:
    n = len(input_string)
    count_S = 0
    i = 0
    while i < n:
        if input_string[i] == "R":
            if count_S == 0:
                return "Bad boy"
            else:
                while i < n and input_string[i] == "R":
                    count_S = max(count_S - 1, 0)
                    i += 1
        elif input_string[i] == "S":
            count_S += 1
            i += 1

    return "Good boy" if count_S == 0 else "Bad boy"


def main():
    input_string = input()
    print(identify_baby_boss_habit(input_string))


if __name__ == "__main__":
    main()
