from siegeapi import Auth
from siegeapi.exceptions import InvalidRequest
import asyncio
import credentials

async def main():
    print(f"Logging in with email: {credentials.email}")
    auth = Auth(credentials.email, credentials.password)

    try:
        with open("usernames.txt", "r") as f:
            usernames = [line.strip() for line in f.readlines()]

        for username in usernames:
            try:
                await auth.get_player(username)
                print(f"Username {username} is taken")
            except InvalidRequest:
                print(f"Username {username} is available")

                with open("available.txt", "a") as f:
                    f.write(username)
                    f.write("\n")
    
    finally:
        print("Closing connection...")
        await auth.close()


if __name__ == "__main__":
    with open("available.txt", "w") as f:
        f.write("")

    asyncio.run(main())