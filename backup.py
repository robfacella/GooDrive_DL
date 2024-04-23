
import os
import subprocess

# Whatever you named your Remote when using: rclone config
# Pull the REMOTE name
file = open("remoteName.txt")
rember = file.readlines()
file.close()

remoteDriveName=rember[0].strip("\n")
print (remoteDriveName)

print ("Hey, " + os.getlogin() + ", let's get started de-Googling your life.\n")

os.chdir("..")

childName = os.getcwd()
childName = childName.split("/")[-1]

print ( "creating a subfolder for backup: " + childName )
os.makedirs(childName, exist_ok=True)

print ( "Have you already run: ")
print ( "rclone config")
print ( " " )

command = ( 'rclone ls ' + remoteDriveName + ':' )
subprocess.Popen(command, shell=True)
