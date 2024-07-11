import random
import base64

random.seed(2)
rand_int = random.randint(1, 10) 

def mask_ip(ip_address):
    """
    Mask an IP address by swapping and modifying octets.
    
    Args:
    ip_address (str): The original IP address.
    
    Returns:
    str: The masked IP address encoded in base64.
    """
    # Split IP address into octets
    octets = ip_address.split('.')
    # Swap the second and the last octet
    octets[1], octets[-1] = octets[-1], octets[1]
    # Modify the first and the last octets with random integer
    octets[0] = str(int(octets[0]) + rand_int)
    octets[-1] = str(int(octets[-1]) + rand_int * 3)
    # Join the octets with commas
    masked_ip = ','.join(octets)
    # Encode the masked IP in base64
    return base64.b64encode(masked_ip.encode("utf-8")).decode("utf-8")

def unmask_ip(masked_ip):
    """
    Unmask a base64 encoded IP address.
    
    Args:
    masked_ip (str): The masked IP address encoded in base64.
    
    Returns:
    str: The original IP address.
    """
    # Decode the base64 encoded masked IP
    unmasked_ip = base64.b64decode(masked_ip).decode("utf-8")
    # Split the unmasked IP into octets
    octets = unmasked_ip.split(',')
    # Reverse the modifications to the first and the last octets
    octets[0] = str(int(octets[0]) - rand_int)
    octets[-1] = str(int(octets[-1]) - (rand_int * 3))
    # Swap the second and the last octet back to original positions
    octets[1], octets[-1] = octets[-1], octets[1]
    # Join the octets with dots to form the original IP address
    original_ip = '.'.join(octets)
    return original_ip

def mask_device(device_id):
    """
    Mask a device ID by swapping and modifying segments.
    
    Args:
    device_id (str): The original device ID.
    
    Returns:
    str: The masked device ID encoded in base64.
    """
    # Split device ID into segments
    octets = device_id.split('-')
    # Swap the first and the last segment
    octets[0], octets[-1] = octets[-1], octets[0]
    # Modify the last and the second last segments with random integer
    octets[-1] = str(int(octets[-1]) + rand_int * 2)
    octets[-2] = str(int(octets[-2]) + rand_int + 4)
    # Join the segments with '#'
    masked_device = '#'.join(octets)
    # Encode the masked device ID in base64
    return base64.b64encode(masked_device.encode("utf-8")).decode("utf-8")

def unmask_device(device_id):
    """
    Unmask a base64 encoded device ID.
    
    Args:
    device_id (str): The masked device ID encoded in base64.
    
    Returns:
    str: The original device ID.
    """
    # Decode the base64 encoded masked device ID
    unmasked_device = base64.b64decode(device_id).decode("utf-8")
    # Split the unmasked device ID into segments
    octets = unmasked_device.split('#')
    # Reverse the modifications to the last and the second last segments
    octets[-1] = str(int(octets[-1]) - rand_int * 2)
    octets[-2] = str(int(octets[-2]) - rand_int - 4)
    # Swap the first and the last segment back to original positions
    octets[0], octets[-1] = octets[-1], octets[0]
    # Join the segments with '-' to form the original device ID
    original_device = '-'.join(octets)
    return original_device

def ver_to_int(version):
    """
    Convert a version string to an integer for DB storage.
    
    Args:
    version (str): The version string (e.g., "1.2.3").
    
    Returns:
    int: The version string converted to an integer.
    """
    # Split the version string into its components and convert them to integers
    ver_list = [int(x) for x in version.split(".")]
    # Reverse the list to process from the least significant to the most significant
    ver_list.reverse()
    # Convert the reversed list to an integer
    version_int = sum(x * (100**i) for i, x in enumerate(ver_list))
    return version_int

def int_to_ver(version_int):
    """
    Convert an integer back to a version string.
    
    Args:
    version_int (int): The integer representing the version.
    
    Returns:
    str: The integer converted back to a version string.
    """
    parts = []
    # Extract each part of the version from the integer
    while version_int > 0:
        part = version_int % 100
        parts.append(str(part))
        version_int //= 100
    # Reverse the parts to form the version string
    parts.reverse()
    version_str = ".".join(parts)
    return version_str