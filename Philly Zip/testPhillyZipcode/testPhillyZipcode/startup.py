"""
This file functions as the startup file for the project.
"""

from testPhillyZipcode import parseData
import os
import json
from geopy.geocoders import Nominatim, Bing, GoogleV3
import random

NomGeo = Nominatim()
GoogleGeo = GoogleV3(api_key="AIzaSyApwMLR3DeQIt9xZnuzhYVkLQWkhpmU80s")
BingGeo = Bing(api_key="AiGUQfZyZFqGzOjObdMetvAiYV-kqsY5hTspooG4SLhwa5FakjGTDzYwVLWgKtsk")
GoogleGeo2 = GoogleV3(api_key="AIzaSyD84mq1aMGnX0Mm7sG9nsdB8PMWge3vi3k")

def getPoliceData(geolocator):
    path = os.path.join("testPhillyZipcode", "data", "Police_Stations.json")
    data = parseData.getData(path, geolocator)
    parseData.saveOutput(data, "police_dict")

def getFireDeptData(geolocator):
    path = os.path.join("testPhillyZipcode", "data", "Fire_Dept_Facilities.json")
    data = parseData.getData(path, geolocator)
    parseData.saveOutput(data, "fire_dept_dict")

def getLibraryData(geolocator):
    path = os.path.join("testPhillyZipcode", "data", "Libraries.json")
    data = parseData.getData(path, geolocator)
    parseData.saveOutput(data, "libraries_dict")

def getCrashesData(geolocator):
    path = os.path.join("testPhillyZipcode", "data", "all_crashes_2012.json")
    data = parseData.getData(path, geolocator)
    parseData.saveOutput(data, "crashes_dict")

def getRecFacilitiesData(geolocator):
    path = os.path.join("testPhillyZipcode", "data", "Rec_Facilities.json")
    data = parseData.getData(path, geolocator)
    parseData.saveOutput(data, "rec_facilities_dict")

#getPoliceData(GoogleGeo)
#getFireDeptData(GoogleGeo)
#getLibraryData(GoogleGeo)
#getCrashesData(BingGeo)
#getRecFacilitiesData(GoogleGeo)

def getLitterData(geolocator):
    path = os.path.join("testPhillyZipcode", "data", "litter_index.json")
    data = parseData.getLitterData(path, geolocator)
    parseData.saveOutput(data, "litter_dict")

getLitterData(GoogleGeo2)