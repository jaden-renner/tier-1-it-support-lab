# Tier-1 Support Lab

Tier 1 IT support training lab using Linux (Ubuntu), CLI, JIRA, and scripting for realistic IT scenarios.

## About This Project

This project serves two main goals:

1. **Showcase my skills** in IT support, system administration, and scripting by building realistic, hands-on scenarios that demonstrate troubleshooting and problem-solving abilities.

2. **Provide a free, practical resource** for others who are learning or training in IT support, offering customizable scripts, documentation, and environments to practice with.

By sharing this work openly, I hope to contribute to a broader community of learners and professionals who want accessible tools to develop their skills and confidence.


## Project Disclaimer

**Base Two** is a completely fictional company created solely for the purpose of this IT Home Lab project.  
**ALL** employee names, roles, and data are entirely made up for training and practice purposes, **except for my own name, which is real**.  
This project does not represent any actual organization or its employees.  
If your name appears in this project, please know it is entirely coincidental and unintentional.  
I am happy to remove or anonymize any information upon request. Feel free to reach out if you have any concerns.

## Overview

This project aims to simulate a realistic Tier 1 IT support environment to practice user account management, group permissions, access control, and issue triage.

## Project Components

- **User Directory:** A spreadsheet listing employees, roles, departments, and group memberships.  
- **Group Access Matrix:** Defines permissions for company resources by department and group.  
- **Ubuntu Server VM:** Virtual environment running Ubuntu Server 24.04.2 (latest) with users, groups, and folder permissions configured.  
- **Scripting:** Python scripts (in development) to simulate random permission changes and generate IT support tickets for troubleshooting practice.  
- **Issue Tracking:** JIRA board set up to manage simulated tickets and track progress.

## Permission Issue Simulator

This Python script simulates real-world access issues by modifying ACL permissions for randomly selected employees. It logs a ticket in CSV format and allows for manual triage in a help desk setting.

- Randomizes users and permission types
- Works with Linux `setfacl` for realism
- Designed to be used in a VirtualBox-based IT lab
- Ticket logs saved to `ticket_log.csv`

To view or download Triage Guide, Click [HERE](https://github.com/jaden-renner/tier-1-it-support-lab/blob/main/Documentation/triage_guide.md)  
To download Company Directory & Group Access Matrix - Template, Click [HERE](https://github.com/jaden-renner/tier-1-it-support-lab/blob/main/Documentation/Company_UserDirectory_and_AccessMatrix%20-%20Template.xlsx)  
To download Python Script, Click [HERE](https://github.com/jaden-renner/tier-1-it-support-lab/blob/main/scripts/perm_issue_sim.py)  

## Tools Used

- [VirtualBox](https://www.virtualbox.org/wiki/Downloads) — for virtualization  
- [Ubuntu Server (latest)](https://ubuntu.com/download/server) — command-line interface (CLI)  
- [Python](https://www.python.org/downloads/) — for scripting  
- [JIRA](https://www.atlassian.com/software/jira/free) — for ticket management  
- GitHub — for version control and documentation

## Future Plans

- Complete the Python ticket generator script. ✓
- Integrate more complex permissions and auditing tools. **(WIP)**
- Expand the lab with network services like Samba and log monitoring. **(WIP)**

## License

This project is licensed under the **Creative Commons Attribution-NonCommercial 4.0 International License**. See the [LICENSE](./LICENSE.md) file for details.
