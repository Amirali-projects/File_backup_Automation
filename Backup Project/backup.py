import shutil
import datetime
import os

def backup_files(source, destination):
    today = datetime.date.today()
    backup_file_name = os.path.join(destination, f"backup_{today}")  # No .tar.gz extension here
    shutil.make_archive(backup_file_name, 'gztar', source)
    print(f"Backup created: {backup_file_name}.tar.gz")

# Define source and destination outside the function
source = r"D:\Coding Files\Python Basic files\Backup project"
destination = r"D:\Coding Files\Python Basic files\Backup project\backup"

backup_files(source, destination)  # Call the function only once




    