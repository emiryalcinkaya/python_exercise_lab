"""
Validate passwords based on security requirements.
"""

import re

passwords = input("Enter passwords: ").split(",")

valid_passwords = []

for password in passwords:

    if len(password) < 6 or len(password) > 12:
        continue

    if not re.search("[a-z]", password):
        continue

    if not re.search("[A-Z]", password):
        continue

    if not re.search("[0-9]", password):
        continue

    if not re.search("[$#@]", password):
        continue

    valid_passwords.append(password)

print(",".join(valid_passwords))