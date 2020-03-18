import math

# Pascal's Triangle
def printTriange(num):
    for i in range(0, num):
        for j in range(0,i+1):
            temp = int(math.factorial(i)//(math.factorial(j) * math.factorial(i-j)))
            print(temp, end=" ", flush=True)
        print(flush=True)

printTriange(10)