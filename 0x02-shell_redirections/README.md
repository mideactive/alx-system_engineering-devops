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
