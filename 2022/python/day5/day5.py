import re

def main():
    instructions = open("input.txt")
    crates = [
        [],
        ['s','l','w'],
        ['j','t','n','q'],
        ['s', 'c', 'h', 'f', 'j',],
        ['t','r','m','w','n','g','b'],
        ['t','r','l','s','d','h','q','b'],
        ['m','j','b','v','f','h','r','l'],
        ['d','w','r','n','j','m'],
        ['b','z','t','f','h','n','d','j'],
        ['h','l','q','n','b','f','t']
    ]
    line = instructions.readline()
    while(line):
        instr = re.findall(r'\d+', line)
        amount = int(instr[0])
        source = int(instr[1])
        dest = int(instr[2])
        print(amount,source,dest)
        items = []
        for i in range(amount):
            items.append( crates[source].pop() )
        for i in range(len(items)):
            item = items.pop()
            crates[dest].append(item)
        line = instructions.readline()
    for i in range(1,len(crates)):
        print(crates[i].pop())
    return 0

if __name__ == "__main__":
    main()
