# Login Form Flask Application

This is a simple Flask web application that provides a login form and saves the submitted login data (email and password) to a MongoDB database.

## Features

- Displays a login form to the user.
- Accepts login data via POST request.
- Saves login data (email and password) to a MongoDB collection.
- Uses Flask for the web framework and PyMongo for MongoDB interaction.

## Prerequisites

- Python 3.x installed on your system.
- MongoDB database (MongoDB Atlas or local instance).
- Internet connection if using MongoDB Atlas.

## Installation

1. Clone the repository or download the project files.

2. Create and activate a virtual environment (optional but recommended):

```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

3. Install the required Python packages:

```bash
pip install -r requirements.txt
```

4. Configure the MongoDB connection URI:

- Open the `config.py` file.
- Replace the `MONGO_URI` value with your MongoDB connection string.

## Running the Application

Run the Flask application using:

```bash
python app.py
```

The application will start in debug mode and be accessible at `http://127.0.0.1:5000/`.

## Usage

- Open your web browser and navigate to `http://127.0.0.1:5000/`.
- You will see a login form.
- Enter your email and password and submit the form.
- The login data will be saved to the MongoDB database.

## Project Structure

- `app.py`: Main Flask application file.
- `config.py`: Configuration file containing MongoDB URI.
- `requirements.txt`: Python dependencies.
- `templates/login.html`: HTML template for the login form.

## Dependencies

- Flask
- PyMongo
- dnspython

## Notes

- This project saves passwords in plain text for demonstration purposes only. For production use, always hash passwords before storing them.
- Ensure your MongoDB URI is kept secure and not exposed publicly.

## Demo 

https://drive.google.com/file/d/1XKq5fbM3HfO-XSpAJlyaGuUfV95anhCT/view?usp=drivesdk
