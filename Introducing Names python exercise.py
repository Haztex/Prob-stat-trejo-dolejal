values = int(input("How much data do you want to introduce?"))
names = []
total = 0
for i in range(0, values):
    X = input("Introduce a name ")
    names.append(X)
namez = int(input("Which name do you want to know?"))
print(names [namez])