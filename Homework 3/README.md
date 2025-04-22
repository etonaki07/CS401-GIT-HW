# Homework 3

This project analyzes movie data from a imbd JSON file and provides descriptions such as:
- The movie with the largest net profit.
- The highest-rated movie.
- The actor who appeared in the most movies.

## Prerequisites

Before running the program, make you have the following installed:
- [Docker](https://www.docker.com/) (if running in a container)
- Python with a version of 3.9 or higher (if running locally)

## Files in the Project

- analyze_data.py: The main Python script that performs the analysis.
- test_analyze_data.py: The .py file that allows you to run pytest.
- data.json: The input JSON file containing movie data.
- Dockerfile: The Docker configuration file for building and running the program.
- requirements.txt: The Python dependencies required for the program.

## Running the Program Locally

1. **Install Dependencies**:
   Run the following command to install the required Python packages:
   ```bash
   pip install -r requirements.txt
