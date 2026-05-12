# BOB's Trainer 
---

# 1. Create a virtual environment

Create the virtual environment inside the main folder

```bash
 python -m venv venv
```
#
Run the venv while in the main folder

```bash
venv\Scripts\activate
```
#

# 2. Install the requirments
While the virtual environment is running run the following command

```bash
pip install -r requirements.txt
```
## 3. Initialize the Database

After setting up your models, you must apply migrations to create the tables in PostgreSQL/pgAdmin. Run the following commands in your terminal:

### Step 1. Initialize your database
Create `.env` file and add your database credentials to it.
⚠️ Don't forget to hide them during deployment using gitignore.

```bash
DB_NAME = "db_name"
DB_USER = "db_user"
DB_PASSWORD = "your_db_password"
SECRET_KEY = "secret_key"
```

### Step 2. Create the Migrations
This command scans your `models.py` for changes and creates the instructions for the database.
```bash
python manage.py makemigrations
```
```bash
python manage.py migrate
```

### How to run this program

1. Go to your main folder
2. Enable the virtual-environment  
3. Go to your my_trainer folder and then run the following command.
```bash
python manage.py runserver
```
