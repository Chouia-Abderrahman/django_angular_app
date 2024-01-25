# Django angular News article app

A web application with Django and Django REST framework as the backend to fetch
news from the News API,

## Django API Backend

This project consists of a Django API backend that interacts with the News API to fetch and store news articles in a database.

### Getting Started

Follow these steps to set up and run the Django API backend:

1. Clone the repository:

2. Change to the project directory:

    ```bash
    cd django_angular_app
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
## Running django backend using Docker
or you can use docker to run the django backend:
Certainly! Here's the updated response:

1. **Build the Docker image:**

   ```bash
   docker build -t django_backend:latest .
   ```

   - `-t`: Specifies the name and optionally a tag to the Docker image.
   - `django_backend`: This is the desired name for your Docker image.
   - `latest`: This is the tag for versioning, indicating it's the latest version.

   The dot (`.`) at the end indicates the build context is the current directory.

2. **Run the Docker container:**

   ```bash
   docker run -p 8000:8000 django_backend:latest
   ```

   - `-p 8000:8000`: Maps port 8000 on your local machine to port 8000 in the Docker container. Adjust the ports as needed.

   After running this command, your Docker container should be up and running.

Remember to adjust the ports and tags according to your application's configuration and versioning needs.

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
