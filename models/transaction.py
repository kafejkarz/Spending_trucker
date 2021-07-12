class Transaction:
    def __init__(self,transaction_title, amount, tag, merchant, id=None):
        self.transaction_title = transaction_title
        self.amount = amount
        self.tag = tag
        self.merchant = merchant
        self.id = id 
