import os
import shutil
import subprocess
from faker import Faker

fake = Faker('en_UK')

# Specify the target directory path
target_dir = "target_directory"

# Generate fake data for last names, names, and addresses
num_docs = 3
num_allowlist_entries = 2

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

# Generate files in originals and updates directories
for last_name, address in zip(last_names, addresses):
    filename = last_name + ".txt"
    file_path = os.path.join(originals_dir, filename)
    with open(file_path, "w") as f:
        f.write("\n".join(address))

    # Copy the file to the updates directory
    shutil.copy(file_path, os.path.join(updates_dir, filename))

# Run the program with the target directory as an argument
try:
    subprocess.check_output(["python", "document_updater.py", target_dir], stderr=subprocess.STDOUT)
except subprocess.CalledProcessError as e:
    output = e.output.decode()
    print(output)
