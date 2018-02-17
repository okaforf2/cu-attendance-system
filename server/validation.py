def sid(value):
    """
    Get valid Student ID
    Must be a <=7 digit integer
    :param value: sid
    :return: valid sid
    """
    if not isinstance(value, int):
        try:
            value = int(value)
        except ValueError:
            raise ValueError("sid (Student ID) must be an integer")

    if len(str(value)) > 7:
        raise ValueError("sid (Student ID) must be <=7 digits long")

    return value


def name(value):
    """
    Get valid name
    Must be a string
    :param value: name
    :return: valid name
    """
    if not isinstance(value, str):
        raise ValueError("Name must be an string")

    # Make first letter of each word uppercase
    value = value.title()

    return value


def username(value):
    """
    Get valid username
    Must be a string
    :param value: username
    :return: valid username
    """
    if not isinstance(value, str):
        raise ValueError("Username must be an string")

    return value