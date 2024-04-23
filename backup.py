
import os

print ("Hey, " + os.getlogin() + ", let's get started de-Googling your life.\n")

os.chdir("..")

childName = os.getcwd()
childName = childName.split("/")[-1]

print ( childName )
