**Problem**: You are climbing a staircase that has n steps. You can take the steps either 1 or 2 at a time. Calculate how many distinct ways you can climb to the top of the staircase.

For n = 1, the output should be climbingStairs(n) = 1
For n = 2, the output should be climbingStairs(n) = 2 (you can either climb 2 steps at once or climb 1 step two times)

**Solution**: After writing the first few combinations for step climbing, we will notice that the number of steps follows the Fibonacci sequence. Therefore, this problem can be solved recursively: we have 2 base cases, and for each new case, the number of steps can be given as steps = climbingStairs(n-1) + climbingStairs(n-2).

However, recusrion is really slow, and this problem can be solved dynamically. Let a list stepNumber contain the number of steps for each consecutive step combination. Since lists are indexed from 0, we can write it as stepNumber[0] = 0. Similarly, stepNumber[1] = 1 and stepNumber[2] = 2. Since each next element is the sum of previous two, we can dynamically add to the loop like so: stepNumber.append(stepNumber[index-1] + stepNumber[index-2]) for each index greater than 3 and less than n.
