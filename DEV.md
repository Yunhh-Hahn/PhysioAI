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
python3 -m venv venv
source venv/bin/activate
```

To exit the venv:
```
deactive
```

## Running the project locally

To install dependencies, run the following
```
pip3 install -r requirements.txt
```

After installing dependencies:

1. Run registration.py to create an empty database first 
2. Open two cmd or two terminal
3. Run server.py first then run client.py

Remove server.close() if want to run infinitely and with multiple client as once
