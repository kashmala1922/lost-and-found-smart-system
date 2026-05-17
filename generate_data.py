"""
Lost and Found Smart System - Sample Data Generator
This script generates 100 rows of realistic fake data for each table
and saves them as CSV files for importing into MySQL.
"""

import csv
import random
from datetime import datetime, timedelta
from faker import Faker

# Initialize Faker
fake = Faker()

# Set seed so we get the same data every time we run this (helps with testing)
random.seed(42)
Faker.seed(42)

# ============================================================
# Configuration
# ============================================================
NUM_USERS = 100
NUM_LOST_ITEMS = 100
NUM_FOUND_ITEMS = 100
NUM_MATCHES = 60
NUM_NOTIFICATIONS = 120
NUM_MESSAGES = 80

# Sample data for IMSciences context
LOCATIONS = [
    ("IMSciences Cafeteria", 33.99880, 71.46834),
    ("IMSciences Library 1st Floor", 33.99895, 71.46850),
    ("IMSciences Library 2nd Floor", 33.99900, 71.46852),
    ("IMSciences Main Gate", 33.99889, 71.46839),
    ("IMSciences Parking Area", 33.99890, 71.46840),
    ("IMSciences Block A", 33.99910, 71.46858),
    ("IMSciences Block B", 33.99915, 71.46861),
    ("IMSciences Block C", 33.99920, 71.46863),
    ("IMSciences Auditorium", 33.99875, 71.46830),
    ("IMSciences Sports Ground", 33.99935, 71.46870),
    ("IMSciences Mosque", 33.99885, 71.46845),
    ("IMSciences Lab 1", 33.99905, 71.46855),
    ("IMSciences Lab 2", 33.99907, 71.46856),
    ("IMSciences Admin Office", 33.99878, 71.46832),
    ("IMSciences Reception", 33.99880, 71.46836),
]

LOST_ITEM_TITLES = {
    1: ["iPhone 13 black", "Samsung Galaxy phone", "Lenovo laptop", "Apple AirPods",
        "USB drive 32GB", "Power bank", "Bluetooth headphones", "Smart watch",
        "Calculator (Casio fx-991)", "Tablet device"],
    2: ["Student ID card", "Driving license", "Passport", "Library card",
        "Admit slip", "Roll number slip", "Result card", "Birth certificate copy",
        "CNIC card", "Class registration form"],
    3: ["House keys", "Honda car keys", "Suzuki bike keys", "Office keys",
        "Locker keys", "Hostel room keys", "Bicycle lock keys", "Cabinet keys"],
    4: ["Black leather wallet", "Brown wallet", "Card holder", "Cash purse",
        "Slim wallet", "Travel wallet", "Coin pouch"],
    5: ["Blue backpack", "Black laptop bag", "Sports bag", "Tote bag",
        "Sling bag", "Travel suitcase", "Lunch bag", "Pencil case"],
    6: ["Black jacket", "Red scarf", "Wool cap", "Pair of gloves",
        "Hoodie sweatshirt", "Cardigan", "Sweater", "Shawl"],
    7: ["Water bottle", "Lunch box", "Umbrella", "Notebook",
        "Textbook (Calculus)", "Pen set", "Glasses case", "Wristband"]
}

PAKISTANI_FIRST_NAMES = [
    "Ahmed", "Ali", "Hassan", "Hussain", "Bilal", "Hamza", "Usman", "Umar", "Yousaf", "Zain",
    "Asad", "Faisal", "Imran", "Khalid", "Saad", "Tariq", "Waqar", "Adnan", "Junaid", "Fahad",
    "Sara", "Ayesha", "Fatima", "Maryam", "Zainab", "Hina", "Maira", "Sana", "Noor", "Iqra",
    "Rabia", "Saba", "Aisha", "Bushra", "Anum", "Mariam", "Kiran", "Tahira", "Nadia", "Zara",
    "Kashmala", "Zarmeen", "Hafsa", "Sumaira", "Naila", "Saima", "Sadia", "Mehwish", "Areeba", "Anaya"
]

