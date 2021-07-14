class Transaction:
    def __init__(self,transaction_title, amount, tag_id, merchant_id, id=None):
        self.transaction_title = transaction_title
        self.amount = amount
        self.tag_id = tag_id
        self.merchant_id = merchant_id
        self.id = id 
