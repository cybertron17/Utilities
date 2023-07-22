import json

with open("C:/Users/mpatil/WorkSpace/Production_Issues/TS-2866/FEED_FILES/GOVCORP_ASSET_FULL_20230422212025_00003.txt", "r") as f:
    input_data = f.readlines()
f.close()

finalOutput = open("C:/Users/mpatil/WorkSpace/Production_Issues/TS-2866/FEED_FILES/ASSET_IDs.txt", "a")
for data in input_data:
    json_data = json.loads(data)
    parsed_data = json.dumps(json_data["govcorp"]["asset"]["asset_id"])
    finalOutput.write(parsed_data + "\n")

finalOutput.close()