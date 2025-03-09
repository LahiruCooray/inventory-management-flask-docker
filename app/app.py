from flask import Flask, request, render_template, url_for
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
import os

app = Flask(__name__) 

load_dotenv()

app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URI')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

if os.getenv('FLASK_ENV') == 'development':
    app.config['DEBUG'] = True
elif os.getenv('FLASK_ENV') == 'production':
    app.config['DEBUG'] = False


db = SQLAlchemy(app)



class Inventory(db.Model):
    '''Create a table called inventory with columns id, name, price, quantity, description'''
    __tablename__ = 'inventory'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Float, nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    description = db.Column(db.Text, nullable=True)
    def __init__(self, name, price, quantity, description):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.description = description



@app.route('/')
def index():
    '''Display all the products in the inventory'''
    products = Inventory.query.all()
    return render_template('index.html', products=products)



@app.route('/add', methods=['POST','GET'])
def add():
    '''Add a product to the inventory'''
    if request.method == "POST":
        name = request.form['name']
        price = request.form['price']
        quantity = request.form['quantity']
        description = request.form["description"]
        if name == '' or price == '' or quantity == '':
            return render_template('add.html', message='Please fill all the fields')
        if db.session.query(Inventory).filter(db.func.lower(Inventory.name) == name.lower()).count() == 0: # Check if product already exists : SELECT COUNT(*) FROM inventory WHERE LOWER(name) = LOWER('product_name');
            data = Inventory(name,price,quantity,description)
            db.session.add(data)                #INSERT INTO inventory (name, price, quantity, description) VALUES ('product_name', 'product_price', 'product_quantity', 'product_description');
            db.session.commit()
            return render_template('add.html', message='Product added successfully')
        return render_template('add.html', nmessage='Product already exists')
    return render_template('add.html')

    

@app.route('/edit/<int:id>', methods=['POST','GET'])
def update_or_delete(id):
    '''Update or delete a product from the inventory'''
    product = Inventory.query.get(id)
    if not product:
        return render_template('edit.html', nmessage='Product not found')

    action = request.form.get('action')  

    if action == 'update':
        product.name = request.form['name']
        product.price = request.form['price']
        product.quantity = request.form['quantity']
        product.description = request.form['description']
        db.session.commit()
        return render_template('edit.html',message='Product updated successfully', product=product)

    elif action == 'delete':
        db.session.delete(product)
        db.session.commit()
        return render_template('edit.html',message='Product deleted successfully')

    else:
        return render_template('edit.html', nmessage='Invalid action')
    


@app.route('/search' , methods=['POST','GET'])
def search_product():
    '''Search for a product in the inventory'''
    if request.method == "POST":
        name = request.form['name'].lower()  # Convert input to lowercase
        product = Inventory.query.filter(db.func.lower(Inventory.name) == name).first()

        if not product:
            return render_template('edit.html', nmessage='Product not found')
        return render_template('edit.html',product=product)
    return render_template('edit.html')



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)


  

