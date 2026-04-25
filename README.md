# Fuel Optimizer API 🚗⛽

## 📌 Project Overview
This project is a Django REST API that helps optimize routes and find the cheapest fuel stops between two locations.

---

## ⚙️ Tech Stack
- Python
- Django
- Django REST Framework
- Pandas

---

## 🚀 Features
- Accepts start and end locations
- Returns optimized route details
- Finds cheapest fuel stop (basic logic)
- REST API endpoint for integration

---

## 📡 API Endpoint

### POST /route/

#### Request Body:
```json
{
  "start": "New York",
  "end": "Los Angeles"
}
