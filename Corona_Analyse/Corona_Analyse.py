#!/usr/bin/python
import pprint
from Analysis_functions import *
import Interface_data_europe_eu
import system_handling

menu_actions  = {}
DATA_DIRECTORY = './'
FILE_CORONA_FIG = 'corona_data_eu.csv'

# =======================
#     MENUS FUNCTIONS
# =======================

# Main menu
def main_menu():
    #system_handling.clean_console()
    print("Welcome to the corona analysis tool. ")
    print("Please select the menu item if you want to start:")
    print("1. Download latest statistics")
    print("2. Statistical analyses")
    print("3. Graphical analyses")
    print("0. Quit")
    choice = input(" >>  ")
    exec_menu(choice)

    return

def download():
    # Download the file to use it offline
    # Rethink about this fanction. Does it make sense to transfer the parameters here? Or does this function only download the one document?
    Interface_data_europe_eu.download_corona_data_to_file("https://opendata.ecdc.europa.eu/covid19/casedistribution/csv", FILE_CORONA_FIG)
    print("\n")
    menu_actions['main_menu']()

# Execute menu
def exec_menu(choice):
    system_handling.clean_console()
    ch = choice.lower()
    if ch == '':
        menu_actions['main_menu']()
    else:
        try:
            menu_actions[ch]()
        except KeyError:
            print("No available menu item. Please select a valid number.\n")
            menu_actions['main_menu']()
    return

def menu_1():
    print("Statistical analyses\n")
    print("4. Standard Analysis")
    print("9. Back")
    print("0. Quit")
    choice = input(" >>  ")
    exec_menu(choice)
    return

def s_standard_analysis():
    ############################################################
    print("-- Corona Analysis start --\n")
    ############################################################
    # Download and parse
    ############################################################
    # download from eu server
    # and convert csv data to list of dictionarys
    corona_data_dictlist = Interface_data_europe_eu.download_corona_data_as_dictlist()
    ############################################################
    # Analyze
    ############################################################
    print("Starting to analyze data\n")
    #show all Countries
    #print_countrys(corona_data_dictlist)
    base_analysis(corona_data_dictlist)
    menu_actions['main_menu']()

def menu_2():
    print("Graphical analyses\n")
    print("5. Show cases and deaths as graph from Germany")
    print("9. Back")
    print("0. Quit")
    choice = input(" >>  ")
    exec_menu(choice)
    return

def g_standard_analysis():
    if system_handling.check_file_exist(DATA_DIRECTORY, FILE_CORONA_FIG) == False:
        Interface_data_europe_eu.download_corona_data_to_file("https://opendata.ecdc.europa.eu/covid19/casedistribution/csv", FILE_CORONA_FIG)
    print_current_figures_in_germany(system_handling.combine_path_and_file(DATA_DIRECTORY, FILE_CORONA_FIG))
    menu_actions['main_menu']()
def back():
    menu_actions['main_menu']()

def exit():
    system_handling.exit_console()

# Menu definition
menu_actions = {
    'main_menu': main_menu,
    '1': download,
    '2': menu_1,
    '3': menu_2,
    '4': s_standard_analysis,
    '5': g_standard_analysis,
    '9': back,
    '0': exit,
    }

if __name__ == "__main__":
    # scheduling
    main_menu()
