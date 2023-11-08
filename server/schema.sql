CREATE TABLE users (
    user_id SERIAL PRIMARY KEY,
    username VARCHAR(255) UNIQUE NOT NULL,
    password VARCHAR(255) NOT NULL,
    role VARCHAR(50) NOT NULL
);

CREATE TABLE menu_items (
    item_id SERIAL PRIMARY KEY,
    item_name VARCHAR(255) NOT NULL,
    price DECIMAL(10, 2) NOT NULL
);

CREATE TABLE tables (
    table_id SERIAL PRIMARY KEY,
    table_number VARCHAR(10) UNIQUE NOT NULL
);

CREATE TABLE orders (
    order_id SERIAL PRIMARY KEY,
    table_id INTEGER REFERENCES tables(table_id),
    item_id INTEGER REFERENCES menu_items(item_id),
    quantity INTEGER NOT NULL,
    order_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    status VARCHAR(50) DEFAULT 'Đang chờ'
);

CREATE TABLE invoice_details (
    detail_id SERIAL PRIMARY KEY,
    order_id INTEGER REFERENCES orders(order_id),
    item_id INTEGER REFERENCES menu_items(item_id),
    quantity INTEGER NOT NULL,
    price DECIMAL(10, 2) NOT NULL,
    subtotal DECIMAL(10, 2) NOT NULL
);

---------------------------------------------------
INSERT INTO public.menu_items
(item_id, item_name, price)
VALUES(1, 'Cơm Tấm', 50000.00);
INSERT INTO public.menu_items
(item_id, item_name, price)
VALUES(2, 'Phở', 50000.00);
INSERT INTO public.menu_items
(item_id, item_name, price)
VALUES(3, 'Hủ Tiếu', 50000.00);
INSERT INTO public.menu_items
(item_id, item_name, price)
VALUES(4, 'Bún chả', 50000.00);
INSERT INTO public.menu_items
(item_id, item_name, price)
VALUES(5, 'Gỏi cuốn', 50000.00);


---------------------------------------------------