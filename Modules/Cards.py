class Cards:
   
    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank
   
    def __str__(self):
       return " %s of %s " %(self.suit,self.rank)




