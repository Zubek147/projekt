from flask import Flask, render_template, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

@app.route('/')
def index():
    return render_template('index.html', expenses = expenses)

expenses = []

class ExpenseList(Resource):
    def get(self):
        return expenses

    def post(self):
        data = request.get_json()
        expenses.append(data)
        return data, 201

api.add_resource(ExpenseList, '/expenses')

@app.route('/add_expense', methods=['POST'])
def add_expense():
    new_expense = request.form.get('expense')
    expenses.append(new_expense)
    return render_template('index.html', expenses=expenses)

if __name__ == '__main__':
    app.run(debug=True)