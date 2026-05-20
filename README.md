*** Expense Tracker

A Django web application to track and manage personal expenses with secure user authentication.

*** Features

- User registration and login — only authenticated users can access the tracker
- Add expenses with category, date, and amount
- Dashboard showing all your recorded expenses
- Filter expenses by category, month, or both combined

*** Tech Stack

- **Backend:** Python, Django
- **Frontend:** HTML, CSS, Bootstrap
- **Database:** SQLite
- **Auth:** Django built-in authentication

*** Getting Started

git clone https://github.com/mahendra960/expense-tracker.git
cd expense-tracker
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver

Visit http://127.0.0.1:8000

*** How It Works

1. Register an account or log in
2. Add an expense — pick a category, enter the date and amount
3. View your dashboard with all expenses
4. Use filters to analyze spending by category, month, or both

