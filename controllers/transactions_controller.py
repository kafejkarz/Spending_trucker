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
    return render_template("transactions/index.html")


@transactions_blueprint.route("/transactions/new", methods=["GET"])
def new_transaction():
    transactions = transaction_repository.select_all()
    return render_template("transactions/new.html")


@transactions_blueprint.route("/transactions", methods=['POST'])
def create_transaction():
    amount = request.form['amount']
    merchant = request.form['merchant']
    date = request.form['date']
    tag = request.form['tag']
    transaction = Transaction(transaction_title, amount, tag_id, merchand_id)
    transaction_repository.save(transaction)
    return redirect('/transactions')


