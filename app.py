from flask import render_template
from config import app, db
from models import Customer, Order
import people  

@app.route('/')
def home():
    customers = Customer.query.all()
    return render_template('home.html', customers=customers)

if __name__ == '__main__':
    app.run(debug=True, port=8000)
