# empty lists for the columns
leftCol = []
rightCol = []

# open file and process each line
with open('dayOneInput.txt', 'r') as file:
    for line in file:
        # Split the line into two parts
        parts = line.strip().split()
        if len(parts) == 2:
            leftCol.append(int(parts[0]))
            rightCol.append(int(parts[1]))

# loop through left column compare to count of right
score = 0
for i in range(len(leftCol)):
    score += leftCol[i] * rightCol.count(leftCol[i])
print(score)