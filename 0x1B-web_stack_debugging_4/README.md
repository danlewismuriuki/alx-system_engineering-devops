# Web Stack Debugging Task

This project involves debugging a web server stack that includes Nginx. The task focuses on improving the server's performance under high load, particularly by addressing issues related to the maximum number of open files that can be handled by the system.

## Prerequisites

- Ubuntu 14.04 LTS
- Puppet v3.4
- Puppet-lint version 2.1.1

## Project Structure

- `0-the_sky_is_the_limit_not.pp`: Puppet manifest to restart Nginx when the configuration file changes.
- `change_limits.pp`: Puppet manifest to change the soft and hard limits of open files for the user `holberton`.

## Puppet Manifests

### `0-the_sky_is_the_limit_not.pp`

This Puppet manifest ensures that Nginx is restarted whenever its configuration file changes.

#### Contents

```puppet
# Puppet manifest to fix Nginx configuration for handling high request load

exec { 'fix--for-nginx':
  command     => '/usr/sbin/service nginx restart',
  path        => '/usr/sbin/',
  refreshonly => true,
  subscribe   => File['/etc/nginx/sites-available/default'],
}
change_limits.pp
This Puppet manifest updates the soft and hard limits on the number of open files for the user holberton in the /etc/security/limits.conf file.

Contents
puppet
Copy code
# Change the limit of open files in OS

exec {'change limit soft':
  command  => "sudo sed -i 's/holberton soft nofile [0-9]*/holberton soft nofile 88888/g' /etc/security/limits.conf",
  provider => shell,
  onlyif   => "grep -q 'holberton soft nofile' /etc/security/limits.conf",
}

exec {'change limit hard':
  command  => "sudo sed -i 's/holberton hard nofile [0-9]*/holberton hard nofile 88888/g' /etc/security/limits.conf",
  provider => shell,
  onlyif   => "grep -q 'holberton hard nofile' /etc/security/limits.conf",
  require  => Exec['change limit soft'],
}
Usage
Install Puppet and Puppet-lint

bash
Copy code
sudo apt-get update
sudo apt-get install -y puppet
sudo gem install puppet-lint -v 2.1.1
Run Puppet Manifests

Ensure you are in the root directory of your project where the .pp files are located.

bash
Copy code
sudo puppet apply 0-the_sky_is_the_limit_not.pp
sudo puppet apply change_limits.pp
Verify Puppet Manifests with Puppet-lint

bash
Copy code
puppet-lint 0-the_sky_is_the_limit_not.pp
puppet-lint change_limits.pp
Testing
To test the configuration changes, use ApacheBench to simulate HTTP requests:

bash
Copy code
ab -c 100 -n 2000 localhost/
Expected Results
Initial test might show failed requests.
After applying the Puppet manifests, there should be no failed requests.
Example output:
bash
Copy code
Benchmarking localhost (be patient)
Completed 2000 requests

Server Software:        nginx/1.4.6
Server Hostname:        localhost
Server Port:            80

Document Path:          /
Document Length:        612 bytes

Concurrency Level:      100
Time taken for tests:   0.301 seconds
Complete requests:      2000
Failed requests:        0
Total transferred:      1706000 bytes
HTML transferred:       1224000 bytes
Requests per second:    6650.99 [#/sec] (mean)
Time per request:       15.035 [ms] (mean)
Time per request:       0.150 [ms] (mean, across all concurrent requests)
Transfer rate:          5540.33 [Kbytes/sec] received

Connection Times (ms)
              min  mean[+/-sd] median   max
Connect:        0    4   2.5      3      12
Processing:     2   11   5.2     10      31
Waiting:        1   10   5.2      8      29
Total:          5   15   5.2     14      31

Percentage of the requests served within a certain time (ms)
  50%     14
  66%     17
  75%     18
  80%     19
  90%     22
  95%     26
  98%     27
  99%     28
 100%     31 (longest request)
Conclusion
This project ensures that the web server stack, particularly Nginx, can handle high loads efficiently by adjusting system limits and ensuring Nginx is correctly configured and restarted when necessary.
