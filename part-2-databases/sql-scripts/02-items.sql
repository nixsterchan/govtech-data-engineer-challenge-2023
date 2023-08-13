-- Create Items Table
CREATE TABLE Items (
    item_id SERIAL PRIMARY KEY,
    item_name VARCHAR(100) NOT NULL,
    manufacturer_name VARCHAR(100) NOT NULL,
    cost DECIMAL(10, 2) NOT NULL,
    weight_kg DECIMAL(10, 2) NOT NULL,
    created_at TIMESTAMP DEFAULT NOW(),
    updated_at TIMESTAMP DEFAULT NOW(),
    CONSTRAINT unique_item_name UNIQUE (item_name)
);
