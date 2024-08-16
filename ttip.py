#!/usr/bin/env python3

import time
from verif import verif
from shfunc import fold, uncom, recog, load
from hierarchy import comput_hierarchy
from phymat import comput_branches, pr_phymat

print("#######################\n###                 ###\n###    TTiP v0.1    ###\n###                 ###\n#######################")
print("Designed and coded by M. G. Faure-Brac.\nContact at: faurebrac.mathieu@gmail.com, or through GitHub.")

## DICTIONNARIES ##
tree = {}

## LISTS ##
phymat = []
errors = []
taxa = []
tax_val = []
nod_tax = []
nod_val = []
hierarchy = []
val = []
abs_nod_val = []
prvar = [errors,taxa,tax_val,nod_tax,nod_val,hierarchy,val,abs_nod_val]

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
verbose = False
speed = 0.2 # Speed of time.sleep if verbose == T
q = False # Exit variable

while q == False:
    choice = input("What do you want to do?\n1) Load a file\n2) Check tree structure\n3) Check tree branch lengths\n4) Assemble trees\n5) Manipulate trees\n6) Print output\n7) Access parameters\n8) Quit TTiP --- ")
    while options.find(str(choice)) == -1:
        choice = input("Please, enter a choice between 1 to 8.\n1) Load a file\n2) Check tree structure\n3) Check tree branch lengths\n4) Assemble trees\n5) Manipulate trees\n6) Print output\n7) Access parameters\n8) Quit software --- ")
    if int(choice) == 1: # Load a new file
        if len(tree) != 0 or len(path_tree) != 0: # If there is already a tree loaded
            replace = input("You already have at least a tree or a file loaded. Would you like to replace it? Y/N --- \n")
            while yn.find(replace.lower()) == -1:
                print("Please, answer by Y or N. --- ")
            if replace.lower() == "y":
                path_tree = input("Provide file path: ")
                tree = load(path_tree, verbose, speed)
                print("Extraction successfull")
            else:
                print("Back to main menu")
        else:
            path_tree = input("Provide file path: ")
            tree = load(path_tree, verbose, speed)
            print("Extraction successfull")
    elif int(choice) == 2:
        try:
            tree
        except:
            print(f"There is no tree in cache. Please load a file.")
        else:
            for i in range(len(tree)):                
                if verbose == True:
                    print(f"Verification of tree {i} on {len(tree) -1}")
                error = {}
                tax = {}
                tax_v = {}
                nod_t = {}
                nod_v = {}
                hier = {}
                error, tax, tax_v, nod_t, nod_v = verif(tree[i], verbose, speed)
                errors.append(error)
                taxa.append(tax)
                tax_val.append(tax_v)
                nod_tax.append(nod_t)
                nod_val.append(nod_v)
                val.append(tax_v)
                val[-1].update(nod_v)
                hier = comput_hierarchy(tree[i], taxa[i], nod_tax[i])
                hierarchy.append(hier)
                time.sleep(speed)
    elif int(choice) == 3:
        print("This option is in development. Please, choose another one.")
        #phymat = comput_branches(hierarchy, taxa, verbose = verbose, speed= speed)
        #abs_nod_val = comput_abs_nod(hierarchy, val, taxa, verbose = verbose, speed= speed)
    elif int(choice) == 4:
        print("This option is in development. Please, choose another one.")
    elif int(choice) == 5:
        print("This option is in development. Please, choose another one.")
    elif int(choice) == 6:
        print("This option is in development. Please, choose another one.")
        #tmp_prvar = []
        #for i in range(len(prvar)):
        #    if len(prvar[i]) > 0:
        #       tmp_prvar.append(prvar[i])
        #pr_phymat(hierarchy, taxa, phymat)
    elif int(choice) == 7:
        change_param = input(f"Which parameter would you like to modify?\n1. Verbose: {verbose} - Displays additional information in various functions\n2. Speed: {speed} - Verbose option. Change the speed of the printing of additional information. Warning: slow done the computations\n3. None")
        while param.find(change_param) == -1:
            change_param = input("Please, enter a choice between 1 to 3.\n1. Verbose\n2. Speed\n3. None")
        if int(change_param) == 1:
            verbose = not verbose
            if verbose == True:
                print(f"Verbose is now activated. Additional information will appear during the computation.")
            else:
                print(f"Verbose is now deactivated. There will be no additional information during the computation.")
        elif int(change_param) == 2:
            speed = input("Please, enter a new numerical value. It corresponds to the time in seconds the software will wait between two information.")
            while not isinstance(speed, int) or not isinstance(speed, float):
                speed = input("Please, enter a numerical value.")
            print(f"The new speed is now of {speed}s.")
        else:
            print("Back to main menu")
    else:
        q = True
        
quit()