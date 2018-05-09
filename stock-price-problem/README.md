Classic interview question: given stock prices for a day (stored as a list), write an efficient algorithm which takes stock prices and returns the best profit that could be made from one purchase and one sale that day.

First, I write an inefficient algorithm which stores the differences between each pair of purchase/sale prices and returns the maximum. I do it to have a baseline brute force algorithm against which I can check my other soltions.

After some trial and error, I come with a better algorithm which simply tracks the lowest price throughout the day and the maximum profit I could make by selling the stock, since I keep track of the lowest price yet AND a list is an ordered object, so I know my maximum profit sell will occur AFTER my recorded minimum price.
