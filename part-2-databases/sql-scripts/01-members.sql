-- Create Members Table
CREATE TABLE Members (
    membership_id VARCHAR(100) PRIMARY KEY NOT NULL,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    email VARCHAR(100) NOT NULL,
    mobile_number VARCHAR(10) NOT NULL,
    date_of_birth VARCHAR(10) NOT NULL,
    above_eighteen BOOLEAN NOT NULL,
    created_at TIMESTAMP DEFAULT NOW(),
    updated_at TIMESTAMP DEFAULT NOW(),
    CONSTRAINT unique_membership_id UNIQUE (membership_id)
);