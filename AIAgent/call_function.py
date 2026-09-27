# List the functions available for the LLM to use

from functions.get_files_info import schema_get_files_info

available_functions = [
    schema_get_files_info,
]