
You have a list of integers, and for each index you want to find the product of every integer except the integer at that index.

The solution utilizes the .pop() and reduce() methods of the list: a loop goes through the list, pops the first element, computes the product of the remaining elements with reduce, and then appends the dropped element at the end of the list.
