def verif_tree(tree):
    operators = "()[],;:."
    # Count brackets
    brack_open = tree.count("(")
    brack_clos = tree.count(")")
    if brack_open == brack_clos:
        print("The number of bracket is correct.")
        check_bracket = 1
    elif brack_open > brack_clos:
        errors["X"] = "Number of opening bracket superior to closing bracket."
        print("Number of opening bracket superior to closing bracket. The programm will not search for empty brackets.")
        check_bracket = 2
    else:
        check_bracket = 3
        print("Number of opening bracket inferior to closing bracket. The programm will not search for empty brackets.")
    # Reading tree
    c = 0 # character counter
    bp = 0 # bypass counter
    brc = 0 # bracket counter ; missing
    cob = 0 # bracket counter ; empty
    t = "" # taxon name storage
    taxa = []
    errors = {}
    nodes = {}
    brackets = []
    while c != len(tree):
        if operators.find(tree[c]) != -1: # Character c is an operator
            if len(t) > 0: # If t contains a taxon, then append the list of taxa and empty t.
                taxa.append(t)
                for i in range(len(brackets)):
                    nodes[brackets[i]].append(t)
                print(t,"added to the list of taxa")
                t = ""
            if operators.find(tree[c]) == 4: # test coma
                bp += 1
                if operators.find(tree[c - 1]) == -1 and operators.find(tree [c + 1]) == -1: # Both character c - 1 and c + 1 are taxa -- Rule 1
                    print("Coma at position",c,"ok")
                else:
                    if operators.find(tree[c - 1]) == -1 and operators.find(tree [c + 1]) == 0: # If rule 1 false and character c-1 is taxa and c + 1 is opening bracket -- Rule 2
                        print("Coma at position",c,"ok")
                    else:
                        if operators.find(tree[c - 1]) == 1 and operators.find(tree[c + 1]) == 0: # If rule 1 and 2 are false, and character c-1 is closed bracket and character c + 1 is opening bracket -- Rule 3
                            print("Coma at position",c,"ok")
                        else:
                            if operators.find(tree[c - 1]) == 1 and operators.find(tree[c + 1]) == -1: # IF previous rules false and taxa following a closing bracket -- Rule 4
                                print("Coma at position",c,"ok")
                            else:
                                print("Coma at position",c,"misplaced")
                                errors[c] = "Coma misplaced" # Add error to the list of errors
            if bp == 0 & operators.find(tree[c]) == 5: # semicolon
                bp += 1
                if c != len(tree) - 1: # If semicolon is not the last character of the string
                    errors[c] = "Semicolon misplaced"
            if check_bracket == 3 and bp == 0 and operators.find(tree[c]) == 0: # opening bracket ; search for missing brackets
                bp += 1
                brc += 1
                print(brc,"opened nodes.")
            if check_bracket == 3 and bp == 0 and operators.find(tree[c]) == 1: # closing bracket ; search for missing brackets
                bp += 1
                brc -= 1
                if brc == 0 & c != len(tree) - 1:
                    errors[c] = "Number of opening brackets inferior to closing brackets"
                elif brc < 0:
                    errors[c] = "Number of opening brackets inferior to closing brackets"
                else:
                    print(brc,"opened nodes.")
            if check_bracket == 1 and bp == 0 and operators.find(tree[c]) == 0: # opening bracket ; search for empty brackets
                bp += 1
                nodes[cob] = []
                brackets.append(cob)
                cob += 1
            if check_bracket == 1 and bp == 0 and operators.find(tree[c]) == 1: # closing bracket ; search for empty brackets
                if len(brackets) > 0:
                    brackets.pop(-1)
        else: # Character c is not an operator
            t += tree[c]
        bp = 0
        c += 1
        # Code rencontre un caractère différent des operateurs
    # Loop ending
    if tree[len(tree) - 1] != ";":
        errors[len(tree) - 1] = "Absence of semicolon at the end of the tree"
    if tree[len(tree) - 2] != ")":
        errors[len(tree) - 2] = "There should be a closing bracket here"
    if tree[0] != "(":
        errors[0] = "The tree should begin by an opening bracket"
    for i in range(len(nodes) - 1):
        if len(nodes[i]) < 2:
            errors["Node",i] = "The node",i,"contains less than two taxa"
        j = i + 1
        while j != len(nodes):
            if len(nodes[i]) == len(nodes[j]):
                if nodes[i] == nodes[j]:
                    errors[i,"-",j] = "The nodes",i,"and",j,"have the same content"
            j += 1
    print("Results:\n",brack_open,"opening brackets\n",brack_clos,"closing brackets\n",len(taxa),"taxa\n",len(errors),"errors")
    print("Do you want to display the full list of taxa? y/n")
    disp_taxa = input()
    if disp_taxa == "y":
        print(taxa)
    if len(errors) > 0:
        print("Do you want to display the full list of errors? y/n")
        disp_errors = input()
        if disp_errors == "y":
            print(errors)
