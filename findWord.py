wordFoundFlag = False

def checkWordExists(grid, word, i, j, k):
    global wordFoundFlag
    if wordFoundFlag == False:
        if (i < 0 or j < 0 or i > 3 or j > 3):
            return False
        if grid[i][j] == '*':
            return False
        if k < len(word) and word[k] == grid[i][j]:
            k += 1
            grid[i][j] = '*';
            if k == len(word):
                wordFoundFlag = True;
            if k <= len(word):
                if (checkWordExists(grid, word, i - 1, j, k) or checkWordExists(grid, word, i + 1, j, k)
                             or checkWordExists(grid, word, i, j + 1, k) or checkWordExists(grid, word, i, j - 1, k)):
                                 return True
                else:
                    return False
    return wordFoundFlag


if __name__ == '__main__':

    _grid = [list("axmy"), list("bgdf"), list("xeet"), list("raks")]
    _word = "geeksa"
    row = 4
    col = 4
    k = 0

    for i in range(0, row):
        for j in range(0, col):
            if wordFoundFlag == False:
                checkWordExists(_grid, _word, i, j, k)
    print(wordFoundFlag)
                
    
