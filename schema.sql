-- =====================================================
-- Lost and Found Smart System - Database Schema (DDL)
-- Milestone 4: CREATE TABLE statements with constraints
-- =====================================================

DROP DATABASE IF EXISTS lost_and_found;
CREATE DATABASE lost_and_found;
USE lost_and_found;

-- Table 1: organization
CREATE TABLE organization (
    organization_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(150) UNIQUE NOT NULL,
    address VARCHAR(255),
    contact_email VARCHAR(150),
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP
);

-- Table 2: category
CREATE TABLE category (
    category_id INT AUTO_INCREMENT PRIMARY KEY,
    category_name VARCHAR(100) UNIQUE NOT NULL
);

-- Table 3: user
CREATE TABLE user (
    user_id INT AUTO_INCREMENT PRIMARY KEY,
    organization_id INT NOT NULL,
    full_name VARCHAR(100) NOT NULL,
    email VARCHAR(150) UNIQUE NOT NULL,
    password_hash VARCHAR(255) NOT NULL,
    phone_number VARCHAR(20),
    role ENUM('user', 'admin') NOT NULL DEFAULT 'user',
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (organization_id) REFERENCES organization(organization_id)
);

-- Table 4: lost_item
CREATE TABLE lost_item (
    lost_item_id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL,
    organization_id INT NOT NULL,
    category_id INT NOT NULL,
    title VARCHAR(150) NOT NULL,
    description TEXT,
    size ENUM('Small', 'Medium', 'Large'),
    date_lost DATE NOT NULL,
    location_lat DECIMAL(10,7),
    location_lng DECIMAL(10,7),
    location_name VARCHAR(200),
    status ENUM('Pending', 'Matched', 'Returned', 'Closed') DEFAULT 'Pending',
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES user(user_id),
    FOREIGN KEY (organization_id) REFERENCES organization(organization_id),
    FOREIGN KEY (category_id) REFERENCES category(category_id)
);

-- Table 5: found_item
CREATE TABLE found_item (
    found_item_id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL,
    organization_id INT NOT NULL,
    category_id INT NOT NULL,
    title VARCHAR(150) NOT NULL,
    description TEXT,
    size ENUM('Small', 'Medium', 'Large'),
    date_found DATE NOT NULL,
    location_lat DECIMAL(10,7),
    location_lng DECIMAL(10,7),
    location_name VARCHAR(200),
    status ENUM('Pending', 'Matched', 'Returned', 'Closed') DEFAULT 'Pending',
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES user(user_id),
    FOREIGN KEY (organization_id) REFERENCES organization(organization_id),
    FOREIGN KEY (category_id) REFERENCES category(category_id)
);

-- Table 6: match_record
CREATE TABLE match_record (
    match_id INT AUTO_INCREMENT PRIMARY KEY,
    lost_item_id INT NOT NULL,
    found_item_id INT NOT NULL,
    match_score DECIMAL(5,2) NOT NULL CHECK (match_score >= 0 AND match_score <= 100),
    status ENUM('Pending', 'Confirmed', 'Rejected', 'Returned') DEFAULT 'Pending',
    reviewed_by INT,
    matched_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (lost_item_id) REFERENCES lost_item(lost_item_id),
    FOREIGN KEY (found_item_id) REFERENCES found_item(found_item_id),
    FOREIGN KEY (reviewed_by) REFERENCES user(user_id)
);

-- Table 7: notification
CREATE TABLE notification (
    notification_id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL,
    match_id INT,
    message TEXT NOT NULL,
    is_read BOOLEAN DEFAULT FALSE,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES user(user_id),
    FOREIGN KEY (match_id) REFERENCES match_record(match_id)
);

-- Table 8: message
CREATE TABLE message (
    message_id INT AUTO_INCREMENT PRIMARY KEY,
    match_id INT NOT NULL,
    sender_id INT NOT NULL,
    receiver_id INT NOT NULL,
    content TEXT NOT NULL,
    sent_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (match_id) REFERENCES match_record(match_id),
    FOREIGN KEY (sender_id) REFERENCES user(user_id),
    FOREIGN KEY (receiver_id) REFERENCES user(user_id)
);

-- Verify
SHOW TABLES;