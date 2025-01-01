# 1346. Check If N and Its Double Exist
class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:

        if 0 in arr and arr.count(0) > 1:
            return True
        for num in arr:
            if 2*num in arr and num!=0:
                return True
        return False
