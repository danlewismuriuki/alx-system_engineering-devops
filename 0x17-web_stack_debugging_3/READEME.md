# Web Stack Debugging 3

This project focuses on web stack debugging using Puppet. The following instructions and guidelines ensure that the Puppet manifests adhere to the specified requirements and are properly interpreted on Ubuntu 14.04 LTS.

## Requirements

- All files should end with a new line.
- A `README.md` file at the root of the folder of the project is mandatory.
- Puppet manifests must pass puppet-lint version 2.1.1 without any errors.
- Puppet manifests must run without error.
- Puppet manifests' first line must be a comment explaining what the Puppet manifest is about.
- Puppet manifests files must end with the extension `.pp`.
- Files will be checked with Puppet v3.4.

## Setup

### Installing Dependencies

Ensure you have the correct version of puppet-lint and Puppet installed:

```sh
sudo apt-get update
sudo apt-get install -y ruby
sudo gem install puppet-lint -v 2.1.1
sudo apt-get install -y puppet=3.4*
