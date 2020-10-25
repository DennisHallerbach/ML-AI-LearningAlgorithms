
setergebnis = dict()
table = []
startlist = []
tmp=""
def trial():
    global table
    global setergebnis
    global startlist
    global tmp
    string = ""
    while True:
        try:
            word = str(input())
            word = word.replace("-","")
            short = [word[0],[word[1],int(word[2:])]]
            table.append(short)
            if word[0] not in startlist:
                startlist.append(word[0])
        except EOFError:
            break
    setergebnis[startlist[0]] = [startlist[0]+"-", 0]
    for i in range (1, len(startlist)):
        setergebnis[startlist[i]] = [startlist[i]+"-", -1]
        tmp = startlist[i]
        recur(startlist[i],startlist[i]+"-",0)
    values = setergebnis.keys()
    for i in values:
        string += setergebnis[i][0] + str(setergebnis[i][1]) + "\n"
    print(string)

def recur(A,test,counter):
    global startlist
    values =[]
    if startlist[0] not in test:
        if A != startlist[0]:
            for i in range(len(table)):
                if table[i][0] == A:
                    values.append(table[i][1])
            for i in range(len(values)):
                if values[i][0] not in test:
                    if values[i][0]  != startlist[0]:
                        test += values[i][0] + "-"
                        counter+= values[i][1]
                        print ( str (i) + ":" + test + str(counter))
                        recur(values[i][0],test,counter)
                    else:
                        test2 = test+ values[i][0] + "-"
                        counter2 = counter + values[i][1]
                        print ( str (i) + " printing?:" + test2 + str(counter2))
                        if setergebnis[tmp][1] == -1 or counter < setergebnis[tmp][1]:
                            setergebnis[tmp] = [test2,counter2]
                            recur(values[i][0],test2,counter2)
                return
        return False
    return True               
                
                    
                
                
        


if __name__ == "__main__":
        trial()



