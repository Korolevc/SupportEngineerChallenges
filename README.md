# SupportEngineerChallenges
Esercise 1: the solution is to fetch recursively every dir/file starting by a root folder (it's a parameter) using the os.walk(root) method in os py lib. Foreach file founded we use the replace method (accessible by the open(file, modality) object) to replace, additionally, my code prints to console the path of the replaced files.
To run: 
open cmd > write the command: python replace_data_in_directories.py <directoryToFetch> <oldString> <newstring> 
modify the .bat file replacing the last two string of the command respectively: <oldString> <newString>

Esercise 2: the solution to detect the shebang interpreter is to check the first line of the code. To avoid opening files unnecessarily, we first check it's extension, if it's .py, .sh, .pl, .rb or .php then we check it's first line, if starts with "#!" we add it to a frequency array. Additionaly than just printing to console, the script creates a new file with the result.

To run: via console python ScriptCounter.py <directoryToFetch> [reportPath] 

Exercise 3: the solution is first to create a tar object that copies the /home/user path, then call the ssh object using the paramiko lib and set the connection to user@192.168.1.100. Finally create an sftp object a send the backup! 
To run:  #IMPORTANT: on MacOS and Linux the cron string for sunday night is 0 0 * * 0, in windows is 0 0 * * 7
windows: just click the batch file in the repository and it will set the cronstring 0 0 * * 7 with the python send_backup.py 
linux: 0 0 * * 0 python send_backup.py
macOS: 0 0 * * 0 /usr/bin/python3 send_backup.py

Exercise 4: Unfortunately, I have not been able to overcome all the exceptions I faced with this exercise, but the exercise is theoretically very clear:
To automate the creation of the infrastructure and configuration of the WordPress application, I would have used CloudFormation. This tool allows you to describe the desired infrastructure as code and automatically create and manage the necessary resources. For this purpose, I added the .yml file to this repository for configuration by parameterising the wordpress version as required.

make it secure: I would have used an EC2 instance with an AMI image of WordPress updated to the required version (since I could use only free images I went for the aws-linux), and configure security rules to ensure only authorised persons have access. 
NOTE: t2.micro and t3.micro are the only free options for my plan, t3.micro is better since has a better CPU (more expensive in general) 

make it fast: Use an RDS cluster database for data storage, configuring it for maximum availability and performance or even use a cache instance such as Amazon ElastiCache to improve site performance.

make it fault-tolerant: we could use many features AWS like: EC2 Auto Scaling, RDS-MultiAZ.

make it adaptive to avarage load: Configure a load balancer to distribute traffic across multiple EC2 instances to ensure fault tolerance and system scalability when traffic increases.

All the things I've just said, are implementable in "oneclick" by using the Wordpress MultiAZ Template in CloudFormation. 

