backupName="YourDesiredBackupFolderName"
mkdir -P "$backupName"
cd "$backupName"
git clone https://github.com/robfacella/GooDrive_DL.git
cd GooDrive_DL
# As Root
#bash install_Dependencies.sh

# Create/Edit a Config
rclone config
# Change this to your Config name
nano remoteName.txt

# BackupAhoy
python3 backup.py
