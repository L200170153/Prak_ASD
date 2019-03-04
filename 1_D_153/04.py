def rerata(x):
    total = 0
    for i in x:
        total += i;
    return total/len(x)

print(rerata([5,9]))
