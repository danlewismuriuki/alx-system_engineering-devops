Debugging Nginx Listening on Port 80
Problem Statement
The Nginx installation on an Ubuntu container is not listening on port 80 as expected. When attempting to access port 80 using curl, the connection is refused.

Objective
The objective is to troubleshoot the issue and ensure that Nginx is running and listening on port 80 of all the server's active IPv4 IPs.

Steps Taken
Installation of Debugging Tools: Installed debugging tools and inspected the Nginx configuration files to identify any misconfigurations or issues.

Verification of Nginx Status: Checked the status of the Nginx service to ensure it is running.

Examination of Nginx Configuration: Reviewed the Nginx configuration files (nginx.conf, sites-available/default, etc.) to verify the port settings and server configurations.

Network Configuration: Ensured that the server's network configuration allows traffic on port 80 and that there are no firewall rules blocking access.

Restarting Nginx Service: Restarted the Nginx service to apply any changes made to the configuration files.

Testing Connectivity: Used curl command to test connectivity to port 80 after making changes to the configuration.

Bash Script for Automation
bash
Copy code
#!/bin/bash

# Restart Nginx service
service nginx restart

# Check Nginx service status
service nginx status

# Display Nginx configuration files for review
cat /etc/nginx/nginx.conf
cat /etc/nginx/sites-available/default

# Check network configuration
iptables -L

# Test connectivity to port 80
curl 0:80
Execution
Execute the Bash script on the server experiencing the issue.
Review the output to identify any errors or misconfigurations.
Make necessary adjustments to the Nginx configuration files.
Re-run the script to verify that Nginx is now listening on port 80.
Conclusion
The troubleshooting steps outlined above should help resolve the issue of Nginx not listening on port 80. By following the steps and using the provided Bash script, administrators can quickly diagnose and fix similar issues with Nginx installations.
