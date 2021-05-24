def isPrime(number):
    if number > 1:
        for i in range(2, number):
            if (number % i) == 0:
                return False
        else:
            return True
    else:
        return False

inputFile = open('test.txt')
lines = inputFile.readlines()
inputFile.close()
pyramid = []
for i in lines:
    print(i)


for line in lines:
    pyramid.append(line.split())
for i in range(0,len(pyramid)):
    for j in range(0,len(pyramid[i])):
        pyramid[i][j] = int(pyramid[i][j])


for i in range(len(pyramid)-2, -1, -1):
    for j in range(0, len(pyramid[i])):
        if isPrime(pyramid[i][j]) == False:
            pyramid[i][j] += max(pyramid[i+1][j], pyramid[i+1][j+1])

print('\nThe maximum sum of the numbers is',max(pyramid)[0])