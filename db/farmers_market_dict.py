import json

# Reads the farmer data and then creates a dictionary with the zip as a key
# and the number of markets as its val
def read(file):
    with open(file) as json_data:
        data = json.load(json_data)
        zips = dict()

        for i in xrange(len(data["features"])):
            #Reading in the zip codes where farmers markets are located
            cur = data["features"][i]["properties"]["ZIP"]
            # Storing it into a dictionary
            if cur in zips:
                zips[cur] = zips[cur] + 1
            elif cur != None:
                zips[cur] = 1
    
    return zips

# Returns a dict with the zipcode as the key and the number of markets
# as the value
def main():
    zips = read("Farmers_Markets.geojson")
    print zips
    return zips

main()