PAKISTANI_LAST_NAMES = [
    "Khan", "Ali", "Ahmed", "Malik", "Sheikh", "Hussain", "Raza", "Tariq", "Rashid", "Akhtar",
    "Hassan", "Iqbal", "Aslam", "Mehmood", "Bashir", "Yousaf", "Anwar", "Saleem", "Nawaz", "Akram",
    "Shah", "Qureshi", "Abbasi", "Awan", "Butt", "Chaudhry", "Siddiqui", "Farooq", "Mughal", "Niazi"
]

# ============================================================
# Helper Functions
# ============================================================
def random_date_in_range(start_days_ago, end_days_ago):
    """Generate a random date between start and end days ago"""
    today = datetime(2026, 5, 16)
    start = today - timedelta(days=start_days_ago)
    end = today - timedelta(days=end_days_ago)
    random_date = fake.date_between(start_date=start, end_date=end)
    return random_date

def random_datetime_in_range(start_days_ago, end_days_ago):
    """Generate a random datetime between start and end days ago"""
    today = datetime(2026, 5, 16)
    start = today - timedelta(days=start_days_ago)
    end = today - timedelta(days=end_days_ago)
    return fake.date_time_between(start_date=start, end_date=end)

def generate_pakistani_name():
    first = random.choice(PAKISTANI_FIRST_NAMES)
    last = random.choice(PAKISTANI_LAST_NAMES)
    return f"{first} {last}"

def generate_phone():
    """Generate a Pakistani phone number"""
    return f"030{random.randint(0, 9)}{random.randint(1000000, 9999999)}"

