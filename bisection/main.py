def formatNumber(num, precision):
    return round(num, precision)

def equation(x):
    return x ** 3 - 10 * x ** 2 + 5

interval = [0.6, 0.8]
counter = 0
finalResult = 0

while True:
    if counter == 0:
        yValueOfLowerBound = equation(interval[0])
        yValueOfUpperBound = equation(interval[1])
        print({
            'x': interval[0],
            'F(x)': yValueOfLowerBound,
            'interval': '-',
        })
        print({
            'x': interval[1],
            'F(x)': yValueOfUpperBound,
            'interval': f'({interval[0]}, {interval[1]})',
        })
        isRootExists = yValueOfLowerBound * yValueOfUpperBound < 0
        if not isRootExists:
            print(f'There is no root in interval {interval[0]} - {interval[1]}')
            break

    halfOfInterval = (interval[0] + interval[1]) / 2
    yValueOfHalfInterval = equation(halfOfInterval)

    if formatNumber(yValueOfHalfInterval, 3) == 0.0:
        print({
            'x': f'({interval[0]} + {interval[1]})/2 = {halfOfInterval}',
            'F(x)': formatNumber(yValueOfHalfInterval, 3),
            'interval': '-',
        })
        finalResult = halfOfInterval
        break
    else:
        if yValueOfHalfInterval > 0:
            interval[0] = halfOfInterval
        else:
            interval[1] = halfOfInterval

    print({
        'x': f'({interval[0]} + {interval[1]})/2 = {halfOfInterval}',
        'F(x)': yValueOfHalfInterval,
        'interval': f'({interval[0]}, {interval[1]})',
    })
    
    counter += 1

print({
    'finalResult': formatNumber(finalResult, 4),
    # Plus 3 because 2 first counter is calculating yValue of both interval border and plus one when calculating y value that has value 0.000
    'counter': counter + 3,
})
