# Web Stack Debugging Project

## Description
In this debugging project, the goal is to get Apache to run on a Docker container and return a page containing "Hello Holberton" when querying the root of it. The provided example demonstrates the initial state where accessing the container returns an error message instead of the expected page.

## Steps to Achieve the Goal
1. Start a Docker container with Apache running on port 8080 mapped to port 80.
   ```bash
   docker run -p 8080:80 -d -it holbertonschool/265-0
Check the status of the Docker container.
bash
Copy code
docker ps
Use curl to query the root of the container's web server.
bash
Copy code
curl 0:8080
Identify and fix the issue preventing the container from returning the expected page.
After fixing the issue, use curl again to verify that accessing port 80 returns a page containing "Hello Holberton."
Repository Structure
0-give_me_a_page: Bash script containing the commands used to fix the issue.
README.md: Documentation providing an overview of the debugging project and instructions for resolving the issue.
Requirements
Basic understanding of Docker and web server configuration.
Familiarity with debugging techniques for web applications.
