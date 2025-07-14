# Tier-1 IT Support Lab – Triage Guide

## Initial Set-up
Assuming you've added the python script to the server, run:  
`sudo python3 perm_issue_sim.py`

This creates the permission change and generates a ticket in the ticket_log.csv

`cat ticket_log.csv` to view the ticket.
##
## Scenario
A user reports:
“I can view the [department] folder, but I can’t open or modify any files.” (Removes Write Access)
Or
“I can’t access or modify any files in the [department] folder.” 
(Removes Read & Write Access)
##
## Objective
Use Linux tools to diagnose and resolve permission issues using UNIX permissions and ACLs.

### Step-by-Step Triage Process
1. **Confirm folder visibility and base permissions**  
`sudo ls -ld /srv/company/[department]`

2. **Review standard UNIX permissions across all department folders**  
`sudo ls -l /srv/company/*`

3. **Inspect ACLs for custom permissions**  
`sudo getfacl /srv/company/[department]`

**Expected Output:**  
`user:npatel:r-x`

4. **Compare expected access**  
- Refer to Group Access Matrix (available in Documentation folder on Github as a part of the excel spreadsheet)
- Compare to another user in the same department.
- Check the user’s groups:
`groups npatel`



5. **Restore or adjust permissions**  
	To grant full access (read, write, execute):
	`sudo setfacl -m u:[user]:rwx /srv/company/[department]`


6. **Recheck user permissions to confirm they have been successfully restored.**  
`sudo getfacl /srv/company/[department]`

***Bonus:***
To remove a specific ACL entry:
`sudo setfacl -x u:[user] /srv/company/[department]`
