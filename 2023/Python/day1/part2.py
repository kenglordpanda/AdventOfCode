import re


def main():
    file = open("input.txt")
    line = file.readline()
    sum = 0
    word_to_num = {
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9",
        "zero": "0",
    }
    while line:
        nums = []
        low = 0
        for i in range(1, len(line) + 1):
            string = line[low:i]
            if any(chr.isdigit() for chr in string) or re.findall(
                r"one|two|three|four|five|six|seven|eight|nine|zero", string
            ):
                parsed = re.findall(
                    r"\d|one|two|three|four|five|six|seven|eight|nine", string
                )
                nums.append(parsed[0])
                low = i - 1
        for i in range(len(nums)):
            if len(nums[i]) > 1:
                nums[i] = word_to_num[nums[i]]
        if len(nums) > 0:
            sum += int(nums[0] + nums[-1])
        line = file.readline()


if __name__ == "__main__":
    main()
