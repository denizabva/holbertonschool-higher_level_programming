-- Create user if it does not exist
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost';

-- Set password
SET PASSWORD FOR 'user_0d_1'@'localhost' = 'user_0d_1_pwd';

-- Give all privileges
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost';
