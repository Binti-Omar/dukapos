from flask import Flask,render_template,request,redirect,url_for
from database import display_products,display_sales,display_stock,insert_products,insert_sales,insert_stock

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/products")
def products():
    products=display_products()
    return render_template("products.html",products=products)

@app.route("/add_products",methods=["GET","POST"])
def add_products():
    if request.method=="POST":
        product_name=request.form["p_name"]
        buying_price=request.form["b_price"]
        selling_price=request.form["s_price"]
        new_product=(product_name,buying_price,selling_price)
        # print(new_product)
        insert_products(new_product)
    return redirect(url_for("products"))




@app.route("/sales")
def sales():
    sales=display_sales()
    products=display_products()
    return render_template("sales.html",sales=sales,products=products)

@app.route("/make_sale",methods=["GET","POST"])
def make_sale():
    if request.method=="POST":
        pid=request.form["pid"]
        quantity=request.form["quantity"]
        new_sale=(pid,quantity)
        insert_sales(new_sale)
    return redirect(url_for("sales"))



@app.route("/stock")
def stock():
    stock=display_stock()
    products=display_products()
    return render_template("stock.html",stock=stock,products=products)

@app.route("/add_stock",methods=["GET","POST"])
def add_stock():
    if request.method=="POST":
        pid=request.form["pid"]
        stock_quantity=request.form["s_quantity"]
        new_stock=(pid,stock_quantity)
        insert_stock(new_stock)
        return redirect(url_for("stock"))

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