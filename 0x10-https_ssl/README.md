# HTTPS and SSL/TLS

## What is HTTPS?

HTTPS stands for Hypertext Transfer Protocol Secure. It is an extension of HTTP, the protocol used for communication on the World Wide Web. HTTPS is designed to provide secure communication over a computer network, typically the internet. It encrypts the data exchanged between the client (such as a web browser) and the server, ensuring that it cannot be intercepted or tampered with by malicious actors.

## SSL/TLS: Two Main Elements

SSL (Secure Sockets Layer) and its successor, TLS (Transport Layer Security), provide two main elements:

1. **Encryption**: SSL/TLS protocols encrypt data transmitted between a client and a server, preventing eavesdropping and tampering by unauthorized parties.

2. **Authentication**: SSL/TLS protocols enable authentication of the server by the client, ensuring that the client is communicating with the intended server and not an impostor.

## HAProxy SSL Termination on Ubuntu 16.04

HAProxy is a free, fast, and reliable solution for high availability, load balancing, and proxying for TCP and HTTP-based applications. SSL termination refers to the process of decrypting SSL/TLS-encrypted traffic at the load balancer or proxy server and then forwarding it to the backend servers in an unencrypted form. This allows the backend servers to focus on processing requests without the overhead of SSL encryption and decryption.

## Bash Function

The provided Bash script `audit_subdomains.sh` demonstrates how to query DNS information for specified domains and subdomains using the `dig` command and parse the output using `awk`. It accepts domain and subdomain parameters and displays information about the DNS records associated with them.

## Learning Objectives

After completing this project, you should be able to:

- Explain what HTTPS is and its role in securing communication over the internet.
- Describe the two main elements provided by SSL/TLS: encryption and authentication.
- Understand the concept of SSL termination and its implementation using HAProxy on Ubuntu 16.04.
- Demonstrate knowledge of using Bash functions, `awk`, and `dig` for querying and analyzing DNS information.


