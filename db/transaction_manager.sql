DROP TABLE IF EXISTS tag;
DROP TABLE IF EXISTS merchant;
DROP TABLE IF EXISTS transaction;


CREATE TABLE transaction (
    id SERIAL PRIMARY KEY,
    transaction_title VARCHANT(225),
    amount INT,
    tag_id INT REFERENCE transactions(id),
    merchant_id INT REFERENCE merchant(id)
);

CREATE TABLE merchant(
    id SERIAL PRIMARY KEY,
    merchant_title VARCHANT(225),
);

CREATE TABLE tag (
    id SERIAL PRIMARY KEY,
    tag_title VARCHANT(225)
);

