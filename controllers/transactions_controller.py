from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.transaction import Transaction
import repositories.transaction_repository as transaction_repository
import repositories.merchant_repository as merchant_repository
import repositories.tag_repository as tag_repository

transactions_blueprint = Blueprint("transactions", __name__)





@transactions_blueprint.route("/transactions")
def transactions():
    transactions = transaction_repository.select_all()
    return render_template("transactions/index.html", transactions=transactions)

# NEW
# GET

@transactions_blueprint.route("/transactions/new", methods=["GET"])
def new_transaction():
    transactions = transaction_repository.select_all()
    return render_template("transactions/new.html", transactions=transactions)


@transactions_blueprint.route("/transactions", methods=['POST'])
def create_transaction():
    transaction_title =request.form["transaction_title"]
    amount = request.form['amount']
    merchant = request.form['merchant']
    tag = request.form['tag']
    new_transaction = Transaction(transaction_title, amount, tag ,merchant )
    transaction_repository.save(new_transaction)
    return redirect('/transactions')

@transactions_blueprint.route("/transactions/<id>/delete", methods=['POST'])
def delete_transaction(id):
    transaction_repository.delete(id)
    return redirect("/transactions")


