## Further Testing

Each scenario that could happen:

|In Original | in AllowList | In Updates| In Finale |
|------------|--------------|-----------|-----------|
| In | Out | Out | Out |
| In | In | Out | Out |
| In | In | In | In |
| Out | In | In | In |
| Out | Out | In | Out |
| Out | Out | Out | Out |
| Out | In | Out | Out |

From this I need a generator that can generate a file for each scenario above and then to test each scenario

**Scenario 1: Adding a file to the originals directory only**
Add a file to the originals directory.
Run the program.
Assert that the file remains unchanged in the originals directory.
Assert that the file does not exist in the updates directory.
Assert that the file does not exist in the finals directory.

*Actual Results:*
As expected

**Scenario 2: Adding a file to originals and allowlist directories**
Add a file to the originals directory.
Add the same file name to the allowlist file.
Run the program.
Assert that the file remains unchanged in the originals directory.
Assert that the file does not exist in the updates directory.
Assert that the file is copied to the finals directory.

*Actual Results:*
As expected

**Scenario 3: Adding a file to originals, allowlist, and updates directories**
Add a file to the originals directory.
Add the same file name to the allowlist file.
Add the same file to the updates directory.
Run the program.
Assert that the file remains unchanged in the originals directory.
Assert that the file remains unchanged in the updates directory.
Assert that the file is copied to the finals directory.

*Actual Results:*
Seems to not want to push the file into final despite it acheiving all reqiurments

**Scenario 4: Adding a file to allowlist and updates directories only**
Add a file name to the allowlist file.
Add a file to the updates directory.
Run the program.
Assert that the file does not exist in the originals directory.
Assert that the file remains unchanged in the updates directory.
Assert that the file is copied to the finals directory.

*Actual Results:*
Seems to not want to push the file into final despite it acheiving all reqiurments 

**Scenario 5: Adding a file to neither originals, allowlist, nor updates directories**
Run the program.
Assert that there are no changes in the originals, updates, or finals directories.

*Actual Results:*
As expected

**Scenario 6: Adding a file to allowlist directory only**
Add a file name to the allowlist file.
Run the program.
Assert that there are no changes in the originals, updates, or finals directories.

*Actual Results:*
As expected

***
Unsure as to why tests 3 and 4 fail when executing to finals when all other aspect of the test function as intended.

***
Transfered all test to 'Faker' so data is randomly made for these tests rather than being statically made before hand.
Still cannot figure out how to get the document_updater.py to run alongside tests.

***
The 'document_updater.py' script is designed to be run from the command line or terminal. When executing a Python script from the command line, it typically receives command-line arguments that can be accessed within the script.

The line I used to try to activate the script from testing included a subprocess module to execute the 'document_updater.py' script as a separate process. It essentially simulates running the script from the terminal. The command-line arguments are passed as a list of strings, where "python3" is the command to run the Python interpreter and "document_updater.py" is the name of the script file. self.target_dir is the target directory path, which is passed as an argument to the script.

The reason it breaks when running from testing is that the document_updater.py script expects to receive command-line arguments. However, when I directly call the script from a test case using subprocess.check_output, it doesn't receive the expected command-line arguments, which may cause the script to behave differently or encounter errors.

While I tried multiple ways of running the script from the test cases non of them worked and the only way I could think of to get it to work is it would be best to refactor the script into modular functions or classes that can be imported and tested directly within the test cases, without relying on the command-line interface.
***