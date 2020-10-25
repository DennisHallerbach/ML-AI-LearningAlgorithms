
setergebnis =[]
table = dict()
def trial():
    global table
    global setergebnis
    startlist = []
    while True:
        try:
            word = str(input())
            table[word[0]] = word[2:]
            startlist.append(word[0])
        except EOFError:
            break
    setergebnis.append(startlist[0])
    recur(setergebnis[0])

    
    print("".join(setergebnis) + "\n")

def recur(A):
    global setergebnis
    values = list(table[A])
    for i in range(len(values)):
        if values[i]  not in setergebnis:
            setergebnis.append(values[i])
            recur(values[i])
        


if __name__ == "__main__":
        trial()



