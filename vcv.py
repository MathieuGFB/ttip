import time
from rich.text import Text

#(A,(B,(C,((E,D),(F,(G,H))))));

#   A  B  C  D  E  F  G  H  Distance de Manhattan ?
#A  0
#B  2  0
#C        0
#D           0
#E           1  0
#F           3  3  0
#G           4  4  2  0
#H           4  4  2  1  0

def varcov(seq, taxa, verbose = False, speed = 0.02):
    # Init varcov matrix (i,i) full of 0
    vcv = []
    for i in len(taxa):
        vcv[i] = []
        for j in len(taxa):
            vcv[i].append(0)
    
    # Read seq & count taxa plus nodes?
    

    return(vcv)