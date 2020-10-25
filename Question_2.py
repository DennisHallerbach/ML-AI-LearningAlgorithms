def trial():
    string = ""
    while True:
        try:
            number = int(input())
            string = string + str(number*2) + "\n"
        except EOFError:
            break
    print(string)

if __name__ == "__main__":
        trial()
