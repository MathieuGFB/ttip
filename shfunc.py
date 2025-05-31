import time

from rich.text import Text
from rich.console import Console
from rich.table import Table
from rich import print as rprint

from tree import tree_obj

console = Console()

# Rich styles
error = "red bold"
shc_val = "cyan bold"
correct = "green bold"

def fold(tree): # Function aiming to 'fold' trees in a unique line
    tree = tree.replace(' ','')
    c = 0
    while c != len(tree):
        if tree[c] == "\n":
            if tree[c - 1] != ";":
                bf_c = tree[:c]
                af_c = tree[c + 1:]
                tree = bf_c + af_c
        c += 1
    return(tree)

def uncom(tree): # Removing comment from a Newick tree
    try:
        if tree.count("[") > 0:
            tree.count("[") == tree.count("]")
    except:
        console.print(Text.assemble("Error: there is an unpaired number of square bracket in the provided tree.", style = error))
    else:
        c = 0 # counter
        while c != len(tree):
            if tree[c] == "[":
                d = c + 1
                while tree[d] != "]":
                    d += 1
                tree = tree[:c] + tree[d+1:]
            c += 1
    return(tree)

def recog(tree, verbose, speed):
    st = "" # Storage
    t = 0
    c = 0
    if tree[-1] == "\n":
        srt_trees = {key:[] for key in range(tree.count(";\n"))}
    else:
        srt_trees = {key:[] for key in range(tree.count(";\n")+1)}
    if verbose == True:
        console.print(Text.assemble((f"{len(srt_trees)}", shc_val)," trees have been found"))
        time.sleep(speed)
    while c != len(tree):
        if tree[c] == "\n" and tree[c - 1] == ";":
            srt_trees[t].append(st)
            if verbose == True:
                console.print(Text.assemble("Tree ", (f"{t}", shc_val), f" extracted: {st}"))
                time.sleep(speed)
            t += 1
            st = ""
        else:
            st += tree[c]
        c += 1
    if st:    
        srt_trees[t].append(st)
    return(srt_trees)

def load(path_tree, verbose, speed):
    trees_list = {}
    trees = {}
    try:
        open(path_tree, "r").read()
    except:
        console.print(Text.assemble("This file cannot be loaded. Please, check it.", style = error))
    else:
        if path_tree.lower().endswith((".tre", ".tree", ".phy")):
            filext = "newick"
        elif path_tree.lower().endswith((".nex", ".nexus")):
            filext = "nexus"
        else:
            filext = "other"
        if filext == "newick":
            rawtree = open(path_tree, "r").read()
            if rawtree.count(";\n") > 1:
                trees = recog(rawtree, verbose, speed)
            else:
                trees[0] = rawtree
            for i in range(len(trees)):
                if len(trees) > 1:
                    tmp = str(trees[i])
                    tmp = tmp[2:len(tmp)-2]
                    trees_list[i] = tree_obj()
                    trees_list[i].seq = uncom(fold(tmp))
                else:
                    trees_list[0] = tree_obj()
                    trees_list[0].seq = uncom(fold(trees[0]))
            if verbose == True:
                console.print(Text.assemble((f"{len(trees_list)}", shc_val), " trees have been extracted"))
            return(trees_list)
        elif filext == "nexus":
            rawtree = open(path_tree, "r").read()
            if rawtree.lower().find("begin trees;") != -1:
                start = rawtree.lower().find("begin trees;") + 13
                end = rawtree.lower().find("end;",start)
                extraction = rawtree[start:end]
                if rawtree.count("=") > 1:
                    print("WIP. Not available yet.")
                else:
                    start = extraction.find("=") + 1
                    end = extraction.find(";") + 1
                    trees_list[0] = tree_obj()
                    trees_list[0].seq = uncom(fold(extraction[start:end]))
                    console.print(Text.assemble((f"{len(trees_list)}", shc_val), " trees have been extracted"))
                    return(trees_list)
            else:
                console.print(Text.assemble("Nexus file is missing a valid TREE block.", style = error))
        else:
            console.print(Text.assemble("This file is not supported. Newick format (.tre; .tree; .phy) and Nexus files (.nex; .nexus) are the only supported files.", style = error))     
    
