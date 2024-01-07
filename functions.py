FILEPATH = "todos.txt"


def get_todos(filepath=FILEPATH):
    """
    Reads text file and returns the data
    :param filepath: a path to file
    :return: list of lines of text
    """
    with open(filepath, "r") as file:
        data = file.readlines()
    return data


def write_todos(data, filepath=FILEPATH):
    with open(filepath, "w") as file:
        file.writelines(data)
