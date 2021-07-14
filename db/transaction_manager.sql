DROP TABLE IF EXISTS transactions;
DROP TABLE IF EXISTS tags;
DROP TABLE IF EXISTS merchants;


CREATE TABLE merchants (
    id SERIAL PRIMARY KEY,
    merchant_title VARCHAR(225)
);

CREATE TABLE tags (
    id SERIAL PRIMARY KEY,
    tag_title VARCHAR(225)
);


CREATE TABLE transactions (
    id SERIAL PRIMARY KEY,
    transaction_title VARCHAR(225),
    amount INT,
    tag_name VARCHAR REFERENCES tags(tag_title),
    merchant_id INT REFERENCES merchants(id)
);