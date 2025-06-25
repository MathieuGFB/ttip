import requests, json
from rich.text import Text
from rich.console import Console

console = Console()

# Rich styles
error = "red bold"
correct = "green bold"
shc_tax = "magenta bold"
attention = "yellow bold"
shc_dat = "cyan bold"

strati = ["Cambrian", "Ordovician", "Silurian", "Devonian", "Carboniferous", "Permian", "Triassic", "Jurassic", "Cretaceous", "Paleogene", "Neogene", "Quaternary"]

headers = {
    "User-Agent":"Mozilla/5.0",
    "Referer":"https://paleobiodb.org"
}

## from taxa
# What about extant taxa ? Should be at 0
def calib_taxa(taxa, dat = "lag", verbose = False):
    err = False # if taxon missing in pbdb, stop the function
    i = 0 # counter
    dattax = {} # dic to store lag / eag for each taxon
    while err == False & i != len(taxa):
        url = "https://paleobiodb.org/data1.2/occs/list.json?base_name=" + taxa[i] + "&show=class"
        f = requests.get(url, headers=headers)
        rec = json.loads(f.text)["records"]
        if len() != 0:
            for j in range(0, len(rec)):
                if dattax[taxa[i]] == 0:
                    dattax[taxa[i]] == rec[j][dat]
                    if verbose == True:
                        console.print(
                            Text.assemble(
                                "New date for taxon",
                                (f"{taxa[i]}", shc_tax),
                                ": ",
                                (f"{dattax[taxai]}", shc_dat)
                            )
                        )
                elif rec[j][dat] < dattax[taxa[i]]:
                    dattax[taxa[i]] == rec[j][dat]
            i += 1
        else:
            console.print(
                Text.assemble("No record for the taxon ", taxa[i], ". Consider checking your taxonomy. Aborting calibration"),
                style = error
            )
            err = True
        if err == False:
            if verbose == True:
                console.print(
                    Text.assemble(
                        "Data successfully retrieved from Paleobiodb.org",
                        style = correct
                    )
                )
            return(dattax)

# How to treat data ? 1. find lowest date (up to 0) if no 0, then should change the lowest to 0... Shall we? 
# If : in tree, remove every one of them

if tree.find(":") != -1: # Detection and removal of former node values
    if verbose == True:
        console.print(
            Text.assemble(
                "Nodes values have been detected and will be erased by the new calibration",
                style = attention
            )
        )
    while n != len(tree):
        if tree[n] == ":":
            m = n+1
            while tree[m] != ")" & tree[m] != ",":
                m += 1
            sttree = tree[0:n] + tree[m:len(tree)]


## part 0 : identify the taxa to query
### 0.1 Leaves
### 0.2 Nodes

## part 1 : building the url to fetch data from

name = "Pseudosuchia" # To get from the tree or another method
i = 0
url = "https://paleobiodb.org/data1.2/occs/list.json?base_name=" + name + "&interval=" + strati[i] + "&show=class"
f = requests.get(url, headers=headers)

if len(json.loads(f.text)["records"]) == 0:
    while len(json.loads(f.text)["records"]) == 0:
        i += 1
        url = "https://paleobiodb.org/data1.2/occs/list.json?base_name=" + name + "&interval=" + strati[i] + "&show=class"

for n in json.loads(f.text)["records"]: # loop to find highest lag
    if n == 0:
        idn = json.loads(f.text)["records"][0]["idn"]
        lag = json.loads(f.text)["records"][0]["lag"]
    elif json.loads(f.text)["records"][0]["lag"] > lag:
        idn = json.loads(f.text)["records"][0]["idn"]
        lag = json.loads(f.text)["records"][0]["lag"]
    

## part 2 : use this data
