## Bug Report
#### Bug 1: Strict Address Formatting Requirements
**Description:**
<br>The document_updater.py script enforces strict address formatting requirements 
for the generated addresses. Specifically, it expects the addresses to follow 
the format of name, street address, city, postcode for each file. However, real-world 
addresses may not always adhere to this specific format. This strict requirement may 
lead to issues when processing actual user data that doesn't conform to the expected format.

**Steps to Reproduce:**
<br>Run the document_updater.py script with test cases that generate fake 
addresses using the faker library.
<br>Inspect the generated addresses in the resulting files.

**Expected Result:**
<br>The script should handle a variety of address formats and not rely on a 
strict format that may not reflect real-world addresses accurately.

**Actual Result:**
<br>The document_updater.py script requires addresses to be in the specific 
format of name, street address, city, postcode. If addresses don't conform to 
this format, the script may encounter errors or produce incorrect results.
<br>![Screenshot 2023-05-23 at 15.27.19.png](..%2F..%2FDesktop%2FScreenshot%202023-05-23%20at%2015.27.19.png)

**Impact:**
<br>This issue limits the usability and applicability of the document_updater.py 
script in scenarios where real-world addresses may have different formatting or 
structures. It may introduce errors or inaccuracies when processing user data 
that deviates from the expected address format.

#### Bug 2: Compatibility Issues with Running document_updater.py from Tests
**Description:**
<br>The document_updater.py script is primarily designed to be executed from the 
command line, accepting the target directory as a command-line argument. However, 
when attempting to run the script from test cases using approaches like direct import 
or subprocess.check_output, it doesn't behave as expected. The script relies on the 
command-line context and environment, making it challenging to properly execute and 
test within the test framework.

**Steps to Reproduce:**
<br>Attempt to import and call functions or classes from document_updater.py 
directly within test cases.
<br>Try running document_updater.py as a separate process using 
subprocess.check_output from the test cases.

**Expected Result:**
<br>The document_updater.py script should execute correctly within the test framework, 
allowing for proper testing and verification of its functionality.

**Actual Result:**
<br>When attempting to import and call functions or classes from 
document_updater.py directly within test cases or running it as a separate 
process using subprocess.check_output, the script doesn't execute as expected. 
It may encounter errors or behave differently due to the lack of the command-line 
context and expected environment.

**Impact:**
<br>The compatibility issues prevent seamless integration of the document_updater.py 
script with the testing framework. It hampers the ability to effectively test the 
script's functionality and ensure its correctness within the test environment.

#### Bug 3: Inconsistent Handling of Files in Originals and Allowlist without Updates
**Description:**
<br>The document_updater.py script does not include files that exist in the originals 
directory and allowlist but have no corresponding updates in the updates directory. 
This behavior can lead to inconsistent handling of files, as addresses that have not 
been updated are not being pushed to the finals' directory.
<br>Whilst not a 'bug' I think the functionality should include that if it is in original and allowlist 
but not in updated it should still be added to finals - just my opinion though.

**Steps to Reproduce:**
<br>Place a file in the originals' directory.
<br>Include the filename in the allowlist file.
<br>Run the document_updater.py script.

**Expected Result:**
<br>Files that are present in the originals directory and listed 
in the allowlist should be pushed to the finals directory, even if 
there are no updates for those addresses.

**Actual Result:**
Files in the originals directory and allowlist without corresponding 
updates in the updates directory are not included in the finals' directory.
<br>![Screenshot 2023-05-24 at 12.13.05.png](..%2F..%2FDesktop%2FScreenshot%202023-05-24%20at%2012.13.05.png)

**Impact:**
The current behavior of the document_updater.py script may lead to inconsistencies 
in the output and prevent the expected behavior of including all relevant files 
in the finals directory. It can cause confusion and misrepresentation of the actual 
status of addresses that have not undergone updates but are still considered valid 
and should be included in the finals.