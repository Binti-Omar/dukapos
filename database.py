import psycopg2

conn = psycopg2.connect(host = "localhost",port = 5432,user = "postgres",password = "C0717824020",dbname = "duka_pos")

cur = conn.cursor()

def display_products():
    cur.execute("select * from products")
    products=cur.fetchall()
    return products

products=display_products()
# print(products)

def display_sales():
    cur.execute("select * from sales")
    sales=cur.fetchall()
    return sales

sales=display_sales()
# print(sales)

def display_stock():
    cur.execute("select * from stock")
    stock=cur.fetchall()
    return stock

stock=display_stock()
# print(stock)

def insert_products(product_values):
    cur.execute(f"insert into products(product_name,buying_price,selling_price)values{product_values}")
    conn.commit()

product1=("Bread",50,75)
product2=("Kiwi",150,200)
# insert_products(product1)
# insert_products(product2)

def insert_sales(sales_values):
    cur.execute(f"insert into sales(pid,quantity)values{sales_values}")
    conn.commit()

sale1=(2,1)
sale2=(1,2)
# insert_sales(sale1)
# insert_sales(sale2)

def insert_stock(stock_values):
    cur.execute(f"insert into stock(pid,stock_quantity)values{stock_values}")
    conn.commit()

stock1=(1,34)
stock2=(2,29)
# insert_stock(stock1)
# insert_stock(stock2)

def insert_user(user_values):
    query='insert into users (fullname,email,password,role) values (%s,%s,%s,%s);'
    cur.execute(query,user_values)
    conn.commit()

def check_email(email):
    query='select * from users where email=%s'
    cur.execute(query,(email,))
    data=cur.fetchone()
    return data