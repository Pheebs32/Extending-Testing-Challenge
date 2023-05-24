import os
import shutil
import subprocess
from faker import Faker

fake = Faker('en_UK')

# Specify the target directory path
target_dir = "target_directory"

# Generate fake data for last names, names, and addresses
num_docs = 5
num_allowlist_entries = 3

# Generate last names, names, and addresses
last_names = [fake.last_name() for _ in range(num_docs)]

names = [fake.prefix() + " " + fake.first_name() + " " + last_name for last_name in last_names]

addresses = [
    [
        name,
        fake.street_address(),
        fake.city(),
        fake.postcode()
    ]
    for name in names
]

# Create originals directory if it doesn't exist
originals_dir = os.path.join(target_dir, "originals")
os.makedirs(originals_dir, exist_ok=True)

# Create updates directory if it doesn't exist
updates_dir = os.path.join(target_dir, "updates")
os.makedirs(updates_dir, exist_ok=True)

# Create allowlist file
allowlist_file = os.path.join(target_dir, "allowlist")
allowlist_entries = [last_name for last_name in last_names[:num_allowlist_entries]]
with open(allowlist_file, "w") as f:
    f.write("\n".join(allowlist_entries))

# Scenario 1: Add a file to originals but not to updates
filename = last_names[0] + ".txt"
file_path = os.path.join(originals_dir, filename)
with open(file_path, "w") as f:
    f.write("\n".join(addresses[0]))

# Scenario 2: Add a file to originals and allowlist, but not to updates
filename = last_names[1] + ".txt"
file_path = os.path.join(originals_dir, filename)
with open(file_path, "w") as f:
    f.write("\n".join(addresses[1]))
allowlist_entries.append(last_names[1])
with open(allowlist_file, "w") as f:
    f.write("\n".join(allowlist_entries))

# Scenario 3: Add a file to originals, allowlist, and updates
filename = last_names[2] + ".txt"
file_path = os.path.join(originals_dir, filename)
with open(file_path, "w") as f:
    f.write("\n".join(addresses[2]))
shutil.copy(file_path, os.path.join(updates_dir, filename))
allowlist_entries.append(last_names[2])
with open(allowlist_file, "w") as f:
    f.write("\n".join(allowlist_entries))

# Scenario 4: Add a file to allowlist and updates, but not to originals
filename = last_names[3] + ".txt"
file_path = os.path.join(updates_dir, filename)
with open(file_path, "w") as f:
    f.write("\n".join(addresses[3]))
allowlist_entries.append(last_names[3])
with open(allowlist_file, "w") as f:
    f.write("\n".join(allowlist_entries))

# Scenario 5: Add a file to allowlist only
filename = last_names[4] + ".txt"
with open(allowlist_file, "a") as f:
    f.write("\n" + last_names[4])

# Run the program with the target directory as an argument
try:
    subprocess.check_output(["document.updater.py", target_dir], stderr=subprocess.STDOUT)
except subprocess.CalledProcessError as e:
    output = e.output.decode()
    print(output)
