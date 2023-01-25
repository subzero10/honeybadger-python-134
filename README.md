# Minimal example python app with Honeybadger integration

This is a FastApi python app with Honeybadger integration.

## Usage

1. Open `main.py` and set your replace "YOUR_API_KEY" with your Honeybadger API key.
2. run `poetry install`
3. run `poetry shell`
4. run `uvicorn main:app`
5. using a web browser, navigate to http://127.0.0.1:8080
6. you should see the message "Internal Server Error"
7. the exception should be reported to Honeybadger, with the environment "production"
