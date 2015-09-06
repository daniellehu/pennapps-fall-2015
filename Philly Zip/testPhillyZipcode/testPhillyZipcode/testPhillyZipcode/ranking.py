from pydocumentdb import document_client
import config

def getDatabaseDict():
    client = document_client.DocumentClient(config.DOCUMENTDB_HOST, {'masterKey': config.DOCUMENTDB_KEY})
    # Read databases and take the first since the id should not be duplicated.
    for data in client.ReadDatabases():
        if data['id'] == config.DOCUMENTDB_DATABASE:
            db = data
            break
    for coll in client.ReadCollections(db['_self']):
        if coll['id'] == config.DOCUMENTDB_COLLECTION:
            collection = coll
            break
    for doc in client.ReadDocuments(collection['_self']):
        if doc['id'] == config.DOCUMENTDB_DOCUMENT:
            dictionary = doc
            break
    print "dict =",dictionary
    return dictionary

# Takes in data dictionary and user input dictionary
def calculation(data, inputs):
    # Creating the zipcode viability dictionary
    output = dict()
    for i in data.keys():
        if "19" in i:
            output[i] = 0

    max_quality = 1
    # Calculating how well the zipcodes fit the user parameters
    for j in data.keys():
        if "19" in j:
            quality = 0.0
            for k in inputs.keys():
                quality = quality + float(inputs[k]) * data[j][k]

            # Checking for the highest quality of neighborhood and saving
            # the highest quality number for the user
            if quality > max_quality:
                max_quality = quality
            output[j] = quality

    # Regularizing the output
    for l in output.keys():
        output[l] = output[l] / max_quality
        # print output[l]
    
    return output

fake_inputs = dict(pool=5, healthy_corner=3, farmer_market=7,
                   parks=1, golf=10, police=5, fire_department=1,
                   recreation=8, healthcare=5, libraries=4, litter=7)
