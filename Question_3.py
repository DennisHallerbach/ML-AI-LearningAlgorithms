def trial():
    string = ""
    while True:
        try:
            word = str(input())
            array = list(word)
            tmp = ""
            for i in range (len(word)):
                tmp = array.copy()
                for y in range (0, len(word)-1-i):
                    
                    if ord(array[y]) > ord(array[y+1]):
                        test = array[y]
                        array[y] = array[y+1]
                        array[y+1] = test
                if tmp == array:
                    
                    break
                else:
                    string += "".join(array) + "\n"

        except EOFError:
            break
    print(string)

if __name__ == "__main__":
        trial()
