-- Create TransactionItems Table
CREATE TABLE TransactionItems (
    transaction_item_id SERIAL PRIMARY KEY,
    transaction_id INT REFERENCES Transactions(transaction_id) NOT NULL,
    item_id INT REFERENCES Items(item_id) NOT NULL,
    item_quantity INT NOT NULL,
    price_per_item DECIMAL(10, 2) NOT NULL,
    created_at TIMESTAMP DEFAULT NOW(),
    updated_at TIMESTAMP DEFAULT NOW()
);
