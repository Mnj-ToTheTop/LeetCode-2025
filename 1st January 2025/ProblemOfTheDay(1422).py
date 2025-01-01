# 1422. Maximum Score After Splitting a String
class Solution:
    def maxScore(self, s: str) -> int:
        sol = 0
        zeroes = s.count('0')
        ones = s.count('1')
        split = 1
        left = 1 if s[0] == '0' else 0
        right = ones if s[0] == '0' else ones - 1
        sol = left + right
        while split < len(s) - 1:
            if s[split] == '0':
                left+=1
            else:
                right-=1
            
            sol = max(sol, left+right)
            split+=1
        return sol

# TIME --> 1ms
