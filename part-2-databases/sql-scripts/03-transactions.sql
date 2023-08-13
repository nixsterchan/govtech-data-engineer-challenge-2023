-- Create Transactions Table
CREATE TABLE Transactions (
    transaction_id SERIAL PRIMARY KEY,
    membership_id VARCHAR REFERENCES Members(membership_id),
    items_bought TEXT, -- Store JSON or serialized data
    total_items_price DECIMAL(10, 2),
    total_items_weight_kg DECIMAL(10, 2)
);
