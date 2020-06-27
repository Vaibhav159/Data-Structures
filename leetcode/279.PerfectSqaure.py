"""279. Perfect Squares

Given a positive integer n, find the least number of perfect square numbers (for example, 1, 4, 9, 16, ...) which sum to n.

Example 1:

Input: n = 12
Output: 3 
Explanation: 12 = 4 + 4 + 4.
Example 2:

Input: n = 13
Output: 2
Explanation: 13 = 4 + 9.
"""


class Solution:
    def numSquares(self, n: int) -> int:
        
        #creating a dictionary to store n values
        d = {}
        
        #list to store all square's
        sq = []
        
        #setting all n values in dict to infinity (max value)
        for i in range(n + 1):
            d[i] = float("inf")
            
        #setting the sqaure value to 1 and adding them into the sq
        for i in range(1, math.ceil(math.sqrt(n)) + 1):
            d[i ** 2] = 1
            sq.append(i ** 2)

	#updating all the n values 
        for i in range(n + 1):
        
            #checking for all values in sq
            for j in sq:
            	 
            	 #if value of j is greater we will simply break as we cant have sqaure greater than curr number eg 9 > 8 (break)
                if j > i :
                    break
                    
                #otherwise we will update the value of i by taking min of current value and the value after we subtract it from square value + 1
                d[i] = min(d[i - j] + 1, d[i])
         
        #return the d[n] which is asked               
        return d[n]
             

