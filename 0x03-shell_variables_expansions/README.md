### <div align="center">Shell variable expansions</div>

#### OS:Linux-ubuntu 20.04

#### Requirements

Allowed editors: vi, vim, emacs
All your scripts will be tested on Ubuntu 20.04 LTS
All your scripts should be exactly two lines long ($ wc -l file should print 2)
All your files should end with a new line (why?)
The first line of all your files should be exactly #!/bin/bash
A README.md file, at the root of the folder of the project, describing what each script is doing
You are not allowed to use &&, || or ;
You are not allowed to use bc, sed or awk
All your files must be executable



##### 0.Task <o>

  Create a script that creates an alias.

    Name: ls
    Value: rm *
  
#### Solution:
  
[0-alias](https://github.com/mideactive/alx-system_engineering-devops/blob/master/0x03-shell_variables_expansions/0-alias) 'alias ls="rm *" written in a bash script will the alis 'ls'.   

  
  
##### 1. Hello you

    Create a script that prints hello user, where user is the current Linux user.
  
#### Solution:
  
[1-hello_you](https://github.com/mideactive/alx-system_engineering-devops/blob/master/0x03-shell_variables_expansions/1-hello_you): 'echo "hello $USER"' in a shell script will print the word 'hello' followed by the current use name.    


##### 2. The path to success is to take massive, determined action

          Add /action to the PATH. /action should be the last directory the shell looks into when looking for a program.
          
#### Solution:

[2-path](https://github.com/mideactive/alx-system_engineering-devops/blob/master/0x03-shell_variables_expansions/2-path): 'export PATH=$PATH:/action' this script will temporarily add the '/action' dir to '$PATH'. To make it pamanent, it should be added to the ~/.bashrc file.



##### 3. If the path be beautiful, let us not ask where it leads

          Create a script that counts the number of directories in the PATH.
  
#### Solution:
  
[3-paths](https://github.com/mideactive/alx-system_engineering-devops/blob/master/0x03-shell_variables_expansions/3-paths): "echo $PATH | tr ':' '\n' | wc -l" this code used in a bash script with display the '$PATH', breaks the '$PATH' into lines, and count the number of lines in the script.

|COmmand      |Uses                                                   |Synopsis                                                    |
|-------------|-------------------------------------------------------|------------------------------------------------------------|
|echo         |Use to dislay text to standard output                  |echo [options] [FILE.txt]                                   |
|tr           |Translates of deletes character(s)                     |tr [option] "character_to_be replaced" "subtitude           |
|wc           |print newline, word, and byte counts for each file     |wc [options] [FILE]                                         |

  
  
##### 4. Global variables

      Create a script that lists environment variables.
  
#### Solution:
  
[4-global_variables](https://github.com/mideactive/alx-system_engineering-devops/blob/master/0x03-shell_variables_expansions/4-global_variables): "printenv" or "env" will list global or environment variables.
  
  
##### 5. Local variables

      Create a script that lists all local variables and environment variables, and functions.
  
#### Solution:
  
[5-local_variables](https://github.com/mideactive/alx-system_engineering-devops/blob/master/0x03-shell_variables_expansions/5-local_variables): "set | less" will display the local variables.
  
  
##### 6. Local variable

      Create a script that creates a new local variable.
        Name: BEST
        Value: School
  
#### Solurion:
  
[6-create_local_variable](https://github.com/mideactive/alx-system_engineering-devops/blob/master/0x03-shell_variables_expansions/6-create_local_variable): 'set BEST="School"' this line of code in a bash script will set 'BEST' as a local variable with the value 'School'
  
  
  
  


