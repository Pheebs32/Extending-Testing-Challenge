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
As expected

**Scenario 4: Adding a file to allowlist and updates directories only**
Add a file name to the allowlist file.
Add a file to the updates directory.
Run the program.
Assert that the file does not exist in the originals directory.
Assert that the file remains unchanged in the updates directory.
Assert that the file is copied to the finals directory.

*Actual Results:*
As expected

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

## UPDATE ON TESTS - WORKING

After coming back with fresh eyes I saw my issues in my test conditions.
<br>The first one is that when I passsed the information through I was using 'name.txt' and somewhere in the source code there must be a strip function for punctuation which at the point of writing the files name to output which prevents the files from being passed into 'finals'.

<br>My second error was a race condition where in I asserted the test case before the program had finished executing therefor not giving me the required assertion. By adding the proc.wait() function this means that the test cases wait untill the program has finished and produces an exit code.

***

I have now discovered as I have looked further into this that this test suite is not complete. 
<br>I have done what I can in the time given but if I had further time I would add tests to increase test covereage into looking into the files contents so not the wrong file from 'originals' or 'updates' is passed over and I would look into tests with more than one file to carry over for more coverage. 