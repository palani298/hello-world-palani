
# Hello World Palani


## Setup

1. Clone the repository:
   ```sh
   git clone https://github.com/palani298/hello-world-palani.git
   cd hello-world-palani
   ```
2. (Optional) Create and activate a virtual environment:
   ```sh
   python3 -m venv venv
   source venv/bin/activate
   ```
3. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```

## Running the Server

To start the server locally:
```sh
make run
```
This will run the FastAPI server at http://127.0.0.1:8000

## Example Requests

### GET /helloworld

- Simple request (plain text):
  ```sh
  curl http://127.0.0.1:8000/helloworld
  ```
- Request with JSON response:
  ```sh
  curl -H "Accept: application/json" http://127.0.0.1:8000/helloworld
  ```
- Request with timezone:
  ```sh
  curl -H "Accept: application/json" "http://127.0.0.1:8000/helloworld?tz=America/New_York"
  ```

### POST /unravel

- Request with JSON body:
  ```sh
  curl -X POST -H "Content-Type: application/json" -d '{"key1": {"keyA": ["foo", 0, "bar"]}, "some other key": 2, "finally": "end"}' http://127.0.0.1:8000/unravel
  ```
  Expected response:
  ```json
  ["key1", "keyA", "foo", 0, "bar", "some other key", 2, "finally", "end"]
  ```

### GET /roll

- This route pulls the latest code from GitHub and restarts the server.
- Example request:
  ```sh
  curl http://127.0.0.1:8000/roll
  ```

#### Setting up a GitHub Webhook

1. Go to your GitHub repository settings.
2. Navigate to "Webhooks" and add a new webhook.
3. Set the Payload URL to your public endpoint (e.g., using ngrok: `https://your-ngrok-url/roll`).
4. Set the Content type to `application/json`.
5. Select the "Just the push event" trigger.
6. Ensure the webhook is active.

#### Using ngrok

To expose your local server to the internet:

1. Install ngrok: [ngrok download](https://ngrok.com/download)
2. Run ngrok:
   ```sh
   ngrok http 8000
   ```
3. Use the provided URL (e.g., `https://your-ngrok-url`) as your webhook Payload URL.