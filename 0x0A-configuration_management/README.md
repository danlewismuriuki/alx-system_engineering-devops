Puppet Configuration Management
This project includes Puppet manifests for managing configuration files and resources on Ubuntu 20.04 LTS. It covers basic usage of Puppet's declarative language to model system configuration.

Resources
Intro to Configuration Management
Puppet Resource Type: File
Puppet’s Declarative Language: Modeling Instead of Scripting
Puppet Lint
Puppet Emacs Mode
Requirements
General
All files are interpreted on Ubuntu 20.04 LTS.
Files end with a new line.
A README.md file at the root of the project folder is mandatory.
Puppet manifests must pass puppet-lint version 2.1.1 without any errors.
Puppet manifests must run without error.
Puppet manifests' first line must be a comment explaining what the Puppet manifest is about.
Puppet manifests files must end with the extension .pp.
Note on Versioning
Ubuntu 20.04 VM should have Puppet 5.5 preinstalled.
Installation
bash
Copy code
$ apt-get install -y ruby=1:2.7+1 --allow-downgrades
$ apt-get install -y ruby-augeas
$ apt-get install -y ruby-shadow
$ apt-get install -y puppet
No need to attempt upgrading versions; this project focuses on familiarizing you with basic-level syntax virtually identical in newer versions of Puppet.






