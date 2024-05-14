Project Overview:
This project focuses on understanding the importance of running software as another user rather than the root user on Linux systems. By doing so, we enhance security measures and mitigate the risks associated with potential system vulnerabilities.

Script 0-iamsomeoneelse:
This Bash script accepts one argument, which is the username of the user under which the whoami command will be executed. Here's how to create and use the script:

Create the Script:

bash
Copy code
touch 0-iamsomeoneelse
Open the Script in an Editor:

bash
Copy code
nano 0-iamsomeoneelse
Write the Script:

bash
Copy code
#!/bin/bash

# Check if an argument is provided
if [ -z "$1" ]; then
    echo "Usage: $0 <username>"
    exit 1
fi

# Run whoami command under the specified user
sudo -u "$1" whoami
Save and Exit the Editor.

Provide Execution Permission:

bash
Copy code
chmod +x 0-iamsomeoneelse
Run the Script:

bash
Copy code
./0-iamsomeoneelse <username>
Replace <username> with the desired username to execute the whoami command under that user.

Script 1-run_nginx_as_nginx:
This Bash script configures the Nginx web server to run as the nginx user instead of the root user. Additionally, it ensures that Nginx listens on all active IPs on port 8080. Here's how to create and use the script:

Create the Script:

bash
Copy code
touch 1-run_nginx_as_nginx
Open the Script in an Editor:

bash
Copy code
nano 1-run_nginx_as_nginx
Write the Script:

bash
Copy code
#!/bin/bash

# Replace 'user' directive in Nginx configuration file
sed -i 's/user .*/user nginx;/g' /etc/nginx/nginx.conf

# Restart Nginx to apply changes
service nginx restart
Save and Exit the Editor.

Provide Execution Permission:

bash
Copy code
chmod +x 1-run_nginx_as_nginx
Run the Script:

bash
Copy code
./1-run_nginx_as_nginx
This script modifies the Nginx configuration file to specify the nginx user and then restarts Nginx to apply the changes.

Conclusion:
By following these steps and scripts, we ensure that software is run securely under the appropriate user, enhancing system security and minimizing potential risks. This approach aligns with best practices in system administration and software deployment.
