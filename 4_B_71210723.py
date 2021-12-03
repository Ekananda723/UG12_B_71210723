a = int(input("Input : "))

print("Output : ")

for i in range(a):
    for x in range(a-i-1):
        print(" " , end = "  ")
    for x in range(a):
        if x == 0 or i == a-1 or i == x:
            print("*" ,end = "  ")
        else:
            print(end = "   ")
    print()
