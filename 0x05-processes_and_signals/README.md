# alx-system_engineering-devops

## Processes and Signals

This repository contains files related to the ALX System Engineering & DevOps program, specifically focusing on processes and signals in Unix-like operating systems.

## What is a PID?

- **PID**: Process Identification Number. It is a unique identifier assigned to each process running on a Unix-like operating system. PIDs are used by the operating system to track and manage processes.

## What is a process?

- **Process**: An executing instance of a program. It represents a single running task or program on a computer system. Each process has its own memory space, resources, and state.

## How to find a process' PID?

- There are several ways to find a process's PID:
  - Use the `ps` command: `ps aux | grep <process_name>`
  - Use the `pgrep` command: `pgrep <process_name>`
  - Use the `top` command: `top`
  - Use the `pidof` command: `pidof <process_name>`

## How to kill a process?

- To kill a process, you can use the `kill` command followed by the process's PID. For example:
  - `kill <pid>`: Sends a SIGTERM signal to the process.
  - `kill -9 <pid>`: Sends a SIGKILL signal to forcefully terminate the process.

## What is a signal?

- In computing, a signal is a software interrupt delivered to a process. Signals can be used to notify processes of events, errors, or other conditions. Processes can handle signals by installing signal handlers, which are functions that are executed in response to specific signals.

## What are the 2 signals that cannot be ignored?

- The two signals that cannot be ignored by a process are:
  - **SIGKILL** (signal number 9): This signal causes the process to be terminated immediately and cannot be caught or ignored.
  - **SIGSTOP** (signal number 19): This signal causes the process to be stopped (paused) and cannot be caught or ignored. It can be resumed later using the SIGCONT signal.

## Author

This repository is maintained by [Your Name].

