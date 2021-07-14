class Transaction:
    def __init__(self,transaction_title, amount, tag_name, merchant_id, id=None):
        self.transaction_title = transaction_title
        self.amount = amount
        self.tag_name = tag_name
        self.merchant_id = merchant_id
        self.id = id 
