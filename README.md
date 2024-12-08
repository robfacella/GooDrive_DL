# GooDrive_DL
Download from G Suite Drive to a Local Location

# Make a folder where you want your backup. 
# Clone this repo into that backup directory.

# Navigate into Repo to configure and run Script

Script will automatically create a Folder next to the Repo Directory within your backup folder
Default name identical to the Parent Backup Folder.

Copy entire Drive into the backup maintaining heirarchy, using rclone

# Dependencies
python
rclone

# Setting up rclone
$ rclone config

Create a new Remote Connection

Set a name for the connection you're making.
A good choice would be the [username] of the account you are backing up

Choose the type of connection, in this case we are searching for Google Drive.
( Dec 8, 2024 : Currently "18" but may be something else as formats included by default may change. )

For personal use? 
Give it the #1 read write access option.

Keep just about everything else at default values.

It'll popup with a window in your default browser to choose a Google Account to give rclone access to.
Choose the account you wish, confirm that you are allowing access and return to rclone

once complete, q + Enter to close the configuration prompt.

edit remoteName.txt to match the name of the Remote you've configured.

# For Multiple Drives
No direct support yet.

Reccomended option:
1) Clone an Instance of this Repository per Email you're trying to backup.

Not Reccomended:
2) Rename the Backup Location to juggle multiple accounts ~For Exanple:
if parentDir is 'Backup'
rename internal 'Backup'Dir to the email it backed up, 
allow next email to be created as new 'backup',
repeat and hope you don't ever forget to change everything needed.

(1 is a better idea for numerous reasons, 
but hey, we get it,
this Repo is super saturated at MB) 
