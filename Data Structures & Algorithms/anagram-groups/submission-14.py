class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        A = []
        for i, string in enumerate(strs):
            A.append([sorted(string), i])
        A.sort()

        templist = []

        i = 0
        for j in range(len(A)):
            if A[j][0] != A[i][0]:
                templist.append([strs[A[k][1]] for k in range(i, j)])
                i = j
        templist.append([strs[A[k][1]] for k in range(i, len(A))])

        return templist
