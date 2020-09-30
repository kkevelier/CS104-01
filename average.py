numberOfTests = 0
score = 0
total = 0
average = 0.0
scoreCount = 0

numberOfTests = int(input("Please enter the number of tests you want to average: "))

#make these next 3 lines repeat until scoreCount = numberOfTests
while scoreCount < numberOfTests:
    score = int(input("Please enter the score: "))
    
    #scoreCount is at 0 but 1 is added each time a number is inputed by user
    scoreCount += 1
    
    #total is at 0 but a sum accumulates as the user adds more values
    total += score
    
    #When the number of scores = the initial number inputed the loop stops
    if scoreCount == numberOfTests:
        break

average = total/scoreCount
print("The average is ",average)
