numberOfTests = 0
score = 0
total = 0
average = 0.0
scoreCount = 0

numberOfTests = int(input("Please enter the number of tests you want to average: "))
#make these next 3 lines repeat until scoreCount = numberOfTests
score = int(input("Please enter a score: "))
scoreCount = scoreCount + 1
total = total + score

average = (score1 + score2)/2
print("The average is ",average)
