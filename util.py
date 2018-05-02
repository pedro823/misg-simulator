import os

def is_windows():
    return os.name == 'nt'

def unix_to_nt(file_name):
    return file_name.replace('/', '\\')
