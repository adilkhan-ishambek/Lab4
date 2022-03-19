n = int(input())


def even(i):
    if i % 2 == 0:
        print(i, end=" ")


s = [even(i) for i in range(n)]