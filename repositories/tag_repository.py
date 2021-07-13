from db.run_sql import run_sql

from models.tag import Tag
from models.merchant import Merchant
from models.transaction import Transaction


def save(tag):
    sql = "INSERT INTO tags (tag_title) VALUES (%s) RETURNING *"
    values = [tag.tag_title]
    results = run_sql(sql, values)
    id = results[0]['id']
    tag.id = id
    return tag


def select_all():
    tags = []

    sql = "SELECT * FROM tags"
    results = run_sql(sql)

    for row in results:
        tag = Tag( row['tag_title'], row['id'] )
        tags.append(tag)
    return tags


def select(id):
    tag = None
    sql = "SELECT * FROM tags WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        tag = Tag(result['tag_title'], result['id'] )
    return tag


def delete_all():
    sql = "DELETE  FROM tags"
    run_sql(sql)


def delete(id):
    sql = "DELETE  FROM tags WHERE id = %s"
    values = [id]
    run_sql(sql, values)


def update(author):
    sql = "UPDATE tags SET (tag_title) = (%s) WHERE id = %s"
    values = [Tag.tag_title, Tag.id]
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