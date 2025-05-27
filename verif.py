import time
from rich.progress import Progress
from rich.text import Text

def verif(tree, verbose = False, values = False, speed = 0.2):
    errors = {} # Errors
    taxa = {} # Taxa
    tax_val = {} # Values associated to taxa
    nod_val = {} # Values associated to nodes
    nod_tax = {} # Taxonomic content of nodes
    tf_nod_val = {} # Corrected nodes numbering

    ob = [] # open brackets
    nod_l = [] # node list

    st = "" # Storage
    pos = "" # Last colon position
    ctax = 0 # Taxa counter
    switch = True # Switch between branch - False / taxon storage - True
    obc = 0 # Open nodes counter

    operators = "(),;:" # All operators

    # Rich styles
    error = "red bold"
    correct = "green bold"
    step = "italic"
    shc_tax = "magenta bold"
    shc_val = "cyan bold"

    with Progress() as progress:
        # Check absolute number of brackets
        if verbose == True:
            progress.console.print(Text.assemble("Checking the number of brackets...", style = step))
        if tree.count("(") == tree.count(")"):
            if verbose == True:
                progress.console.print(Text.assemble("The number of bracket is correct. The software will search empty brackets.", style = correct))
            brack = 1
        elif tree.count("(") > tree.count(")"):
            if verbose == True:
                progress.console.print(Text.assemble("There are more opening than closing brackets. The software will not search empty brackets.", style = error))
            errors["Brackets"] = "Number of opening brackets superior to closing brackets."
            brack = 2
        else:
            if verbose == True:
                progress.console.print(Text.assemble("There are less opening than closing brackets. The software will not search empty brackets.", style = error))
            brack = 3
        # Preliminary tests
        if verbose == True:
            progress.console.print(Text.assemble("Running preliminary tests...", style = step))
        if tree[0] != "(":
            errors[0] = "The tree should start with an opening bracket."
            if verbose == True:
                progress.console.print(Text.assemble("The tree does not start with an opening bracket.", style = error))
        if tree[len(tree) - 1] != ";":
            errors[len(tree) - 1] = "Absence of a closing semicolon at the end of the tree"
            if verbose == True:
                progress.console.print(Text.assemble("Absence of semicolon at the end of the sequence.", style = error))
        if tree[len(tree) - 2] != ")":
            errors[len(tree) - 2] = "Absence of the bracket closing the root"
            if verbose == True:
                progress.console.print(Text.assemble("Absence of a bracket at the end of the tree.", style = error))
        if verbose == True:
            time.sleep(speed)
        # Reading tree
        if verbose == True:
            progress.console.print(Text.assemble("Starting tree sequence verification...", style = step))
        task = progress.add_task("Processing...", total = len(tree))
        for i in range(len(tree)): # Initializing the loop
            if operators.find(tree[i]) != -1: # Char i is an operator
                if len(st) > 0: # Non empty storage
                    if switch == True: # Switch is on taxa
                        taxa[ctax] = st
                        if verbose == True:
                            progress.console.print(Text.assemble((f"{st}", shc_tax)," added to the list of taxa"))
                        ctax += 1
                        for j in range(len(ob)):
                            nod_tax[ob[j]].append(st)
                            if verbose == True:
                                progress.console.print(Text.assemble((f"{st}", shc_tax),f" added to node ", (f"{ob[j]}", shc_val)))
                        st = ""
                    else: # Switch is on values
                        if operators.find(tree[pos]) == -1: # Char before colon is not an operator
                            tax_val[ctax - 1] = st
                            if verbose == True:
                                progress.console.print(Text.assemble("Value ", (f"{st}", shc_val), " associated to ", (f"{taxa[ctax -1]}", shc_tax)))
                            st = ""
                        elif tree[pos] == ")": # Char before colon is a closing bracket
                            nod_val[nod_l[-1]] = st
                            nod_l.pop(-1)
                            if verbose == True:
                                progress.console.print(Text.assemble(f"Open nodes without associated values: ",(f"{nod_l}", shc_val)))
                            st = ""
                            pos = ""
                        else:
                            errors[pos] = "Missplaced colon."
                            if verbose == True:
                                progress.console.print(Text.assemble(f"Colon at position {pos} missplaced.", style = error))
                            st = ""
                            pos = ""
                        switch = True
                if tree[i] == ",": # Char is a coma
                    if operators.find(tree[i - 1]) == -1 and operators.find(tree[i + 1]) == -1: # Coma is between two taxa -- RULE 1
                        if verbose == True:
                            progress.console.print(Text.assemble(f"Coma at position {i}: OK"), style = correct)
                    elif operators.find(tree[i - 1]) == -1 and tree[i + 1] == "(": # Coma is between a taxon and an opening bracket -- RULE 2
                        if verbose == True:
                            progress.console.print(Text.assemble(f"Coma at position {i}: OK"), style = correct)
                    elif tree[i - 1] == ")" and tree[i + 1] == "(": # Coma is between a closing and an opening bracket -- RULE 3
                        if verbose == True:
                            progress.console.print(Text.assemble(f"Coma at position {i}: OK"), style = correct)
                    elif tree[i - 1] == ")" and operators.find(tree[i + 1]) == -1: # Coma is between a closing bracket and a taxon -- RULE 4
                        if verbose == True:
                            progress.console.print(Text.assemble(f"Coma at position {i}: OK"), style = correct)
                    else: # If the four rules have proven to be false
                        errors[i] = "Coma missplaced at position", i
                        if verbose == True:
                            progress.console.print(Text.assemble(f"Coma at position {i} is missplaced."), style = error)
                elif tree[i] == ";": # Char is a semicolon
                    if i != len(tree) -1:
                        errors[i] = "Missplaced semicolon"
                        if verbose == True:
                            progress.console.print(Text.assemble(f"Missplaced semicolon at position {i}."), style = error)
                elif tree[i] == "(": # Char is an opening bracket
                    if brack == 1:
                        nod_l.append(obc)
                        nod_tax[obc] = []
                        ob.append(obc)
                        if verbose == True:
                            progress.console.print(Text.assemble("Opening node ", (f"{obc}", shc_val), " for taxonomic content."))
                    obc += 1
                    if verbose == True:
                        progress.console.print(Text.assemble((f"{len(ob)}", shc_val), " open nodes."))
                elif tree[i] == ")": # Char is a closing bracket
                    if brack == 1:    
                        if len(ob) > 0: # There is at least one open bracket
                            if verbose == True:
                                progress.console.print(Text.assemble("Closing node ", (f"{ob[-1]}", shc_val), ". There are still ", (f"{len(ob)-1}", shc_val), " open nodes."))
                            ob.pop(-1) # Closing last bracket
                    elif brack == 3:
                        obc -= 1
                        if (obc == 0 and i != len(tree) -1) or obc < 0:
                            errors[i] = "Extra closing bracket"
                            if verbose == True:
                                progress.console.print(Text.assemble(f"Extra closing bracket found at position {i}.", style = error))
                        else:
                            if verbose == True:
                                progress.console.print(Text.assemble((f"{obc}", shc_val), " open nodes remaining."))
                elif tree[i] == ":": # Char is a colon
                    if operators.find(tree[i + 1]) != -1: # Colon followed by another operator. Empty value
                        errors[i] = "Associated value missing."
                        if verbose == True:
                            progress.console.print(Text.assemble(f"Colon at position {i} is missing an associated value.", style = error))
                    else:
                        switch = False # Begin storage of a value
                        pos = i - 1
            else: # Char i is not an operator
                st += tree[i]
            if verbose == True:
                time.sleep(speed)
            progress.update(task, advance = 1)
        # Check number of values
        if values == True:
            if verbose == True:
                progress.console.print(Text.assemble("Node values verifications..."), style = step)
            if len(tax_val) + len(nod_val) != len(taxa) + len(nod_tax) - 1:
                errors["Nvalue"]  = "Number of values is incorrect."
                if verbose == True:
                    progress.console.print(Text.assemble(f"The number of values does not match the number of taxa and nodes.", style = error))
            for i in range(1, len(nod_val)):
                tf_nod_val[i + len(taxa) - 1] = nod_val[i]
        # Check of taxonomic content of nodes
        if verbose == True:
            progress.console.print(Text.assemble("Last verifications..."), style = step)
        for i in range(len(nod_tax) -1):
            if len(nod_tax[i]) <2:
                errors[len(taxa) + i] = "Taxonomic content too low."
                if verbose == True:
                    progress.console.print(Text.assemble(f"The node {len(taxa) + 1} contains less than two taxa, or one taxa and a non-empty node.", style = error))
            j = i + 1
            while j != len(nod_tax):
                if nod_tax[i] == nod_tax[j]:
                    errors[len(taxa) + i, "-", len(taxa) + j] = "These two nodes have the exact same content"
                    if verbose == True:
                        progress.console.print(Text.assemble(f"The taxonomic content of the nodes {len(taxa) + j} and {len(taxa) + i} are identical.", style = error))
                j += 1
        if verbose == True:
            progress.console.print(Text.assemble("Verification completed !"), style = step)
    if values == True:
        return(errors, taxa, tax_val, tf_nod_val)
    else:
        return(errors, taxa)