#!/usr/bin/env python3

import time
from verif import verif
from shfunc import load
from hierarchy import comput_hierarchy
from phymat import comput_vcv, comput_anv
from print import probject

v = '0.1.1' # Current version of software

print(f"#######################\n###                 ###\n###   TTiP v{v}   ###\n###                 ###\n#######################\n\nDesigned and coded by M. G. Faure-Brac.\nContact at: faurebrac.mathieu@gmail.com, or through GitHub.\n\n")

## DICTIONNARIES ##
trees_list = {} # Containing all objects of class 'tree_obj'

## LISTS ##
tax_val = []
nod_tax = []
nod_val = []
hierarchy = []
val = []
abs_nod_val = []
root_tip = []

## VARIABLES ##
options = "12345678"
# 1 - Load file
# 2 - Verif + hierarchy
# 3 - Branch length
# 4 - Assemble
# 5 - Manipulate
# 6 - Print
# 7 - Parameters
# 8 - EXIT TO DESKTOP
param = "123"
# 1 - Verbose
# 2 - Speed
# 3 - EXIT TO MENU
yn = "yn"
path_tree = ""

# DEFAULT PARAMETERS #
verbose = True
speed = 0.05 # Speed of time.sleep if verbose == T
q = False # Exit variable

while q == False:
    choice = input("What do you want to do?\n\n1) Load a file\n2) Check tree structure\n3) Check tree branch lengths\n4) Assemble trees\n5) Manipulate trees\n6) Print output\n7) Access parameters\n8) Quit TTiP\n\n Your choice :  ")
    while options.find(str(choice)) == -1:
        choice = input("Please, enter a choice between 1 to 8.\n\n1) Load a file\n2) Check tree structure\n3) Check tree branch lengths\n4) Assemble trees\n5) Manipulate trees\n6) Print output\n7) Access parameters\n8) Quit TTiP\n\n Your choice :  ")
    if int(choice) == 1: # Load a new file
        if len(trees_list) != 0 or len(path_tree) != 0: # If there is already a tree loaded
            replace = input("You already have at least a tree or a file loaded. Would you like to replace it? Y/N --- \n")
            while yn.find(replace.lower()) == -1:
                print("Please, answer by Y or N. --- ")
            if replace.lower() == "y":
                trees_list = {}
                tax_val = []
                nod_tax = []
                nod_val = []
                hierarchy = []
                val = []
                abs_nod_val = []
                root_tip = []
                path_tree = input("Provide file path: ")
                trees_list = load(path_tree, verbose, speed)
                print("Extraction successfull")
            else:
                print("Back to main menu")
        else:
            path_tree = input("Provide file path: ")
            trees_list = load(path_tree, verbose, speed)
            print("Extraction successfull")
    elif int(choice) == 2:
        if len(trees_list) == 0:
            print(f"There is no tree in cache. Consider loading a file.")
        else:
            for i in range(len(trees_list)):                
                if verbose == True:
                    print(f"Verification of tree {i} on {len(trees_list) -1}")
                tax_v = {}
                nod_t = {}
                nod_v = {}
                hier = {}
                trees_list[i].errors, trees_list[i].taxa, tax_v, nod_t, nod_v = verif(trees_list[i].seq, verbose, speed)
                if len(tax_v) > 0 or len(nod_v) > 0:
                    trees_list[i].bl = True
                tax_val.append(tax_v)
                nod_tax.append(nod_t)
                nod_val.append(nod_v)
                val.append(tax_v)
                val[-1].update(nod_v)
                hier = comput_hierarchy(trees_list[i].seq, trees_list[i].taxa, nod_tax[i])
                hierarchy.append(hier)
                trees_list[i].vcv = comput_vcv(hierarchy[i], trees_list[i].taxa, verbose, speed)
                time.sleep(speed)
            del(tax_v, nod_t, nod_v, hier)
    elif int(choice) == 3:
        print("This option is in development. Use with caution.")
        for i in range(len(trees_list)):
            if len(val[i]) == 0:
                print(f"Tree {i} does not contains any values.")
            else:
                rt = comput_anv(trees_list[i].vcv, trees_list[i].taxa, hierarchy[i], verbose, speed)
                root_tip.append(rt)
                k = list(root_tip[i].keys())[-2]
                root = root_tip[i][list(root_tip[i].keys())[-1]]
                while k != list(root_tip[i].keys())[0]:
                    if root_tip[i][k] >= root:
                        root = root_tip[i][k]
                        if verbose == True:
                            r = k
                k -= 1
                if verbose == True:
                    print(f"Root values anchored on taxon {r}")
                    time.sleep(speed)
                del(rt)
    elif int(choice) == 4:
        print("This option is in development. Please, choose another one.")
    elif int(choice) == 5:
        print("This option is in development. Please, choose another one.")
    elif int(choice) == 6:
        if len(trees_list) > 0:
            probject(trees_list)
        else:
            print(f"There is no tree in cache. Consider loading a file.")
    elif int(choice) == 7:
        change_param = input(f"Which parameter would you like to modify?\n1. Verbose: {verbose} - Displays additional information in various functions\n2. Speed: {speed} - Verbose option. Change the speed of the printing of additional information. Warning: slow done the computations\n3. None --- ")
        while param.find(change_param) == -1:
            change_param = input("Please, enter a choice between 1 to 3.\n1. Verbose\n2. Speed\n3. None --- ")
        if int(change_param) == 1:
            verbose = not verbose
            if verbose == True:
                print(f"Verbose is now activated. Additional information will appear during the computation.")
            else:
                print(f"Verbose is now deactivated. There will be no additional information during the computation.")
        elif int(change_param) == 2:
            speed = input("Please, enter a new numerical value. It corresponds to the time in seconds the software will wait between two information. --- ")
            while not isinstance(speed, int) or not isinstance(speed, float):
                speed = input("Please, enter a numerical value. --- ")
            print(f"The new speed is now of {speed}s.")
        else:
            print("Back to main menu")
    else:
        q = True
        
quit()