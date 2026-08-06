from flask import Flask,render_template,request,redirect,url_for,session,flash
from database import display_products,display_sales,display_stock,insert_products,insert_sales,insert_stock,insert_user,check_email
from flask_bcrypt import Bcrypt
from functools import wraps


app = Flask(__name__)
bcrypt = Bcrypt(app)
app.secret_key="kdjuiwehdjslmcmdjvbef"

@app.route("/")
def home():
    return render_template("index.html")

def login_required(f):
    @wraps(f) 
    def protected(*args,**kwargs):
        if 'email' not in session:
            return redirect(url_for('login'))
        return f(*args,**kwargs)
    return protected

@app.route("/products")
@login_required
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
        flash('Products added successfully',"success")
    return redirect(url_for("products"))

@app.route('/update_products',methods=['GET','POST'])
def update_products():
    if request.method=='POST':
        product_id=request.form['id']
        product_name=request.form['p_name']
        buying_price=request.form['b_price']
        selling_price=request.form['s_price']

        update_products(product_name,buying_price,selling_price,id)
        flash('Product updated successfully',"success")
        return redirect(url_for('products'))
    return redirect(url_for('products'))

@app.route("/sales")
@login_required
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
        flash('Sales added successfully',"success")
    return redirect(url_for("sales"))

@app.route("/stock")
@login_required
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
        flash('Stock added successfully',"succes")
        return redirect(url_for("stock"))

@app.route("/dashboard")
@login_required
def dashboard():
    return render_template("dashboard.html")

@app.route("/register",methods=["GET","POST"])
def register():
    if request.method=="POST":
        fullname=request.form["f_name"]
        email=request.form["email"]
        password=request.form["password"]
        role=request.form["role"]
        hashed_password=bcrypt.generate_password_hash(password).decode("utf-8")
        new_user=(fullname,email,hashed_password,role)

        check=check_email(email)
        if check==None:
            insert_user(new_user)
            flash('Registered successfully,please proceed to login',"success")
            return redirect(url_for('login'))
        else:
            flash('User already exists use a different email or login please',"warning")
    return render_template('register.html')

@app.route("/login",methods=["GET","POST"])
def login():
    if request.method=="POST":
        email=request.form["email"]
        password=request.form["password"]

        check=check_email(email)
        if check==None:
            flash("The email does not exist,please register","danger")
            return redirect(url_for("register"))
        else:
            if bcrypt.check_password_hash(check[3],password):
                session['email']=email
                flash('login successfully',"success")
                return redirect(url_for('dashboard'))
            else:
                flash('Incorrect password',"warning")
                return render_template('login.html')
    return render_template("login.html")

@app.route('/logout')
def logout():
    session.pop('email',None)
    flash('You have been logged out',"danger")
    return redirect(url_for('login'))

app.run(debug=True)