import re


def main():
    file = open("input.txt")
    line = file.readline()
    power = 0
    while line:
        best_red = 0
        best_blue = 0
        best_green = 0
        reds = 0
        greens = 0
        blues = 0
        words = re.findall(r"\b[a-zA-Z]+[;]?", line)
        numbers = re.findall(r"\d+", line)
        for i in range(1, len(words)):
            color = re.findall(r"red|blue|green", words[i])[0]
            match color:
                case "red":
                    reds = int(numbers[i])
                case "blue":
                    blues = int(numbers[i])
                case "green":
                    greens = int(numbers[i])
                case _:
                    continue
            if re.search(";", words[i]) or i + 1 == len(words):
                best_red = max(best_red, reds)
                best_blue = max(best_blue, blues)
                best_green = max(best_green, greens)
                reds = 0
                blues = 0
                greens = 0
        power += best_red * best_blue * best_green
        line = file.readline()
    print(power)


if __name__ == "__main__":
    main()
