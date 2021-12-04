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


def calculate_pos_with_aim():
    input_list = _read_input()
    aim = 0
    horizontal = 0
    depth = 0
    for line in input_list:
        position, num = line.split(" ")
        num = int(num)
        if position == "down":
            aim += num
        elif position == "up":
            aim -= num
        elif position == "forward":
            horizontal += num
            depth = depth + (aim * num)

    return abs(horizontal) * abs(depth)


if __name__ == "__main__":
    position = calculate_position()
    print(f"The position (horizontal * depth) is {position}")
    position_with_aim = calculate_pos_with_aim()
    print(f"The position (horizontal * depth) with aim is {position_with_aim}")
