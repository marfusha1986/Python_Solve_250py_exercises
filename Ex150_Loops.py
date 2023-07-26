x = [2, 4, 6, 8]
y = [5, 10, 15, 20]

for i in x:
    for n in y:
        if n <= 10:
            print(i * n)
        elif n > 10:
            print(i * (n ** 2))