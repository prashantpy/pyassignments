
def checkWordExists(grid, word, i, j):
    k = 0
    print(i,j)
    if word[0] == grid[i][j]:
        print(word[0])
    if (i < 0 or j < 0 or i > 3 or j > 3):
        return False
    if word[k] == grid[i][j]:
        k += 1;
        print(grid[i][j])
        if checkWordExists(grid, word, i - 1, j) or checkWordExists(grid, word, i + 1, j) or checkWordExists(grid, word, i, j + 1) or checkWordExists(grid, word, i, j - 1):

            return True
        else:
            return False


if __name__ == '__main__':

    _grid = [list("axmy"), list("bgdf"), list("xcet"), list("rass")]
    _word = "geeks"
    row = 4
    col = 4

    for i in range(0, row):
        for j in range(0, col):
            checkWordExists(_grid, _word, i, j)
    
