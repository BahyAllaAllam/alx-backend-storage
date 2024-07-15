#!/usr/bin/env python3
"""
Script to provide statistics about Nginx logs stored in MongoDB.
"""


from pymongo import MongoClient


def main():
    """
    Script to provide statistics about Nginx logs stored in MongoDB.
    """
    client = MongoClient('mongodb://127.0.0.1:27017')
    db = client.logs
    nginx_collection = db.nginx

    total_logs = nginx_collection.count_documents({})

    methods_count = nginx_collection.aggregate([
        {"$group": {"_id": "$method", "count": {"$sum": 1}}}
    ])

    status_check_count = nginx_collection.count_documents(
            {"method": "GET", "path": "/status"})

    top_ips = nginx_collection.aggregate([
        {"$group": {"_id": "$ip", "count": {"$sum": 1}}},
        {"$sort": {"count": -1}},
        {"$limit": 10}
    ])
    print(f"{total_logs} logs")
    print("Methods:")
    for method in methods_count:
        print(f"    method {method['_id']}: {method['count']}")

    print(f"{status_check_count} status check")

    print("IPs:")
    for ip in top_ips:
        print(f"    {ip['_id']}: {ip['count']}")


if __name__ == "__main__":
    main()
