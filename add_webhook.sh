#!/bin/bash

# Colors for output
GREEN='\033[0;32m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Check if token is provided
if [ -z "$1" ]; then
    echo -e "${BLUE}Usage: ./add_webhook.sh <GITHUB_TOKEN>${NC}"
    echo -e "Please provide your GitHub Personal Access Token"
    exit 1
fi

GITHUB_TOKEN=$1
REPO_OWNER="palani298"
REPO_NAME="hello_world_palani"
 Get ngrok URL if available
 if command -v ngrok &> /dev/null; then
     NGROK_URL=$(curl -s http://localhost:4040/api/tunnels | jq -r '.tunnels[0].public_url')
     if [ "$NGROK_URL" != "null" ]; then
         WEBHOOK_URL="${NGROK_URL}/roll"
     else
         echo -e "${BLUE}Enter your webhook URL (e.g., https://your-server.com/roll):${NC}"
         read WEBHOOK_URL
     fi
 else
     echo -e "${BLUE}Enter your webhook URL (e.g., https://your-server.com/roll):${NC}"
     read WEBHOOK_URL
 fi

# Create webhook using GitHub API
echo -e "${BLUE}Adding webhook to repository...${NC}"

curl -L \
  -X POST \
  -H "Accept: application/vnd.github+json" \
  -H "Authorization: token ${GITHUB_TOKEN}" \
  -H "X-GitHub-Api-Version: 2022-11-28" \
  -H "Content-Type: application/json" \
  "https://github.com/repos/${REPO_OWNER}/${REPO_NAME}/hooks" \
  -d "{
    \"name\": \"web\",
    \"active\": true,
    \"events\": [\"push\"],
    \"config\": {
      \"url\": \"${WEBHOOK_URL}\",
      \"content_type\": \"json\",
      \"insecure_ssl\": \"0\"
    }
  }"

echo -e "\n${GREEN}Webhook added!${NC}"
echo -e "${BLUE}To test the webhook:${NC}"
echo -e "1. Make a small change to your repository"
echo -e "2. Push the changes to GitHub"
echo -e "3. Check your server logs for the webhook response" 