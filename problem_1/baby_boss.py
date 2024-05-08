ERROR_WRONG_INPUT_LENGTH_TEXT = "Wrong input string length"
ERROR_WRONG_INPUT_TYPE = "Wrong input type"


# Time Complexity O(n)
# Space Complexity O(n)
# auxiliary space O(1)
def identify_baby_boss_habit(input_string: str) -> str:
    if not isinstance(input_string, str):
        raise Exception(ERROR_WRONG_INPUT_TYPE)

    n = len(input_string)
    if n < 1 or n > 1000000:
        raise Exception(ERROR_WRONG_INPUT_LENGTH_TEXT)

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
    print(identify_baby_boss_habit("SRSSRRR"))


if __name__ == "__main__":
    main()
