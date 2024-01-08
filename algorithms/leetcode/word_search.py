class Solution:
    def exist(self, grid, word):
        """
        Determines if a given word can be found in a 2D grid.

        This function iterates over each cell in the grid. If a cell contains the first letter of the
        word, it initiates a DFS from that cell to see if the full word can be constructed.

        Parameters:
        grid (List[List[str]]): The 2D grid of characters.
        word (str): The word to search for in the grid.

        Returns:
        bool: True if the word can be formed, False otherwise.
        """
        if not grid:
            return False

        for x in range(len(grid)):
            for y in range(len(grid[0])):
                if self.dfs(grid, x, y, word, 0):
                    return True
        return False

    def dfs(self, board, x, y, word, count):
        """
        Recursively searches for the word in the grid using DFS.

        Starting from a specific cell, this method explores all four directions (up, down, left, right),
        checking if the next character in the word matches the neighboring cell. If a mismatch occurs,
        or the cell is out of bounds, the search backtracks.

        Parameters:
        board (List[List[str]]): The 2D grid of characters.
        x, y (int): Current coordinates in the grid.
        word (str): The word to search for.
        count (int): Current position in the word.

        Returns:
        bool: True if the current path can form the word, False otherwise.
        """
        if count == len(word):
            return True
        if x < 0 or y < 0 or x >= len(board) or y >= len(board[0]) or board[x][y] != word[count]:
            return False

        temp = board[x][y]
        board[x][y] = "visited"
        found = self.dfs(board, x+1, y, word, count+1) or \
                self.dfs(board, x-1, y, word, count+1) or \
                self.dfs(board, x, y+1, word, count+1) or \
                self.dfs(board, x, y-1, word, count+1)
        board[x][y] = temp  # Backtrack

        return found
