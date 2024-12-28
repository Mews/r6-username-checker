
# r6 username checker

A script to check from a list of r6 usernames which ones are available

# How to use

1. Make sure you have python installed.

2. Open the command line on the folder containing the script and run `pip install -r requirements.txt`.

3. Open `credentials.py` and write your Ubisoft email and password like so:
```
# Your ubisoft email
email = "johndoe@gmail.com"

# Your ubisoft password
password = "password123"
```
4. Add the usernames you want to check line by line to `usernames.txt`

5. Run `py main.py`. The availabe usernames will be saved to `available.txt`