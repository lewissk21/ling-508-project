CREATE DATABASE IF NOT EXISTS menus;

USE menus;


CREATE TABLE restaurant (
    id      INT AUTO_INCREMENT PRIMARY KEY,
    name    VARCHAR(255) NOT NULL,
    address VARCHAR(255),
    base_url TEXT
);

CREATE TABLE menu (
    id            INT AUTO_INCREMENT PRIMARY KEY,
    restaurant_id INT NOT NULL,
    type          ENUM('breakfast', 'lunch', 'dinner', 'drinks') NOT NULL,
    image_path    VARCHAR(255),
    transcription TEXT,
    url           TEXT,
    CONSTRAINT fk_menu_restaurant
        FOREIGN KEY (restaurant_id) REFERENCES restaurant (id)
        ON DELETE CASCADE
);

CREATE TABLE dish (
    id          INT AUTO_INCREMENT PRIMARY KEY,
    name        VARCHAR(255) NOT NULL,
    description TEXT,
    price       DECIMAL(10, 2)
);

CREATE TABLE menu_dish (
    menu_id INT NOT NULL,
    dish_id INT NOT NULL,
    PRIMARY KEY (menu_id, dish_id),
    CONSTRAINT fk_menu
        FOREIGN KEY (menu_id) REFERENCES menu (id)
        ON DELETE CASCADE,
    CONSTRAINT fk_dish
        FOREIGN KEY (dish_id) REFERENCES dish (id)
        ON DELETE CASCADE
);

CREATE TABLE ingredient (
    id   INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    UNIQUE KEY uniq_ingredient_name (name)
);

CREATE TABLE dish_ingredient (
    dish_id       INT NOT NULL,
    ingredient_id INT NOT NULL,
    PRIMARY KEY (dish_id, ingredient_id),
    CONSTRAINT fk_dish_id
        FOREIGN KEY (dish_id) REFERENCES dish (id)
        ON DELETE CASCADE,
    CONSTRAINT fk_ingredient_id
        FOREIGN KEY (ingredient_id) REFERENCES ingredient (id)
        ON DELETE CASCADE
);

-- Example data for now
INSERT INTO restaurant (id, name, address, base_url) VALUES
    (1, 'Roxy''s Grilled Cheese', '292 Massachusetts Ave, Cambridge, MA 02139', 'https://roxysgrilledcheese.com');


INSERT INTO menu (id, restaurant_id, type, image_path, transcription, url) VALUES
    (1, 1, 'lunch', 'images/roxys_lunch.jpg',
        'GRILLED CHEESE

            Served on locally baked slow rise bread with our 3 cheese blend

            Classic Three Cheese — $8

            Cheddar • Muenster • Monterey Jack',
        'https://lh3.googleusercontent.com/gps-cs-s/AHRPTWkKJExfKuE3J73hYJcbTdueIJdLxDHECAqqPizWwEJ4DeQCCLM7PnmZBv1P5OdAHwR8oHQxMK_H55ruNFUqkrlGpo-lW45LkCqtme9OcDqbOTrkpW5CEOQ-3pzYfL_C4RuUWQMR=s1360-w1360-h1020-rw');


INSERT INTO dish (id, name, description, price) VALUES
    (1, 'Grilled Cheese Sandwich', 'Served on locally baked slow rise bread with our 3 cheese blend',          8.00);

INSERT INTO menu_dish (menu_id, dish_id) VALUES
    (1, 1);

INSERT INTO ingredient (id, name) VALUES
    (1,  'Cheddar'),
    (2,  'Muenster'),
    (3,  'Monterey Jack');


INSERT INTO dish_ingredient (dish_id, ingredient_id) VALUES
    (1, 1),  (1, 2),  (1, 3);