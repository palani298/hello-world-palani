#!/bin/bash

# Colors for output
GREEN='\033[0;32m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

echo -e "${BLUE}Setting up GitHub Webhook with ngrok...${NC}"

# Check if ngrok is installed
if ! command -v ngrok &> /dev/null; then
    echo -e "${GREEN}Installing ngrok...${NC}"
    if [[ "$OSTYPE" == "darwin"* ]]; then
        # macOS
        brew install ngrok
    else
        echo "Please install ngrok manually from https://ngrok.com/download"
        exit 1
    fi
fi

# Start ngrok in the background
echo -e "${GREEN}Starting ngrok tunnel...${NC}"
ngrok http 8000 > /dev/null &
NGROK_PID=$!

# Wait for ngrok to start
sleep 2

# Get the ngrok URL
NGROK_URL=$(curl -s http://localhost:4040/api/tunnels | jq -r '.tunnels[0].public_url')

echo -e "\n${BLUE}Your ngrok URL is:${NC}"
echo -e "${GREEN}$NGROK_URL${NC}"

echo -e "\n${BLUE}GitHub Webhook Setup Instructions:${NC}"
echo -e "1. Go to your GitHub repository"
echo -e "2. Click Settings → Webhooks → Add webhook"
echo -e "3. Configure the webhook:"
echo -e "   - Payload URL: ${GREEN}$NGROK_URL/roll${NC}"
echo -e "   - Content type: ${GREEN}application/json${NC}"
echo -e "   - Secret: ${GREEN}(leave empty for now)${NC}"
echo -e "   - Events: ${GREEN}Just the push event${NC}"
echo -e "4. Click 'Add webhook'"

echo -e "\n${BLUE}Testing the webhook:${NC}"
echo -e "1. Make a small change to your repository"
echo -e "2. Push the changes to GitHub"
echo -e "3. Check your terminal for the webhook response"
echo -e "4. The server should automatically pull and restart"

echo -e "\n${BLUE}To stop ngrok:${NC}"
echo -e "Run: ${GREEN}kill $NGROK_PID${NC}"

# Keep the script running
wait $NGROK_PID 