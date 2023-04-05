### <div align="center">Shell permissions</div>
### OS: Linux-ubuntu 20.4

#### Requirements

Allowed editors: vi, vim, emacs
All your scripts will be tested on Ubuntu 20.04 LTS
All your scripts should be exactly two lines long ($ wc -l file should print 2)
All your files should end with a new line (why?)
The first line of all your files should be exactly #!/bin/bash
A README.md file, at the root of the folder of the project, describing what each script is doing
You are not allowed to use backticks, &&, || or ;
All your files must be executable

##### 0. My name is Betty

      Create a script that switches the current user to the user betty.

      You should use exactly 8 characters for your command (+1 character for the new line)
      You can assume that the user betty will exist when we will run your script
      
### Solution:

[0-iam_betty](https://github.com/mideactive/alx-system_engineering-devops/blob/master/0x01-shell_permissions/0-iam_betty): The 'su' command followed by the name of an existing user will change the user to required one.


##### 1. Who am I

      Write a script that prints the effective username of the current user.
      
### Solution: 

[1-who_am_i](https://github.com/mideactive/alx-system_engineering-devops/blob/master/0x01-shell_permissions/1-who_am_i): The shell command 'whoami' will print out the name of the current user


2. Groups

            Write a script that prints all the groups the current user is part of.
            
#### Solution:

[2-groups](https://github.com/mideactive/alx-system_engineering-devops/blob/master/0x01-shell_permissions/2-groups): The shell command 'groups' will print all the group a user is part of.



##### 3. New owner

      Write a script that changes the owner of the file hello to the user betty.
      
#### Solution:

[3-new_owner](https://github.com/mideactive/alx-system_engineering-devops/blob/master/0x01-shell_permissions/3-new_owner): 'chown owner file-name' changes the owner of a file to the one suplied.


##### 4. Empty!

Write a script that creates an empty file called hello.

#### Solution:

[4-empty](https://github.com/mideactive/alx-system_engineering-devops/blob/master/0x01-shell_permissions/4-empty): the command 'touch <file_name>' creaates an empty file with the name supplied.


##### 5. Execute

      Write a script that adds execute permission to the owner of the file hello.

            . The file hello will be in the working directory
            
#### Solution:

[5-execute](https://github.com/mideactive/alx-system_engineering-devops/blob/master/0x01-shell_permissions/5-execute): The command 'chmod u+x <file_name>' gives execute permission to owner when executed in the current working dir.
            
            
##### 6. Multiple permissions

      Write a script that adds execute permission to the owner and the group owner, and read permission to other users, to the file hello.

            The file hello will be in the working directory
            
#### Solution:

[6-multiple_permissions](https://github.com/mideactive/alx-system_engineering-devops/blob/master/0x01-shell_permissions/6-multiple_permissions): 'chmod 554 <file_name>' grants execute permission to owner, group owner, and readonly to others.


##### 7. Everybody!

      Write a script that adds execution permission to the owner, the group owner and the other users, to the file hello

            The file hello will be in the working directory
            You are not allowed to use commas for this script
            
#### Solution:

[7-everybody](https://github.com/mideactive/alx-system_engineering-devops/blob/master/0x01-shell_permissions/7-everybody):'chmod a+x <file_name>' or 'chmod 555 <file_name>' gives permission to owner, group owner, and other users.


##### 8. James Bond

      Write a script that sets the permission to the file hello as follows:

            Owner: no permission at all
            Group: no permission at all
            Other users: all the permissions
            The file hello will be in the working directory You are not allowed to use commas for this script
            
#### Solution:

[8-James_Bond](https://github.com/mideactive/alx-system_engineering-devops/blob/master/0x01-shell_permissions/8-James_Bond): 'chmod 7 <file_name>' add to all other users, except owner and group.


##### 9. John Doe

      Write a script that sets the mode of the file hello to this:

            -rwxr-x-wx 1 julien julien 23 Sep 20 14:25 hello
            
#### Solution:
[9-John_Doe](https://github.com/mideactive/alx-system_engineering-devops/blob/master/0x01-shell_permissions/9-John_Doe):'chmod 753 <file_name>' set file permission to the above.
