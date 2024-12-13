def safeReport(report):
    # check if increasing or decreasing
    increasing = all(report[i] < report[i+1] and 1 <= report[i+1] - report[i] <= 3 for i in range(len(report) - 1))
    decreasing = all(report[i] > report[i+1] and 1 <= report[i] - report[i+1] <= 3 for i in range(len(report) - 1))
    
    if increasing or decreasing:
        return True
    
    # Check for bad level
    for i in range(len(report)):
        newReport = report[:i] + report[i+1:]  # Create a new report without the i-th element
        if all(newReport[j] < newReport[j+1] and 1 <= newReport[j+1] - newReport[j] <= 3 for j in range(len(newReport) - 1)) or \
           all(newReport[j] > newReport[j+1] and 1 <= newReport[j] - newReport[j+1] <= 3 for j in range(len(newReport) - 1)):
            return True
    
    return False

totalSafe = 0
with open('dayTwoInput.txt', 'r') as file:
    reports = [list(map(int, line.split())) for line in file]
    results = [safeReport(report) for report in reports]
    totalSafe = sum(results)

print(totalSafe)
