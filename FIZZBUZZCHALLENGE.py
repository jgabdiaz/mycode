#!/usr/bin/env python3

def main():
    def Mult_3(x):
        if x%3 == 0:
            return True

    def Mult_5(B):
        if B%5 == 0:
            return True

    def Mult_3_5(Z):
        if Z%3 == 0 and Z%5 == 0:
            return True


    x = range(101)
    for i in x:
        if Mult_3_5(i):
            print("FizzBuzz")
        elif Mult_3(i):
            print("Fizz")
        elif Mult_5(i):
            print("Buzz")
        else:
            print(i)

main()            

