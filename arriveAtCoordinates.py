class Solution:
    def solve(self, moves, x, y):
        res = [0, 0]
        t = {"NORTH": 1, "SOUTH": -1, "EAST": 1, "WEST": -1}
        for move in moves:
            if move == "NORTH" or move == "SOUTH":
                res[1] += t[move]
            else:
                res[0] += t[move]
        
        if res[0] == x and res[1] == y:
            return True
        else:
            return False
