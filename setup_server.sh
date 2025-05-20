#!/bin/bash

# Colors for output
GREEN='\033[0;32m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

echo -e "${BLUE}Setting up SSH keys and server configuration...${NC}"

# Generate SSH key if it doesn't exist
if [ ! -f ~/.ssh/id_ed25519 ]; then
    echo -e "${GREEN}Generating new SSH key...${NC}"
    ssh-keygen -t ed25519 -C "github-actions-deploy"
    echo -e "${GREEN}SSH key generated!${NC}"
else
    echo -e "${GREEN}SSH key already exists.${NC}"
fi

# Display the public key
echo -e "\n${BLUE}Your public key (add this to server's authorized_keys):${NC}"
echo -e "${GREEN}$(cat ~/.ssh/id_ed25519.pub)${NC}"

# Display the private key
echo -e "\n${BLUE}Your private key (add this to GitHub Secrets as SSH_PRIVATE_KEY):${NC}"
echo -e "${GREEN}$(cat ~/.ssh/id_ed25519)${NC}"

# Instructions for server setup
echo -e "\n${BLUE}Server Setup Instructions:${NC}"
echo -e "1. SSH into your server:"
echo -e "   ${GREEN}ssh your_username@your_server_ip${NC}"
echo -e "\n2. Create application directory:"
echo -e "   ${GREEN}sudo mkdir -p /var/www/hello-world-palani${NC}"
echo -e "   ${GREEN}sudo chown -R \$USER:\$USER /var/www/hello-world-palani${NC}"
echo -e "\n3. Set up SSH access:"
echo -e "   ${GREEN}mkdir -p ~/.ssh${NC}"
echo -e "   ${GREEN}echo \"$(cat ~/.ssh/id_ed25519.pub)\" >> ~/.ssh/authorized_keys${NC}"
echo -e "   ${GREEN}chmod 600 ~/.ssh/authorized_keys${NC}"
echo -e "\n4. Set up Python environment:"
echo -e "   ${GREEN}cd /var/www/hello-world-palani${NC}"
echo -e "   ${GREEN}python3 -m venv venv${NC}"
echo -e "   ${GREEN}source venv/bin/activate${NC}"
echo -e "   ${GREEN}pip install -r requirements.txt${NC}"

# Instructions for GitHub Secrets
echo -e "\n${BLUE}GitHub Secrets Setup:${NC}"
echo -e "1. Go to your GitHub repository"
echo -e "2. Click Settings → Secrets and variables → Actions"
echo -e "3. Add these secrets:"
echo -e "   ${GREEN}SSH_HOST: your_server_ip${NC}"
echo -e "   ${GREEN}SSH_USER: your_username${NC}"
echo -e "   ${GREEN}SSH_PRIVATE_KEY: (paste the private key shown above)${NC}"
echo -e "   ${GREEN}REMOTE_PATH: /var/www/hello-world-palani${NC}"

# Test connection instructions
echo -e "\n${BLUE}To test the connection:${NC}"
echo -e "1. Replace placeholders in the command below:"
echo -e "   ${GREEN}ssh your_username@your_server_ip${NC}"
echo -e "2. If successful, you'll be logged into your server"
echo -e "3. If it fails, check:"
echo -e "   - Server IP is correct"
echo -e "   - Username is correct"
echo -e "   - SSH key is properly added to authorized_keys" 