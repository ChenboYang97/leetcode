import math
class Solution:
    def generateMatrix(self, n: int) -> list[list[int]]:
        result = [[0] * n for _ in range(n)]
        mid = math.ceil(n / 2)
        loop = 0
        index = 1

        while loop < mid:
            num_times = n - 1
            starti = startj = loop
            num_times -= 2 * loop
            if num_times == 0:
                result[starti][startj] = index
                return result
            endj = endi = loop + num_times

            # Fill out the row from left to right
            for j in range(startj, endj):
                result[starti][j] = index
                index += 1

            # Fill out the column from top to bottom
            for i in range(starti, endi):
                result[i][endj] = index
                index += 1

            # Fill out the row from right to left
            for j in range(endj, startj, -1):
                result[endi][j] = index
                index += 1

            # Fill out the column from bottom to top
            for i in range(endi, starti, -1):
                result[i][startj] = index
                index += 1

            loop += 1

        return result

if __name__ == '__main__':
    n = 3
    assert(Solution().generateMatrix(n) == [[1,2,3],[8,9,4],[7,6,5]])
    n = 1
    assert(Solution().generateMatrix(n) == [[1]])

