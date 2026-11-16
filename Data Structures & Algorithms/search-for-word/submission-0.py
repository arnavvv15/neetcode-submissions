class Solution:
    def exist(self, board: list[list[str]], word: str) -> bool:
        n_rows = len(board)
        n_cols = len(board[0])
        def search(row, col, pos):
            if pos == len(word):
                return True
            if row < 0 or row >= n_rows or col < 0 or col >= n_cols:
                return False
            if board[row][col] != word[pos]:
                return False
            letter = board[row][col]
            board[row][col] = "*"
            for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                if search(row + dr, col + dc, pos + 1):
                    board[row][col] = letter
                    return True
            board[row][col] = letter
            return False
        for row in range(n_rows):
            for col in range(n_cols):
                if board[row][col] == word[0] and search(row, col, 0):
                    return True
        return False
        