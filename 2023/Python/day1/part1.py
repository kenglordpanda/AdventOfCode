import re


def main():
    file = open("input.txt")
    line = file.readline()
    sum = 0
    while line:
        nums = re.findall(r"\d", line)
        if len(nums) > 0:
            sum += int(nums[0] + nums[-1])
        line = file.readline()
    print(sum)


if __name__ == "__main__":
    main()
