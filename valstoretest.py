import json

testdata = '{"Java": "3 Credits", "PHP": "2 Credits", "C++": "3 Credits"}'
storedata = json.loads(testdata)
try:
    with open('cryptotracker_DB.json') as f:
        data = json.load(f)    
except json.decoder.JSONDecodeError:
    with open("cryptotracker_DB.json", "a") as write_file:
        json.dump(testdata, write_file)
    print("No file or empty file - started new DB")
except FileNotFoundError:
    with open("cryptotracker_DB.json", "a") as write_file:
        json.dump(testdata, write_file)
    print("No file or empty file - started new DB")
else:
    with open("cryptotracker_DB.json", "a") as write_file:
        json.dump(testdata, write_file)
    # for val in storedata:
    # print(f"{val} {storedata}")
try:
    print(data)
except NameError:
    pass