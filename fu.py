import json

FILE="data/viwe.json"

def read_json():
    try:
        with open (FILE) as f:
            data=json.load(f)
        return data
    except:
        with open (FILE,"w") as f:
            data={"students":[]}
            json.dump(data,f,indent=3)
    return data
def write_json(data):
    with open(FILE,"w") as f:
        json.dump(data,f,indent=3)