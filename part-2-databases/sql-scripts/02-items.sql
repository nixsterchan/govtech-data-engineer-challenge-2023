-- Create Items Table
CREATE TABLE Items (
    item_id SERIAL PRIMARY KEY,
    item_name VARCHAR(100) NOT NULL,
    manufacturer_name VARCHAR(100),
    cost DECIMAL(10, 2),
    weight_kg DECIMAL(10, 2),
    CONSTRAINT unique_item_name UNIQUE (item_name)
);
