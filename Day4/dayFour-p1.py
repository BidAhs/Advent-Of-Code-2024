
with open('dayFourInput.txt') as file:
    grid = [line.strip() for line in file]

# define directions
directions = [
    (0, 1),   #  right
    (0, -1),  #  left
    (1, 0),   #  down
    (-1, 0),  #  up
    (1, 1),   #  down-right
    (1, -1),  #  down-left
    (-1, 1),  #  up-right
    (-1, -1)  #  up-left
]

word = 'XMAS'
rows = len(grid)
cols = len(grid[0])
count = 0

# check for word
def checkForWord(row, col, direction):
    for i in range(4):
        r = row + i * direction[0]
        c = col + i * direction[1]
        if not (0 <= r < rows and 0 <= c < cols) or grid[r][c] != word[i]:
            return False
    return True

# loop through grid
for row in range(rows):
    for col in range(cols):
        for direction in directions:
            if checkForWord(row, col, direction):
                count += 1

print(count)