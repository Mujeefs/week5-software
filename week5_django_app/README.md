
# Hello World Django App

## Description
This is a simple Django application that returns a JSON object with the message `{"Message": "Hello World!"}`.
Optionally, it can also display "Hello World!" in bold on an HTML page.

## Prerequisites
Python 3.9 or above
Django 4.x
Git

## Installation and Running the App
1. Clone the repository:
   git clone <your-repo-url>
   cd hello_world_app
2. Install dependencies:
   pip install django
3. Run the development server:
   python manage.py runserver
   
4. Access the responses in your browser:
      JSON Response: 
        Navigate to `http://127.0.0.1:8000/` to see the JSON response:
        json
        {"Message": "Hello World!"}
      HTML Response:
        Navigate to `http://127.0.0.1:8000/?format=html` to see the HTML page with "Hello World!" in bold.
