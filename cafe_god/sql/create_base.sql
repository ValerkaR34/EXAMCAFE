-- Таблица пользователей
CREATE TABLE IF NOT EXISTS users (
    user_id INTEGER PRIMARY KEY,
    username TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE,
    password TEXT NOT NULL,
    registration_date DATETIME DEFAULT CURRENT_TIMESTAMP
);

-- Таблица заказов
CREATE TABLE IF NOT EXISTS orders (
    order_id INTEGER PRIMARY KEY,
    user_id INTEGER,
    order_date DATETIME DEFAULT CURRENT_TIMESTAMP,
    total_amount REAL NOT NULL,
    FOREIGN KEY (user_id) REFERENCES users(user_id)
);

-- Таблица меню
CREATE TABLE IF NOT EXISTS menu (
    item_id INTEGER PRIMARY KEY,
    item_name TEXT NOT NULL,
    item_description TEXT,
    price REAL NOT NULL
);

-- Таблица специального меню
CREATE TABLE IF NOT EXISTS special_menu (
    special_id INTEGER PRIMARY KEY,
    item_id INTEGER,
    special_name TEXT NOT NULL,
    special_description TEXT,
    special_price REAL NOT NULL,
    FOREIGN KEY (item_id) REFERENCES menu(item_id)
);

-- Таблица книги отзывов
CREATE TABLE IF NOT EXISTS reviews (
    review_id INTEGER PRIMARY KEY,
    user_id INTEGER,
    order_id INTEGER,
    rating INTEGER NOT NULL,
    comment TEXT,
    review_date DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(user_id),
    FOREIGN KEY (order_id) REFERENCES orders(order_id)
);
