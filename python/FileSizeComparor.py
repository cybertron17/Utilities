listOfVfsMetrics = [
"annadaily230907.txt,306787438",
"annadaily230908.txt,158063215",
"annadaily230911.txt,209055580",
"annadaily230912.txt,209279301",
"annadaily230913.txt,207518212",
"annadaily230914.txt,173148057",
"annadaily230915.txt,222359574",
"annadaily230918.txt,217617382",
"annadaily230919.txt,196609485",
"annadaily230920.txt,192034974",
"annadaily230921.txt,178813926",
"annadaily230922.txt,185824903",
"annadaily230925.txt,216991669",
"annadaily230926.txt,185680822",
"annadaily230927.txt,197667676",
"annadaily230928.txt,164686834",
"annadaily230929.txt,198240517",
"annadaily231002.txt,246721274",
"annadaily231003.txt,216076330",
"annadaily231004.txt,177894084"
]

listOfUdlMetrics = [
"annadaily231004.txt,19841024",
"annadaily231003.txt,194887680",
"annadaily231002.txt,163168256",
"annadaily230929.txt,74366976",
"annadaily230928.txt,164686834",
"annadaily230927.txt,126509056",
"annadaily230926.txt,167886848",
"annadaily230925.txt,216991669",
"annadaily230925.txt,163299328",
"annadaily230922.txt,185824903",
"annadaily230922.txt,120045568",
"annadaily230921.txt,178813926",
"annadaily230921.txt,143048704",
"annadaily230920.txt,43892736",
"annadaily230919.txt,196609485",
"annadaily230918.txt,95748096",
"annadaily230915.txt,222359574",
"annadaily230915.txt,90292224",
"annadaily230914.txt,173148057",
"annadaily230914.txt,67223552",
"annadaily230913.txt,207518212",
"annadaily230913.txt,53768192",
"annadaily230912.txt,209279301",
"annadaily230912.txt,88457216",
"annadaily230911.txt,209055580",
"annadaily230911.txt,93765632",
"annadaily230908.txt,158063215",
"annadaily230908.txt,101695488",
"annadaily230907.txt,306787438",
"annadaily230907.txt,27639808"
]

udlMetricsDict = {}

for entry in listOfUdlMetrics:
    splitEntry = entry.split(',')
    if splitEntry[0] in udlMetricsDict:
        if int(udlMetricsDict[splitEntry[0]]) < int(splitEntry[1]):
            udlMetricsDict[splitEntry[0]] = int(splitEntry[1])
    else:
        udlMetricsDict[splitEntry[0]] = int(splitEntry[1])

for entry in listOfVfsMetrics:
    splitEntry = entry.split(',')
    if udlMetricsDict[splitEntry[0]] != int(splitEntry[1]):
        print(splitEntry[0])