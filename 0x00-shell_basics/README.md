## <div align="center">shell_basics</div>
### OS: Linux ubuntu20.4

#### Tasks:

##### 0. Where am I?
##### Write a script that prints the absolute path name of the current working directory.
### solution:
#### [0-current_working_directory](https://github.com/mideactive/alx-system_engineering-devops/blob/master/0x00-shell_basics/0-current_working_directory)(pwd): used to print the absolute path of the current working dir.


##### 1. What’s in there?
##### Display the contents list of your current directory.
### Solution:
#### [1-listit](https://github.com/mideactive/alx-system_engineering-devops/blob/master/0x00-shell_basics/1-listit)(ls):list the content of a dir


##### 2. There is no place like home
##### Write a script that changes the working directory to the user’s home directory.

*****You are not allowed to use any shell variables*****
### Solution:
#### [2-bring_me_home](https://github.com/mideactive/alx-system_engineering-devops/blob/master/0x00-shell_basics/2-bring_me_home)(cd): changes the working dir to the user's dir.

  
##### 3. The long format
##### Display current directory contents in a long format
### Solution:
#### [3-listfiles](https://github.com/mideactive/alx-system_engineering-devops/blob/master/0x00-shell_basics/3-listfiles)(ls -l): Lists the content of a working dir in a long format.


##### 4. Hidden files
##### Display current directory contents, including hidden files (starting with .). Use the long format.
### Solution:
#### [4-listmorefiles](https://github.com/mideactive/alx-system_engineering-devops/blob/master/0x00-shell_basics/4-listmorefiles)(ls -al): Lists current dir with hidden files in a long list.



##### 5. I love numbers
##### Display current directory contents.

***** Long format
with user and group IDs displayed numerically
And hidden files (starting with .) *****
### Solution:
[5-listfilesdigitonly](https://github.com/mideactive/alx-system_engineering-devops/blob/master/0x00-shell_basics/5-listfilesdigitonly)(ls -n -al): displays the content of the current working dir, with user's and group IDs displayed numerically, with hidden files.



##### 6. Welcome
##### Create a script that creates a directory named my_first_directory in the /tmp/ directory.
#### Solution:
[6-firstdirectory](https://github.com/mideactive/alx-system_engineering-devops/blob/master/0x00-shell_basics/6-firstdirectory)(mkdir /tmp/my_first_directory): Creates a dir in the /tmp dir. 



##### 7. Betty in my first directory
##### Move the file betty from /tmp/ to /tmp/my_first_directory.
### Solution:
#### [7-movethatfile](https://github.com/mideactive/alx-system_engineering-devops/blob/master/0x00-shell_basics/7-movethatfile)(mv /tmp/betty /tmp/my_first_directory): Moves a file that is inside the /tmp/ dir to a directory inside the /tmp/ dir.




##### 8. Bye bye Betty
##### Delete the file betty.

***** The file betty is in /tmp/my_first_directory *****
### Solution:
#### [8-firstdelete](https://github.com/mideactive/alx-system_engineering-devops/blob/master/0x00-shell_basics/8-firstdelete)(rm /tmp/my_first_directory/betty): deletes the file 'betty' from the /tmp/my_first_directory



##### 9. Bye bye My first directory
##### Delete the directory my_first_directory that is in the /tmp directory.
### Solution:
#### [9-firstdirdeletion](https://github.com/mideactive/alx-system_engineering-devops/blob/master/0x00-shell_basics/9-firstdirdeletion)(rmdir /tmp/my_first_directory): Deletes the my_first_directory dir from the /tmp dir.



##### 10. Back to the future
##### Write a script that changes the working directory to the previous one.
### Solution:
[10-back](https://github.com/mideactive/alx-system_engineering-devops/blob/master/0x00-shell_basics/10-back)(cd -): Changes the current woring dir to the previous one.



##### 11. Lists
##### Write a script that lists all files (even ones with names beginning with a period character, which are normally hidden) in the current directory and the parent of the working directory and the /boot directory (in this order), in long format.
### Solution:
[11-lists](https://github.com/mideactive/alx-system_engineering-devops/blob/master/0x00-shell_basics/11-lists)(ls -al . .. /boot): Lists hidden contents in a long format in specified dir.



##### 12. File type
##### Write a script that prints the type of the file named iamafile. The file iamafile will be in the /tmp directory when we will run your script.
### Solution:
#### [12-file_type](https://github.com/mideactive/alx-system_engineering-devops/blob/master/0x00-shell_basics/12-file_type)(file /tmp/iamafile): Prints out the type of file located in the /tmp dir.



##### 13 We are symbols, and inhabit symbols
##### Create a symbolic link to /bin/ls, named __ls__. The symbolic link should be created in the current working
### Solution:
[13-symbolic_link](https://github.com/mideactive/alx-system_engineering-devops/blob/master/0x00-shell_basics/13-symbolic_link)(ln -s /bin/ls __ls__): Creates a simbolic link __ls__ that points to /bin/ls in the current woring dir.



##### 14. Copy HTML files
##### Create a script that copies all the HTML files from the current working directory to the parent of the working directory, but only copy files that did not exist in the parent of the working directory or were newer than the versions in the parent of the working directory.

***** You can consider that all HTML files have the extension .html *****
### Solution:
[14-copy_html](https://github.com/mideactive/alx-system_engineering-devops/blob/master/0x00-shell_basics/14-copy_html)(cp -u *.html ../): copy file to a file that is not exists or a newer version to the parrent dir.



##### 15. Let’s move
##### Create a script that moves all files beginning with an uppercase letter to the directory /tmp/u.

##### You can assume that the directory /tmp/u will exist when we will run your script
### Solution:
[100-lets_move](https://github.com/mideactive/alx-system_engineering-devops/blob/master/0x00-shell_basics/100-lets_move)(mv [[:upper:]]* /tmp/u):Moves all file beginning with an uppercase letter ti the /tmp/dir.



##### 16. Clean Emacs
##### Create a script that deletes all files in the current working directory that end with the character ~.
### Solution:
[101-clean_emacs](https://github.com/mideactive/alx-system_engineering-devops/blob/master/0x00-shell_basics/101-clean_emacs)(rm *~): Deletes all files that ends with ~ .



##### 17. Tree
##### #advanced
##### Create a script that creates the directories welcome/, welcome/to/ and welcome/to/school in the current directory.

##### You are only allowed to use two spaces (and lines) in your script, not more.
### Solution:
[102-tree](https://github.com/mideactive/alx-system_engineering-devops/blob/master/0x00-shell_basics/102-tree)(mkdir -p welcome/to/school): The mkdir -p flag creates multiple dir inside a parents dir.
