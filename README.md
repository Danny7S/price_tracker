
# Price Tracker

Price Tracker is a web application developed with Django.
It allows users to manage products, categories and stores,
and compare product prices across different stores.

## Features

- Create, edit and delete product categories
- Add products with images, brands and descriptions
- Assign products to multiple categories
- Create and manage stores
- Add, edit and delete product prices
- Compare prices and identify the lowest available price
- Search products by name or brand
- Filter products by category
- Sort products by name or creation date
- Form validation
- Custom 404 error page
- Bootstrap 5 interface

## Technologies

- Python
- Django
- SQLite
- HTML and CSS
- Bootstrap 5
- Pillow

## Project Structure

The project consists of three Django applications:

- **catalog** - manages products and categories
- **stores** - manages stores and their information
- **prices** - manages product prices across stores

## How to Run

Install the required dependencies:

    pip install -r requirements.txt

Apply database migrations:

    python manage.py migrate

Start the development server:

    python manage.py runserver

The application will be available at:
http://127.0.0.1:8000/

## Author

Daniel Slavchev

Django Basics Project
