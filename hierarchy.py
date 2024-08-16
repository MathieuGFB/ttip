def comput_hierarchy(tree, taxa, nodes):
    c = 0 # count
    ob = [] # open brackets
    cob = 0 # count open brackets
    hierarchy = {} # hierarchy
    for i in range(tree.count("(")):
        hierarchy[i + len(taxa)] = []

    while c != len(tree):
        if tree[c] == "(":
            if len(ob) > 0:
                hierarchy[ob[-1]].append(cob + len(taxa))
                ob.append(cob + len(taxa))
                cob += 1
            else:
                ob.append(len(taxa))
                cob += 1
        if tree[c] == ")":
            ob.pop(-1)
        c += 1

    i = len(taxa)
    while i != len(nodes) + len(taxa):
        j = i + 1
        while j != len(nodes) + len(taxa):
            a = []
            k = 0
            while k != len(nodes[i]):
                if nodes[j].count(nodes[i][k]) == 0:
                    a.append(nodes[i][k])
                k += 1
            j += 1
            if a != nodes[i]:
                nodes[i] = a
        i += 1

    c = len(taxa)
    while c != len(hierarchy) + len(taxa):
        if len(nodes[c]) > 0:
            for k in range(len(nodes[c])):
                hierarchy[c].append(list(taxa.values()).index(nodes[c][k]))
        c += 1
    
    return(hierarchy)