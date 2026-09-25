from functions.write_file import write_file

tests = [
    ("calculator", "lorem.txt", "wait, this isn't lorem ipsum"),
    ("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet"),
    ("calculator", "/tmp/temp.txt", "this should not be allowed")
]

for item in tests:
    print(write_file(item[0], item[1], item[2]))
    print("------------------------------------------------------------")