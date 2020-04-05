import pprint

from Analysis_functions import *
import Interface_data_europe_eu 



############################################################
print("-- Corona Analysis start --")
############################################################
# Download and parse
############################################################
# download from eu server
# and convert csv data to list of dictionarys
corona_data_dictlist = Interface_data_europe_eu.download_corona_data_as_dictlist()


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





 





