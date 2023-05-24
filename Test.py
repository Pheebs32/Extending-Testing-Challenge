import importlib
import shutil
import unittest
import os
import subprocess

class DocumentUpdaterTestCase(unittest.TestCase):
    def setUp(self):
        # Specify the target directory path
        self.target_dir = "test_target_directory"

        # Generate the necessary directories in the target directory
        os.makedirs(os.path.join(self.target_dir, "originals"))
        os.makedirs(os.path.join(self.target_dir, "updates"))
        os.makedirs(os.path.join(self.target_dir, "finals"))
        with open(os.path.join(self.target_dir, "allowlist"), "w") as allowlist_file:
            allowlist_file.write("Doe.txt\n")


    def tearDown(self):
        # Clean up the target directory after each test
        shutil.rmtree(self.target_dir)


    def test_file_added_to_originals_only(self):
        # Add a file to the originals directory
        filename = "Doe.txt"
        with open(os.path.join(self.target_dir, "originals", filename), "w") as file:
            file.write("Dr Doe\nMakers Academy\nZetland House\nLondon\nEC2A 4HJ\n")

        # Run the program
        subprocess.check_output(["python3", "document_updater.py", self.target_dir])

        # Assert that the file remains unchanged in the originals directory
        self.assertTrue(os.path.exists(os.path.join(self.target_dir, "originals", filename)))

        # Assert that the file does not exist in the updates directory
        self.assertFalse(os.path.exists(os.path.join(self.target_dir, "updates", filename)))

        # Assert that the file does not exist in the finals directory
        self.assertFalse(os.path.exists(os.path.join(self.target_dir, "finals", filename)))


    def test_file_added_to_originals_and_allowlist(self):
        # Add a file to the originals directory
        filename = "Doe.txt"
        with open(os.path.join(self.target_dir, "originals", filename), "w") as file:
            file.write("Dr Doe\nMakers Academy\nZetland House\nLondon\nEC2A 4HJ\n")

        # Add the same file name to the allowlist
        with open(os.path.join(self.target_dir, "allowlist"), "a") as file:
            file.write("Doe.txt\n")

        # Run the program
        subprocess.check_output(["python3", "document_updater.py", self.target_dir])

        # Assert that the file remains unchanged in the originals directory
        self.assertTrue(os.path.exists(os.path.join(self.target_dir, "originals", filename)))

        # Assert that the file does not exist in the updates directory
        self.assertFalse(os.path.exists(os.path.join(self.target_dir, "updates", filename)))

        # Assert that the file does not exist in the finals directory
        self.assertFalse(os.path.exists(os.path.join(self.target_dir, "finals", filename)))


    def test_file_in_originals_allowlist_and_updates(self):
        # Add a file to the originals directory
        filename = "Doe.txt"
        with open(os.path.join(self.target_dir, "originals", filename), "w") as file:
            file.write("Dr Doe\nMakers Academy\nZetland House\nLondon\nEC2A 4HJ\n")

        # Add the same file name to the allowlist
        with open(os.path.join(self.target_dir, "allowlist"), "a") as file:
            file.write("Doe.txt\n")

        # Add the same file name to the updates directory
        with open(os.path.join(self.target_dir, "updates", filename), "w") as file:
            file.write("Dr Doe\nMakers Academy\nZetland House\nLondon\nEC2A 4HJ\n")

        # Run the program
        subprocess.check_output(["python3", "document_updater.py", self.target_dir])

        # Assert that the file remains unchanged in the originals directory
        self.assertTrue(os.path.exists(os.path.join(self.target_dir, "originals", filename)))

        # Assert that the file remains unchanged in the updates directory
        self.assertTrue(os.path.exists(os.path.join(self.target_dir, "updates", filename)))

        # Assert that the file is copied to the finals directory
        self.assertTrue(os.path.exists(os.path.join(self.target_dir, "finals", filename)))

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
        # Add a file to the allowlist
        filename = "Doe.txt"
        with open(os.path.join(self.target_dir, "allowlist"), "a") as file:
            file.write("Doe.txt\n")

        # Add the same file name to the updates directory
        with open(os.path.join(self.target_dir, "updates", filename), "w") as file:
            file.write("Dr Doe\nMakers Academy\nZetland House\nLondon\nEC2A 4HJ\n")

        # Run the program
        subprocess.check_output(["python3", "document_updater.py", self.target_dir])

        # Assert that the file is not copied to the originals directory
        self.assertFalse(os.path.exists(os.path.join(self.target_dir, "originals", filename)))

        # Assert that the file remains unchanged in the updates directory
        self.assertTrue(os.path.exists(os.path.join(self.target_dir, "updates", filename)))

        # Assert that the file is copied to the finals directory
        self.assertTrue(os.path.exists(os.path.join(self.target_dir, "finals", filename)))

        # Assert that the file is not copied to the originals directory
        self.assertFalse(os.path.exists(os.path.join(self.target_dir, "originals", filename)))

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


    def test_file_not_in_any_directories(self):
        # Add a file name to the allowlist
        filename = "Doe.txt"
        with open(os.path.join(self.target_dir, "allowlist"), "a") as file:
            file.write("Doe.txt\n")

        # Run the program
        subprocess.check_output(["python3", "document_updater.py", self.target_dir])

        # Assert that the file is not copied to the originals directory
        self.assertFalse(os.path.exists(os.path.join(self.target_dir, "originals", filename)))

        # Assert that the file does not exist in the updates directory
        self.assertFalse(os.path.exists(os.path.join(self.target_dir, "updates", filename)))

        # Assert that the file does not exist in the finals directory
        self.assertFalse(os.path.exists(os.path.join(self.target_dir, "finals", filename)))


if __name__ == "__main__":
    unittest.main()
