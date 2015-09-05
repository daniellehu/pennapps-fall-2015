import json

# Reads the corner store data and then creates a dictionary with the zip as 
# a key and the number of stores as its val
def read(file):
    with open(file) as json_data:
        data = json.load(json_data)
        zips = dict()
        for i in xrange(len(data["features"])):
            #Reading in the zip code of the corner store location
            cur = data["features"][i]["properties"]["ZIP"]
            # Storing it into a dictionary
            if cur in zips:
                zips[cur] = zips[cur] + 1
            elif cur != None:
                zips[cur] = 1
    return zips
# Returns a dict with the zipcode as the key and the number of healthy corner 
# stores as the value
def main():
    zips = read("Healthy_Corner_Stores.geojson")
    with open('healthy_corner_dictionary.geojson', 'w') as outfile:
        json.dump(zips, outfile)

    return zips

main()