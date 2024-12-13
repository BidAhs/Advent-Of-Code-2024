# empty lists for columns
leftCol = []
rightCol = []

# open file process each line
with open('dayOneInput.txt', 'r') as file:
    for line in file:
        left, right = map(int, line.split())
        leftCol.append(left)
        rightCol.append(right)

# sort small to high
leftCol.sort()
rightCol.sort()
# compare small to small from each column
sorted_pairs = list(zip(leftCol, rightCol))

# find total distance 
total = 0
for pair in sorted_pairs:
    total += abs(pair[0] - pair[1])

print(total)