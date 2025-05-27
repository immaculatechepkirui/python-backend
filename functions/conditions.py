# IF STATEMENT
# CHECKS IF A STATEMENT IS TRUE
def check_if_even(number):
    if number % 2 == 0:
        print(f'Number is even')




    # If--- ELSE STATEMENT
def check_even_or_odd(num):
    if num % 2 == 0:
        print(f'Number is even')
    else:
        print(f'Number is odd')



# MULTIPLE IF CHECKS
def check_divisibility(n):
    for x in range(1, n+1):
        if x % 2 == 0:
            print(f'x is divisible by 2')
        elif x % 3 == 0:
            print(f'x is divisible by 3')
        elif x % 5 == 0:
            print(f'x is divisible by 5')
        else:
            print(f'x is not divisible by 2, 3, or 5') 



# FIZBUZZ

def fizzbuzz(n):
      for i in range(1, n + 1):
        if i % 3 == 0 and i % 5 == 0:
            print("fizzbuzz")
        elif i % 3 == 0:
            print("fizz")
        elif i % 5 == 0:
            print("buzz")
        else:
            print(i)



# WHILE STATEMENT

def count_down(start):
    while start  >= 0:
        print(f'Count Down at {start}')

def counting_down(start):
    while start  >= 0:
        print(f'Count Down at {start}')
        start -= 1

def counter_down_with_break(start, stop):
    while start >= 0:
        print(f'counter down at {start}')
        if start == stop:
            print(f'stopping at {stop}')
            break
        start -= 1



    # CONTINUE STATEMENTSIN PYTHON

def count_down_with_odd_numbers(start):
    while start >= 0:
        if start % 2 == 0:
            start -= 1
            continue
        print(f'Count Down at {start}')
        start -= 1




def print_even_numbers():
    number = 2
    while number <= 100:
        if number % 2 != 0:
            continue
        print(number)
        number += 2




def even_numbers():
    num = 0
    while num < 100:
        num += 1
        if num % 2 != 0:
            continue
        print(num)

even_numbers()


def second_largest(arr):
    first = second = float('-inf')
    for num in arr:
        if num > first:
            second = first
            first = num
        elif first > num > second:
            second = num
    return second if second != float('-inf') else None



        