import json


def read_file(file):
    """
    (str)->(dict)
    the function reads file given and returns dictionary with list a a value
    """
    f = open(file, encoding='utf-8')
    file_dictionary = dict(json.load(f))
    return file_dictionary


def find_inf(file_dictionary):
    """
    (dict)->(dict)
    The function takes dictionary of all user information and returns a dictionary of only needed one.
    """
    dictionary_user = dict()
    lst_of_data = []
    for i in file_dictionary['events']:
        dictionary_user[i['eventId']] = i['systemTime'], i['value'], i['eventSubType']
    lst_of_data.append(dictionary_user)
    return(lst_of_data)


if __name__ == '__main__':
    print(find_inf(read_file('example.json')))