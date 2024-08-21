import time

from tree import tree_obj

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
        print("Error: there is an unpaired number of square bracket in the provided tree.")
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
    srt_trees = {key:[] for key in range(tree.count(";\n"))}
    if verbose == True:
        print(f"{len(srt_trees)} have been found")
        time.sleep(speed)
    while c != len(tree):
        if tree[c] == "\n" and tree[c - 1] == ";":
            srt_trees[t].append(st)
            if verbose == True:
                print(f"Tree {t} extracted: {st}")
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
    try:
        open(path_tree, "r").read()
    except:
        print(f"This file is not reedable or does not exist. Please, check it.")
    else:
        if path_tree.lower().endswith((".tre", ".tree", ".phy")):
            filext = True
        elif path_tree.lower().endswith((".nex", ".nexus", ".tnt")):
            filext = False
        else:
            filext = False
        if filext == True:
            rawtree = open(path_tree, "r").read()
            if rawtree.count(";\n") > 1:
                trees = recog(rawtree, verbose,speed)
            else:
                trees[0] = rawtree
            for i in range(len(trees)):
                if len(trees) > 1:
                    tmp = str(trees[i])
                    tmp = tmp[2:len(tmp)-2]
                    trees_list[i] = tree_obj()
                    trees_list[i].seq = uncom(fold(tmp))
                    if verbose == True:
                        print(f"Object tree {i} created.")
                else:
                    trees_list[0] = tree_obj()
                    trees_list[0].seq = uncom(fold(trees[0]))
                    if verbose == True:
                        print("Object tree created")
            return(trees_list)
        else:
            print(f"This file is non supported. .tre; .tree and .phy are the only supported files.")