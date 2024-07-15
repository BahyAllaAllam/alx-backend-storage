#!/usr/bin/env python3
"""
Inserts a new document in a MongoDB collection based on kwargs.
"""


def insert_school(mongo_collection, **kwargs):
    """
    Inserts a new document in a MongoDB collection based on kwargs.
    """
    if mongo_collection is None:
        return None

    result = mongo_collection.insert_one(kwargs)
    return result.inserted_id
