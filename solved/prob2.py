"""Project Euler - Problem 2.

Each new term in the Fibonacci sequence is generated by adding the
previous two terms. By starting with 1 and 2, the first 10 terms will be:

1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

By considering the terms in the Fibonacci sequence whose values do not
exceed four million, find the sum of the even-valued terms.
"""

fib_terms = [0, 1]  # list with the first two terms
even_terms_sum = 0

while fib_terms[-1] < 4000000:
    new_term = fib_terms[-1] + fib_terms[-2]  # F(N) = F(N-1) + F(N-2)
    fib_terms.append(new_term)

    if new_term % 2 == 0:
        even_terms_sum += new_term

print(even_terms_sum)
