# Introduction to Servers and SSH

This repository provides an introduction to servers, SSH (Secure Shell), and creating SSH RSA key pairs. It also explains the advantage of using `#!/usr/bin/env bash` instead of `/bin/bash` in scripts.

## Table of Contents

- [What is a server?](#what-is-a-server)
- [Where servers usually live](#where-servers-usually-live)
- [What is SSH?](#what-is-ssh)
- [How to create an SSH RSA key pair](#how-to-create-an-ssh-rsa-key-pair)
- [How to connect to a remote host using an SSH RSA key pair](#how-to-connect-to-a-remote-host-using-an-ssh-rsa-key-pair)
- [The advantage of using #!/usr/bin/env bash instead of /bin/bash](#the-advantage-of-using-usrbinenv-bash-instead-of-binbash)

## What is a server?

A server is a computer or a device that provides functionality or resources to other computers, known as clients, over a network.

## Where servers usually live

Servers are typically located in data centers or server rooms with controlled environments to ensure optimal performance and security. However, servers can also be hosted in the cloud.

## What is SSH?

SSH (Secure Shell) is a cryptographic network protocol used for secure communication between a client and a server. It provides a secure way to access and manage remote devices or servers over an unsecured network, such as the internet.

## How to create an SSH RSA key pair

To create an SSH RSA key pair, you can use the `ssh-keygen` command.

```bash
ssh-keygen -t rsa -b 4096 -C "your_email@example.com"

