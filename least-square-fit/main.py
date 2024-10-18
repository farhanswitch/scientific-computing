precision = 4

def formatNumber(num: float) -> float:
    return round(num, precision)

listData = [
    {"x": 0, "y": 14.6210},
    {"x": 8, "y": 11.8430},
    {"x": 16, "y": 9.8700},
    {"x": 24, "y": 8.4180},
    {"x": 32, "y": 7.3050},
    {"x": 40, "y": 6.4130},
]

listValueToPredict = [
    {"x": 4, "y": 0},
    {"x": 12, "y": 0},
    {"x": 28, "y": 0},
    {"x": 36, "y": 0},
]

average = {
    "x": formatNumber(sum([d["x"] for d in listData]) / len(listData)),
    "y": formatNumber(sum([d["y"] for d in listData]) / len(listData)),
}

def computeSlope(listData, average):
    sumOfY = 0
    sumOfX = 0
    for current in listData:
        sumOfX += formatNumber(current["x"] * (current["x"] - average["x"]))
        sumOfY += formatNumber(current["y"] * (current["x"] - average["x"]))
    return formatNumber(sumOfY / sumOfX)

def computeIntercept(average, slope):
    return formatNumber(average["y"] - average["x"] * slope)

slope = computeSlope(listData, average)
intercept = computeIntercept(average, slope)

print(f"Function to predict the value -> f(x) = {intercept} + {slope}x")

def predict(x, slope, intercept):
    return formatNumber(intercept + slope * x)

for i in range(len(listValueToPredict)):
    listValueToPredict[i]["y"] = predict(listValueToPredict[i]["x"], slope, intercept)

print(listValueToPredict)

def computeStandardDeviation(listData):
    sumOfError = 0
    for current in listData:
        sumOfError += formatNumber(
            (current["y"] - predict(current["x"], slope, intercept)) ** 2
        )
    return formatNumber((sumOfError / (len(listData) - 2)) ** 0.5)

print(f"The standard deviation is: {computeStandardDeviation(listData)}")
