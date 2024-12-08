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

