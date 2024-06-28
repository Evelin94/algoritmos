from datetime import datetime
from config import db, app
from models import Customer, Order

with app.app_context():
    db.create_all()
    
    
    if not Customer.query.filter_by(email='juan1234@gmail.com').first():
        customer1 = Customer(name='Juan Oliva', email='juan1234@gmail.com')
        db.session.add(customer1)
    
    if not Customer.query.filter_by(email='maria.4567@gmail.com').first():
        customer2 = Customer(name='Maria Tomas', email='maria.4567@gmail.com')
        db.session.add(customer2)

    db.session.commit()


    customer1 = Customer.query.filter_by(email='juan1234@gmail.com').first()
    customer2 = Customer.query.filter_by(email='maria.4567@gmail.com').first()

    if not Order.query.filter_by(total_amount=150.00, customer_id=customer1.id).first():
        order1 = Order(date_ordered=datetime.utcnow(), total_amount=150.00, customer_id=customer1.id)
        db.session.add(order1)
    
    if not Order.query.filter_by(total_amount=200.00, customer_id=customer1.id).first():
        order2 = Order(date_ordered=datetime.utcnow(), total_amount=200.00, customer_id=customer1.id)
        db.session.add(order2)

    if not Order.query.filter_by(total_amount=300.00, customer_id=customer2.id).first():
        order3 = Order(date_ordered=datetime.utcnow(), total_amount=300.00, customer_id=customer2.id)
        db.session.add(order3)

    db.session.commit()
