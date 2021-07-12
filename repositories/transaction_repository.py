from db.run_sql import run_sql

from models.transaction import Transaction
from models.merchant import Merchant
from models.tag import Tag

import repositories.transaction_repository as transaction_repository


def save(transaction):
    sql = "INSERT INTO transactions (transaction_title, amount, tag_id, merchant_id) VALUES (%s, %s, %s, %s) RETURNING * "
    values = [transaction.transaction_title, transaction.amount, transaction.tag_id, transaction.merchant_id]
    results = run_sql(sql, values)
    id = results[0]['id']
    transaction.id = id
    return transaction