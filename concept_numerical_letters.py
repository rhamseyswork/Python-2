def main(variable: str) -> int:
    variable = list(variable[::-1])
    result = sum(
        int(ord(char_i) - 64) * int(26**i) for i, char_i in enumerate(variable)
    )
    return result


if __name__ == "__main__":
    # variable = list(str('AA'))#input("letters to convert to numerical values: ")
    variable = "CC"
    print(main(variable))
