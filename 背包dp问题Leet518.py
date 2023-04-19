class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        combination = (amount+1) * [0] #define the answer array combination and set its initial value to 0 with length as amount + 1
        combination[0] = 1 #base case that there is 1 way to make up for amount 0
        for coin in coins: #because this is combination problem so we need to iterate every coin for every possibility
            for i in range(coin, amount+1): #i means all possible amounts 
                combination[i] = combination[i-coin] + combination [i] #update i with all remaining combinations 
        return combination[amount] #return combination for all amounts 
        
