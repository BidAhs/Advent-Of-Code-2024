import re

with open('dayThreeInput.txt') as file:
    content = file.read()

pattern = r"mul\((\d+),(\d+)\)"
matches = re.findall(pattern, content)

total = 0
for match in matches:
    num1, num2 = map(int, match) 
    total += num1 * num2
print(total)