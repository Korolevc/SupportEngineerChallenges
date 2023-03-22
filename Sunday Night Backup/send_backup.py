import tarfile
import paramiko
import datetime

#Creating the backupfile
backupFilePath= f"Backup-{datetime.datetime.now().strftime('%y-%m-%d')}+'.tar.gz"
with tarfile.open(backupFilePath,'w:gz') as tar:
    tar.add("/home/user")

#Creating the ssh object 
ssh= paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect('192.168.1.100', username='user')

#Sending the backup using ssh

sftp= ssh.open_sftp()
sftp.put(backupFilePath, f'/remote/backup/{backupFilePath}')
sftp.close()
ssh.close()



