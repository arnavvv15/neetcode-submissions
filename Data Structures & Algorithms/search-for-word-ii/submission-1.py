
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:

        trie = {}

        for word in words:
            current = trie

            for letter in word:
                if letter not in current:
                    current[letter] = {}

                current = current[letter]

            current["end"] = word

        result = []

        rows = len(board)
        cols = len(board[0])

        def search(row, col, current):

            letter = board[row][col]

            if letter not in current:
                return

            current = current[letter]

            if "end" in current:
                result.append(current["end"])
                del current["end"]

            board[row][col] = "#"

            directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

            for row_change, col_change in directions:

                new_row = row + row_change
                new_col = col + col_change

                if 0 <= new_row < rows and 0 <= new_col < cols:
                    if board[new_row][new_col] != "#":
                        search(new_row, new_col, current)

            board[row][col] = letter

        for row in range(rows):
            for col in range(cols):
                search(row, col, trie)

        return result

        