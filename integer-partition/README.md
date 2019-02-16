For a positive integer n, a partition is way of writing n as a sum of positive integers (in which the order does not matter). 
Here is a list of all the partitions of n = 4:
1) 4
2) 3 + 1
3) 2 + 2
4) 2 + 1 + 1
5) 1 + 1 + 1 + 1

We would like to write a function to calculate all integer partitions for a given integers.

The classic solution defines a recursive function p(k, n), which represents the partitions of n which only use numbers
≥ k in the sum. Function p(k, n) can be defined recursively, with two base cases and one recursive case:
• if k > n, then p(k, n) = 0 
• if k = n, then p(k, n) = 1 
• else p(k, n) = p(k + 1, n) + p(k, n − k) 

There is also a third "base case", p(k, n) = 0 if k ≤ 0 or n ≤ 0, but it is rather vacuous, since we are working with natural numbers to begin with, and can only occur if the user enters invalid input. This case won't be considered in algorithm implementation.
