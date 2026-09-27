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

schema_write_file = {
    "type": "function",
    "function": {
        "name": "write_file",
        "description": "Writes or overwrites a file at 'file_path' with the designated 'content'",
        "parameters": {
            "type": "object",
            "properties": {
                "file_path": {
                    "type": "string",
                    "description": "File path to the file wanting to be written or overwritten, relative to the working directory"
                },
                "content": {
                    "type": "string",
                    "description": "Content to be written to the specified file"
                }
            },
            "required": ["file_path", "content"],
        }
    }
}