import re


def eval_game(
    reds,
    blues,
    greens,
):
    max_reds = 12
    max_greens = 13
    max_blues = 14
    game_failed = False
    if reds > max_reds or blues > max_blues or greens > max_greens:
        game_failed = True
    return game_failed


def main():
    file = open("input.txt")
    line = file.readline()

    good_games = 0

    while line:
        reds = 0
        greens = 0
        blues = 0
        words = re.findall(r"\b[a-zA-Z]+[;]?", line)
        numbers = re.findall(r"\d+", line)
        game_id = int(numbers[0])
        game_safe = True
        for i in range(1, len(words)):
            color = re.findall(r"red|blue|green", words[i])[0]
            match color:
                case "red":
                    reds += int(numbers[i])
                case "blue":
                    blues += int(numbers[i])
                case "green":
                    greens += int(numbers[i])
                case _:
                    continue
            if (re.search(";", words[i]) or i + 1 == len(words)) and game_safe:
                print("game check")
                game_failed = eval_game(reds, blues, greens)
                if game_failed:
                    print(f"{game_id} has failed")
                    game_safe = False
                reds = 0
                blues = 0
                greens = 0
        line = file.readline()
        if game_safe:
            good_games += game_id
    print(f"Sum of good game IDS: {good_games}")
    return 0


if __name__ == "__main__":
    main()
