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
[7-file](https://github.com/mideactive/alx-system_engineering-devops/blob/master/0x02-shell_redirections/7-file): "echo "Best School" > '\*\\'\''"Best School"\'\''\\*$\?\*\*\*\*\*:)'" the 'echo' and output redirection '>' operator will create the file name, and output the data into the excaped file.


##### 8. Save current state of directory

    Write a script that writes into the file ls_cwd_content the result of the command ls -la. If the file ls_cwd_content already exists, it should be         overwritten. If the file ls_cwd_content does not exist, create it.
    
#### Solution:

[8-cwd_state](https://github.com/mideactive/alx-system_engineering-devops/blob/master/0x02-shell_redirections/8-cwd_state): 'ls -al > <file_name>' will redirect the output of the list into the  file_name.


##### 9. Duplicate last line

    Write a script that duplicates the last line of the file iacta

        The file iacta will be in the working directory
        
#### Solution:

[9-duplicate_last_line](https://github.com/mideactive/alx-system_engineering-devops/blob/master/0x02-shell_redirections/9-duplicate_last_line): 'tail -n 1 <file_name> >> <file_name>' the 'tail' command used with the append operator '>>' will duplicate the last line in the file. 
