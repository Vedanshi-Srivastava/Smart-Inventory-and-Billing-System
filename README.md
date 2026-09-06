# 🛒 Smart Inventory and Billing System

A complete **Inventory and Billing Management System** built using **Python, Streamlit, and PostgreSQL**.

The application helps businesses manage customers, products, inventory, sales, billing, stock levels, and customer purchase history through an interactive web interface.

🔗 **Live Application:**  
https://vedanshi-srivastava-smart-inventory-and-billing-syst-app-yedbru.streamlit.app/

---

## 📌 Project Overview

The Smart Inventory and Billing System is a database-driven web application designed to simplify inventory and sales management.

It provides a centralized platform where users can:

- Manage customer records
- Manage products and inventory
- Track available stock
- Create and manage sales
- Automatically update inventory after sales
- Monitor low-stock products
- Identify out-of-stock products
- View sales analytics
- View customer purchase history
- Maintain relationships between customers, sales, and products

The application uses **PostgreSQL** as the relational database and **Neon PostgreSQL** as the cloud database for the deployed application.

---

## 🚀 Live Demo

👉 **Try the application here:**

https://vedanshi-srivastava-smart-inventory-and-billing-syst-app-yedbru.streamlit.app/

---

## ✨ Features

### 👥 Customer Management

- Add new customers
- Store customer names and contact information
- View existing customers
- Maintain unique customer records
- Connect customers with their sales history

---

### 📦 Product & Inventory Management

- Add new products
- Store product descriptions
- Maintain product prices
- Track available quantities
- Update product information
- Monitor inventory levels

---

### 🧾 Sales & Billing

- Create new sales
- Select customers
- Select products
- Specify product quantities
- Automatically calculate sale amounts
- Store individual sale items
- Calculate total sale amount
- Maintain complete sales records

---

### ⚠️ Inventory Alerts

The system automatically monitors inventory after a sale.

#### Out of Stock

When the product quantity reaches `0`, the application displays:

> 🔴 OUT OF STOCK

#### Low Stock

When the remaining quantity falls below the defined threshold, the application displays a low-stock warning.

This helps prevent inventory shortages.

---

### 📊 Sales Analytics

The application provides analytical views such as:

- Sales Summary
- Sales by Date Range
- Top Selling Products
- Low Stock Alerts
- Customer Purchase History

These reports help understand sales performance and inventory movement.

---

### 👤 Customer Purchase History

Users can view:

- Customer name
- Purchase date
- Products purchased
- Quantity purchased
- Product price
- Total sale amount

This creates a useful history of customer transactions.

---

## 🛠️ Tech Stack

| Technology | Purpose |
|------------|---------|
| Python | Application development |
| Streamlit | Web application interface |
| PostgreSQL | Relational database |
| Neon PostgreSQL | Cloud database |
| Psycopg2 | PostgreSQL connectivity |
| SQL | Database operations |
| Git | Version control |
| GitHub | Source code management |
| Streamlit Community Cloud | Application deployment |

---

