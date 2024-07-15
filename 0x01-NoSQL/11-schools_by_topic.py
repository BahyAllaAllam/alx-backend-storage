#!/usr/bin/env python3
"""
Returns the list of schools having a specific topic.
"""


def schools_by_topic(mongo_collection, topic):
    """
    Returns the list of schools having a specific topic.
    """
    if mongo_collection is None:
        return []
    return list(mongo_collection.find({"topics": topic}))
