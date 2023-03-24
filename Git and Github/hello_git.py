print("Hello Git world!")

# Configuring Git
# To configure git you need to told git who you are
# use the following command in the command line
# $ git config --global user.name "username"
# $ git config --global user.email "username@example.com" This is optional
# Ignoring Files
# Files with the extension .pyc are automatically generated from .py files, so 
# we don’t need Git to keep track of them. These files are stored in a directory called __pycache__. To tell Git to ignore this directory, make a special 
# file called .gitignore—with a dot at the beginning of the filename and no file 
# extension—and add the following line to it:
# _pycache__/
