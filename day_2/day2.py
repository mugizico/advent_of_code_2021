def _read_input():
    with open("day_2/day_2_input.txt", "r") as f:
        return [line for line in f]


def calculate_position():
    input_list = _read_input()
    horizontal_sum = 0
    depth_sum = 0

    for line in input_list:
        position, num = line.split(" ")
        num = int(num)
        if position == "forward":
            horizontal_sum += num
        elif position == "up":
            depth_sum += num
        elif position == "down":
            depth_sum -= num

    return abs(horizontal_sum) * abs(depth_sum)


if __name__ == "__main__":
    position = calculate_position()
    print(f"The position (horizontal * depth) is {position}")
