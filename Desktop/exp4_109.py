print("\nExp 4 - Devanshi Patel\n")
print("Prime numbers from 1 to 20\n")
for Number in range (1, 20):
    count = 0
    for i in range(2, (Number//2 + 1)):
        if(Number % i == 0):
            count = count + 1
            break

    if (count == 0 and Number != 1):
        print(" %d" %Number, end = '  ')
