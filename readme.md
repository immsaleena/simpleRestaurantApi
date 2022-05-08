# Step 1: Install Dependencies
pip install -r requirements.txt

# Step 2: Migrate database
python db_migrate.py

# Step 3: To start app
python -m flask run

# Goto the url shown on terminal to use app
example: http://127.0.0.1:5000
