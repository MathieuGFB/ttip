"""Main program file"""
# ttip/ttip.py
# v 0.0.3

from verif import verif
from shfunc import load, write_log, replace
from rich.text import Text
from rich.console import Console

# Rich styles
shc_val = "cyan bold"
correct = "green bold"
error = "red bold"
attention = "yellow bold"

def verify(path_to_tree, verbose = False):
    console = Console()
    if verbose == True:
        console.print(Text.assemble("Provided filepath: ", (f"{path_to_tree}", "underline"), style = "italic"))
    trees_list = {}
    trees_list = load(path_to_tree, verbose, speed = 0.02)
    for i in range(len(trees_list)):
        if verbose == True:
            console.print(Text.assemble(f"\n--- Verification of tree ", (f"{i+1}", shc_val), " on ", (f"{len(trees_list)}\n", shc_val), style = "italic bold"))
        if ":".find(trees_list[i].seq) != -1:
            trees_list[i].errors, trees_list[i].taxa, trees_list[i].tax_val, trees_list[i].nod_val= verif(trees_list[i].seq, verbose, values = True, speed = 0.02)
        else:
            trees_list[i].errors, trees_list[i].taxa, = verif(trees_list[i].seq, verbose, speed = 0.02)
    write_log(trees_list)

def merge(path_to_main_tree, path_to_subtree, keyword, verbose = False, check = False):
    console = Console()
    if verbose == True:
        console.print(Text.assemble("Provided filepath for maintree ", (f"{path_to_main_tree}", "underline"), style = "italic"))
    maintree = {}
    maintree = load(path_to_main_tree, verbose, speed = 0.02)
    if range(len(maintree)) != 1:
        console.print(Text.assemble("The file indicated for the main tree contains several trees. It should only contain one.", style = error))
    else:
        try:
            maintree[0].seq.find(keyword) != -1
        except:
            console.print(Text.assemble("The main tree does not contain the given keyword."), style = error)
        else:
            if verbose == True:
                console.print(Text.assemble("Provided filepath for subtrees ", (f"{path_to_subtree}", "underline"), style = "italic"))
            subtrees = {}
            subtrees = load(path_to_subtree, verbose, speed = 0.02)
            if check == True:
                if ":".find(maintree[0].seq) != -1:
                    maintree[0].errors, maintree[0].taxa, maintree[0].tax_val, maintree[0].nod_val= verif(maintree[0].seq, verbose, values = True, speed = 0.02)
                else:
                    maintree[0].errors, maintree[0].taxa, = verif(maintree[0].seq, verbose, speed = 0.02)
                for i in range(len(subtrees)):
                    if ":".find(subtree[i].seq) != -1:
                        subtree[i].errors, subtree[i].taxa, subtree[i].tax_val, subtree[i].nod_val= verif(subtree[i].seq, verbose, values = True, speed = 0.02)
                    else:
                        subtree[i].errors, subtree[i].taxa, = verif(subtree[i].seq, verbose, speed = 0.02)
                if len(maintree[0].error) == 0:
                    chk = True
                    for i in range(len(subtrees)):
                        if len(subtrees.error) != 0:
                            chk = False
                    if chk == False:
                        console.print(Text.assemble("At least one of the provided trees contains errors. Please fix them first."), style = error)
                mergetrees = {}
                mergetrees = {key:[] for key in range(len(subtrees))}
                for i in range(len(subtrees)):
                    mergetrees[i] = tree_obj()
                    mergetrees[i].seq = replace(maintree[0].seq, subtrees[i].seq, keyword, verbose, speed = 0.2)
                with open("mergetrees.tre", "w") as save_file:
                    for i in range(len(mergetrees)):
                        print(mergetrees[i].seq, "\n", file = save_file)
            else:
                console.print(Text.assemble("As the 'check' option was not indicated, the provided trees will not be verified. Please know that it can lead to errors in the process of merging."), style = attention)
                mergetrees = {}
                mergetrees = {key:[] for key in range(len(subtrees))}
                for i in range(len(subtrees)):
                    mergetrees[i] = tree_obj()
                    mergetrees[i].seq = replace(maintree[0].seq, subtrees[i].seq, keyword, verbose, speed = 0.2)
                with open("mergetrees.tre", "w") as save_file:
                    for i in range(len(mergetrees)):
                        print(mergetrees[i].seq, "\n", file = save_file)
                    
def convert(path_to_tree, to_format, check = False, verbose = False):
    console = Console()
    if verbose == True:
        console.print(Text.assemble("Provided filepath for tree ", (f"{path_to_tree}", "underline"), style = "italic"))
    trees_list = {}
    trees_list = load(path_to_tree, verbose, speed = 0.02)
    if check == True:
        for i in range(len(trees_list)):
            if verbose == True:
                console.print(Text.assemble(f"\n--- Verification of tree ", (f"{i+1}", shc_val), " on ", (f"{len(trees_list)}\n", shc_val), style = "italic bold"))
            if ":".find(trees_list[i].seq) != -1:
                trees_list[i].errors, trees_list[i].taxa, trees_list[i].tax_val, trees_list[i].nod_val= verif(trees_list[i].seq, verbose, values = True, speed = 0.02)
            else:
                trees_list[i].errors, trees_list[i].taxa, = verif(trees_list[i].seq, verbose, speed = 0.02)
        if len(maintree[0].error) == 0:
            chk = True
            for i in range(len(subtrees)):
                if len(subtrees.error) != 0:
                    chk = False
            if chk == False:
                console.print(Text.assemble("At least one of the provided trees contains errors. Please fix them first."), style = error)
    print("Work in progress")

def calibrate(path_to_tree, check = False, verbose = False):
    print("Work in progress")
