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




