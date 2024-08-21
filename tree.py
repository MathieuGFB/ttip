class tree_obj:
    """A hierarchical tree object"""
    def __init__(self):
        self.taxa = {} # List of taxa associated with numerical key
        self.vcv = [] # Var covar matrix
        self.errors = {} # Errors list
        self.seq = "" # Raw tree sequence
        self.nn = 0 # Number of nodes
        self.bl = False # Branch lengths
        self.ultram = True # Is ultrametric