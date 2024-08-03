# BookHub

## Setup Instructions

1. Clone the repository:
    ```bash
    git clone <repository_url>
    cd bookhub
    ```

2. Create and activate a virtual environment:
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

3. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

4. Run migrations:
    ```bash
    python manage.py migrate
    ```

5. Create a superuser:
    ```bash
    python manage.py createsuperuser
    ```

6. Start the development server:
    ```bash
    python manage.py runserver
    ```

## API Endpoints

- `GET /api/recommendations/` - List all book recommendations
- `POST /api/recommendations/` - Create a new book recommendation
- `GET /api/recommendations/<id>/` - Retrieve a specific book recommendation
- `PUT /api/recommendations/<id>/` - Update a specific book recommendation
- `DELETE /api/recommendations/<id>/` - Delete a specific book recommendation
- `GET /api/search/<query>/` - Search for books using the Google Books API

## External Dependencies

- Django
- Django REST framework
- django-filter
- requests
