import csv
import pprint
import datetime
import urllib.parse
import urllib.request
import os

eu_corona_data_url = "https://opendata.ecdc.europa.eu/covid19/casedistribution/csv"
corona_file_name = 'corona_data.csv'

def download_corona_data_to_file(url,corona_file_name):
	print("Download corona data...")
	dir_path = os.path.dirname(os.path.realpath(__file__)) + "/"
	urllib.request.urlretrieve(url, dir_path + corona_file_name)
	print("Download corona data successful" + "data written to file " + corona_file_name)

	
def dict_list_from_csv_file(variables_file):
    print("Converting csv data to list of dictionarys")
    # Open variable-based csv, iterate over the rows and map values to a list of dictionaries containing key/value pairs
    reader = csv.DictReader(open(variables_file, 'rt'))
    dict_list = []
    for line in reader:
        dict_list.append(line)
    print("Converting csv data to list of dictionarys successful")
    return dict_list

def elements_of_actual_day(dict_list):
    print("Parse corona data for today")
    date_today = datetime.datetime.now()
    actual_day_elemets = elements_of_day(dict_list,date_today)
    print("Parse corona data for today successful")
    return actual_day_elemets

def elements_of_day(dict_list, date):
    date_today_str = date.strftime("%d/%m/%Y")
    print("Parse Corona data for day: " + date_today_str)
    day_elements = []
    for element in dict_list:
        if element.get("dateRep") == date_today_str:
            day_elements.append(element)
    print("Parse Corona data for day sucessful")
    return day_elements


print("-- Corona Analysis start --")

#download from eu server
download_corona_data_to_file(eu_corona_data_url, corona_file_name)

#convert csv data to list of dictionarys
# keys in dicts will be:dateRep,day,month,year,cases,deaths,countriesAndTerritories,geoId,countryterritoryCode,popData2018
corona_data_dictlist = dict_list_from_csv_file(corona_file_name)

#filter for data of current day
actual_day_data_dictlist = elements_of_actual_day(corona_data_dictlist)

pprint.pprint(actual_day_data_dictlist)
	






 





