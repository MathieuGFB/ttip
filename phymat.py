import time

def comput_branches(hierarchy, taxa, verbose = False, speed = 0.2):
    phymat = []
    for r in range(len(hierarchy)):
        row = []
        for c in range(len(hierarchy) + len(taxa)):
            prs = False
            for k in range(len(hierarchy[r + len(taxa)])):
                if hierarchy[r + len(taxa)][k] == c:
                    prs = True
            if prs == True:
                row.append(1)
                if verbose == True:
                    print(f"{r}, {c} : 1")
            else:
                row.append(0)
                if verbose == True:
                    print(f"{r}, {c} : 0")
        phymat.append(row)
        if verbose == True:
            time.sleep(speed)    
    return(phymat)

def comput_abs_nod(hierarchy, val, taxa, verbose = False, speed = 0.2):
    abs_nod_val = {}
    while list(abs_nod_val.keys()) != list(hierarchy.keys()):
        temp_abs_nod_val = abs_nod_val
        temp_val = {}
        abs_nod_val = {}
        chk_nodes = []
        for i in list(hierarchy.keys()):
            if i not in list(temp_abs_nod_val.keys()):
                chk_nodes.append(i)
        comp_nodes = []
        for i in chk_nodes:
            print(f"{i}")
            chk = 0
            for k in range(len(hierarchy[i])):
                print(f"{k}")
                if hierarchy[i][k] in list(taxa.keys()):
                    chk += 1
                elif hierarchy[i][k] in list(temp_abs_nod_val.keys()):
                    chk += 1
            print(f"i = {i}, chk = {chk}")
            if len(hierarchy[i]) == chk:
                comp_nodes.append(i)
                if verbose == True:
                    print(f"{comp_nodes}")
        for i in comp_nodes:
            for k in range(len(hierarchy[i])):
                if k == 0:
                    temp_val[i] = float(val[hierarchy[i][k]])
                elif hierarchy[i][k] in list(abs_nod_val.keys()):
                    if float(temp_val[i]) < float(temp_abs_nod_val[hierarchy[i][k]]) + float(val[hierarchy[i][k]]):
                        temp_val[i] = float(temp_abs_nod_val[hierarchy[i][k]]) + float(val[hierarchy[i][k]])
                elif float(temp_val[i]) < float(val[hierarchy[i][k]]):
                    temp_val[i] = float(val[hierarchy[i][k]])
        for i in list(hierarchy.keys()):
            if i in list(temp_val.keys()):
                abs_nod_val[i] = temp_val[i]
            elif i in list(temp_abs_nod_val.keys()):
                abs_nod_val[i] = temp_abs_nod_val[i]
        if verbose == True:
            print(f"{abs_nod_val}")
            time.sleep(speed)
    return(abs_nod_val)

def comput_br_len(phymat, val, hierarchy, verbose = False, speed = 0.2):
    rbl = phymat
    for r in range(len(hierarchy)):
        for c in list(val.keys()):
            if phymat[r][c] == 1:
                    rbl[r][c] = float(val[c])
            if verbose == True:
                print(f"Branch between {r} and {c}: {rbl[r][c]}")
            time.sleep(speed)
    return(rbl)

def pr_phymat(hierarchy, taxa, phymat):
    for r in range(len(hierarchy)):
        print(r)
        for c in range(len(hierarchy) + len(taxa)):
            print(phymat[r][c], end="")
        print()