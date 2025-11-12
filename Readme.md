🔐 Token Management API








A simplified OAuth-like API built with Flask and JWT for studying and experimenting with token-based authentication systems.
Users can register, log in, and generate up to 3 personal tokens for their own applications.
The API also provides an endpoint to inspect token claims and validate them securely.

🧭 Overview

This project simulates a lightweight authorization service — similar to OAuth0, but focused on learning and experimentation with JWT authentication and token lifecycle management.

Core Features

🧑‍💻 User registration and login

🔑 Token generation using JWT

🧩 Retrieve and inspect token claims

⛔ Token validation with claim verification

🚫 Token limit: each user can create up to 3 tokens for their app

⚙️ Tech Stack

Python 3.10+

Flask

Flask-JWT-Extended

SQLAlchemy

Werkzeug (for password hashing)

Email Validator

SQLite (default)

📁 Project Structure
project/
│
├── app.py
├── extensions/
│   └── database.py
├── models/
│   ├── clientModel.py
│   └── token_model.py
├── service/
│   ├── cliente_service.py
│   └── token_service.py
├── exceptions/
│   └── my_exceptions.py
└── routes/
    └── cliente_controller.py

🚀 Getting Started
1️⃣ Clone the Repository
git clone https://github.com/<your-username>/token-manager-api.git
cd token-manager-api

2️⃣ Create a Virtual Environment
python -m venv venv
source venv/bin/activate  # for Linux/Mac
venv\Scripts\activate     # for Windows

3️⃣ Install Dependencies
pip install -r requirements.txt

4️⃣ Run the Application
flask run


By default, the API will be available at:
👉 http://127.0.0.1:5000

🔐 Authentication Flow
1. User Registration
POST /clientes/cadastro
Content-Type: application/json

{
  "nome": "John Doe",
  "email": "john@example.com",
  "senha": "123456"
}


✅ Response:

{"Message": "Cliente cadastrado com sucesso"}

2. Login and Retrieve Token
POST /clientes/login
Content-Type: application/json

{
  "email": "john@example.com",
  "senha": "123456"
}


✅ Response:

{
  "token": "<JWT_USER_TOKEN>"
}

3. Generate Application Token

Requires a valid user JWT (from login).

POST /clientes/create/token
Authorization: Bearer <JWT_USER_TOKEN>
Content-Type: application/json

{
  "app_name": "myApp",
  "permissions": ["read", "write"]
}


✅ Response:

{
  "token": "<JWT_APP_TOKEN>"
}


⚠️ Each user can generate up to 3 tokens.
If exceeded, the system will raise a QuantidadeExcedidaException.

4. Retrieve Token Claims
POST /clientes/claims
Content-Type: application/json

{
  "token": "<JWT_APP_TOKEN>"
}


✅ Response Example:

{
  "id": 1,
  "owner": "gerenciaToken",
  "target": "cliente",
  "permissions": ["read", "write"],
  "exp": 1731234567
}

🧠 Business Rules

A “user token” (login token) cannot be used to access /claims.
It contains a "bloqueado": true claim and is invalid for that purpose.

Each “application token” contains:

"owner": "gerenciaToken"

"target": "cliente"

Tokens expire after 7 days.

Attempting to decode a blocked or malformed token raises a custom TokenInvalidoException.

🧱 Custom Exceptions
Exception	Description
UserNotFoundException	Raised when a user is not found in the database.
LoginInvalidoException	Raised for invalid login credentials.
TokenInvalidoException	Raised when a token contains invalid or blocked claims.
QuantidadeExcedidaException	Raised when the user attempts to generate more than 3 tokens.
🧩 Example JWT Claim Structure
{
  "id": 1,
  "owner": "gerenciaToken",
  "target": "cliente",
  "permissions": ["read", "write"],
  "iat": 1731230000,
  "exp": 1731834800
}

🧰 Development Notes

Built entirely for educational purposes — not intended for production use.

Ideal for studying:

JWT authentication flow

Token validation and claim management

Python + Flask best practices

🧑‍💻 Author

Gui — Software Developer
📍 Focused on backend development with Python and Java
🌐 LinkedIn
 | GitHub

🪪 License

This project is licensed under the MIT License – feel free to use, modify, and share for learning purposes.

💬 "A simple project, but a powerful step in understanding authentication systems."