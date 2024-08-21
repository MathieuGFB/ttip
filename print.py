def probject(tree_obj):
    for i in tree_obj.keys():
        print(f"-- Tree {i} --\n\n{tree_obj[i].seq}")
        if tree_obj[i].taxa:
            for j in tree_obj[i].taxa.keys():
                print(f"{j}: {tree_obj[i].taxa[j]}")
            if len(tree_obj[i].errors) > 0:
                for j in tree_obj[i].errors.keys():
                    print(f"{j}: {tree_obj[i].errors[j]}")
            else:
                print("No errors in this tree.")
            if tree_obj[i].bl == True:
                print("This tree contains branch lengths")
            else:
                print("This tree does not contain branch lengths")
            print("Print of VCV is in development.")
        else:
            print("This tree was not verified and analysed.")