Web Infrastructure for Airbnb Clone Project
This project sets up a web infrastructure to serve an Airbnb clone project using Nginx as the web server and Gunicorn as the application server.

Concepts Covered
Web Server
Server
Web Stack Debugging
Background Context
Our web infrastructure is already serving web pages via Nginx from a previous project. In this project, we add an application server (Gunicorn) to serve dynamic content for our Flask-based Airbnb clone project. This setup integrates Nginx with Gunicorn to efficiently handle web requests.

Resources
Before starting, you should familiarize yourself with the following resources:

Application server vs web server
How to Serve a Flask Application with Gunicorn and Nginx on Ubuntu 16.04 (Note: Install Gunicorn globally, not via virtualenv)
Running Gunicorn
Flask Route Slash Handling
Upstart documentation
Prerequisites
Ubuntu 16.04 or later
Nginx installed
Python 3.6 or later
Flask application
Installation Steps
1. Install Gunicorn Globally
sh
Copy code
sudo apt update
sudo apt install gunicorn
2. Create a Flask Application
Make sure you have a Flask application ready. Here is a simple example:

python
Copy code
# app.py
from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello, World!"

if __name__ == '__main__':
    app.run()
3. Test Gunicorn with Flask Application
Run the Flask application with Gunicorn to ensure everything is set up correctly:

sh
Copy code
gunicorn --bind 0.0.0.0:5000 app:app
4. Configure Nginx to Proxy Pass to Gunicorn
Edit the Nginx configuration file to set up a reverse proxy:

sh
Copy code
sudo nano /etc/nginx/sites-available/your_project
Add the following content:

nginx
Copy code
server {
    listen 80;
    server_name your_domain_or_IP;

    location / {
        proxy_pass http://127.0.0.1:5000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }
}
Enable the Nginx configuration:

sh
Copy code
sudo ln -s /etc/nginx/sites-available/your_project /etc/nginx/sites-enabled
sudo nginx -t
sudo systemctl restart nginx
5. Create a Systemd Service File for Gunicorn
Create a systemd service file to manage the Gunicorn process:

sh
Copy code
sudo nano /etc/systemd/system/gunicorn.service
Add the following content:

ini
Copy code
[Unit]
Description=Gunicorn instance to serve your_project
After=network.target

[Service]
User=your_username
Group=www-data
WorkingDirectory=/path/to/your/project
ExecStart=/usr/bin/gunicorn --workers 3 --bind unix:/path/to/your/project/your_project.sock app:app

[Install]
WantedBy=multi-user.target
Start and enable the Gunicorn service:

sh
Copy code
sudo systemctl start gunicorn
sudo systemctl enable gunicorn
6. Update Nginx Configuration to Use Unix Socket
Edit your Nginx configuration file again:

sh
Copy code
sudo nano /etc/nginx/sites-available/your_project
Update the proxy_pass directive to use the Unix socket:

nginx
Copy code
location / {
    proxy_pass http://unix:/path/to/your/project/your_project.sock;
    proxy_set_header Host $host;
    proxy_set_header X-Real-IP $remote_addr;
    proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
    proxy_set_header X-Forwarded-Proto $scheme;
}
Restart Nginx:

sh
Copy code
sudo systemctl restart nginx
Debugging
Nginx Logs: /var/log/nginx/error.log
Gunicorn Logs: You can configure Gunicorn to log errors by adding --log-file /path/to/logfile.log to the ExecStart command in the systemd service file.
Conclusion
You now have a fully functioning web infrastructure serving your Flask application via Gunicorn and Nginx. This setup ensures that your application can handle both static and dynamic content efficiently.


