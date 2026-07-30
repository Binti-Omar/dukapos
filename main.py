from flask import Flask,render_template
from database import display_products,display_sales,display_stock

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/products")
def products():
    products=display_products()
    return render_template("products.html",products=products)

@app.route("/sales")
def sales():
    sales=display_sales()
    products=display_products()
    return render_template("sales.html",sales=sales,products=products)

@app.route("/stock")
def stock():
    stock=display_stock()
    products=display_products()
    return render_template("stock.html",stock=stock,products=products)

@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")

@app.route("/register")
def register():
    return render_template("register.html")

@app.route("/login")
def login():
    return render_template("login.html")

app.run(debug=True)