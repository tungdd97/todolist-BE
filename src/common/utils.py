import hashlib


def generate_md5_by_str(string_input):
    return str(hashlib.md5(str(string_input).encode('utf-8')).hexdigest())