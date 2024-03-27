-- Creat new user user_0d_1.
-- user_0d_1 ought to be granted full access.
-- User_0d_1_pwd should be the password for user_0d_1.
-- If user_0d_1 is already created, then your script shouldn't fail.
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost';
