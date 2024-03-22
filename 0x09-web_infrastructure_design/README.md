# Web Stack Overview

This document provides an overview of the web stack built as part of the sysadmin/devops track projects. It includes a diagram of the architecture, explanations of each component, and discussions on system redundancy and related acronyms.

## Architecture Diagram

![Web Stack Architecture](web_stack_diagram.png)

## Components

### 1. Load Balancer (LB)

The load balancer distributes incoming network traffic across multiple servers to ensure no single server is overwhelmed. It helps improve the reliability and scalability of the web application by distributing the load efficiently.

### 2. Web Servers

The web servers host the web application and serve content to users. They handle HTTP requests, process dynamic content (if applicable), and return responses to clients.

### 3. Database Server

The database server stores and manages data used by the web application. It handles queries, transactions, and data retrieval operations requested by the web servers.

### 4. Application Server

The application server runs the business logic and application code of the web application. It processes user requests, interacts with the database, and generates dynamic content to be served by the web servers.

## System Redundancy

System redundancy refers to the practice of duplicating critical components or services within a system to ensure continued operation in the event of failures or outages. In the web stack architecture:

- Load balancers can be configured in a redundant or failover mode to ensure uninterrupted traffic distribution.
- Multiple web servers provide redundancy in serving content and handling user requests.
- Database servers may implement replication or clustering for data redundancy and failover capabilities.
- Application servers can be deployed in redundant configurations to ensure continuous availability of business logic and application services.

## Acronyms

- **LAMP**: Stands for Linux, Apache, MySQL, and PHP/Python/Perl, representing a common open-source web development stack.
- **SPOF**: Stands for Single Point of Failure, referring to any component whose failure can cause the entire system to fail.
- **QPS**: Stands for Queries Per Second, a metric used to measure the throughput or capacity of a system in processing queries or requests.


