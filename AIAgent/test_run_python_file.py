from functions.run_python_file import run_python_file

tests = [
    ("calculator", "main.py"),
    ("calculator", "main.py", "3 + 5"),
    ("calculator", "tests.py"),
    ("calculator", "../main.py"),
    ("calculator", "nonexistent.py"),
    ("calculator", "lorem.txt")
]

for item in tests:
    if len(item) == 3:
        print(run_python_file(item[0], item[1], item[2]))
    else:
        print(run_python_file(item[0], item[1]))
    print("------------------------------------------------------------")