import os

def get_files_info(working_directory: str, directory: str = ".") -> str:
    wd_abs = os.path.abspath(working_directory)
    target_dir = os.path.normpath(os.path.join(wd_abs, directory))
    valid_target_dir = os.path.commonpath([wd_abs, target_dir]) == wd_abs
    if valid_target_dir == False:
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
    elif os.path.isdir(directory) == False:
        return f'Error: "{directory}" is not a directory'
    else:
        return f'Success: "{directory}" is within the working directory'


