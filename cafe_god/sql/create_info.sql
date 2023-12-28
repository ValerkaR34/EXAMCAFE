
-- Вставка данных в таблицу специального меню
INSERT INTO special_menu (item_id, special_name, special_description, special_price) VALUES
    (1, 'Special Burger', 'Our signature burger with extra toppings', 14.99),
    (2, 'Chef''s Special Pizza', 'Unique pizza with chef''s special toppings', 15.99),
    (3, 'Weekend Pasta', 'Special pasta dish for the weekend', 11.50),
    (4, 'Healthy Salad', 'Fresh and healthy salad option', 7.99);

-- Вставка данных в таблицу пользователей
INSERT INTO users (username, email, password) VALUES
    ('JohnDoe', 'john@example.com', 'password123'),
    ('JaneSmith', 'jane@example.com', 'securepass'),
    ('AliceJones', 'alice@example.com', 'letmein'),
    ('BobJohnson', 'bob@example.com', 'userpass');

-- Вставка данных в таблицу заказов
INSERT INTO orders (user_id, total_amount) VALUES
    (1, 25.99),
    (2, 18.50),
    (3, 32.75),
    (4, 21.00);

-- Вставка данных в таблицу меню
INSERT INTO menu (item_name, item_description, price) VALUES
    ('Burger', 'Delicious beef burger', 10.99),
    ('Pizza', 'Margherita pizza', 12.50),
    ('Pasta', 'Spaghetti with marinara sauce', 9.75),
    ('Salad', 'Caesar salad with grilled chicken', 8.50);



-- Вставка данных в таблицу книги отзывов
INSERT INTO reviews (user_id, order_id, rating, comment) VALUES
    (1, 1, 5, 'Great experience! The food was amazing.'),
    (2, 2, 4, 'Nice atmosphere and friendly staff.'),
    (3, 3, 3, 'Decent food, but service could be improved.'),
    (4, 4, 5, 'Loved the variety of options on the menu.');