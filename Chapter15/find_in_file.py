class StringNotFoundException(Exception):
    pass

def find_string(file, string):
    for i,lines in enumerate(file.readlines()):
        if string in lines:
            return i
    raise StringNotFoundException(
          f'String {string} not found in File {file.name}.')
