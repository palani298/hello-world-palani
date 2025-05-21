# Hello World Palani

A FastAPI-based REST API server with webhook support for automatic deployment.

## Features

- `/helloworld` endpoint with timezone support
- `/unravel` endpoint for JSON payload processing
- `/roll` endpoint for GitHub webhook integration
- Automatic deployment via GitHub webhooks

## API Endpoints

### Hello World
- `GET /helloworld` - Returns a greeting message
- `GET /helloworld?format=json` - Returns JSON response
- `GET /helloworld?timezone=UTC` - Returns greeting with specified timezone

### Unravel
- `POST /unravel` - Processes JSON payload
  ```json
  {
    "message": "Hello",
    "count": 3
  }
  ```

### Roll (Webhook)
- `POST /roll` - GitHub webhook endpoint for automatic deployment
  - Pulls latest code
  - Restarts the server

<!-- ### CRUD Operations
- `GET /items/` - List all items
- `POST /items/` - Create new item
- `GET /items/{item_id}` - Get specific item
- `PUT /items/{item_id}` - Update item
- `DELETE /items/{item_id}` - Delete item -->

## Setup

### Prerequisites
- Python 3.9+
- pip
- ngrok (for local webhook testing)
- jq (for webhook setup script)

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/palani298/hello_world_palani.git
   cd hello_world_palani
   ```

2. Create and activate virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Start the server:
   ```bash
   uvicorn app.main:app --host 0.0.0.0 --port 8000
   ```

### Webhook Setup

1. Install ngrok:
   ```bash
   brew install ngrok  # macOS
   # or download from https://ngrok.com/download
   ```

2. Start ngrok tunnel:
   ```bash
   ngrok http 8000
   ```

3. Generate GitHub Personal Access Token:
   - Go to GitHub → Settings → Developer settings → Personal access tokens
   - Generate new token (classic)
   - Select scopes: `repo` and `admin:repo_hook`
   - Copy the token

4. Add webhook using the setup script:
   ```bash
   chmod +x add_webhook.sh
   ./add_webhook.sh YOUR_GITHUB_TOKEN
   ```

### Testing Webhook

1. Make a small change to your repository
2. Push the changes to GitHub
3. The webhook will automatically:
   - Pull the latest code
   - Restart the server

## Deployment

### Local Development
- Run `uvicorn app.main:app --host 0.0.0.0 --port 8000`
- Access API at `http://localhost:8000`
- Use ngrok for webhook testing

### Production Deployment
1. Set up a server with SSH access
2. Configure GitHub Actions secrets:
   - `SSH_HOST`: Server IP/domain
   - `SSH_USER`: SSH username
   - `SSH_PRIVATE_KEY`: SSH private key
   - `REMOTE_PATH`: Server deployment path

3. Push to main branch to trigger deployment

## Testing

Run tests with pytest:
```bash
pytest
```

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request
