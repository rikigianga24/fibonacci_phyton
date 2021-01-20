# Fibonacci

listaFibonacci = [0, 1]
input = int(input("Insert number of maximun lenght of fibonacci sequence: "))
for i in range(2, input):
    listaFibonacci.append(listaFibonacci.__getitem__(i - 1) + listaFibonacci.__getitem__(i - 2))
print(listaFibonacci)
