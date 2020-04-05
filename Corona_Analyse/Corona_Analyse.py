import pprint

from base_Operations import *

eu_corona_data_url = "https://opendata.ecdc.europa.eu/covid19/casedistribution/csv"
corona_file_name = 'corona_data.csv'

print("-- Corona Analysis start --")

# download from eu server
download_corona_data_to_file(eu_corona_data_url, corona_file_name)

# convert csv data to list of dictionarys
corona_data_dictlist = dict_list_from_csv_file(corona_file_name)

# filter for data of current day
actual_day_data_dictlist = elements_of_actual_day(corona_data_dictlist)

# filter for country
country_data_dictlist = elements_of_country(actual_day_data_dictlist, Countries.Germany)

#show all Countries
print_countrys(corona_data_dictlist)

#print info for today germany
pprint.pprint(elements_of_country(actual_day_data_dictlist, Countries.Germany))	






 





