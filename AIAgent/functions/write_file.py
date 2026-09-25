import os

def write_file(working_directory: str, file_path: str, content: str) -> str:
    wd_abs = os.path.abspath(working_directory)
    target_file = os.path.normpath(os.path.join(wd_abs, file_path))
    valid_target_file = os.path.commonpath([wd_abs, target_file]) == wd_abs
    if valid_target_file == False:
        return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'
    elif os.path.isdir(target_file):
        return f'Error: Cannot write to "{file_path}" as it is a directory'
    target_dir = os.path.dirname(target_file)
    os.makedirs(target_dir, exist_ok=True)
    with open(target_file, "w") as f:
        f.write(content)
    return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'