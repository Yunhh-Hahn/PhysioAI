# Installation

## Prereqs

You need to have Python3 installed along with the latest version of pip.
To install the project and run it in a local environment, follow these steps:
```
git clone https://github.com/Nakul727/PhysioAI.git
cd PhysioAI
```

## Creating a virtual environment

Virtual environments are great for managing dependencies of a Python project. We can install specific versions of the dependencies, independent of the global packages. Make sure you have the `venv` package installed, which usually comes with the default Python installation.
To create a venv for this project:
```
python3 -m venv ./venv
source ./venv/bin/activate
```

If you want to exit the venv:
```
deactive
```

## Prepare Database

Before running the project, you need to set up a MySQL database. Follow these steps:

1. Install MySQL Server if you haven't already. You can download it from the official MySQL website.

2. Once MySQL is installed, open the MySQL command-line client or a GUI tool like MySQL Workbench.

3. Log in with a user that has sufficient privileges to create new users and grant privileges. Usually, this is the 'root' user.

4. Create a new database for the project:

```sql
CREATE DATABASE physioai;
```

5. Create a new user and grant it all privileges on the new database. Replace 'username' and 'password' with the username and password you want to use:

```sql
CREATE USER 'username'@'localhost' IDENTIFIED BY 'password';
GRANT ALL PRIVILEGES ON physioai.* TO 'username'@'localhost';
FLUSH PRIVILEGES;
```
6. Create a `.env` file in the `src` directory and add the following lines to it:

```env
OPENAI_API_KEY=sk-abcdefghijklmnopquwsyz123456789
DB_NAME=physioai
DB_USER=username
DB_PASSWORD=password
DB_HOST=localhost
```

## Running the project locally

After making a venv, to install dependencies run the following:
```
pip3 install -r requirements.txt
```

After installing dependencies:

1. Run registration.py to create an empty database first 
2. Open two cmd or two terminal
3. Run server.py first then run client.py

Remove server.close() if want to run infinitely and with multiple client as once
