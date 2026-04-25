# Fuel Optimizer API 🚗⛽

## 📌 Project Overview

This project is a Django REST API that helps optimize routes and find the cheapest fuel stops between two locations.

## ⚙️ Tech Stack

* Python
* Django
* Django REST Framework
* Pandas

## 🚀 Features

* Accepts start and end locations
* Returns optimized route details
* Finds cheapest fuel stop (basic logic)
* REST API endpoint for integration

## 📡 API Endpoint

POST /route/

Request:
{
"start": "New York",
"end": "Los Angeles"
}

Response:
{
"start": "New York",
"end": "Los Angeles",
"cheapest_fuel_stop": "Houston",
"price": 1.0,
"message": "Route optimized (basic logic)"
}

## ▶️ How to Run

pip install -r requirements.txt
python manage.py migrate
python manage.py runserver

## 🌐 Test API

* Thunder Client / Postman
* Browser (Django REST UI)

## 👨‍💻 Author

Shubham Panwar

---

EMAIL / SUBMISSION MESSAGE

Subject: Fuel Optimizer Backend Assignment Submission

Dear Sir/Ma’am,

I have completed the Fuel Optimizer Backend Assignment using Django REST Framework.

The project includes:

* A working API endpoint (/route/)
* Basic route optimization logic
* Integration with CSV data for fuel pricing
* Tested using Thunder Client and browser

GitHub Repository:
https://github.com/Shubhampanwar20/fuel-optimizer

Thank you for the opportunity.

Regards,
Shubham Panwar
