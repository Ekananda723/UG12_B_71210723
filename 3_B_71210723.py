a = input("Input : ")
b = len(a)

print("Output : ")

for i in range(b):
    for x in range(b-i-1):
        print(" " ,end = "")
    for x in range(i+1):
        print(a[x] ,end = "")
    print()
for i in range(1,b):
    for y in range(i):
        print(" " ,end = "")
    for y in range(b-i):
        print(a[y], end = "")
    print()
