# User Management API with FastAPI

This project is a user management API implemented with FastAPI. It allows performing CRUD operations (Create, Read, Update, Delete) on users in a database. The API is designed to be fast, efficient, and easy to use, taking advantage of FastAPI's features like interactive documentation generation and data validation.

## Getting Started

Follow these instructions to get a copy of the project running on your local machine for development and testing purposes.

### Prerequisites

You will need to have Docker installed on your machine. If you don't have it, follow the instructions to install Docker for your operating system here: [Install Docker](https://docs.docker.com/get-docker/).

### Installation

To install and run the API on your local environment, follow these steps:

1. Clone the repository to your local machine:
git clone https://github.com/devecode/crud-fastAPI.git

2. Navigate to the project directory
3. Set the MongoDB Atlas path in your .env at MONGO_DETAILS: `mongodb+srv://<username>:<password>@cluster0.1cczvbi.mongodb.net/?retryWrites=true&w=majority&appName=<appName>`
4. Build and run the Docker container using `docker-compose`:
docker-compose up -d --build

This will build your application's Docker image (if it hasn't been built before) and then start the container.

4. Once the container is running, the API will be accessible at [http://localhost:8000](http://localhost:8000).

### Usage

To start using the API, you can navigate to [http://localhost:8000/docs](http://localhost:8000/docs) in your web browser to access the Swagger UI interactive documentation, where you can make requests directly from the interface.

### Development

If you want to contribute to the project or make modifications, here are the recommended steps for development:

1. Make sure you have all the dependencies installed using the Docker environment.
2. Make your changes in the source code.
3. To test your changes locally, use `docker-compose up` to rebuild and restart the containers.

## Built With

* [FastAPI](https://fastapi.tiangolo.com/) - The web framework used.
* [Docker](https://www.docker.com/) - Container manager.
* [MongoDB Atlas](https://cloud.mongodb.com//) - NoSql database manager.
