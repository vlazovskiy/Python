*Problem*: You are climbing a staircase that has n steps. You can take the steps either 1 or 2 at a time. Calculate how many distinct ways you can climb to the top of the staircase.

For n = 1, the output should be
climbingStairs(n) = 1;

For n = 2, the output should be
climbingStairs(n) = 2 (you can either climb 2 steps at once or climb 1 step two times)

*Solution:* After writing the first few combinations for step climbing, we will notice that the number of steps follows the Fibonacci sequence. Therefore, this problem can be solved recursively: we have 2 base cases, and for each new case, the number of steps can be given as steps = climbingStairs(n-1) + climbingStairs(n-2). 
