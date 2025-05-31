import time
from rich.text import Text

def to_nexus(tree, verbose = False, speed = 0.02): #tree = dico de tous les arbres
    nexus = "#NEXUS\n\n\nBEGIN TAXA:\n\n\n"
    # Add taxa


    nexus.append = "END\n\nBEGIN TREES:"
    for i in (range(len(tree))):
        nexus.append("tree_", [i], "= ", tree[i].seq, "\n")

    with open("newfile.nex", "w") as save_file:
        print(nexus, file = save_file)