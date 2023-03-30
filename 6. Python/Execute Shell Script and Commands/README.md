### Executing Shell Scripts and Commands with Python

Three primary ways to run Python shell commands.

os.system()
subprocess.run()
subprocess.Popen() 

## Executing Shell Commands with Python using the subprocess module

The Python subprocess module can be used to run new programs or applications.

# subprocess.Popen()

   # Importing required module
    import subprocess

    subprocess.Popen('echo "Geeks 4 Geeks"', shell=True)

# subprocess.run()
run() is more flexible and quicker approach to run shell scripts

   # Importing required module
    import subprocess

    subprocess.run(["powershell", "pwd"], shell=True)



## Executing Shell Commands with Python using the os module

The os module in Python includes functionality to communicate with the operating system. 
It is one of the standard utility modules of Python. It also offers a convenient way to use operating system-dependent features, 
shell commands can be executed using the system() method in the os module.

# Example 1:
Here. we are using the system() method to execute shell commands of echo.

    import os
 
    os.system('echo "Welcome to Python for Devops"')
    os.system('pwd')
    os.system('cat')
      
    myCmd = 'ls -la'
    os.system(myCmd)
    
    

## Execute Shell Script using python

Ex 1:
     import subprocess

     subprocess.run(['./test.sh'])
     
Ex 2: In case the script is having multiple arguements.

      import subprocess

      output = subprocess.call(["./test.sh","xyz","1234"])
      print(output)
      
      
