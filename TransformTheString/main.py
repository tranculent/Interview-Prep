def Solution():
    nCases = int(input())

    def solve(S, F):
        if len(S) == 0 or len(F) == 0: return 0
        ans = 0

        for i in range(len(S)):
            min_diff_for_i = abs(ord(S[i]) - ord(F[0]))
            for j in range(len(F)):
                if abs(ord(S[i]) - ord(F[j])) < min_diff_for_i:
                    min_diff_for_i = abs(ord(S[i]) - ord(F[j]))
            ans += min(min_diff_for_i, 26-min_diff_for_i)

        return ans
        
    for i in range(nCases):
        S = input()
        F = input()

        print("Case #{}: {}".format(str(i+1), solve(S, F)))   

Solution()