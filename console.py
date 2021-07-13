import pdb
from models.transaction import Transaction
from models.merchant import Merchant
from models.tag import Tag

import repositories.transaction_repository as transaction_repository
import repositories.merchant_repository as merchant_repository
import repositories.tag_repository as tag_repository

transaction_repository.delete_all()
merchant_repository.delete_all()
tag_repository.delete_all()

tag = Tag("home")
tag_repository.save(tag)
# tag1 = Tag("Groceries")
# tag_repository.save(tag1)
# tag2 = Tag("entertainment")
# tag_repository.save(tag2)



merchant = Merchant("tesco")
merchant_repository.save(merchant)
# merchant1 = Merchant("ebay")
# merchant_repository.save(merchant1)
# merchant2 = Merchant("amazon")
# merchant_repository.save(merchant2)





pdb.set_trace()