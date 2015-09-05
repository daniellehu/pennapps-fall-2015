import json
import copy
import calculate_zip_quality as calc

# Reads and stores the information
def read(file):
    with open(file) as json_data:
        data = json.load(json_data)
    return data

def update_zips(cur_dict, master_dict, template):
    for i in cur_dict.keys():
        if i not in master_dict:
            master_dict[i] = copy.deepcopy(template)

def update_features(dictType ,cur_dict, master_dict):
    for i in cur_dict.keys():
        master_dict[i][dictType] = cur_dict[i]


# imports all data sets and concatenates them into a single dataset
def main():
    # Gathering seperate data sets
    pool_dict = read("pool_dictionary.geojson")
    healthy_corner_dict = read("healthy_corner_dictionary.geojson")
    farmer_market_dict = read("farmer_market_dictionary.geojson")
    parks_dict = read("parks_dictionary.geojson")
    golf_dict = read("golf_dictionary.geojson")
    police_dict = read("police_dict.geojson")
    fire_department_dict = read("fire_dept_dict.geojson")
    recreation_dict = read("recreation_dict.geojson")
    healthcare_dict = read("healthcare_dict.geojson")
    libraries_dict = read("libraries_dict.geojson")
    litter_dict = read("litter_dict.geojson")

    # Template of available data sets
    template = dict(pool=0, healthy_corner=0, farmer_market=0,
                    parks=0, golf=0, police=0, fire_department=0,
                    recreation=0, healthcare=0, libraries=0, litter=0)

    # Master data set to be used in the final product
    master_dict = dict()

    # Updating list of available zips
    update_zips(pool_dict, master_dict, template)
    update_zips(healthy_corner_dict, master_dict, template)
    update_zips(farmer_market_dict, master_dict, template)
    update_zips(parks_dict, master_dict, template)
    update_zips(golf_dict, master_dict, template)
    update_zips(police_dict, master_dict, template)
    update_zips(fire_department_dict, master_dict, template)
    update_zips(recreation_dict, master_dict, template)
    update_zips(healthcare_dict, master_dict, template)
    update_zips(libraries_dict, master_dict, template)
    update_zips(litter_dict, master_dict, template)    

    # Updating features with numerical data
    update_features("pool", pool_dict, master_dict)
    update_features("healthy_corner", healthy_corner_dict, master_dict)
    update_features("farmer_market", farmer_market_dict, master_dict)
    update_features("parks", parks_dict, master_dict)
    update_features("golf", golf_dict, master_dict)
    update_features("police", police_dict, master_dict)
    update_features("fire_department", fire_department_dict, master_dict)
    update_features("recreation", recreation_dict, master_dict)
    update_features("healthcare", healthcare_dict, master_dict)
    update_features("libraries", libraries_dict, master_dict)
    update_features("litter", litter_dict, master_dict)

    # Save the dictionary to the file "master_dict" as a .geojson file
    with open('master_dict.json', 'w') as outfile:
        json.dump(master_dict, outfile)

    output = calc.calculation(master_dict)
    # remove comments to print out the entire master_dictionary
    '''
    for j in master_dict.keys():
        print j 
        print master_dict[j]
    '''


main()
