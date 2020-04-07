# !/usr/bin/env python
# -*- coding:utf-8 -*-
# description: These implementations are to distinguish in which system the program is executed. To achieve a better performance in all implemented functions. Mainly for print and console functions.
# Python version: 3.7

import sys, os

def exit_console():
    sys.exit()

def combine_path_and_file(ue_path, ue_file):
    return os.path.join(ue_path, ue_file)

def check_file_exist(ue_path, ue_file):
    return os.path.isfile(combine_path_and_file(ue_path, ue_file))

def clean_console():
    if os.name == 'nt':
        # For Windows
        os.system('CLS')
    else:
        # For Linux and Mac
        os.system('clear')

if __name__ == "__main__":
    main()
