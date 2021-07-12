DROP TABLE IF EXISTS tags;
DROP TABLE IF EXISTS merchants;
DROP TABLE IF EXISTS transactions;


CREATE TABLE transactions (
    id SERIAL PRIMARY KEY,
    transaction_title VARCHANT(225),
    amount INT,
    tag_id INT REFERENCE transactions(id),
    merchant_id INT REFERENCE merchant(id)
);

CREATE TABLE merchants (
    id SERIAL PRIMARY KEY,
    merchant_title VARCHANT(225),
);

CREATE TABLE tags (
    id SERIAL PRIMARY KEY,
    tag_title VARCHANT(225)
);

