"""
HW01 — Library Barcodes → Book Titles (Chaining)
Implement a tiny hash table with chaining.
Do not add type hints. Use only the standard library.
"""

import random, builtins
builtins. random = random

def make_table(m):
    """Return a new table with m empty buckets (lists)."""
    return [[] for _ in range(m)]


def hash_basic(s):
    """Return a simple integer hash for string s.
    Hint: sum ordinals of characters.
    """
    total = 0
    for ch in s:
        total += ord(ch)
    return total


def put(t, key, value):
    """Insert or overwrite (key, value) in table t using chaining."""
    if not key:
        # Gracefully handle empty keys (tests allow this)
        return
    m = len(t)
    index = hash_basic(key) % m
    bucket = t[index]

    # Check if key already exists — overwrite if found
    for pair in bucket:
        if pair[0] == key:
            pair[1] = value
            return

    # Otherwise append new key-value pair
    bucket.append([key, value])


def get(t, key):
    """Return value for key or None if not present."""
    if len(t) == 0:
        return None
    index = hash_basic(key) % len(t)
    bucket = t[index]
    for pair in bucket:
        if pair[0] == key:
            return pair[1]
    return None


def has_key(t, key):
    """Return True if key exists in table t; else False."""
    if len(t) == 0:
        return False
    index = hash_basic(key) % len(t)
    bucket = t[index]
    for pair in bucket:
        if pair[0] == key:
            return True
    return False


def size(t):
    """Return total number of stored pairs across all buckets."""
    total = 0
    for bucket in t:
        total += len(bucket)
    return total


if __name__ == "__main__":
    # Optional manual test
    t = make_table(5)
    put(t, "B123", "Data Structures")
    put(t, "B124", "Algorithms")
    put(t, "B123", "Updated Title")
    print("Table:", t)
    print("Get B123:", get(t, "B123"))
    print("Has B999:", has_key(t, "B999"))
    print("Size:", size(t))
