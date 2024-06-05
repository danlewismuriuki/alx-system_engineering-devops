# Setting Up Datadog Agent on Server

This guide provides detailed steps to install and configure the Datadog Agent on your server and ensure it is visible in Datadog under the hostname `XX-web-01`.

## Prerequisites

- A Datadog account (US site: [https://app.datadoghq.com](https://app.datadoghq.com))
- Access to your server
- Datadog API Key

## Steps

### 1. Sign Up and Log In

Ensure you are signed up and logged into the US Datadog site at [https://app.datadoghq.com](https://app.datadoghq.com).

### 2. Connect to Your Server

Use SSH to connect to your server. Replace `54.90.20.153` with your server's IP address.

```sh
ssh ubuntu@54.90.20.153
