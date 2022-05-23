class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]: #given n
        Left, Right, Up, Down = 0, n-1, 0, n-1 #define dimensions from top left (0,0) to bottom right (n-1, n-1)
        position = 1 #initial position

        matrix = [[0] * n for _ in range(n)] #set up n*n matrix
        while Left <= Right and Up <= Down: #make sure right coordinates
            for i in range(Up, Down+1): 
                matrix[Left][i] = position  #same logic for all four branches below: move right/up/left/down
                position += 1
            Left += 1
            for i in range(Left, Right+1):
                matrix[i][Down] = position
                position += 1
            Down -= 1
            for i in range(Down, Up-1, -1):
                if Left <= Right:
                    matrix[Right][i] = position
                    position += 1
            Right -= 1
            for i in range(Right, Left-1, -1):
                if Up <= Down:
                    matrix[i][Up] = position
                    position += 1
            Up += 1
        return matrix #return result
