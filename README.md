[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/Q03QBD2o)
# HW02 — Airport Luggage Tags (Open Addressing with Delete)

**Story intro (new theme):**  
At the **airport baggage desk**, each bag has a **tag ID**. You must find a bag’s **status** fast. You store tag → status in a table with **open addressing** (linear probing). Sometimes bags get removed (delete).

**Today’s topic focus:** **Hash tables with open addressing** (linear probing) + **delete with tombstones**.

---

## Technical description
- **Goal:** Implement a fixed-size table with **linear probing**, using special markers `EMPTY` and `DELETED`.
- **Functions to write in `main.py`:**
  - `make_table_open(m)` → new table with `m` slots.
  - `put_open(t, key, value)` → insert or overwrite; return `True` on success, `False` if table full.
  - `get_open(t, key)` → return value or `None`.
  - `delete_open(t, key)` → remove key; return `True` if removed, else `False`.
- **Inputs/Outputs:** Keys and values are strings. Table length `m ≥ 3`.
- **Rules:** Linear probe order: `i, i+1, i+2, ...` wrap to start.  
  - `EMPTY` means “never used.”  
  - `DELETED` means “used before, now removed.” Inserts may reuse `DELETED`.
- **Expected complexity:** Average **O(1)** for `put/get/delete` at low load; **O(m)** worst-case near full.

---

## ESL scaffold — The 8 Steps
**Steps 1–5: explicit**
1. **Read & Understand:** Need fast tag → status with one array.  
2. **Re-phrase:** If slot busy, move to the **next** until we find **key** or an **EMPTY**.  
3. **Identify I/O/vars:** Input: `key`, `value`, `table`; Output: value/None, True/False. Vars: `index`, `start`, `marker`.  
4. **Break down:** Write a helper to **find slot** for insert/search. Handle wrap.  
5. **Pseudocode:**

```  
i = hash(key) % m; start = i
while True:
if slot is EMPTY or DELETED or key matches: return i
i = (i + 1) % m
if i == start: return None (full)

```
**Steps 6–8: hints**

6. **Write code:** Use two markers: `EMPTY`, `DELETED`.  
7. **Debug:** Fill table; test delete; then insert into a DELETED slot.  
8. **Optimize:** Fail early if probe returns `None`.

---

## Hints
- When searching for an existing key, **skip** over `DELETED` slots (keep probing).
- When inserting, remember the **first DELETED** slot seen; you may place the new pair there.
- Keep keys and values as tuples like `(key, value)`.

---

## How to run tests locally
```python -m pytest -q```



---

## FAQ
**Q1. Environment?** Python 3.10 or 3.11.  
**Q2. Read from stdin?** No. Implement the functions.  
**Q3. Big-O expectations?** Average O(1); degrades as table gets full.  
**Q4. Pitfalls?** Not wrapping around; stopping at DELETED when searching; not reusing DELETED when inserting.  
**Q5. Grading?** Pytest autograder.  
**Q6. Failures?** Read assertion diff; check probe logic.  
**Q7. Resize?** Not in this HW. If full, `put_open` returns `False`.