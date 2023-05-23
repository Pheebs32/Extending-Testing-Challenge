## Early Planning

**Program Description:**
The program expects a target directory as an argument. It checks for the presence of two files: droplist and allowlist. If both files are found or if neither file is found, an error is displayed. If only one of the files is found, it proceeds with the following steps:

1. Reads the content of the found list file (droplist or allowlist).
2. Reads the documents present in the originals and updates directories.
3. Validates the document files in terms of their content length.
4. Creates a new directory called finals or empties an existing finals directory.
5. Depending on the type of list file found (droplist or allowlist), applies specific rules to filter the document files.
6. Performs a blend operation on documents that exist in both originals and updates directories if the list file is a droplist.
7. Copies the filtered and blended documents to the finals directory.

**Scenario:**

1. Target directory: /target_directory
2. originals directory contains three documents: test1.txt, test2.txt, and test3.txt.
3. updates directory contains four documents: test2.txt, test3.txt, test4.txt, and test5.txt.
4. allowlist file contains the following names: "Smith", "Johnson", "Williams".

**Expected Behavior:**
Since only the allowlist file is present, the program should copy the documents from the originals and updates directories to the finals directory, excluding any documents with names not listed in the allowlist file.
