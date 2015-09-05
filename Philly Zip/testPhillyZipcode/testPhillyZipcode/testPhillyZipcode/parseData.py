import json
import os

def findZipcode(lat, long, geolocator):
    point = "{0}, {1}".format(lat, long)
    print "point =", point
    return geolocator.reverse(point, exactly_one=True)

def getData(file, geolocator):
    output = {}
    with open(file, 'r') as json_data:
        d = json.load(json_data)
        for f in d['features']:
            coord = f['geometry']['coordinates']
            long, lat = coord[0], coord[1]
            loc = findZipcode(lat, long, geolocator)
            if loc != None:
                zip = loc.address.strip(", USA")[-5:]
                if "19" in zip:
                    print "loc =", loc, "\nzip =", zip
                    if zip in output:
                        output[zip] += 1
                    else:
                        output[zip] = 1
    return output

def getLitterData(file, geolocator):
    output = {}
    with open(file, 'r') as json_data:
        d = json.load(json_data)
        for f in d['features']:
            polygon = f['geometry']['coordinates']
            litter = f['properties']['SCORE0913']
            for coords in polygon:
                coord = coords[len(coords)/2]
                print "coord =",coord
                print "litter = ", litter
                long, lat = coord[0], coord[1]
                loc = findZipcode(lat, long, geolocator)
                if loc != None:
                    zip = loc.address.strip(", USA")[-5:]
                    if "19" in zip:
                        print "loc =", loc, "\nzip =", zip
                        addAverageToDatabase(zip, output, litter)
    return output

def saveOutput(data, name):
    path = os.path.join("testPhillyZipcode", "output", name)
    with open(path + ".geojson", 'w') as outfile:
        json.dump(data, outfile)
    #with open(path+'.json', 'w') as outfile:
    #    json.dump(data, outfile)

def addAverageToDatabase(zip, output, value):
    if zip in output:
        newVal = (output[zip] + value) / 2.0
        output[zip] = newVal
    else:
        output[zip] = value