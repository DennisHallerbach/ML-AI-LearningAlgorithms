def trial():
    counter = 0
    table = dict()
    setergebnis =[]
    startlist = []
    while True:
        try:
            word = str(input())
            table[word[0]] = word[2:]
            startlist.append(word[0])
        except EOFError:
            break
    setergebnis.append(startlist[0])
    ##setergebnis.append(next(iter(table)))
    while counter < len(setergebnis):
        values = list(table[setergebnis[counter]])
        for i in range(len(values)):
            if values[i] not in setergebnis:
                setergebnis.append(values[i])
        counter += 1

    
    print("".join(setergebnis) + "\n")

if __name__ == "__main__":
        trial()

