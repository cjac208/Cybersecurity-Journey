# Web Directory Enumeration & Unauthorization Access 
**Lab Environment:** TryHackMe (Offensive Security Intro)

## Objective 
Identify hidden web directiories using automated discovery tools to locate unauthorized administrative panels.

## Tools & Skills
*  **Tool:** Gobuster
*  **Wordlist:** common.txt
*  **Skill:** Web Enumeration, Broken Access Control Testing

## Methodology
1. **Reconnaissance:** Performed directory brute-forcing using Gobuster with 10 threads
2. **Discovery:** Successfully identified a hidden '/bank-transfer' directory with an HTTP 200 status code.
3. **Exploitation:** Accessed the administrative panel and performed a Proof of Concept (PoC) transfer to demonstrate the vulnerability.

## Technical Proof
### 1. Enumeration Command & Results 
![Gobuster Preparation & Command](img/01-preparation-command.png)
![Gobuster Results](img/02-results.png)

### 2. Unauthorized Access & PoC Transfer 
![Unauthorized Access](img/03-unauthorized-access.png)
![PoC Transfer](img/04-poc-transfer.png)

### 3. Room Completion
![Completion](img/05-completion.png)
