class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols = collections.defaultdict(set)  # Collection.defaultdict makes sure that every row and col gets a new set for checking
        rows = collections.defaultdict(set)
        square = collections.defaultdict(set)

        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":       # I put = instead of ==
                    continue
                if(board[r][c] in rows[r] or
                   board[r][c] in cols[c] or
                   board[r][c] in square[r//3,c//3]):
                   return False
                cols[c].add(board[r][c])    # I forgot to put col[c] rows[r] i just put col and row 
                rows[r].add(board[r][c])
                square[r//3,c//3].add(board[r][c])
        return True

        
        
    