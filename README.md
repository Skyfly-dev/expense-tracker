💰 Expense Tracker

A simple Python-based Expense Tracker that helps users manage daily expenses, track spending and view category-wise summaries.

The project includes both a Command-Line Interface (CLI) and a Streamlit web interface.

🌐 Live Demo

"Open Expense Tracker" (https://my-simple-expense-tracker.streamlit.app/)

«Demo Notice: This application is deployed for demonstration purposes. Data may reset when the application restarts, and visitors may share the same demo data. Please do not enter personal or sensitive financial information.»

✨ Features

- Add new expenses with amount, category, description and date.
- View all recorded expenses.
- Calculate total spending.
- Generate category-wise summaries.
- Edit existing expenses.
- Delete expenses.
- Store expense records using JSON.
- Validate user inputs and expense records.

🛠️ Technologies Used

- Python
- Streamlit
- JSON
- Git and GitHub

📁 Project Structure

Expense Tracker/
│
├── .streamlit/
│   └── config.toml
│
├── app.py
├── expense_tracker.py
├── requirements.txt
├── README.md
├── .gitignore
└── expenses.json

⚙️ Installation and Setup

1. Clone the repository

git clone YOUR_GITHUB_REPOSITORY_URL

2. Navigate to the project folder

cd expense-tracker

3. Install dependencies

pip install -r requirements.txt

4. Run the Streamlit application

python -m streamlit run app.py

The application will open in your browser.

5. Run the CLI version

python expense_tracker.py

💾 Data Storage

Expense records are stored locally in a JSON file named "expenses.json".

The JSON file is excluded from Git tracking to avoid uploading personal expense records.

📌 Project Purpose

This project was built to practise Python programming through a practical application, including functions, dictionaries, lists, file handling, JSON persistence, input validation and Streamlit.

It also helped me understand how to connect a Python application with a simple web interface and deploy it online.

👩‍💻 Author

Skyfly-dev

GitHub: "Skyfly-dev" (https://github.com/Skyfly-dev)
