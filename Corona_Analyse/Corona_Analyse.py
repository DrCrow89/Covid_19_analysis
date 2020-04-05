import pprint

from base_Operations import *
from Analysis_functions import *

eu_corona_data_url = "https://opendata.ecdc.europa.eu/covid19/casedistribution/csv"
corona_file_name = 'corona_data.csv'

############################################################
print("-- Corona Analysis start --")
############################################################
# Download and parse
############################################################
# download from eu server
download_corona_data_to_file(eu_corona_data_url, corona_file_name)

# convert csv data to list of dictionarys
corona_data_dictlist = dict_list_from_csv_file(corona_file_name)


############################################################
# Analyze
############################################################
print("")
print("Starting to analyze data")
print("")
#show all Countries
#print_countrys(corona_data_dictlist)

base_analysis(corona_data_dictlist)


print("")





 





