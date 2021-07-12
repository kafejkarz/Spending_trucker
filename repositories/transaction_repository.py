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

def select_all():
    transactions = []
    sql = "SELECT * FROM transactions"
    results = run_sql(sql)
    for row in results:
        tag = tag_repository.select(row['tag_ig'])
        merchant = merchant_repository.select(row['merchant_id'])
        transaction = Transaction(row['transaction_title'], row['amount'], row['tag_id'],tag, merchant, row['merchant_id'])
        transactions.append(transaction)
    return transactions


def select(id):
    transaction = None
    sql = "SELECT * FROM transactions WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        tag = tag_repository.select(result['tag_id'])
        merchant = merchant_repository.select(result['merchant_id'])
        transaction = Transaction(result['transaction_title'], result['amount'], result['tag_id'], tag, merchant, result['merchant_id'] )
    return transaction


def delete_all():
    sql = "DELETE  FROM transactions"
    run_sql(sql)


def delete(id):
    sql = "DELETE  FROM transactions WHERE id = %s"
    values = [id]
    run_sql(sql, values)


def update(transaction):
    sql = "UPDATE transactions SET (transaction_title, amount, tag_id, merchant_id) = (%s, %s, %s, %s) WHERE id = %s"
    values = [transaction.transaction_title, transaction.amount, transaction.tag_id, transaction.merchant_id, transaction_id]
    print(values)
    run_sql(sql, values)