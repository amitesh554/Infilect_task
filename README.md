# FastAPI Matrix Analysis

## Overview

This FastAPI application finds the largest rectangle formed by similar numbers in a given matrix. The rectangle is defined by selecting a group of adjacent cells that contain the same number, and the goal is to find the rectangle with the maximum area among all rectangles formed by similar numbers.

## Requirements

- Python 3.6 or later
- pip (Python package installer)

## Installation

1. **Clone the Repository:**

    ```bash
    git clone https://github.com/yourusername/Inflect.git
    ```

2. **Navigate to the Project Directory:**

    ```bash
    cd fastapi-matrix-analysis
    ```

3. **Create a Virtual Environment:**

    ```bash
    python -m venv venv
    ```

4. **Activate the Virtual Environment:**

    - On Linux/macOS:

        ```bash
        source venv/bin/activate
        ```

    - On Windows:

        ```bash
        .\venv\Scripts\activate
        ```

5. **Install Dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

## Running the FastAPI Service

1. **Run the FastAPI Application:**

    ```bash
    uvicorn main:app --reload
    ```

    This command starts the FastAPI application, and the `--reload` flag enables automatic reloading during development.

2. **Access the API Documentation:**

    Open your browser and go to [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs) to access the FastAPI Swagger documentation. You can use this interface to test the API endpoints and understand the available functionality.

3. **Make a POST Request to Get the Largest Rectangle:**

    Use a tool like `curl`, Postman, or Python's requests library to make a POST request to the `/largest_rectangle` endpoint with a matrix payload. Here's an example using `curl`:

    ```bash
    curl -X POST -H "Content-Type: application/json" -d '{"matrix": [[1, 2, 3], [4, 5, 6], [7, 8, 9]]}' http://127.0.0.1:8000/largest_rectangle
    ```

    Adjust the matrix data as needed. The response will contain the largest rectangle's area and the corresponding number.

## Additional Information

- For more details on FastAPI, refer to the [FastAPI Documentation](https://fastapi.tiangolo.com/).
- Explore and modify the `main.py` file to adapt the application to your specific requirements.
