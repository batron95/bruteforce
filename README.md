# bruteforce


USAGE:  Usage: ./bruteforce.sh <password_file>


The script will:

1. Read each password from the provided password list.
2. Send a POST request to http://your_target_url/signin with the username root and each password.
3. If a 302 redirect is detected (indicating a failed login), it moves on to the next password.
4. If a valid password is found, it prints a success message and stops.
