from flask import Flask, render_template, request, redirect, url_for
from datetime import datetime

app = Flask(__name__)
transactions = []

@app.route('/')
def index():
    income = sum(t['amount'] for t in transactions if t['type'] == 'income')
    expense = sum(t['amount'] for t in transactions if t['type'] == 'expense')
    balance = income - expense
    return render_template('index.html', transactions=transactions, income=income, expense=expense, balance=balance)

@app.route('/add', methods=['POST'])
def add():
    t_type = request.form['type']
    category = request.form['category']
    amount = float(request.form['amount'])
    description = request.form['description']
    transaction = {
        'id': len(transactions) + 1,
        'type': t_type,
        'category': category,
        'amount': amount,
        'description': description,
        'date': datetime.now().strftime('%Y-%m-%d')
    }
    transactions.append(transaction)
    return redirect(url_for('index'))

@app.route('/delete/<int:id>')
def delete(id):
    global transactions
    transactions = [t for t in transactions if t['id'] != id]
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)