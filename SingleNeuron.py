
e = 2.718281828459043
learningrate = 0.001
turns = 100
bias = 1
inputs = []
weights = []
expectedoutputs = []
testset=[]


def readin():
    learning = True
    while True:
        try:
            everything = str(input())
            everything = everything.split(',')
            if float(everything[0]) == 0.0:
                learning = False
                continue
            if learning:
                inputs.append([float(everything[0]),float(everything[1]),bias])
                expectedoutputs.append(float(everything[2]))
            else :
                testset.append([float(everything[0]),float(everything[1]),bias])

        except EOFError:
            break

def netinputs(inputs,norm):
    netinput = 0.0
    for i in range (len(inputs)):
        netinput += inputs[i]/norm[i]*weights[i]   
    netinput += bias
    return netinput

def normalization(inputs):
    maxx = 0 
    maxy = 0
    for i in range(len(inputs)):
        if abs(inputs[i][0])>maxx :
            maxx = inputs[i][0]
        if abs(inputs[i][1])>maxy :
            maxy = inputs[i][1]
    return [maxx,maxy,1]

def activation (x):
    if x > 0:
        return 1
    else:
        return -1
    ##x = x-bias
    ##return (e**x - e**(-1*x))/(e**x +e**(-1*x))

def derivate(x):
    return 1- (activation(x)**2)

def randbelow(n):
    "Return a random int in the range [0,n).  Raises ValueError if n<=0."
    if n <= 0:
       raise ValueError
    k = n.bit_length()
    numbytes = (k + 7) // 8
    while True:
        r = int.from_bytes(random_bytes(numbytes), 'big')
        r >>= numbytes * 8 - k
        if r < n:
            return r

def random_bytes(n):
    "Return n random bytes"
    with open('/dev/urandom', 'rb') as file:
        return file.read(n)  

def errordifferenz(expectedout, actualout):
    return (expectedout-actualout)**2

def weightdifferenz(output, expectedoutput, inputs):
    return learningrate * (-2*(output-expectedoutput)*inputs)

def train(set, outputset):
    norm = normalization(set)
    for x in range(turns):
        error = 0
        for i in range (len(set)):
            inputparameter = [set[i][0], set[i][1],bias]
            netinput = netinputs(inputparameter,norm)
            output = activation(netinput)
            error += errordifferenz(outputset[i], output)
        for i in range (len(set)):
            inputparameter = [set[i][0], set[i][1],bias]
            netinput = netinputs(inputparameter,norm)
            output = activation(netinput)
            error += errordifferenz(outputset[i], output)
            
            for j in range (len(weights)):
                weights[j] = weights[j] + weightdifferenz(output,outputset[i],set[i][j]/norm[j])

def test(testset,set):
    norm = normalization(set)
    return activation(netinputs(testset,norm))

if __name__ == "__main__":
        weights = [randbelow(10000)/10000000, randbelow(10000)/10000000,randbelow(10000)/10000000]
        readin()
        train(inputs,expectedoutputs)
        ende = ""
        for i in range (len(testset)):
                if(test(testset[i],inputs)) == 1:
                    ende+= "+"+ str(test(testset[i],inputs))+ "\n"
                else:
                    ende += str(test(testset[i],inputs)) + "\n"
        print(ende)

