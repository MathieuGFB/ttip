import time

def verif(tree, verbose = False, speed = 0.2):
    errors = {} # Errors
    taxa = {} # Taxa
    tax_val = {} # Values associated to taxa
    nod_val = {} # Values associated to nodes
    tf_nod_val = {} # Update of numbers associated to nodes
    nod_tax = {} # Taxonomic content of nodes
    tf_nod_tax = {} # Update of numbers associated to nodes

    ob = [] # open brackets
    nod_l = [] # node list

    st = "" # Storage
    pos = "" # Last colon position
    ctax = 0 # Taxa counter
    switch = True # Switch between branch - False / taxon storage - True
    obc = 0 # Open nodes counter

    operators = "(),;:" # All operators

    # Check absolute number of brackets
    if tree.count("(") == tree.count(")"):
        if verbose == True:
            print("The number of bracket is correct. The software will search empty brackets.")
        brack = 1
    elif tree.count("(") > tree.count(")"):
        if verbose == True:
            print("There are more opening than closing brackets. The software will not search empty brackets.")
        errors["Brackets"] = "Number of opening brackets superior to closing brackets."
        brack = 2
    else:
        if verbose == True:
            print("There are less opening than closing brackets. The software will not search empty brackets.")
        brack = 3
    
    # Preliminary tests
    if tree[0] != "(":
        errors[0] = "The tree should start with an opening bracket."
        if verbose == True:
            print("The tree does not start with an opening bracket.")

    if tree[len(tree) - 1] != ";":
        errors[len(tree) - 1] = "Absence of a closing semicolon at the end of the tree"
        if verbose == True:
            print(f"Absence of semicolon at the end of the sequence.")
    if tree[len(tree) - 2] != ")":
        errors[len(tree) - 2] = "Absence of the bracket closing the root"
        if verbose == True:
            print(f"Absence of a bracket at the end of the tree.")
    
    if verbose == True:
        time.sleep(0.5)

    # Reading tree
    for i in range(len(tree)): # Initializing the loop
        if verbose == True:
            print(f"Loop {i}")
            print(f"Switch is {switch}")
        if operators.find(tree[i]) != -1: # Char i is an operator
            if len(st) > 0: # Non empty storage
                if switch == True: # Switch is on taxa
                    taxa[ctax] = st
                    if verbose == True:
                        print(f"Taxon {st} added to the list of taxa")
                    ctax += 1
                    for j in range(len(ob)):
                        nod_tax[ob[j]].append(st)
                        if verbose == True:
                            print(f"Taxon {st} added to node {j}")
                    st = ""
                else: # Switch is on values
                    if operators.find(tree[pos]) == -1: # Char before colon is not an operator
                        tax_val[ctax - 1] = st
                        if verbose == True:
                            print(f"Value {st} associated to {taxa[ctax -1]}")
                        st = ""
                    elif tree[pos] == ")": # Char before colon is a closing bracket
                        nod_val[nod_l[-1]] = st
                        nod_l.pop(-1)
                        if verbose == True:
                            print(f"Open nodes without associated values: {nod_l}")
                        st = ""
                        pos = ""
                    else:
                        errors[pos] = "Missplaced colon."
                        if verbose == True:
                            print(f"Colon at position {pos} missplaced.")
                        st = ""
                        pos = ""
                    switch = True
            if tree[i] == ",": # Char is a coma
                if operators.find(tree[i - 1]) == -1 and operators.find(tree[i + 1]) == -1: # Coma is between two taxa -- RULE 1
                    if verbose == True:
                        print(f"Coma at position {i}: OK")
                elif operators.find(tree[i - 1]) == -1 and tree[i + 1] == "(": # Coma is between a taxon and an opening bracket -- RULE 2
                    if verbose == True:
                        print(f"Coma at position {i}: OK")
                elif tree[i - 1] == ")" and tree[i + 1] == "(": # Coma is between a closing and an opening bracket -- RULE 3
                    if verbose == True:
                        print(f"Coma at position {i}: OK")
                elif tree[i - 1] == ")" and operators.find(tree[i + 1]) == -1: # Coma is between a closing bracket and a taxon -- RULE 4
                    if verbose == True:
                        print(f"Coma at position {i}: OK")
                else: # If the four rules have proven to be false
                    errors[i] = "Coma missplaced at position", i
                    if verbose == True:
                        print(f"Coma at position {i} is missplace.")
            elif tree[i] == ";": # Char is a semicolon
                if i != len(tree) -1:
                    errors[i] = "Missplaced semicolon"
                    if verbose == True:
                        print(f"Missplaced semicolon at position {i}.")
            elif tree[i] == "(": # Char is an opening bracket
                if brack == 1:
                    nod_l.append(obc)
                    nod_tax[obc] = []
                    ob.append(obc)
                    if verbose == True:
                        print(f"Opening node {obc} for taxonomic content.")
                        print(f"Adding node {obc} to the nodes list.")
                obc += 1
                if verbose == True:
                    print(f"{obc} open nodes.")
            elif tree[i] == ")": # Char is a closing bracket
                if brack == 1:    
                    if len(ob) > 0: # There is at least one open bracket
                        if verbose == True:
                            print(f"Closing node {ob[-1]}. There are still {len(ob)} open nodes.")
                        ob.pop(-1) # Closing last bracket
                elif brack == 3:
                    obc -= 1
                    if (obc == 0 and i != len(tree) -1) or obc < 0:
                        errors[i] = "Extra closing bracket"
                        if verbose == True:
                            print(f"Extra closing bracket found at position {i}.")
                    else:
                        if verbose == True:
                            print(f"{obc} open nodes remaining.")
            elif tree[i] == ":": # Char is a colon
                if operators.find(tree[i + 1]) != -1: # Colon followed by another operator. Empty value
                    errors[i] = "Associated value missing."
                    if verbose == True:
                        print(f"Colon at position {i} is missing an associated value.")
                else:
                    switch = False # Begin storage of a value
                    pos = i - 1
                    if verbose == True:
                        print(f"Colon found followed by a value. Begin storage")
        else: # Char i is not an operator
            st += tree[i]
            if verbose == True:
                print(f"Storage: {st}")
        if verbose == True:
            time.sleep(speed)

    # Check of taxonomic content of nodes
    for i in range(len(nod_tax) -1):
        if len(nod_tax[i]) <2:
            errors[len(taxa) + i] = "Taxonomic content too low."
            if verbose == True:
                print(f"The node {len(taxa) + 1} contains less than two taxa, or one taxa and a non-empty node.")
            j = i + 1
            while j != len(nod_tax):
                if nod_tax[i] == nod_tax[j]:
                    errors[len(taxa) + i, "-", len(taxa) + j] = "These two nodes have the exact same content"
                    if verbose == True:
                        print(f"The taxonomic content of the nodes {len(taxa) + j} and {len(taxa) + i} are identical.")
                j += 1

    t = len(taxa)  
    j = 0
    while t != len(nod_tax) + len(taxa):
        if j > 0 and len(nod_val) > 0:
            tf_nod_val[t] = nod_val[j]
        tf_nod_tax[t] = nod_tax[j]
        j += 1
        t += 1
    
    # Statistics and results
    print(f"Tree statistics:\n{len(nod_tax)} nodes;\n{len(taxa)} taxa;\n{len(errors)} errors")
    if len(nod_val) or len(tax_val) != 0:
        print("This tree contains values.")
    else:
        print("This tree does not contain values.")
    return(errors, taxa, tax_val, tf_nod_tax, tf_nod_val)