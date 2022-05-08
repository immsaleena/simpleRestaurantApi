from flask import Flask, render_template, request, redirect, g, Response
import sqlite3
import random
import models

app = Flask(__name__)
    
@app.route('/', methods = ['GET','POST'])
def create_order():
    if request.method == 'GET':
        return render_template('main.html')

    if request.method == 'POST':
        order_items = request.form['order_item']
        customer_names = request.form['customer_name']
        order_tables = request.form['order_table']

        models.create_order_in_bulk(order_tables, customer_names, order_items)
    
    return Response("success", status=201, mimetype='application/json')
        
@app.route('/added', methods = ['GET'])
def thankyou():
    return render_template('thankyou.html')

@app.route('/orderdatalist', methods = ['GET'])
def retrieveOrderlist():
    orders = models.get_order_list()
    return render_template('orderlist.html',orders=orders)

@app.route('/<int:order_id>/update', methods = ['GET','POST'])
def update(order_id):
    if request.method == 'POST':
        order_id = request.form['order_id']
        order_items = request.form.getlist('order_item')
        order_menu = ",".join(map(str, order_items))
        customer_name = request.form['customer_name']
        order_table = request.form['order_table']

        models.update_order(order_id, customer_name, order_table, order_menu)

        return redirect('/orderdatalist')

    orders = models.get_order_list_by_id(order_id)
    
    return render_template('update.html',orders=orders)

@app.route('/<int:order_id>/delete', methods = ['GET'])
def delete(order_id):
    models.delete_order(order_id=order_id)

    return redirect('/orderdatalist')

@app.route('/<string:order_table>/filter', methods = ['GET'])
def filter_order(order_table):
    orders = models.get_order_list_by_order_table(order_table)

    return render_template('orderlist.html',orders=orders)

if __name__ == '__main__':
    app.run(debug=True)