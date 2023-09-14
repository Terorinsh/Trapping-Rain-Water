
class Solution(object):
    def trap(self, height):
        total = 0
        grid = []
        xxx = list(range(1,max(height)+1))
        xxx.reverse()
        for i in xxx:
            ht = []
            for i2 in height:
                if i2 >= i:
                    i2=1
                else: 
                    i2 = 0
                ht.append(i2)
            grid.append(ht)
        for dc in grid:
            if dc.count(1) > 1:
                for num in dc:
                    if dc[0] == 0:
                        dc.pop(0)
                    else:
                        dc.reverse()
                for num in dc:
                    if dc[0] == 0:
                        dc.pop(0)
                    else:
                        break
                total += dc.count(0)
        return total

height = [0,1,0,2,1,0,1,3,2,1,2,1]
solution = Solution()
print(solution.trap(height))

height = [4,2,0,3,2,5]
print(solution.trap(height))