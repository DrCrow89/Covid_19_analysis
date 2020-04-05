import urllib.parse
import urllib.request
import os
import csv

eu_corona_data_url = "https://opendata.ecdc.europa.eu/covid19/casedistribution/csv"
corona_file_name = 'corona_data_eu.csv'

def download_corona_data_as_dictlist():
    download_corona_data_to_file(eu_corona_data_url, corona_file_name)

    # convert csv data to list of dictionarys
    corona_data_dictlist = dict_list_from_csv_file(corona_file_name)
    return corona_data_dictlist


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
