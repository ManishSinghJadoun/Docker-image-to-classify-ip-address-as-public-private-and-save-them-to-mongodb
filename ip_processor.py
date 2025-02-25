import re
import pymongo
from pymongo import MongoClient

# MongoDB Connection
MONGO_URI = "mongodb://mongo:27017/"
DB_NAME = "IPDatabase"
COLLECTION_PUBLIC = "PublicIPs"
COLLECTION_PRIVATE = "PrivateIPs"

# Function to check if an IP is private
def is_private_ip(ip):
    private_ranges = [
        re.compile(r"^10\."),  # 10.0.0.0 – 10.255.255.255
        re.compile(r"^172\.(1[6-9]|2[0-9]|3[0-1])\."),  # 172.16.0.0 – 172.31.255.255
        re.compile(r"^192\.168\."),  # 192.168.0.0 – 192.168.255.255
        re.compile(r"^127\."),  # Loopback (127.0.0.1)
        re.compile(r"^169\.254\.")  # Link-local (169.254.x.x)
    ]
    return any(pattern.match(ip) for pattern in private_ranges)

# Function to store IPs in MongoDB (No Duplicates)
def store_ip_in_mongo(ip, is_private):
    client = MongoClient(MONGO_URI)
    db = client[DB_NAME]
    collection = db[COLLECTION_PRIVATE] if is_private else db[COLLECTION_PUBLIC]

    # Insert IP only if it does not exist
    if not collection.find_one({"ip": ip}):
        collection.insert_one({"ip": ip})
        print(f"✔ Inserted: {ip}")

# Function to process the log file
def process_log_file(file_path):
    ip_pattern = re.compile(r"\b(?:\d{1,3}\.){3}\d{1,3}\b")

    with open(file_path, "r") as file:
        for line in file:
            ips = ip_pattern.findall(line)
            for ip in ips:
                store_ip_in_mongo(ip, is_private_ip(ip))

# Example Usage
log_file_path = "/app/logs/test.log"  # Path inside Docker
process_log_file(log_file_path)
