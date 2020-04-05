import csv
import pprint
import datetime
import urllib.parse
import urllib.request
import os

from Parameter_containers import Countries, Keys_eu


def download_corona_data_to_file(url,corona_file_name):
	print("Download corona data...")
	dir_path = os.path.dirname(os.path.realpath(__file__)) + "/"
	urllib.request.urlretrieve(url, dir_path + corona_file_name)
	print("Download corona data successful" + "data written to file " + corona_file_name)

def dict_list_from_csv_file(variables_file):
    # Open variable-based csv, iterate over the rows and map values to a list of dictionaries containing key/value pairs
    reader = csv.DictReader(open(variables_file, 'rt'))
    dict_list = []
    for line in reader:
        dict_list.append(line)
    return dict_list

def elements_of_actual_day(dict_list):
    date_today = datetime.datetime.now()
    actual_day_elemets = elements_of_day(dict_list,date_today)
    return actual_day_elemets

def elements_of_day(dict_list, date):
    date_today_str = date.strftime("%d/%m/%Y")
    day_elements = []
    for element in dict_list:
        if element.get(Keys_eu.DateRep) == date_today_str:
            day_elements.append(element)
    return day_elements

def elements_of_country(dict_list, country):
    country_elements = []
    for element in dict_list:
        if element.get(Keys_eu.CountriesAndTerritories) == country:
            country_elements.append(element)
    return country_elements

def print_Countries(dict_list):
    Countries = []
    temp_elements = elements_of_actual_day(dict_list)#returns also country unique elements
    for element in temp_elements:
        print(element.get(Keys_eu.CountriesAndTerritories))
