# Young Kyu Kim
# Assignment 1 : Naive Bayes Theorem
# September 22nd, 2019
#
# Usage: testBayes.data and testBayes.trainlabels.0 in the same directory as young_kyu_kim_assignment1.py
#

from math import sqrt, exp, pow, pi

trainData = 'testBayes.data'
labelData = 'testBayes.trainlabels.0'
output = 'output.txt'

def getMeansOfPair(arr):
    n = len(arr)
    sumFirst = 0
    sumSecond = 0
    for x in arr:
        pair = x.split(' ')
        sumFirst += int(pair[0])
        sumSecond += int(pair[1])
    return [sumFirst/n, sumSecond/n]

def getVarianceOfPair(arr, mean):
    n = len(arr)
    sumFirst = 0
    sumSecond = 0

    for x in arr:
        pair = x.split(' ')
        first = int(pair[0]) - mean[0]
        second = int(pair[1]) - mean[1]
        sumFirst += (first * first)
        sumSecond += (second * second)

    return [sumFirst/n, sumSecond/n]

#process input
lines = None
groupByLabel = {}

lengthOfLabel = 0


with open(labelData, 'r') as f:
    lines = f.readlines()

lengthOfLabel = len(lines)

# Grouping
if lines is not None:
    for line in lines:
        labelDataContent = line.replace('\n', '').split(' ')
        label = labelDataContent[0]

        if label in groupByLabel.keys():
            items = groupByLabel[label]
        else:
            groupByLabel[label] = []
            items = groupByLabel[label]
        items.append(labelDataContent[1])

    with open(trainData, 'r') as f:
        lines = f.readlines()

    inputLines = []
    for x in lines:
        inputLines.append(x.replace('\n', ''))

    topGroup = None
    bottomGroup = None

    for key, value in groupByLabel.items():
        if topGroup is None:
            topGroup = value
            # print('A group:', key)
        else:
            bottomGroup = value

    top = []
    bottom = []
    # missing index in testlabel
    testingPairs = []

    for lineIndex in range(0, len(inputLines)):
        if str(lineIndex) in topGroup:
            top.append(inputLines[lineIndex])
        elif str(lineIndex) in bottomGroup:
            bottom.append(inputLines[lineIndex])
        else:
            testingPairs.append(inputLines[lineIndex])

    # print('class0 group: ', top)
    # print('class1 group: ', bottom)
    # print('testing group: ', testingPairs)
    # print('\n')

    # mean vector of class +1
    meansOfTop = getMeansOfPair(top)

    # mean vector of class -1
    meansOfBottom = getMeansOfPair(bottom)

    # print('means Of class0: ', meansOfTop)
    # print('means Of class1: ', meansOfBottom)

    # variance vecotr of class + 1
    varianceOfTop = getVarianceOfPair(top, meansOfTop)

    # variance of vector of class -1
    varianceOfBottom = getVarianceOfPair(bottom, meansOfBottom)

    # print('variance Of class0: ', varianceOfTop)
    # print('variance Of class1: ', varianceOfBottom)
    # print('\n')

    index = lengthOfLabel - 1
    for test in testingPairs:
        pair = test.split(' ')
        first = int(pair[0])
        second = int(pair[1])
        targetClass = None
        index += 1

        distanceOfLineToTop = ((first-meansOfTop[0])*(first-meansOfTop[0])) + ((second-meansOfTop[1])*(second-meansOfTop[1]))
        distanceOfLineToBottom = ((first-meansOfBottom[0])*(first-meansOfBottom[0])) + ((second-meansOfBottom[1])*(second-meansOfBottom[1]))
        squareRoot_1 = sqrt(distanceOfLineToTop)
        squareRoot_2 = sqrt(distanceOfLineToBottom)

        naiveBayesDistanceOfLineToTop = (((first - meansOfTop[0]) * (first - meansOfTop[0]))/varianceOfTop[0]) + ((
                    (second - meansOfTop[1]) * (second - meansOfTop[1]))/varianceOfTop[1])
        naiveBayesDistanceOfLineToBottom = (((first - meansOfBottom[0]) * (first - meansOfBottom[0]))/varianceOfBottom[0]) + ((
                    (second - meansOfBottom[1]) * (second - meansOfBottom[1]))/varianceOfBottom[1])

        # print('target pair: ', pair)
        # print('distanceOfLine To class0: ', distanceOfLineToTop)
        # print('distanceOfLine To class1: ', distanceOfLineToBottom)
        # print('naiveBayesDistance Of Line To class0: ', naiveBayesDistanceOfLineToTop)
        # print('naiveBayesDistance Of Line To class1: ', naiveBayesDistanceOfLineToBottom)
        # print('\n')

        if(naiveBayesDistanceOfLineToTop < naiveBayesDistanceOfLineToBottom):
            targetClass = 0
        else:
            targetClass = 1

        with open(output, 'a') as f:
            f.write(str(targetClass) + ' ' + str(index) + '\n')
