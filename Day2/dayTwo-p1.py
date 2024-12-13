def safeReport(report):
    increasing = all(report[i] < report[i+1] and 1 <= report[i+1] - report[i] <= 3 for i in range(len(report) - 1))
    decreasing = all(report[i] > report[i+1] and 1 <= report[i] - report[i+1] <= 3 for i in range(len(report) - 1))
    return increasing or decreasing
totalSafe = 0
with open('dayTwoInput.txt', 'r') as file:
    reports = [list(map(int, line.split())) for line in file]

    results = [safeReport(report) for report in reports]
    totalSafe = sum(results)
print(totalSafe) 