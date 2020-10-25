
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
    startlist = sorted(startlist)
    
    for i in range (0, len(startlist)):
        if startlist[i] == table[0][0]:
            setergebnis[startlist[i]] = [startlist[i], 0]
        else:
            setergebnis[startlist[i]] = [startlist[i]+"-", -1]
  
    recur(table[0][0],table[0][0],0)
    values = setergebnis.keys()
    values = sorted(values)
    for i in values:
        string += setergebnis[i][0] +"-"+ str(setergebnis[i][1]) + "\n"
    print(string)

def recur(zeichen,test,counter):
    global setergebnis
    values = []
    for i in range(len(table)):
            if table[i][0] == zeichen:
                values.append(table[i][1])
    for i in range(len(values)):
        if values[i][0] not in test:
            if values[i][0] == table[0][0]:
                test = values[i][0]
            else:
                tmp = test
                test = values[i][0] + "-" + test
            tmp2 = counter
            counter+= values[i][1]
            if setergebnis[values[i][0]][1] == -1 or counter < setergebnis[values[i][0]][1]:
                setergebnis[values[i][0]] = [test,counter]        
            recur(values[i][0],test,counter)
            test = tmp
            counter = tmp2
    return 

                
        


if __name__ == "__main__":
        trial()



