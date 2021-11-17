import math
class Solution:
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        m = len(matrix)
        n = len(matrix[0])
        spiral = [-1] * m * n
        count = 0
        loop = 0
        mid = math.ceil(m / 2)

        while loop < mid:
            # the uppermost and leftmost index for this loop
            starti = startj = loop
            numElements_i = m - 2 * loop
            numElements_j = n - 2 * loop
            # the lowest index for this loop
            endi = starti + numElements_i - 1
            # the rightmost index for this loop
            endj = startj + numElements_j - 1

            if numElements_i == 1 and numElements_j == 1:
                spiral[count] = matrix[starti][startj]
                return spiral

            # go through the row from left to right
            for j in range(startj, endj):
                spiral[count] = matrix[starti][j]
                count += 1
                if count == m * n:
                    return spiral

            # go through the column from top to bottom
            for i in range(starti, endi):
                spiral[count] = matrix[i][endj]
                count += 1
                if count == m * n:
                    return spiral

            # go through the row from right to left
            for j in range(endj, startj, -1):
                spiral[count] = matrix[endi][j]
                count += 1
                if count == m * n:
                    return spiral

            # go through the column from bottom to top
            for i in range(endi, starti, -1):
                spiral[count] = matrix[i][startj]
                count += 1
                if count == m * n:
                    return spiral

            loop += 1

        return spiral

if __name__ == '__main__':
    matrix = [[1,2,3],[4,5,6],[7,8,9]]
    assert(Solution().spiralOrder(matrix) == [1,2,3,6,9,8,7,4,5])
    matrix = [[1],[2],[3]]
    assert(Solution().spiralOrder(matrix) == [1,2,3])

