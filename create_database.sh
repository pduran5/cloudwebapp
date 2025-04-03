#!/bin/bash

#Start by downloading the MySQL CLI:
sudo dnf install mariadb105 -y

#Initiate your DB connection with your Aurora RDS writer endpoint.

# Define variables
rds_endpoint="CHANGE-TO-YOUR-RDS-ENDPOINT"
user_name="CHANGE-TO-USER-NAME"

# Prompt for password
read -s -p "Enter password: " password
echo

# Construct the mysql command using variables
mysql_cmd="mysql -h $rds_endpoint -u $user_name -p$password"

# Execute the mysql command
eval $mysql_cmd 


#Create a database called test_db with the following command using the MySQL CLI:
CREATE DATABASE test_db;
USE test_db;

CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255),
    email VARCHAR(255)
);
EOF
