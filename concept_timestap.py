def timestamp_loop(result: set[int] = []) -> None:
    timestap = [24, 60, 60]
    # for i in range(0,6,1):
    #    result.append(int(input()))
    chunks = [result[i : i + 3] for i in range(0, len(result), 3)]
    print(chunks)


def timestamp_string_method(result: set[int] = []) -> None:
    timestap = [24, 60, 60]
    # for i in range(0,6,1):
    #    result.append(int(input()))
    chunks = list(zip(*[iter(result)] * 3))
    print(chunks)


if __name__ == "__main__":
    timestamp_loop((1, 1, 1, 2, 2, 2))
    timestamp_string_method((1, 1, 1, 2, 2, 2))
