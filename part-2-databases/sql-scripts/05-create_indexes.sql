-- Create index for items.item_name
CREATE INDEX idx_items_item_name ON Items (item_name);

-- Create index for transactions.membership_id
CREATE INDEX idx_transactions_membership_id ON Transactions (membership_id);

-- Create index for transaction_items.transaction_id
CREATE INDEX idx_transaction_items_transaction_id ON TransactionItems (transaction_id);
