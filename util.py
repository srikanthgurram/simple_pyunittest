def hex_byte_to_binary(hex_key):
    """
      convert hex byte to binary

      :param hex_key: Hexa decimal byte
      :return: 4 digit binary string
      :rtype: string
    """
    hex_dictionary = {
        '0': '0000',
        '1': '0001',
        '2': '0010',
        '3': '0011',
        '4': '0100',
        '5': '0101',
        '6': '0110',
        '7': '0111',
        '8': '1000',
        '9': '1001',
        'A': '1010',
        'B': '1011',
        'C': '1100',
        'D': '1101',
        'E': '1110',
        'F': '1111',
        'a': '1010',
        'b': '1011',
        'c': '1100',
        'd': '1101',
        'e': '1110',
        'f': '1111'
    }

    return hex_dictionary[hex_key]


# return length of string
def get_string_length(input_str):
    """
      return length of input string

      :param input_str: input string
      :return: length of input string
      :rtype: int
    """
    counter = 0
    for str in input_str:
        counter += 1
    return counter


# return zeros string as per required length
def get_zeros_string(length=0):
    """
      return string of '0's as per the given length

      :param length: required string length
      :return: '0's matching required length
      :rtype: string
    """
    return '0' * length


# append zeros as per the required width
def append_zeros(binary_string, width):
    """
      return append zeros to the given input binary string as per the required string width

      :param width: required output binary string width
      :param binary_string: binary string
      :return: length of input string
      :rtype: string
    """
    required_string = ''
    string_length = get_string_length(binary_string)

    # check if string length is less than required
    if string_length < width:
        required_string = get_zeros_string(width - string_length)

    # pre-append zeros to the binary string
    required_string += binary_string
    return required_string


def is_integer(input_value):
    """
    Check if given value is valid integer
    :param input_value:
    :return: Boolean
    """
    try:
        int(input_value)
    except ValueError:
        return False
    else:
        return True


def is_str_contains_hex_values(hex_string):
    """
    Check if given substring contains valid hex values
    :param hex_string: input hex
    :return:
    """
    valid_hex_values = '0123456789ABCDEFabcdef'
    # return False if string contains any other characters than specified.
    for char in hex_string:
        if char not in valid_hex_values:
            return False
    return True


def is_valid_hex_string(hex_string):
    """
    Check if given string is valid Hexa decimal value, otherwise raise an error

    :param hex_string:
    :return: Boolean (True / False)
    :raises TypeError: if the given hexa binary string is invalid
    """
    if hex_string[:2] != '0x':
        return False
    else:
        return is_str_contains_hex_values(hex_string[2:])


# convert to binary
def hex_to_bin(hexstring, width=32):
    """
      return length of input string

      :param width: required string width
      :param hexstring: hex string
      :return: binary string that match the width
      :rtype: string
      :raises ValueError: if the hexstring length is greater than required width
    """
    if hexstring is None:
        raise ValueError(f"Invalid hex string")
    elif is_integer(width) is False:
        raise ValueError(f"Invalid width specified")
    elif get_string_length(hexstring[2:]) * 4 > width:
        # raise error if width is less than the hex string input
        raise ValueError(f"Invalid width specified")
    elif is_valid_hex_string(hexstring) is False:
        raise ValueError(f"Invalid hex string")

    binary_string = ''
    for hex_byte in hexstring[2:]:
        binary_value = hex_byte_to_binary(hex_byte)
        binary_string += binary_value
    # pre-append zeros to the string
    final_string = append_zeros(binary_string, width)
    return final_string
