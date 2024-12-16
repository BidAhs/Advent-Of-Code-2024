import re

# read input file
with open('dayThreeInput.txt') as file:
    content = file.read()

# patterns
instruction_pattern = r"\b(do\(\)|don't\(\))"
mul_pattern = r"mul\((\d+),(\d+)\)"

# easy processing 
tokens = re.split(r"(\bdo\(\)|\bdon't\(\)|mul\(\d+,\d+\))", content)

mul_enabled = True
total = 0

# process each token
for token in tokens:
    token = token.strip()
    if token == "do()":
        mul_enabled = True
    elif token == "don't()":
        mul_enabled = False
    elif re.match(mul_pattern, token):
        if mul_enabled:
            num1, num2 = map(int, re.findall(r"\d+", token))
            total += num1 * num2

print(total)
