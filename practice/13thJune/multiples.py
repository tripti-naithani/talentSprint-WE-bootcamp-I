#1
def sum_of_multiples(num1, num2, limit):
    multiples = []
    for i in range(1, limit):
        if (i % num1 == 0 or i % num2 == 0 ):
            multiples.append(i)
    return sum(multiples)

limit = int(input())
print(sum_of_multiples(3, 5, limit))

#2
print(sum([i for i in range(1, 1000) if i % 3 == 0 or i % 5 == 0]))
