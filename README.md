# Simple User Authentication Website

A very basic Flask web application that provides user registration and login functionality.

## Features

- 🔐 User registration and login system
- 🎨 Clean and simple UI design
- 🔒 Session-based authentication
- 📱 Mobile-friendly design

## Usage

1. **Register a new account** or **login** with existing credentials
2. **View your profile** after successful login
3. **Logout** when you're done

## Environment variables

Create a `.env` file (do not commit it) with:

```
FLASK_SECRET_KEY=change-this-to-a-random-long-string
HUGGINGFACEHUB_API_TOKEN=your_hf_token_here
# Optional overrides for local/dev
FLASK_HOST=0.0.0.0
FLASK_PORT=5000
FLASK_DEBUG=True
```

An example is provided in `env.example`.

## Running locally

```
pip install -r requirements.txt
python app.py
```

## Deploying

- Use `gunicorn` in production. A `Procfile` is included for platforms like Heroku/Render:

```
web: gunicorn app:app
```

- Ensure you set `FLASK_SECRET_KEY` and `HUGGINGFACEHUB_API_TOKEN` in platform environment settings.

## Technologies Used

- **Backend:** Flask (Python)
- **Frontend:** HTML5, CSS3
- **Styling:** Simple, clean CSS
- **Data Storage:** JSON-based simple database

## What This Teaches

This project demonstrates:

- Basic Flask routing
- Form handling with POST requests
- Session management
- Simple database operations
- Basic HTML/CSS integration
- User authentication flow

## Perfect For

- Beginner Python developers
- Learning Flask basics
- Understanding web authentication
- Simple project portfolio

## How It Works

1. **Registration:** Users can create new accounts with name, email, and password
2. **Login:** Users can log in with their email and password
3. **Session:** Users stay logged in until they logout
4. **Profile:** Simple welcome page showing the logged-in user's name
5. **Database:** Simple JSON file storage for user data
