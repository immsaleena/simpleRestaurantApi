import sqlite3
import random

DATABASE = 'restaurants.db'

def get_db_connection():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn

def create_order(order_table, customer_name, order_menu, cooking_time):
    conn = get_db_connection()
    conn.execute('INSERT INTO order_list (order_table, customer_name, order_menu, cooking_time) VALUES ( ?, ?, ?, ?)',
                (order_table, customer_name, order_menu, cooking_time))
    conn.commit()
    conn.close()

def create_order_in_bulk(order_tables, customer_names, order_menus):
    order_tables = order_tables.split(",")
    customer_names = customer_names.split(",")
    order_menus = order_menus.split(",")

    conn = get_db_connection()
    for order_table, customer_name, order_menu in zip(order_tables, customer_names, order_menus):
        cooking_time = random.randint(5, 15)
        conn.execute('INSERT INTO order_list (order_table, customer_name, order_menu, cooking_time) VALUES ( ?, ?, ?, ?)',
                (order_table, customer_name, order_menu, cooking_time))
    
    conn.commit()
    conn.close()

def get_order_list():
    conn = get_db_connection()
    orders = conn.execute('SELECT * from order_list').fetchall()
    conn.close()
    return orders

def get_order_list_by_id(order_id):
    conn = get_db_connection()
    order = conn.execute('SELECT * from order_list WHERE order_id=?',(int(order_id),)).fetchone()
    order  = [o for o in order]
    return order

def update_order(order_id, customer_name, order_table, order_menu):
    conn = get_db_connection()
    conn.execute('UPDATE order_list SET customer_name=?, order_table=?, order_menu=? WHERE order_id=?',(customer_name, order_table, order_menu, order_id))
    conn.commit()
    conn.close()

def delete_order(order_id):
    conn = get_db_connection()
    conn.execute('DELETE FROM order_list WHERE order_id=?',(order_id,))
    conn.commit()
    conn.close()

def get_order_list_by_order_table(order_table):
    conn = get_db_connection()
    order = conn.execute('SELECT * from order_list WHERE order_table=?',(str(order_table),)).fetchall()
    # order = [o for o in order]
    return order






