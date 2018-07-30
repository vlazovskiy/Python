In a list of integers, for each index find the product of every integer except the integer at that index.

The greedy solution utilizes the greedy approach, where we first calculate the products of all numbers before the index by storing the previous result and nultiplying it by the next element, and then doing the reverse and u

The reduce solution utilizes pop() and reduce() methods of the list: a loop goes through the list, pops the first element, computes the product of the remaining elements with reduce, and then appends the dropped element at the end of the list.
