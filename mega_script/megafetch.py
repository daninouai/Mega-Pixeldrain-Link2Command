import shutil
import re
import binascii
import base64
import json
from Crypto.Cipher import AES
import requests


def fetch_mega_link(URL):
    missing = False
    for cmd in ["openssl"]:
        if not shutil.which(cmd):
            missing = True
            print(f"{sys.argv[0]}: {cmd}: command not found", file=sys.stderr)

    if missing:
        sys.exit(1)

    if re.match(r'.*/file/[^#]*#[^#]*', URL):
        id = re.search(r'/file/([^#]*)#', URL).group(1)
        key = re.search(r'#([^#]*)', URL).group(1)
    else:
        id = re.search(r'!(.*?)!', URL).group(1)
        key = URL.split('!')[-1]

    padded_key = key + '=' * ((4 - len(key) % 4) % 4)  # Pad key to make it base64 compliant
    decoded_key = base64.urlsafe_b64decode(padded_key.replace(',', ''))
    hex_output = binascii.hexlify(decoded_key).decode('utf-8')
    raw_hex = ''.join(hex_output[i:i + 2] for i in range(0, len(hex_output), 2))

    # Assuming raw_hex is a string containing the hex values from the previous operation
    part1 = int(raw_hex[0:16], 16)
    part2 = int(raw_hex[32:48], 16)
    part3 = int(raw_hex[16:32], 16)
    part4 = int(raw_hex[48:64], 16)

    result1 = '{:016x}'.format(part1 ^ part2)
    result2 = '{:016x}'.format(part3 ^ part4)

    hex_output = result1 + result2

    headers = {'Content-Type': 'application/json'}
    data = [{"a": "g", "g": "1", "p": id}]

    # Send the first request
    response = requests.post('https://g.api.mega.co.nz/cs?id=&ak=', headers=headers, json=data)
    if response.status_code != 200:
        exit(1)

    # Process the JSON response
    json_response = response.json()[0]
    file_url = json_response.get('g', '').replace('"', '')

    # Send the second request
    data = [{"a": "g", "p": id}]
    response = requests.post('https://g.api.mega.co.nz/cs?id=&ak=', headers=headers, json=data)
    if response.status_code != 200:
        exit(1)

    # Process the JSON response
    json_response = response.json()[0]
    at = json_response.get('at', '').replace('"', '')

    # Pad 'at' to make it base64 compliant
    padded_at = at + '=' * ((4 - len(at) % 4) % 4)
    decoded_at = base64.urlsafe_b64decode(padded_at.replace(',', ''))

    # Prepare the key and IV for AES decryption
    key = bytes.fromhex(hex_output)
    iv = b'\x00' * 16  # 16 bytes of zero for IV

    # Decrypt the data
    cipher = AES.new(key, AES.MODE_CBC, iv)
    decrypted = cipher.decrypt(decoded_at)

    # Remove padding bytes
    unpadded = decrypted.rstrip(b'\0')

    # Convert bytes to string and parse JSON
    json_str = unpadded.decode('utf-8')

    json_str = json_str[len("MEGA"):]

    json_data = json.loads(json_str)

    # Extract file name
    file_name = json_data['n']

    raw_hex_iv = raw_hex[32:48] + "0000000000000000"

    return file_url, file_name, hex_output, raw_hex_iv
