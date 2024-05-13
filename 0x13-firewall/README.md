
Firewall Configuration for Web Server (0. Block all incoming traffic but)
This repository contains the necessary configuration files and instructions to set up a firewall on a web server using ufw (Uncomplicated Firewall). The firewall rules are designed to block all incoming traffic by default, except for specific TCP ports required for SSH, HTTP, and HTTPS connections.

Requirements:
The firewall configuration applies to the web server (web-01).
The following TCP ports must be allowed:
Port 22: SSH (Secure Shell) for remote server access.
Port 80: HTTP for web traffic.
Port 443: HTTPS (HTTP Secure) for encrypted web traffic.
Configuration Steps:
Install ufw: If not already installed, install ufw using the package manager.

bash
Copy code
sudo apt-get update
sudo apt-get install ufw
Configure Firewall Rules: Set up firewall rules to block all incoming traffic by default and allow traffic on the required ports.

bash
Copy code
sudo ufw default deny incoming
sudo ufw allow ssh
sudo ufw allow http
sudo ufw allow https
Enable Firewall: Enable the firewall to apply the new rules.

bash
Copy code
sudo ufw enable
Usage:
To apply the firewall rules, follow these steps:

Log in to the web server (web-01).
Execute the provided ufw commands in the terminal to configure the firewall.
Contributions:
Contributions to improve this firewall configuration or provide additional instructions are welcome. To contribute, please fork this repository, make your changes, and submit a pull request.

License:
This project is licensed under the MIT License.

Port Forwarding (1. Port forwarding)
This section outlines the configuration steps to forward port 8080/TCP to port 80/TCP on the web server (web-01).

Requirements:
Configure web-01 so that its firewall redirects port 8080/TCP to port 80/TCP.
Configuration Steps:
Modify ufw Configuration: Update the ufw configuration file to enable port forwarding from 8080/TCP to 80/TCP.

bash
Copy code
# Copy the ufw configuration file that includes the port forwarding rule
cp ufw_configuration_file /etc/ufw/ufw.conf
Verify Configuration:

bash
Copy code
# Check if the port forwarding rule is applied
sudo ufw status
