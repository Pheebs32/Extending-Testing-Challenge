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

Unsure as to why test 3 and 4 fail at when executing to finals when all other aspect of the test function as intended.