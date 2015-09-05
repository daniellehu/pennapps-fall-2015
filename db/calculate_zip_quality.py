def calculation(data, inputs = []):
    # Creating a fake input for testing purposes
    fake_inputs = dict(pool=5, healthy_corner=3, farmer_market=7,
                    parks=0, golf=10, police=5, fire_department=1,
                    recreation=8, healthcare=5, libraries=4, litter=7)
    
    # Creating the zipcode viability dictionary
    output = dict()
    for i in data.keys():
        output[i] = 0

    max_quality = 1
    # Calculating how well the zipcodes fit the user parameters
    for j in data.keys():
        quality = 0.0
        for k in fake_inputs.keys():
            quality = quality + float(fake_inputs[k]) * data[j][k]

        # Checking for the highest quality of neighborhood and saving
        # the highest quality number for the user
        if quality > max_quality:
            max_quality = quality
        output[j] = quality

    # Regularizing the output
    for l in output.keys():
        output[l] = output[l] / max_quality
        print output[l]