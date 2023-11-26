def main():
    file = open( "input.txt" )
    text = file.readline()
    lower = 0
    higher = 14
    marker = -1
    test = ""
    for i in range(len(text)):
        if marker != -1:
            break
        test = text[lower:higher]
        item = list(set(test))
        if len(item) != 14:
            i = higher
            higher += 1
            lower +=1
        else:
            marker = higher 
    print (test)
    print (marker)

if __name__ == "__main__":
    main()
