# Program to Change File or Directory Ownership
import os


def change_ownership(path, uid, gid):
    os.chown(path, uid, gid)


# assigning userid and groupid
file_or_directory_path = "/path/to/file_or_directory"
uid = 1000  # User ID
gid = 1000  # Group ID
change_ownership(file_or_directory_path, uid, gid)
