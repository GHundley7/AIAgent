import os

def get_files_info(working_directory: str, directory: str = ".") -> str:
    wd_abs = os.path.abspath(working_directory)
    target_dir = os.path.normpath(os.path.join(wd_abs, directory))
    valid_target_dir = os.path.commonpath([wd_abs, target_dir]) == wd_abs
    if valid_target_dir == False:
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
    elif os.path.isdir(target_dir) == False:
        return f'Error: "{directory}" is not a directory'
    else:
        contents = os.listdir(target_dir)
        list_items = []
        for item in contents:
            target_file = os.path.normpath(os.path.join(target_dir, item))
            item_size = os.path.getsize(target_file)
            valid_dir = os.path.isdir(target_file)
            list_items.append(f"- {item}: file_size={item_size} bytes, is_dir={valid_dir}")
        return_string = "\n".join(list_items)
        return return_string

