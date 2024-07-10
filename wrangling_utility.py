import hashlib


def ver_to_int(version):
    """Convert a version string to an integer for DB storage."""
    ver_list = [int(x, 10) for x in version.split(".")]
    ver_list.reverse()
    version = sum(x * (100**i) for i, x in enumerate(ver_list))
    return version


def int_to_ver(version_int):
    """Convert an integer back to a version string."""
    parts = []
    while version_int > 0:
        part = version_int % 100
        parts.append(str(part))
        version_int //= 100
    parts.reverse()
    version_str = ".".join(parts)
    return version_str


def string_encode(string_parameter):
    """Function to mask the string with hashcode"""
    return hashlib.md5(string_parameter.encode("utf-8")).hexdigest()