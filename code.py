class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        X =0
        for x in operations:
            if x == "X++" or x == "++X":
                X+=1
            else:
                X-=1
        return X
