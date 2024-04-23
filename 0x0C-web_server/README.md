# DNS and Web Server Basics

### General

### What is the main role of a web server?
A web server's main role is to deliver web content to clients in response to their requests. It handles HTTP requests from clients, processes them, and returns the appropriate HTTP responses, often serving web pages, files, or other resources.

### What is a child process?
A child process is a process that is created by another process, known as its parent process. In the context of web servers, child processes are often spawned to handle incoming requests, allowing the parent process to continue listening for new connections.

### Why do web servers usually have a parent process and child processes?
Web servers typically use a parent-child process model to handle incoming requests efficiently. The parent process listens for incoming connections and spawns child processes to handle those connections. This approach allows the server to handle multiple requests simultaneously, improving scalability and performance.

### What are the main HTTP requests?
The main HTTP requests are:
- **GET**: Retrieves data from the server.
- **POST**: Submits data to be processed by the server.
- **PUT**: Updates existing data on the server.
- **DELETE**: Removes data from the server.
- **HEAD**: Retrieves metadata about a resource without fetching the resource itself.

## DNS

### What does DNS stand for?
DNS stands for Domain Name System.

### What is DNS's main role?
The main role of DNS is to translate human-readable domain names (like example.com) into IP addresses (like 192.0.2.1) that computers use to communicate over the Internet. DNS also provides other services like mail routing and domain registration information.

### DNS Record Types
DNS supports various record types, including:

- **A Record**: Maps a domain name to an IPv4 address.
- **CNAME Record**: Alias of one domain name to another (canonical name).
- **TXT Record**: Text record containing arbitrary text, often used for verifying domain ownership and adding metadata.
- **MX Record**: Specifies the mail server responsible for receiving email on behalf of a domain.


