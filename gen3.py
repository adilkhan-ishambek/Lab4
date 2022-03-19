n = int(input())


def pot(i):
    if i % 3 == 0 or i % 4 == 0:
        print(i, end=" ")


s = [pot(i) for i in range(n + 1)]