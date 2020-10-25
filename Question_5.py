string = ""
def trial():
    
    while True:
        try:
            word = str(input())
            
            divide(word)
        except EOFError:
            break
    print(string)


def divide(divider):
    halflength = int(len(divider)/2)
   
    if len(divider) == 1:
        return divider
    else:
        left = divide(divider[:halflength])
        right = divide(divider[halflength:])
        return merge(left,right)

def merge(l,r):
    lz= 0 
    rz= 0
    mergedlist = ""
    lenl = len(l) 
    while lz < lenl or rz < (len(r)):
        
        if lz == lenl:
            mergedlist += r[rz]
            rz += 1
        elif rz == len(r):
            mergedlist += l[lz]
            lz += 1
        elif l[lz] < r[rz]:
            mergedlist += l[lz]
            lz += 1
        else:
            mergedlist += r[rz]
            rz += 1
    global string 
    string += mergedlist + "\n"
    return mergedlist


if __name__ == "__main__":
        trial()


