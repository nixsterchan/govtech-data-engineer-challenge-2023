-- Create Transactions Table
CREATE TABLE Transactions (
    transaction_id SERIAL PRIMARY KEY,
    membership_id VARCHAR REFERENCES Members(membership_id) NOT NULL,
    items_bought TEXT NOT NULL, 
    total_items_price DECIMAL(10, 2) NOT NULL,
    total_items_weight_kg DECIMAL(10, 2) NOT NULL,
    created_at TIMESTAMP DEFAULT NOW(),
    updated_at TIMESTAMP DEFAULT NOW()
);
