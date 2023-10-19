with open("C:/Users/mpatil/WorkSpace/Production_Issues/TS-2989/XrfInstrumentLinkDetails.out", "r") as f:
    setOfInsLinks = set(f.readlines())
f.close()

with open("C:/Users/mpatil/WorkSpace/Production_Issues/TS-2989/XrfSecurityLinkDetails.out", "r") as f:
    setOfSecLinks = set(f.readlines())
f.close()
  
for line in list(setOfSecLinks - setOfInsLinks):
    entry = line.replace("\n", "")
    print(entry)