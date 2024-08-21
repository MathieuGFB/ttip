import time

def comput_vcv(hierarchy, taxa, verbose = False, speed = 0.2):
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

def vcv_bl(vcv, hierarchy, val, verbose = False, speed = 0.2):
    if val:
        for r in range(len(hierarchy)):
            for c in list(val.keys()):
                if vcv[r][c] == 1:
                        vcv[r][c] = float(val[c])
                if verbose == True:
                    print(f"Branch between {r} and {c}: {vcv[r][c]}")
                    time.sleep(speed)    
    
    return(vcv)

def comput_anv(vcv, taxa, hierarchy, verbose = False, speed = 0.2):
    root_tip = {}
    for i in list(taxa.keys()):
        if verbose == True:
            time.sleep(speed)
            print(f"Taxon {i}")
        for j in list(hierarchy.keys()):
            if i in hierarchy[j]:
                root_tip[i] = vcv[j - len(taxa)][i]
                c = j
                if verbose == True:
                    time.sleep(speed)
                    print(f"Taxon {i} found in node {j}: value = {round(root_tip[i],4)}")
        if verbose == True:
            print(f"Beginning node computation")
            time.sleep(speed)
        while c != list(hierarchy.keys())[0]:
            if verbose == True:
                print(f"Node checked: {c}")
            for k in list(hierarchy.keys()):
                if c in hierarchy[k]:
                    root_tip[i] += vcv[k - len(taxa)][c]
                    c = k
                    if verbose == True:
                        time.sleep(speed)
                        print(f"Node {c} found in node {k}: updated value = {round(root_tip[i],4)}")
        root_tip[i] = round(root_tip[i], 4)
    return(root_tip)