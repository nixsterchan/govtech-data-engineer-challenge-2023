-- Create TransactionItems Table
CREATE TABLE TransactionItems (
    transaction_id INT REFERENCES Transactions(transaction_id),
    item_id INT REFERENCES Items(item_id),
    PRIMARY KEY (transaction_id, item_id)
);
