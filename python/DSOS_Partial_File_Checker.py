def convertData(inputFile): 
    with open(inputFile, "r") as f:
        setOfFileDetails = set(f.readlines())
    f.close()
    return setOfFileDetails

setOfDsosDaqFiles = convertData("C:/Users/mpatil/WorkSpace/Production_Issues/TS-2909/Prod_After_Fix/MUNI_DAQ.txt")

setOfDsosRepoFiles = convertData("C:/Users/mpatil/WorkSpace/Production_Issues/TS-2909/Prod_After_Fix/dsos_muni.repo")

setOfDsosUdlMetrics = convertData("C:/Users/mpatil/WorkSpace/Production_Issues/TS-2909/Prod_After_Fix/MUNI_UdlMetrics.txt")

for line in list(setOfDsosDaqFiles - setOfDsosRepoFiles):
    entry = line.replace("\n", "")
    print(entry)