# main.py
import builtins
import random
builtins.random = random  # for previous test compatibility

DELETED = object()  # special marker for deleted slots


def _hash(key: str) -> int:
    """Simple hash: sum of Unicode code points."""
    if not isinstance(key, str):
        key = str(key)
    return sum(ord(c) for c in key)


def make_table_open(n: int):
    """Create an open-addressed hash table of given size."""
    return [None] * n


def _find_slot(table, key, for_insert=False):
    """Find slot index for key. If for_insert=True, return where to insert."""
    n = len(table)
    h = _hash(key) % n
    first_deleted = None
    for i in range(n):
        idx = (h + i) % n
        entry = table[idx]

        if entry is None:
            # Empty slot — return for insert or lookup
            return first_deleted if (for_insert and first_deleted is not None) else idx

        if entry is DELETED:
            # Mark first deleted slot if not already seen
            if for_insert and first_deleted is None:
                first_deleted = idx
            continue

        k, v = entry
        if k == key:
            return idx
    # Full table, if inserting and we found a deleted, return it
    if for_insert and first_deleted is not None:
        return first_deleted
    return None


def put_open(table, key, value):
    """Insert or update key-value pair with linear probing."""
    slot = _find_slot(table, key, for_insert=True)
    if slot is None:
        # table full
        return False

    entry = table[slot]
    if entry is None or entry is DELETED:
        table[slot] = (key, value)
        return True

    # overwrite existing key
    k, _ = entry
    if k == key:
        table[slot] = (key, value)
        return True

    return False


def get_open(table, key):
    """Retrieve value by key or None if not found."""
    n = len(table)
    h = _hash(key) % n
    for i in range(n):
        idx = (h + i) % n
        entry = table[idx]

        if entry is None:
            return None
        if entry is DELETED:
            continue
        k, v = entry
        if k == key:
            return v
    return None


def delete_open(table, key):
    """Delete key from table if exists. Return True if deleted, else False."""
    n = len(table)
    h = _hash(key) % n
    for i in range(n):
        idx = (h + i) % n
        entry = table[idx]
        if entry is None:
            return False
        if entry is DELETED:
            continue
        k, _ = entry
        if k == key:
            table[idx] = DELETED
            return True
    return False
