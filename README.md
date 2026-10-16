# 📦 InventoryManager

> **Stock it, track it, own it** — A Python-powered inventory management system for keeping your stock data accurate, organized, and always at your fingertips.

![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)
![SQLite](https://img.shields.io/badge/SQLite-003B57?style=for-the-badge&logo=sqlite&logoColor=white)
![License: MIT](https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Active-brightgreen?style=for-the-badge)

---

## 📖 Overview

**InventoryManager** is a lightweight, Python-based inventory management system designed for small to medium-scale stock tracking needs. It provides a clean interface to add, update, search, and delete inventory records, with persistent storage and low-stock alert capabilities. Built to be practical from day one — no bloated dependencies, no unnecessary complexity.

---

## ✨ Key Features

- ➕ **Add & update items** — Create new inventory records or modify existing ones with ease
- 🔍 **Search & filter** — Look up items by name, category, SKU, or stock threshold
- 🗑️ **Remove items** — Safely delete discontinued or out-of-stock entries
- 📉 **Low-stock alerts** — Automatic warnings when item quantities fall below configurable thresholds
- 📊 **Inventory reports** — Generate summaries of current stock levels, total value, and category breakdowns
- 💾 **Persistent storage** — All data saved to a local SQLite database (no external server needed)
- 🖥️ **CLI interface** — Fast, keyboard-driven interaction via a clean command-line menu

---

## 🛠️ Tech Stack

| Layer | Technology |
|---|---|
| Language | Python 3.10+ |
| Database | SQLite (via `sqlite3` stdlib) |
| ORM / Query Layer | Raw SQL / `sqlite3` |
| CLI Interface | argparse / custom menu loop |
| Reporting | tabulate / pandas |

---

## 🚀 Quick Start

### Prerequisites

- **Python** 3.10+
- **pip**

### Installation

```bash
# 1. Clone the repo
git clone https://github.com/devcode-X/INVENTORYMANAGEMET.git
cd INVENTORYMANAGEMET

# 2. (Optional) Create and activate a virtual environment
python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt
```

### Run the Application

```bash
python main.py
```

You'll be greeted by an interactive menu:

```
========== INVENTORY MANAGER ==========
  [1] View All Items
  [2] Add New Item
  [3] Update Item
  [4] Delete Item
  [5] Search Items
  [6] Generate Report
  [7] Exit
=======================================
Enter choice:
```

### CLI Usage (non-interactive)

```bash
# Add an item directly
python main.py --add --name "Laptop" --qty 50 --price 999.99 --category "Electronics"

# View all items below stock threshold
python main.py --low-stock --threshold 10

# Export inventory report
python main.py --report --output report.csv
```

---

## 📁 Folder Structure

```
INVENTORYMANAGEMET/
├── main.py                  # Application entry point & CLI menu
├── db/
│   ├── database.py          # SQLite connection & schema setup
│   └── inventory.db         # SQLite database file (git-ignored)
├── models/
│   └── item.py              # Item data model / CRUD operations
├── utils/
│   ├── alerts.py            # Low-stock alert logic
│   └── reports.py           # Report generation utilities
├── requirements.txt
└── README.md
```

---

## 🗄️ Database Schema

```sql
CREATE TABLE items (
    id          INTEGER PRIMARY KEY AUTOINCREMENT,
    name        TEXT NOT NULL,
    sku         TEXT UNIQUE,
    category    TEXT,
    quantity    INTEGER DEFAULT 0,
    price       REAL DEFAULT 0.0,
    threshold   INTEGER DEFAULT 5,
    updated_at  TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

---

## 👤 Author

**Devansh Awasthi** · [@devcode-X](https://github.com/devcode-X)