def write_log(trees_list):
    for i in range(len(trees_list)):
        if len(trees_list[i].errors) != 0:
            table_err = Table(title = f"Tree {i}: Errors")
            table_err.add_column("Num", justify = "right", style = "bold", no_wrap = True)
            table_err.add_column("Error label", style = "bold")
            for j in range(len(trees_list[i].errors)):
                if type(list(trees_list[i].errors.values())[j]) is tuple:
                    table_err.add_row(str(list(trees_list[i].errors.keys())[j]),str(list(trees_list[i].errors.values())[j][0]))
                else: 
                    table_err.add_row(str(list(trees_list[i].errors.keys())[j]),str(list(trees_list[i].errors.values())[j]))
            console.print(table_err)
        else:
            console.print(Text.assemble("No error have been found.", style = correct))
        table_tax = Table(title = f"Tree {i}: Taxa")
        table_tax.add_column("Num", justify = "right", style = "bold", no_wrap = True)
        table_tax.add_column("Taxon label", style = "bold")
        if len(trees_list[i].tax_val) != 0:
            table_tax.add_column("Absolute value", style = "bold")
            table_nod = Table(title = f"Tree {i}: Node values")
            table_nod.add_column("Num", justify = "right", style = "bold", no_wrap = True)
            table_nod.add_column("Absolute value", style = "bold")
        for j in range(len(trees_list[i].taxa)):
            if len(trees_list[i].tax_val) != 0:
                table_tax.add_row(str(list(trees_list[i].taxa.keys())[j]),(list(trees_list[i].taxa.values())[j]),str(list(trees_list[i].tax_val.values())[j]))
            else:
                table_tax.add_row(str(list(trees_list[i].taxa.keys())[j]),(list(trees_list[i].taxa.values())[j]))
        console.print(table_tax)
        if len(trees_list[i].nod_val) != 0:
            for j in range(len(trees_list[i].nod_val)):
                table_nod.add_row(str(list(trees_list[i].nod_val.keys())[j]),str(list(trees_list[i].nod_val.values())[j]))
            console.print(table_nod)
        if i == 0:    
            with open("verify.log", "w") as save_file:
                if len(trees_list[i].errors) != 0 and len(trees_list[i].nod_val) != 0:
                    rprint(table_err, "\n", table_tax, "\n", table_nod, file = save_file)
                elif len(trees_list[i].errors) != 0 and len(trees_list[i].nod_val) == 0:
                    rprint(table_err, "\n", table_tax, file = save_file)
                elif len(trees_list[i].errors) == 0 and len(trees_list[i].nod_val) != 0:
                    rprint(table_tax, "\n", table_nod, file = save_file)
                else:
                    rprint(table_tax, file = save_file)
        else:
            with open("verify.log", "a") as save_file:
                if len(trees_list[i].errors) != 0 and len(trees_list[i].nod_val) != 0:
                    rprint(table_err, "\n", table_tax, file = save_file)
                elif len(trees_list[i].errors) != 0 and len(trees_list[i].nod_val) == 0:
                    rprint(table_err, "\n", table_tax, file = save_file)
                elif len(trees_list[i].errors) == 0 and len(trees_list[i].nod_val) != 0:
                    rprint(table_tax, file = save_file)
                else:
                    rprint(table_tax, file = save_file)

def replace(maintree, subtree, keyword, verbose = False, speed = 0.2):
    pos = maintree.find(keyword)

    newtree = maintree[0:pos] # First part of the tree
    newtree = newtree + subtree[0:len(subtree)-1] # Insert subtree
    newtree = newtree + maintree[pos+len(kw):len(maintree)] # Second part of the tree minus the keyword
    return(newtree)

def setwd(path):
    wd = path
    # remove last part of path
    return(wd)