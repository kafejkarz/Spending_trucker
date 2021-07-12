from db.run_sql import run_sql

from models.transaction import Transaction
from models.merchant import Merchant
from models.tag import Tag 


def save(merchant):
    sql = "INSERT INTO merchants (merchant_title) VALUES (%s) RETURNING *"
    values = [merchant.merchant_title]
    results = run_sql(sql, values)
    id = results[0]['id']
    merchant.id = id
    return merchant


def select_all():
    merchants = []

    sql = "SELECT * FROM merchants"
    results = run_sql(sql)

    for row in results:
        merchant = Merchant(row['merchant_title'], row['id'] )
        merchants.append(merchant)
    return merchants


def select(id):
    merchant = None
    sql = "SELECT * FROM merchants WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        merchant = Merchant(result['merchant_title'], result['id'] )
    return merchant


def delete_all():
    sql = "DELETE  FROM merchants"
    run_sql(sql)


def delete(id):
    sql = "DELETE  FROM merchants WHERE id = %s"
    values = [id]
    run_sql(sql, values)


def update(merchant):
    sql = "UPDATE merchants SET (merchant_title) = (%s, %s) WHERE id = %s"
    values = [merchant.merchant_title, merchant.id]
    run_sql(sql, values)

# def books(author):
#     books = []

#     sql = "SELECT * FROM books WHERE author_id = %s"
#     values = [author.id]
#     results = run_sql(sql, values)

#     for row in results:
#         book = Book(row['title'], row['genre'], row['publisher'], row['author_id'], row['id'] )
#         books.append(book)
#     return books