# the Fibonacci serie is 1 1 2 3 5 8 13 21 ...
# contruction method the next number is the sum of the previous two numbers

serie_Fibonacci = [1, 1]
# Which number of the Fibonacci series would you like to know
serie_numer = 15

for numer in range(serie_numer):
    Fibonacci_new = serie_Fibonacci[numer]+serie_Fibonacci[numer+1]
    serie_Fibonacci += [Fibonacci_new]


print(serie_Fibonacci)
print(serie_Fibonacci[serie_numer])
