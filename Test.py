import importlib
import shutil
import unittest
import os
import subprocess
from faker import Faker
import time

class DocumentUpdaterTestCase(unittest.TestCase):
    def setUp(self):
        # Specify the target directory path
        self.target_dir = "test_target_directory"

        # Generate the necessary directories in the target directory
        os.makedirs(os.path.join(self.target_dir, "originals"))
        os.makedirs(os.path.join(self.target_dir, "updates"))
        os.makedirs(os.path.join(self.target_dir, "finals"))

        # Generate the allowlist file using Faker
        fake = Faker()
        with open(os.path.join(self.target_dir, "allowlist"), "w") as allowlist_file:
            last_name = fake.last_name()
            filename = f"{last_name}"
            allowlist_file.write(f"{filename}\n")


    def tearDown(self):
        pass
        # Clean up the target directory after each test
        shutil.rmtree(self.target_dir)

    def test_file_added_to_originals_only(self):
        fake = Faker()
        last_name = fake.last_name()
        filename = f"{last_name}"
        content = f"{fake.name()}\n{fake.street_address()}\n{fake.city()}\n{fake.postcode()}\n"

        # Add the file to the originals directory
        with open(os.path.join(self.target_dir, "originals", filename), "w") as file:
            file.write(content)

        # Run the program
        proc = subprocess.Popen(["python3", "document_updater.py", self.target_dir])
        proc.wait()

        # Assert that the file remains unchanged in the originals directory
        self.assertTrue(os.path.exists(os.path.join(self.target_dir, "originals", filename)))

        # Assert that the file does not exist in the updates directory
        self.assertFalse(os.path.exists(os.path.join(self.target_dir, "updates", filename)))

        # Assert that the file does not exist in the finals directory
        self.assertFalse(os.path.exists(os.path.join(self.target_dir, "finals", filename)))


    def test_file_added_to_originals_and_allowlist(self):
        fake = Faker()
        last_name = fake.last_name()
        filename = f"{last_name}"
        content = f"{fake.name()}\n{fake.street_address()}\n{fake.city()}\n{fake.postcode()}\n"

        # Add the file to the originals directory
        with open(os.path.join(self.target_dir, "originals", filename), "w") as file:
            file.write(content)

        # Add the same file name to the allowlist
        with open(os.path.join(self.target_dir, "allowlist"), "a") as file:
            file.write(f"{filename}\n")

        # Run the program
        proc = subprocess.Popen(["python3", "document_updater.py", self.target_dir])
        proc.wait()

        # Assert that the file remains unchanged in the originals directory
        self.assertTrue(os.path.exists(os.path.join(self.target_dir, "originals", filename)))

        # Assert that the file does not exist in the updates directory
        self.assertFalse(os.path.exists(os.path.join(self.target_dir, "updates", filename)))

        # Assert that the file does not exist in the finals directory
        self.assertTrue(os.path.exists(os.path.join(self.target_dir, "finals", filename)))


    def test_file_in_originals_allowlist_and_updates(self):
        fake = Faker()
        last_name = fake.last_name()
        filename = f"{last_name}"
        content = f"{fake.name()}\n{fake.street_address()}\n{fake.city()}\n{fake.postcode()}\n"

        # Add the file to the originals directory
        with open(os.path.join(self.target_dir, "originals", filename), "w") as file:
            file.write(content)

        # Add the same file name to the allowlist
        with open(os.path.join(self.target_dir, "allowlist"), "a") as file:
            file.write(f"{filename}\n")

        # Add the file to the updates directory
        with open(os.path.join(self.target_dir, "updates", filename), "w") as file:
            file.write(content)

        # Run the program
        proc = subprocess.Popen(["python3", "document_updater.py", self.target_dir])
        proc.wait()

        # Assert that the file is not copied to the originals directory
        self.assertTrue(os.path.exists(os.path.join(self.target_dir, "originals", filename)))

        # Assert that the file remains unchanged in the updates directory
        self.assertTrue(os.path.exists(os.path.join(self.target_dir, "updates", filename)))

        # Assert that the file is copied to the finals directory
        self.assertTrue(os.path.exists(os.path.join(self.target_dir, "finals", last_name)))

        # # Assert that the content of the file remains unchanged in the originals directory
        # with open(os.path.join(self.target_dir, "originals", filename), "r") as file:
        #     original_content = file.read()
        # with open(os.path.join(self.target_dir, "finals", filename), "r") as file:
        #     updated_content = file.read()
        # self.assertEqual(original_content, updated_content)

        # # Assert that the content of the file remains unchanged in the updates directory
        # with open(os.path.join(self.target_dir, "updates", filename), "r") as file:
        #     original_content = file.read()
        # with open(os.path.join(self.target_dir, "finals", filename), "r") as file:
        #     updated_content = file.read()
        # self.assertEqual(original_content, updated_content)


    def test_file_not_in_originals_but_in_allowlist_and_updates(self):
        fake = Faker()
        last_name = fake.last_name()
        filename = f"{last_name}"
        content = f"{fake.name()}\n{fake.street_address()}\n{fake.city()}\n{fake.postcode()}\n"

        # Add the same file name to the allowlist
        with open(os.path.join(self.target_dir, "allowlist"), "a") as file:
            file.write(f"{filename}\n")

        # Add the file to the updates directory
        with open(os.path.join(self.target_dir, "updates", filename), "w") as file:
            file.write(content)

        # Run the program
        proc = subprocess.Popen(["python3", "document_updater.py", self.target_dir])
        proc.wait()

        # Assert that the file is not copied to the originals directory
        self.assertFalse(os.path.exists(os.path.join(self.target_dir, "originals", filename)))

        # Assert that the file remains unchanged in the updates directory
        self.assertTrue(os.path.exists(os.path.join(self.target_dir, "updates", filename)))

        # Assert that the file is copied to the finals directory
        self.assertTrue(os.path.exists(os.path.join(self.target_dir, "finals", filename)))

        # # Assert that the content of the file remains unchanged in the updates directory
        # with open(os.path.join(self.target_dir, "updates", filename), "r") as file:
        #     original_content = file.read()
        # with open(os.path.join(self.target_dir, "finals", filename), "r") as file:
        #     updated_content = file.read()
        # self.assertEqual(original_content, updated_content)

        # # Assert that the content of the file is the same in the finals directory
        # with open(os.path.join(self.target_dir, "finals", filename), "r") as file:
        #     final_content = file.read()
        # self.assertEqual(updated_content, final_content)

    def test_file_in_originals_and_updates(self):
        fake = Faker()
        last_name = fake.last_name()
        filename = f"{last_name}"
        content = f"{fake.name()}\n{fake.street_address()}\n{fake.city()}\n{fake.postcode()}\n"
        # Add the file to the originals directory
        with open(os.path.join(self.target_dir, "originals", filename), "w") as file:
            file.write(content)

        # Add the file to the updates directory
        with open(os.path.join(self.target_dir, "updates", filename), "w") as file:
            file.write(content)

        # Run the program
        proc = subprocess.Popen(["python3", "document_updater.py", self.target_dir])
        proc.wait()

        # Assert that the file remains unchanged in the originals directory
        self.assertTrue(os.path.exists(os.path.join(self.target_dir, "originals", filename)))

        # Assert that the file remains unchanged in the updates directory
        self.assertTrue(os.path.exists(os.path.join(self.target_dir, "updates", filename)))

        # Assert that the file is copied to the finals directory
        self.assertTrue(os.path.exists(os.path.join(self.target_dir, "finals", filename)))

        #This is an example of a test that would include content covereage to ensure the correct file was carried over to 'finals'

    def test_file_not_in_any_directories(self):
        fake = Faker()
        last_name = fake.last_name()
        filename = f"{last_name}"
        content = f"{fake.name()}\n{fake.street_address()}\n{fake.city()}\n{fake.postcode()}\n"

        # Add the same file name to the allowlist
        with open(os.path.join(self.target_dir, "allowlist"), "a") as file:
            file.write(f"{filename}\n")

        # Run the program
        proc = subprocess.Popen(["python3", "document_updater.py", self.target_dir])
        proc.wait()

        # Assert that the file is not copied to the originals directory
        self.assertFalse(os.path.exists(os.path.join(self.target_dir, "originals", filename)))

        # Assert that the file does not exist in the updates directory
        self.assertFalse(os.path.exists(os.path.join(self.target_dir, "updates", filename)))

        # Assert that the file does not exist in the finals directory
        self.assertFalse(os.path.exists(os.path.join(self.target_dir, "finals", filename)))


if __name__ == "__main__":
    unittest.main()
