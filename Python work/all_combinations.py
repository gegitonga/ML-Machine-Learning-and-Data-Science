#Given two integers n and k, return all possible combinations of k numbers out of the
#range [1,n]

#input n=4, k = 2
#n =4 [1,2,3,4]
class combine:
    def combine(self, n , k):
        res = []

        def backtrack(start, comb):
            if len(comb) == k:
                res.append(comb.copy())

            for i in range(start, n + 1):
                comb.append(i)
                backtrack(i + 1, comb)
                comb.pop()
        backtrack(1, [])
        return res


