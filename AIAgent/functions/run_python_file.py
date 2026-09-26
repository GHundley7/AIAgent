import os
import subprocess

def run_python_file(working_directory: str, file_path: str, args: list[str] | None = None) -> str:
    wd_abs = os.path.abspath(working_directory)
    target_file = os.path.normpath(os.path.join(wd_abs, file_path))
    valid_target_file = os.path.commonpath([wd_abs, target_file]) == wd_abs
    if valid_target_file == False:
        return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
    elif os.path.isfile(target_file) == False:
        return f'Error: "{file_path}" does not exist or is not a regular file'
    elif ".py" not in file_path:
        return f'Error: "{file_path}" is not a Python file'
    command = ["python", target_file]
    if args:
        command.extend(args)
    file_output = subprocess.run(command, capture_output=True, timeout=30, check=True, text=True)
    return_string = ""
    if file_output.returncode != 0:
        return_string += f"Process exited with code {file_output.returncode}\n"
    if not file_output.stdout and not file_output.stderr:
        return_string += f"No output produced\n"
    if file_output.stdout:
        return_string += f"STDOUT: {file_output.stdout}\n"
    if file_output.stderr:
        return_string += f"STDERR: {file_output.stderr}\n"
    return return_string