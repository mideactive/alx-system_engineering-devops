### <div align="center">Shell redirections</div>
#### OS:linux-ubuntu 20.04

Requirements

Allowed editors: vi, vim, emacs
All your scripts will be tested on Ubuntu 20.04 LTS
All your scripts should be exactly two lines long ($ wc -l file should print 2)
All your files should end with a new line (why?)
The first line of all your files should be exactly #!/bin/bash
A README.md file, at the root of the folder of the project, describing what each script is doing
You are not allowed to use backticks, &&, || or ;
All your files must be executable
You are not allowed to use sed or awk


##### 0. Hello World

    Write a script that prints “Hello, World”, followed by a new line to the standard output.
    
#### Solution:

[0-hello_world](https://github.com/mideactive/alx-system_engineering-devops/blob/master/0x02-shell_redirections/0-hello_world): 'echo "Hello, World"' the 'echo' commad will output the sentence to the standard output.


##### 1. Confused smiley

    Write a script that displays a confused smiley "(Ôo)'.
    
#### Solution:

[1-confused_smiley](https://github.com/mideactive/alx-system_engineering-devops/blob/master/0x02-shell_redirections/1-confused_smiley): 'echo "\\"(Ôo)'" ' echo will print the quoted sign using an escape character '\\'.


##### 2. Let's display a file

    Display the content of the /etc/passwd file.
    
#### Solution:
[2-hellofile](https://github.com/mideactive/alx-system_engineering-devops/blob/master/0x02-shell_redirections/2-hellofile): 'cat /etc/passwd' 'cat' command will display the passwd file, inside the /etc dir in text on a standard output.


##### 3. What about 2?

    Display the content of /etc/passwd and /etc/hosts
    
#### Solution:

[3-twofiles](https://github.com/mideactive/alx-system_engineering-devops/blob/master/0x02-shell_redirections/3-twofiles): 'cat /etc/passwd && cat /etc/hosts' the 'cat' command displays the a file, while the '&&' operators makes it possible to display multiple files.


##### 4. Last lines of a file

    Display the last 10 lines of /etc/passwd
    
#### Solution:

[4-lastlines](https://github.com/mideactive/alx-system_engineering-devops/blob/master/0x02-shell_redirections/4-lastlines): 'tail -n 10 /etc/passwd' displays the last 10 lines in a file.


##### 5. I'd prefer the first ones actually

    Display the first 10 lines of /etc/passwd
    
#### Solution:

[5-firstlines](https://github.com/mideactive/alx-system_engineering-devops/blob/master/0x02-shell_redirections/5-firstlines): 'head -n 10 /etc/passwd' will display the first ten lines in the file.


##### 6. Line #2

    Write a script that displays the third line of the file iacta.

        The file iacta will be in the working directory
        
        You’re not allowed to use sed
        
#### Solution:

[6-third_line](https://github.com/mideactive/alx-system_engineering-devops/blob/master/0x02-shell_redirections/6-third_line): 'head -n 3 < file_name > | tail -n 1' will return only the third line in a file.


##### 7. It is a good file that cuts iron without making a noise

    Write a shell script that creates a file named exactly \*\\'"Best School"\'\\*$\?\*\*\*\*\*:) containing the text Best School ending by a new line.
    
#### Solution:
[7-file](https://github.com/mideactive/alx-system_engineering-devops/blob/master/0x02-shell_redirections/7-file): "echo "Best School" > '\*\\'\''"Best School"\'\''\\*$\?\*\*\*\*\*:)'" the 'echo' and output redirection '>' operator will create the file name, and output the data into the escaped file.


##### 8. Save current state of directory

    Write a script that writes into the file ls_cwd_content the result of the command ls -la. If the file ls_cwd_content already exists, it should be         overwritten. If the file ls_cwd_content does not exist, create it.
    
#### Solution:

[8-cwd_state](https://github.com/mideactive/alx-system_engineering-devops/blob/master/0x02-shell_redirections/8-cwd_state): 'ls -al > <file_name>' will redirect the output of the list into the  file_name.


##### 9. Duplicate last line

    Write a script that duplicates the last line of the file iacta

        The file iacta will be in the working directory
        
#### Solution:

[9-duplicate_last_line](https://github.com/mideactive/alx-system_engineering-devops/blob/master/0x02-shell_redirections/9-duplicate_last_line): 'tail -n 1 <file_name> >> <file_name>' the 'tail' command used with the append operator '>>' will duplicate the last line in the file. 


##### 10. No more javascript

    Write a script that deletes all the regular files (not the directories) with a .js extension that are present in the current directory and all its      subfolders.
    
#### Solution:

[10-no_more_js](https://github.com/mideactive/alx-system_engineering-devops/blob/master/0x02-shell_redirections/10-no_more_js): 'find . -type f -name "*.js" -delete' will delete all .js files in dir and sub-dir.


##### 11. Don't just count your directories, make your directories count

    Write a script that counts the number of directories and sub-directories in the current directory.

    The current and parent directories should not be taken into account
    Hidden directories should be counted
    
#### Solution:

[11-directories](https://github.com/mideactive/alx-system_engineering-devops/blob/master/0x02-shell_redirections/11-directories): 'find ./* -type d -print | wc -l' displays and count all dir and sub-dir in dir which includes hidden files.


##### 12. What’s new

    Create a script that displays the 10 newest files in the current directory.

        Requirements:

            One file per line
            Sorted from the newest to the oldest
            
#### Solution:

[12-newest_files](https://github.com/mideactive/alx-system_engineering-devops/blob/master/0x02-shell_redirections/12-newest_files): 'ls -t | head' will display newest 10 files from the current dir, and sort from newest to old.


##### 13. Being unique is better than being perfect

    Create a script that takes a list of words as input and prints only words that appear exactly once.

        Input format: One line, one word
        Output format: One line, one word
        Words should be sorted
        
#### Solution:

[13-unique](https://github.com/mideactive/alx-system_engineering-devops/blob/master/0x02-shell_redirections/13-unique): 'sort list | uniq -u' this script will return only one instance of value in the list.


##### 14. It must be in that file

    Display lines containing the pattern “root” from the file /etc/passwd
    
#### Solution:

[14-findthatword](https://github.com/mideactive/alx-system_engineering-devops/blob/master/0x02-shell_redirections/14-findthatword): "cat /etc/passwd | grep 'root'" or "grep 'root' /etc/passwd" displays the file content in '/etc/passwd' and hights the all instance of 'root'


##### 15. Count that word

    Display the number of lines that contain the pattern “bin” in the file /etc/passwd
    
#### Solution:

[15-countthatword](https://github.com/mideactive/alx-system_engineering-devops/blob/master/0x02-shell_redirections/15-countthatword): 'grep 'bin' /etc/passwd | wc -l' or 'cat /etc/passwd | grep 'bin' | wc -l' will display the number of lines that contains 'bin' in the /etc/passwd file.


##### 16. What's next?

    Display lines containing the pattern “root” and 3 lines after them in the file /etc/passwd.
    
#### Solution:

[16-whatsnext](https://github.com/mideactive/alx-system_engineering-devops/blob/master/0x02-shell_redirections/16-whatsnext): 'grep -A 3 /etc/passwd' will display lines containing 'root', and also 3 lines after it.


##### 17. I hate bins

    Display all the lines in the file /etc/passwd that do not contain the pattern “bin”.
    
#### Solution:

[17-hidethisword](https://github.com/mideactive/alx-system_engineering-devops/blob/master/0x02-shell_redirections/17-hidethisword): 'grep -v 'bin' /etc/passwd' will display lines not containing the word 'bin'.


##### 18. Letters only please

    Display all lines of the file /etc/ssh/sshd_config starting with a letter.

        include capital letters as well
        
#### Solution:

[18-letteronly](https://github.com/mideactive/alx-system_engineering-devops/blob/master/0x02-shell_redirections/18-letteronly): 'grep '^[[:alpha:]]' /etc/ssh/sshd_config' or 'grep -i "^[a-z]" /etc/ssh/sshd_config' will display all lines in the file starting with a letter.


##### 19. A to Z

    Replace all characters A and c from input to Z and e respectively.
    
#### Solution:

[19-AZ](https://github.com/mideactive/alx-system_engineering-devops/blob/master/0x02-shell_redirections/19-AZ): 'echo "input" | tr 'char(s) to be replaced' 'new char(s)' the 'tr' command will truncate the characters pipped to it by the 'echo' command, and replace characters appropriately.


##### 20. Without C, you would live in hiago

    Create a script that removes all letters c and C from input.
    
#### Solution:

[20-hiago](https://github.com/mideactive/alx-system_engineering-devops/blob/master/0x02-shell_redirections/20-hiago): 'echo "input" | tr -d "char(s) to be deleted"' 'tr' with the '-d' flag will delete character(s) passed to it by the 'echo' command appropriately.


##### 21. esreveR

    Write a script that reverse its input.
    
#### Solution:

[21-reverse](https://github.com/mideactive/alx-system_engineering-devops/blob/master/0x02-shell_redirections/21-reverse): "echo 'word(s)' | rev" the 'rev' command reverses word(s) pipped to it by an input.


##### 22. DJ Cut Killer

    Write a script that displays all users and their home directories, sorted by users.

        Based on the the /etc/passwd file
        
#### Solution:

[22-users_and_homes](https://github.com/mideactive/alx-system_engineering-devops/blob/master/0x02-shell_redirections/22-users_and_homes): 'cut -d":" -f 1,6 /etc/passwd | sort' will display and sort all users and their home dir.


##### 23. Empty casks make the most noise

    Write a command that finds all empty files and directories in the current directory and all sub-directories.

    Only the names of the files and directories should be displayed (not the entire path)
    Hidden files should be listed
    One file name per line
    The listing should end with a new line
    You are not allowed to use basename, grep, egrep, fgrep or rgrep
    
#### Solution:

[100-empty_casks](https://github.com/mideactive/alx-system_engineering-devops/blob/master/0x02-shell_redirections/100-empty_casks): 'find . -empty | rev | cut -d '/' -f 1 | rev' this will list all empty files, dir int the current dir, and all sub-dirs. And the rules requested above will be followed. 

|Command    |Uses                                     |Synopsis                                       |
|-----------|-----------------------------------------|-----------------------------------------------|
|find       |find files/dir etc                       |find . -empty                                  |
|rev        |print in reverse order                   |rev                                            |
|cut        |extract section or column of a text file |cut -d '/' -f 1                                |

##### 24. A gif is worth ten thousand words

    Write a script that lists all the files with a .gif extension in the current directory and all its sub-directories.

    Hidden files should be listed
    Only regular files (not directories) should be listed
    The names of the files should be displayed without their extensions
    The files should be sorted by byte values, but case-insensitive (file aaa should be listed before file bbb, file .b should be listed before file a,     and file Rona should be listed after file jay)
    One file name per line
    The listing should end with a new line
    You are not allowed to use basename, grep, egrep, fgrep or rgrep
    
# Solution:

[101-gifs](https://github.com/mideactive/alx-system_engineering-devops/blob/master/0x02-shell_redirections/101-gifs): "find . -type f -name '*.gif' -printf "%f\n | rev | cut -d "/" -f 1 | cut -d '.' -f 2- | rev | LC_ALL=C sort -f" 
|Command         |Uses                       |synopsis                                        |
|----------------|---------------------------|------------------------------------------------|
|find            |find file/dir etc          |find . -type f -name '*.gif' -printf "%f\n"     |
|rev             |print inreverse order      |rev                                             |
|cut             |extract section or column of txt file|cut -d "/" -f 1                       |
|LC_ALL=C sort -f|Alpha text sort and ignore case sensitivity                                 |


##### 25. Acrostic

    An acrostic is a poem (or other form of writing) in which the first letter (or syllable, or word) of each line (or paragraph, or other recurring        feature in the text) spells out a word, message or the alphabet. The word comes from the French acrostiche from post-classical Latin acrostichis). As    a form of constrained writing, an acrostic can be used as a mnemonic device to aid memory retrieval. Read more.

        Create a script that decodes acrostics that use the first letter of each line.

            The ‘decoded’ message has to end with a new line
            You are not allowed to use grep, egrep, fgrep or rgrep
            
#### Soluiton:

[102-acrostic](https://github.com/mideactive/alx-system_engineering-devops/blob/master/0x02-shell_redirections/102-acrostic): "cut -c 1 | paste -s -d ''" This bash command cuts and paste the first letter in every line in a text file without a newline.

|command        |Uses                                    |Synopsis                                          |
|---------------|----------------------------------------|--------------------------------------------------|
|cut            |remove sections from each line of files |cut OPTION... [FILE]...                           |
|paste          |paste - merge lines of files            |paste [OPTION]... [FILE]...                       |


##### 26. The biggest fan

    Write a script that parses web servers logs in TSV format as input and displays the 11 hosts or IP addresses which did the most requests.

        Order by number of requests, most active host or IP at the top
        You are not allowed to use grep, egrep, fgrep or rgrep
        
#### Solution:

[103-the_biggest_fan](https://github.com/mideactive/alx-system_engineering-devops/blob/master/0x02-shell_redirections/103-the_biggest_fan): "awk '{arr[$1]++} END {for (arrs in arr) print arr[arrs], arrs}' | sort -rn | head -n 11 | cut -d' ' -f 2". awk extracts, loops through, print number of hosts, and the hostname itself that occure most. passed it to be sorted in numeric order, and also in reversal. Then the first 11 lines is displayed. Lastly, we use the 'cut' command to extract the exact column that is required.

|Command              |Use                                       |synopsis                                                               |
|---------------------|------------------------------------------|-----------------------------------------------------------------------|
|Awk                  |pattern scanning and processing language  |awk [ POSIX or GNU style options ] -f program-file [ -- ] file ...     |
|sort                 |sort lines of text files                  |sort [OPTION]... [FILE]...                                             |
|head                 |Returns the first ten lines in a text file|head [options]... [FILE]...                                            |
|cut                  |extracts specified column(s) from a text file| cut [options]... [FILE]...                                         |
