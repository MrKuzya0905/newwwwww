a = [1,4,5]
b= [6,8,9]

print("AxB={", end="")

for i in range(3):
    for j in range(3):
        print(f"({a[i]}, {b[j]});", end="")

print("}")

print("AxA={", end="")

for i in range(3):
    for j in range(3):
        print(f"({a[i]}, {a[j]});", end="")

print("}")