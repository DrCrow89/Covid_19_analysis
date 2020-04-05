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

# filter for data of current day
actual_day_data_dictlist = elements_of_actual_day(corona_data_dictlist)

############################################################
# Analyze
############################################################
print("")
print("Starting to analyze data")
print("")
#show all Countries
#print_countrys(corona_data_dictlist)

# Deaths today worldwide
deaths_today = cumulate_deaths(actual_day_data_dictlist)
print("deaths today worldwide: " + str(deaths_today))

# Cases today worldwide
cases_today = cumulate_cases(actual_day_data_dictlist)
print("cases today worldwide: " + str(cases_today))


# Cumulate deaths worldwide
deaths_worldwide = cumulate_deaths(corona_data_dictlist)
print("deaths worldwide: " + str(deaths_worldwide))

# Cumulate cases worldwide
cases_worldwide = cumulate_cases(corona_data_dictlist)
print("cases worldwide: " + str(cases_worldwide))


# Cumulate deaths germany
country_germany_dictlist = elements_of_country(corona_data_dictlist, Countries.Germany)
deaths_germany = cumulate_deaths(country_germany_dictlist)
print("deaths germany: " + str(deaths_germany))

# Cumulate cases germany
cases_germany = cumulate_cases(country_germany_dictlist)
print("cases germany: " + str(cases_germany))
popData_germany = int(country_germany_dictlist[0].get(Keys_eu.PopData2018))
cases_germany_percent = (cases_germany / popData_germany)*100
print("in percent: %8.2f of Population" % cases_germany_percent)

# Cumulate deaths germany today
country_germany_dictlist_today = elements_of_country(actual_day_data_dictlist, Countries.Germany)
deaths_germany_today = cumulate_deaths(country_germany_dictlist_today)
print("deaths germany today: " + str(deaths_germany_today))

# Cumulate cases germany today
cases_germany_today = cumulate_cases(country_germany_dictlist_today)
print("cases germany today: " + str(cases_germany_today))


print("")





 





