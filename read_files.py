def read_files(filename):
    with open(filename, "r") as file:
        urls = file.readlines()
    return urls

read_files("urls.txt")