def write_csv(filename, headers, rows):
    """Write data to a CSV file"""
    with open(filename, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(headers)
        writer.writerows(rows)
    print(f"  Created: {filename} ({len(rows)} rows)")

# ============================================================
# 1. organization.csv
# ============================================================
print("Generating data...")
print()

organization_data = [
    [1, "IMSciences", "Phase 7, Hayatabad, Peshawar", "info@imsciences.edu.pk", "2026-01-01 09:00:00"]
]
write_csv(
    "organization.csv",
    ["organization_id", "name", "address", "contact_email", "created_at"],
    organization_data
)

# ============================================================
# 2. category.csv
# ============================================================
categories = [
    [1, "Electronics"],
    [2, "Documents"],
    [3, "Keys"],
    [4, "Wallet"],
    [5, "Bag"],
    [6, "Clothing"],
    [7, "Other"]
]
write_csv(
    "category.csv",
    ["category_id", "category_name"],
    categories
)

# ============================================================
# 3. user.csv (1 admin + 99 regular users = 100 total)
# ============================================================
users = []
used_emails = set()

# First user is the admin
users.append([
    1, 1, "IMSciences L&F Admin", "admin@imsciences.edu.pk",
    "admin123", "03001234567", "admin",
    "2026-01-15 10:00:00"
])
used_emails.add("admin@imsciences.edu.pk")

# Generate 99 regular users
for user_id in range(2, NUM_USERS + 1):
    full_name = generate_pakistani_name()
    first_part = full_name.lower().replace(" ", ".")
    email = f"{first_part}{user_id}@imsciences.edu.pk"

    if email in used_emails:
        email = f"{first_part}.{user_id}@imsciences.edu.pk"
    used_emails.add(email)

    password = f"pass{user_id:04d}"
    phone = generate_phone()
    created = random_datetime_in_range(120, 1).isoformat(sep=' ')

    users.append([user_id, 1, full_name, email, password, phone, "user", created])

write_csv(
    "user.csv",
    ["user_id", "organization_id", "full_name", "email", "password_hash", "phone_number", "role", "created_at"],
    users
)

# ============================================================
# 4. lost_item.csv (100 rows)
# ============================================================
lost_items = []
sizes = ["Small", "Medium", "Large"]
statuses_lost = ["Pending", "Matched", "Returned", "Closed"]

for item_id in range(1, NUM_LOST_ITEMS + 1):
    user_id = random.randint(2, NUM_USERS)
    category_id = random.randint(1, 7)
    title = random.choice(LOST_ITEM_TITLES[category_id])
    description = f"{title}. {fake.sentence(nb_words=10)}"
    size = random.choice(sizes)
    date_lost = random_date_in_range(60, 1).isoformat()
    location = random.choice(LOCATIONS)
    location_name, lat, lng = location
    # Add slight variation to coordinates
    lat += random.uniform(-0.0002, 0.0002)
    lng += random.uniform(-0.0002, 0.0002)
    status = random.choices(statuses_lost, weights=[55, 25, 15, 5])[0]
    created = f"{date_lost} {random.randint(8, 22):02d}:{random.randint(0, 59):02d}:00"

    lost_items.append([
        item_id, user_id, 1, category_id, title, description,
        size, date_lost, round(lat, 7), round(lng, 7), location_name, status, created
    ])

write_csv(
    "lost_item.csv",
    ["lost_item_id", "user_id", "organization_id", "category_id", "title", "description",
     "size", "date_lost", "location_lat", "location_lng", "location_name", "status", "created_at"],
    lost_items
)

# ============================================================
# 5. found_item.csv (100 rows)
# ============================================================
found_items = []

for item_id in range(1, NUM_FOUND_ITEMS + 1):
    user_id = random.randint(2, NUM_USERS)
    category_id = random.randint(1, 7)
    title = random.choice(LOST_ITEM_TITLES[category_id])
    description = f"Found - {title}. {fake.sentence(nb_words=10)}"
    size = random.choice(sizes)
    date_found = random_date_in_range(60, 1).isoformat()
    location = random.choice(LOCATIONS)
    location_name, lat, lng = location
    lat += random.uniform(-0.0002, 0.0002)
    lng += random.uniform(-0.0002, 0.0002)
    status = random.choices(statuses_lost, weights=[55, 25, 15, 5])[0]
    created = f"{date_found} {random.randint(8, 22):02d}:{random.randint(0, 59):02d}:00"

    found_items.append([
        item_id, user_id, 1, category_id, title, description,
        size, date_found, round(lat, 7), round(lng, 7), location_name, status, created
    ])

write_csv(
    "found_item.csv",
    ["found_item_id", "user_id", "organization_id", "category_id", "title", "description",
     "size", "date_found", "location_lat", "location_lng", "location_name", "status", "created_at"],
    found_items
)

# ============================================================
# 6. match_record.csv (60 rows)
# ============================================================
matches = []
match_statuses = ["Pending", "Confirmed", "Rejected", "Returned"]
used_match_pairs = set()

for match_id in range(1, NUM_MATCHES + 1):
    # Try to find a unique pair
    attempts = 0
    while attempts < 100:
        lost_id = random.randint(1, NUM_LOST_ITEMS)
        found_id = random.randint(1, NUM_FOUND_ITEMS)
        pair = (lost_id, found_id)
        if pair not in used_match_pairs:
            used_match_pairs.add(pair)
            break
        attempts += 1

    match_score = round(random.uniform(50.0, 100.0), 2)
    status = random.choices(match_statuses, weights=[40, 35, 15, 10])[0]
    # Admin (user_id 1) reviewed the match — only if not Pending
    reviewed_by = 1 if status != "Pending" else ""
    matched_at = random_datetime_in_range(45, 1).isoformat(sep=' ')

    matches.append([match_id, lost_id, found_id, match_score, status, reviewed_by, matched_at])

write_csv(
    "match_record.csv",
    ["match_id", "lost_item_id", "found_item_id", "match_score", "status", "reviewed_by", "matched_at"],
    matches
)

# ============================================================
# 7. notification.csv (120 rows)
# ============================================================
notification_messages = [
    "A possible match has been found for your reported item. Please check.",
    "The admin has reviewed your match. Please log in to see the result.",
    "A new match has been generated for your report.",
    "Your item report has been successfully registered.",
    "Status update: your match has been confirmed by the admin.",
    "Status update: your match has been rejected.",
    "Reminder: please update the status of your reported item.",
    "Congratulations! Your item has been returned. Thank you for using the system.",
    "Your match is awaiting admin review.",
    "A user has sent you a message about your match."
]

notifications = []
for notif_id in range(1, NUM_NOTIFICATIONS + 1):
    user_id = random.randint(2, NUM_USERS)
    match_id = random.randint(1, NUM_MATCHES) if random.random() > 0.2 else ""
    message = random.choice(notification_messages)
    is_read = random.choice([0, 1])
    created = random_datetime_in_range(40, 1).isoformat(sep=' ')

    notifications.append([notif_id, user_id, match_id, message, is_read, created])

write_csv(
    "notification.csv",
    ["notification_id", "user_id", "match_id", "message", "is_read", "created_at"],
    notifications
)

# ============================================================
# 8. message.csv (80 rows)
# ============================================================
message_texts = [
    "Assalam-o-Alaikum, I think this is my item. Can you describe it?",
    "Walaikum Assalam. Yes, please tell me what's inside or any distinguishing features.",
    "It has my name on it and some personal items.",
    "Confirmed, this is your item. When can we meet?",
    "Can we meet at the cafeteria tomorrow at 12 pm?",
    "Sure, see you there. JazakAllah.",
    "Sorry for the late reply. I am available after 2 pm today.",
    "I will be at the main gate. Please bring your student ID for verification.",
    "Thank you so much for finding it!",
    "No problem, glad I could help. Take care.",
    "Where exactly did you find it?",
    "I found it near the library on the second floor.",
    "I have a class right now, can we meet at 3 pm?",
    "That works for me. See you at the admin office.",
    "Please make sure to come on time."
]

# Only generate messages for confirmed or returned matches
confirmed_matches = [m for m in matches if m[4] in ("Confirmed", "Returned")]

messages = []
message_id = 1

while message_id <= NUM_MESSAGES and confirmed_matches:
    match = random.choice(confirmed_matches)
    match_id_for_msg = match[0]
    lost_item_id = match[1]
    found_item_id = match[2]

    # Find the users for this match
    lost_owner = lost_items[lost_item_id - 1][1]
    found_finder = found_items[found_item_id - 1][1]

    # Make sure both users are different
    if lost_owner == found_finder:
        continue

    # Generate 2-6 messages in this conversation
    num_msgs = random.randint(2, 6)
    base_time = random_datetime_in_range(30, 1)

    for i in range(num_msgs):
        if message_id > NUM_MESSAGES:
            break
        sender = lost_owner if i % 2 == 0 else found_finder
        receiver = found_finder if i % 2 == 0 else lost_owner
        content = random.choice(message_texts)
        sent_at = (base_time + timedelta(minutes=i * 15)).isoformat(sep=' ')

        messages.append([message_id, match_id_for_msg, sender, receiver, content, sent_at])
        message_id += 1

write_csv(
    "message.csv",
    ["message_id", "match_id", "sender_id", "receiver_id", "content", "sent_at"],
    messages
)

# ============================================================
# Done!
# ============================================================
print()
print("=" * 50)
print("ALL CSV FILES GENERATED SUCCESSFULLY!")
print("=" * 50)
print()
print("Files created in this folder:")
print("  1. organization.csv")
print("  2. category.csv")
print("  3. user.csv")
print("  4. lost_item.csv")
print("  5. found_item.csv")
print("  6. match_record.csv")
print("  7. notification.csv")
print("  8. message.csv")
print()
print("Total rows generated:")
print(f"  organization: 1")
print(f"  category: 7")
print(f"  user: {NUM_USERS}")
print(f"  lost_item: {NUM_LOST_ITEMS}")
print(f"  found_item: {NUM_FOUND_ITEMS}")
print(f"  match_record: {NUM_MATCHES}")
print(f"  notification: {NUM_NOTIFICATIONS}")
print(f"  message: {len(messages)}")