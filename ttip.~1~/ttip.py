"""Main program file"""
# ttip/ttip.py
# v 0.0.3

from verif import verif
from shfunc import load, write_log
from rich.text import Text
from rich.console import Console

# Rich styles
shc_val = "cyan bold"
correct = "green bold"
error = "red bold"

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

def merge(path_to_main_tree, path_to_subtree, keyword, verbose = False):
    console = Console()
    if verbose == True:
        console.print(Text.assemble("Provided filepath: ", (f"{path_to_tree}", "underline"), style = "italic"))
    maintree = {}
    maintree = load(path_to_main_tree, verbose, speed = 0.02)
    if range(len(maintree)) != 1:
        console.print(Text.assemble("The file indicated for the main tree contains several trees. It should only contain one.", style = error))
    else:
        if maintree[0].seq.find(keyword) == -1:
            console.print(Text.assemble("The main tree does not contain the given keyword."), style = error)
        subtrees = {}
        subtrees = load(path_to_subtree, verbose, speed = 0.02)
    print("Work in progress")

def convert(path_to_tree, from_format, to_format, verbose = False):
    print("Work in progress")

def calibrate(path_to_tree, verbose = False):
    print("Work in progress")
