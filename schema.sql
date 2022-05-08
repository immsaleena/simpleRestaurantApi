DROP TABLE IF EXISTS order_list;

CREATE TABLE order_list (
    order_id INTEGER PRIMARY KEY AUTOINCREMENT,
    customer_name VARCHAR(100) NOT NULL,
    order_table VARCHAR(100) NOT NULL,
    order_menu VARCHAR(40) NOT NULL,
    cooking_time INT NOT NULL
);