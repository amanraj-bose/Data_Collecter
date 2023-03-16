"""
    Author => Aman Raj
    Encoding => UTF-8
    File Created => 26/02/23
"""


import base64

def encode(password):
    return base64.standard_b64encode(bytes(password, 'utf-8'))

def decode(password:bytes):
    return str(base64.standard_b64decode(password)).removeprefix("b'").removesuffix("'")
