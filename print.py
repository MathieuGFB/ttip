def probject(tree_obj):
    for i in tree_obj.keys():
        print(f"-- Tree {i} --\n\n{tree_obj[i].seq}")
        if tree_obj[i].taxa:
            print("- Taxa - \n\n")
            for j in tree_obj[i].taxa.keys():
                print(f"{j}: {tree_obj[i].taxa[j]}")
            if len(tree_obj[i].errors) > 0:
                print("- Errors -\n\n")
                for j in tree_obj[i].errors.keys():
                    print(f"{j}: {tree_obj[i].errors[j]}")
            else:
                print("No errors in this tree.")
            if tree_obj[i].bl == True:
                print("This tree contains branch lengths")
            else:
                print("This tree does not contain branch lengths")
            print("- VCV -\n\n")
            prvcv(tree_obj[i].taxa, tree_obj[i].vcv)
        else:
            print("This tree was not verified and analysed.")

def prvcv(taxa, vcv):
        head = "      "
        for i in range(len(taxa) + len(vcv)):
            head += str(i)
            if i < 10:
                head += "  "
            elif i < 100:
                head += " "
        print(f"{head}")
        for j in range(len(vcv)):
            if len(taxa) + j < 10:
                print(f"00{len(taxa) + j}: {vcv[j]}")
            elif len(taxa) + j < 100:
                print(f"0{len(taxa) + j}: {vcv[j]}")
            else:
                print(f"{len(taxa) + j}: {vcv[j]}")