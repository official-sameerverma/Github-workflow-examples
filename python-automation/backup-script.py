import os
import shutil
from datetime import datetime


source_dir='D://source/'
backup_dir='D://source/backup'

os.makedirs(backup_dir,exist_ok=True)
timestamp=datetime.now().strftime("%d-%m-%Y_%H-%m-%S")

backup_file_name=f"backup-{timestamp}"
back_path=os.path.join(backup_dir,backup_file_name)
shutil.make_archive(back_path,'zip',source_dir)
print("Backup completed successfully")

