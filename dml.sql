-- =====================================================
-- Lost and Found Smart System - Data Loading (DML)
-- Milestone 5: LOAD DATA + Validation Queries
-- =====================================================

USE lost_and_found;

-- =====================================================
-- LOAD DATA FROM CSV FILES
-- Note: Update file paths if running on a different machine
-- =====================================================

LOAD DATA LOCAL INFILE 'organization.csv'
INTO TABLE organization
FIELDS TERMINATED BY ',' ENCLOSED BY '"' LINES TERMINATED BY '\n'
IGNORE 1 ROWS;

LOAD DATA LOCAL INFILE 'category.csv'
INTO TABLE category
FIELDS TERMINATED BY ',' ENCLOSED BY '"' LINES TERMINATED BY '\n'
IGNORE 1 ROWS;

LOAD DATA LOCAL INFILE 'user.csv'
INTO TABLE user
FIELDS TERMINATED BY ',' ENCLOSED BY '"' LINES TERMINATED BY '\n'
IGNORE 1 ROWS;

LOAD DATA LOCAL INFILE 'lost_item.csv'
INTO TABLE lost_item
FIELDS TERMINATED BY ',' ENCLOSED BY '"' LINES TERMINATED BY '\n'
IGNORE 1 ROWS;

LOAD DATA LOCAL INFILE 'found_item.csv'
INTO TABLE found_item
FIELDS TERMINATED BY ',' ENCLOSED BY '"' LINES TERMINATED BY '\n'
IGNORE 1 ROWS;

LOAD DATA LOCAL INFILE 'match_record.csv'
INTO TABLE match_record
FIELDS TERMINATED BY ',' ENCLOSED BY '"' LINES TERMINATED BY '\n'
IGNORE 1 ROWS;

LOAD DATA LOCAL INFILE 'notification.csv'
INTO TABLE notification
FIELDS TERMINATED BY ',' ENCLOSED BY '"' LINES TERMINATED BY '\n'
IGNORE 1 ROWS;

LOAD DATA LOCAL INFILE 'message.csv'
INTO TABLE message
FIELDS TERMINATED BY ',' ENCLOSED BY '"' LINES TERMINATED BY '\n'
IGNORE 1 ROWS;

-- =====================================================
-- VALIDATION QUERIES
-- =====================================================

-- Row counts for each table
SELECT 'organization' AS table_name, COUNT(*) AS row_count FROM organization
UNION ALL SELECT 'category', COUNT(*) FROM category
UNION ALL SELECT 'user', COUNT(*) FROM user
UNION ALL SELECT 'lost_item', COUNT(*) FROM lost_item
UNION ALL SELECT 'found_item', COUNT(*) FROM found_item
UNION ALL SELECT 'match_record', COUNT(*) FROM match_record
UNION ALL SELECT 'notification', COUNT(*) FROM notification
UNION ALL SELECT 'message', COUNT(*) FROM message;

-- NULL checks on required columns
SELECT 'user with NULL email' AS issue, COUNT(*) AS count FROM user WHERE email IS NULL
UNION ALL SELECT 'lost_item with NULL title', COUNT(*) FROM lost_item WHERE title IS NULL
UNION ALL SELECT 'found_item with NULL title', COUNT(*) FROM found_item WHERE title IS NULL;

-- Foreign key integrity check (orphan check)
SELECT COUNT(*) AS orphan_lost_items
FROM lost_item l
LEFT JOIN user u ON l.user_id = u.user_id
WHERE u.user_id IS NULL;

-- JOIN test: show first 5 matches with full details
SELECT m.match_id, m.match_score, m.status,
       li.title AS lost_title, lu.full_name AS lost_reporter,
       fi.title AS found_title, fu.full_name AS found_reporter
FROM match_record m
JOIN lost_item li ON m.lost_item_id = li.lost_item_id
JOIN found_item fi ON m.found_item_id = fi.found_item_id
JOIN user lu ON li.user_id = lu.user_id
JOIN user fu ON fi.user_id = fu.user_id
LIMIT 5;

-- Sample UPDATE: mark all old pending matches as Closed
UPDATE match_record
SET status = 'Closed'
WHERE status = 'Pending' AND matched_at < DATE_SUB(NOW(), INTERVAL 30 DAY);

-- Sample DELETE: remove read notifications older than 60 days
DELETE FROM notification
WHERE is_read = TRUE AND created_at < DATE_SUB(NOW(), INTERVAL 60 DAY);