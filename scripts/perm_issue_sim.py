import random  # To choose a random employee / user
import subprocess  # To run Linux commands like setfacl, etc.
from datetime import datetime  # To timestamp logs
import csv  # Allows for saving ticket logs to .csv format

# Log ticket data to CSV
def log_ticket_to_csv(user, folder_path, department, ticket_msg, filename="ticket_log.csv"):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    row = [timestamp, user["username"], department, folder_path, ticket_msg]

    try:
        with open(filename, mode='x', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Timestamp", "Username", "Department", "Folder", "Message"])
    except FileExistsError:
        pass

    with open(filename, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(row)

    print(f"Ticket logged to {filename}")

# Users this script can reference
users = [
    {
        "username": "aburton",
        "name": "Andrea Burton",
        "department": "Admin",
        "groups": ["executive", "admin"]
    },
    {
        "username": "afoster",
        "name": "Amanda Foster",
        "department": "HR",
        "groups": ["hr"]
    },
    {
        "username": "jmyers",
        "name": "Jacob Myers",
        "department": "HR",
        "groups": ["hr"]
    },
    {
        "username": "lkrablin",
        "name": "Lawrence Krablin",
        "department": "Finance",
        "groups": ["finance"]
    },
    {
        "username": "npatel",
        "name": "Nina Patel",
        "department": "Sales",
        "groups": ["sales"]
    },
    {
        "username": "jlangley",
        "name": "John Langley",
        "department": "Admin",
        "groups": ["executive", "admin"]
    },
    {
        "username": "dvoss",
        "name": "Dana Voss",
        "department": "Sales",
        "groups": ["sales"]
    },
    {
        "username": "mandrews",
        "name": "Michael Andrews",
        "department": "Finance",
        "groups": ["finance"]
    }
]

# Folder paths by department
folders = {
    "HR": "/srv/company/hr/",
    "Sales": "/srv/company/sales/",
    "Finance": "/srv/company/finance/",
    "Admin": "/srv/company/admin/",
    "Executive": "/srv/company/executive/"
}

# Choose a random user
selected_user = random.choice(users)

# Get department and folder path
user_dept = selected_user["department"]
user_folder = folders[user_dept]

# Print details to verify selection
print(f"Selected user: {selected_user['name']} ({selected_user['username']})")
print(f"Department: {user_dept}")
print(f"Folder Path: {user_folder}")

# Function to change permissions and generate ticket message
def change_permissions_and_generate_ticket(user, folder_path, department):
    username = user["username"]
    name = user["name"]

    option = random.choice(['remove_write', 'remove_read_write'])

    if option == 'remove_write':
        # Remove write permission only (user can still read)
        result = subprocess.run(
            ['setfacl', '-m', f'u:{username}:r-x', folder_path],
            capture_output=True, text=True
        )
        ticket_msg = f"{name} can read the contents of the {department} folder, but cannot make changes."
    else:
        # Remove all permissions for the user
        result = subprocess.run(
            ['setfacl', '-x', f'u:{username}', folder_path],
            capture_output=True, text=True
        )
        ticket_msg = f"{name} cannot access anything in the {department} folder."

    if result.returncode != 0:
        print(f"Error changing permissions: {result.stderr}")
    else:
        print("Permissions changed successfully.")

    return ticket_msg

# Run permission change and ticket logging
ticket = change_permissions_and_generate_ticket(selected_user, user_folder, user_dept)
print("Generated Ticket:")
print(ticket)

log_ticket_to_csv(selected_user, user_folder, user_dept, ticket)
