# Books Library Project

This is a simple Flask-based web application designed to manage a library of books. 
It allows users to manage books, authors, and checkout records. 
The app is powered by Flask and uses SQLAlchemy for ORM-based database management, including migrations with Flask-Migrate.

## Project Structure

### /app init.py 
Initializes Flask app and SQLAlchemy 
### models.py 
Contains the Book, Author, and CheckoutRecord models 
### books_library.py 
Shell context processor for accessing models /routes 
### config.py 
App configuration 

## Models

The app includes three primary models:

- **Book**: Represents a book with attributes like title, genre, and publish date.
- **Author**: Represents an author, with a unique constraint on the combination of name and surname.
- **CheckoutRecord**: Tracks book checkouts, including borrow and return dates, and whether the book is currently borrowed.

## Running the Application

#### Set up your environment and install the required dependencies.
pip install -r requirements.txt
#### Run the Flask development server:
flask run
#### You can also use Flask-Migrate to handle database migrations:
flask db init        # Initialize the migrations folder
flask db migrate     # Create a migration script
flask db upgrade     # Apply the migration to the database
