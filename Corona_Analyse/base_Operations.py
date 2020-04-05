import pprint
import datetime

from Parameter_containers import Countries, Keys_eu



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
