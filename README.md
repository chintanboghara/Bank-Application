# Bank Application

## Description

The Bank Application is a simple graphical user interface (GUI) application developed in Python using the Tkinter library. It allows users to perform basic banking operations such as logging in, viewing personal information, depositing money, withdrawing money, and registering as a new user.

## Features

- User authentication: Users can log in using their username and password.
- Personal information: After logging in, users can view their personal information, including name, gender, age, and account balance.
- Deposit and Withdrawal: Users can deposit money into their account or withdraw money from it.
- Registration: New users can register by providing their personal information.
- Data Persistence: User data, including usernames, passwords, and account balances, is stored in a file ('app.dat') using the Pickle library.

## Prerequisites

- Python 3.x installed on your system.

## Getting Started

1. Clone or download the project repository to your local machine.

```bash
git clone https://github.com/your-username/bank-application.git
```

2. Navigate to the project directory.

```bash
cd bank-application
```

3. Run the application.

```bash
python bank_app.py
```

## Usage

- **Login**: Enter your username and password to log in.
- **Register**: New users can click the "Register" button to create an account.
- **Personal Information**: After logging in, click the "Personal Information" button to view your account details.
- **Deposit**: Click the "Deposit" button to deposit money into your account.
- **Withdraw**: Click the "Withdraw" button to withdraw money from your account.
- **Logout**: Click the "Logout" button to log out of your account.

## Known Issues

- The application does not include advanced security features, and it is intended for educational purposes. Do not use it in a production environment.
