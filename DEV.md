# Installation

## Prereqs

To install the project and run it in a local environment, follow these steps:
```
git clone https://github.com/Nakul727/PhysioAI.git
cd PhysioAI
```

You need to have `pyenv` installed which is a python version manager. This project requires the use of python 3.9.7, so we are going to use pyenv to configure that version in the local env. Make sure to install `pyenv` correctly. The .python_verison file in the cloned repo should set the version after installation of pyenv and version 3.9.7:
```
pyenv install 3.9.7
pyenv local 3.9.7
```

## Creating a virtual environment

Virtual environments are great for managing dependencies of a Python project. We can install specific versions of the dependencies, independent of the global packages. Make sure you have the `venv` package installed, which usually comes with the default Python installation.
To create a venv for this project:
```
python -m venv /venv
source /venv/bin/activate
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
6. Create a `.env` file in the `src` directory using .env.example as reference

## Running the project locally

After making a venv and installing correct python version, to install dependencies run the following:
```
pip install -r requirements.txt
```
To run the project, from root directory:
```
python src/app.py
```
