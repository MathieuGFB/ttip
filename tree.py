class tree_obj:
    """A hierarchical tree object"""
    def __init__(self):
        self.taxa = {} # List of taxa associated with numerical key
        self.vcv = [] # Var covar matrix
        self.errors = {} # Errors list
        self.tax_val = {} # List of values associated to taxa
        self.nod_val = {} # List of values associated to nodes
        self.seq = "" # Raw tree sequence
        self.nn = 0 # Number of nodes
        self.bl = False # Branch lengths
        self.ultram = True # Is ultrametric
        #self.name = "" # ID of the object
    
    # TO DO : add a function to give summary of what is registered in each obj.