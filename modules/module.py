#!/usr/bin/env python3

# "" module.py - an example of a Python module ""

counter = 0


def sum(the_list):
    global __counter
    __counter += 1
    the_sum = 0
    for element in the_list:
        the_sum += element
    return the_sum


def prodl(the_list):
    global __counter
    __counter +=1
    prod = 1
    for element in the_list:
        prod *= element
    return prod


if __name__ == "__name__":
    print("Eu prefiro ser uma module, mas eu consigo fazer uns testes para você.")
    my_list = [i+1 for i in range(5)]
    print(sum(my_list) == 15)
    print(prodl(my_list) == 120)


print("Eu gosto de ser uma module.")
print(__name__)

if __name__ == "__name__":
    print("Eu prefiro ser um module.")
else:
    print("Eu gosto de ser uma module :)")

counter = 0

if __name__ == "__name__":
    print("Eu gosto mesmo de ser uma module.")
else:
    print("Eu sou literalmente sou uma module :0")
