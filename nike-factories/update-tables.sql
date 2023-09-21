-- Create products table
CREATE TABLE products (
	product_type_id INT PRIMARY KEY,
    product_type VARCHAR(50)
);

-- Add product_type_id column to the factories table
ALTER TABLE factories
ADD COLUMN product_type_id INT;

-- Add foreign key to the factories table
ALTER TABLE factories
ADD FOREIGN KEY (product_type_id)
REFERENCES products(product_type_id)
ON DELETE SET NULL;

-- Insert the values into the products table
INSERT INTO products VALUES (1, 'Apparel');
INSERT INTO products VALUES (2, 'Equipment');
INSERT INTO products VALUES (3, 'Footwear');

-- Update the product_type_id in the table factories
UPDATE factories
SET product_type_id = 1
WHERE product_type = 'Apparel';

UPDATE factories
SET product_type_id = 2
WHERE product_type = 'Equipment';

UPDATE factories
SET product_type_id = 3
WHERE product_type = 'Footwear';