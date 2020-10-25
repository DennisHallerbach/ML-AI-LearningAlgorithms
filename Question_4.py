def trial():
    string = ""
    while True:
        try:
            word = str(input())
            array = list(word)
            for i in range(1, len(array)):
                for y in range (0,i):
                    if array[i]< array[y]:
                        char = array.pop(i)
                        array.insert(y,char)
                string += "".join(array) + "\n"
        except EOFError:
            break
    print(string)

if __name__ == "__main__":
        trial()
