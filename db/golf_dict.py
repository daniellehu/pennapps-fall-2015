import json

# Reads and stores the information
def read(file):
    with open(file) as json_data:
        data = json.load(json_data)
        zips = dict()

        for i in xrange(len(data["features"])):
            #Reading in the zip code
            cur = int(data["features"][i]["properties"]["ZIPCODE"])
            # Storing it into a dictionary
            if cur in zips:
                zips[cur] = zips[cur] + 1
            elif cur != None:
                zips[cur] = 1
    return zips

# Returns a dict with the zipcode as the key and the number of locations
# as the value
def main():
    zips = read("Golf_point.geojson")
    print zips
    return zips

main()