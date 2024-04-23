
import os

print ("Hey, " + os.getlogin() + ", let's get started de-Googling your life.\n")

os.chdir("..")

childName = os.getcwd()
childName = childName.split("/")[-1]

print ( "creating a subfolder for backup: " + childName )
os.makedirs(childName, exist_ok=True)
