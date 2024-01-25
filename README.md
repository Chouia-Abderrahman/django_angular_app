# Django angular News article app

A web application with Django and Django REST framework as the backend to fetch
news from the News API,

## Django API Backend

This project consists of a Django API backend that interacts with the News API to fetch and store news articles in a database.

### Getting Started

Follow these steps to set up and run the Django API backend:

1. Clone the repository:

    ```bash
    git clone https://github.com/your-username/your-project.git
    ```

2. Change to the project directory:

    ```bash
    cd your-project
    ```

3. Create a virtual environment:

    ```bash
    python -m venv venv
    ```

4. Activate the virtual environment:

    - On Windows:

        ```bash
        venv\Scripts\activate
        ```

    - On macOS and Linux:

        ```bash
        source venv/bin/activate
        ```

5. Install the required packages:

    ```bash
    pip install -r requirements.txt
    ```

6. Apply database migrations:

    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```

7. Run the development server:

    ```bash
    python manage.py runserver
    ```

### API Documentation

#### `GET /api/fetch_news`

Fetches the top headlines from the News API and stores them in the database.

#### `GET /api/get_news_by_category/{category}`

Fetches top headlines by category from the News API and stores them in the database.

#### `GET /api/get_news_by_country/{country}`

Fetches top headlines by country from the News API and stores them in the database.

#### `GET /api/get_news_by_source/{source}`

Retrieves news articles from the database based on the specified news source.

#### `GET /api/get_news_by_query/{query}`

Retrieves news articles from the database based on the specified query string in the article title.

#### `GET /api/get_news_by_description/{description}`

Retrieves news articles from the database based on the specified query string in the article description.

#### `GET /api/get_all_news_in_database`

Retrieves all news articles stored in the database.

Feel free to explore and modify the code to suit your needs. If you encounter any issues or have suggestions for improvement, please open an issue on GitHub.
