# -*- coding: utf-8 -*-

import sys
import datetime
import getopt

from reddit_user import RedditUser, UserNotFoundError, NoDataError

if len(sys.argv) < 2:
    print("Usage: script.py <username>")
    sys.exit(1)

username = sys.argv[1]
print(f"Processing user {username}")
start = datetime.datetime.now()

try:
    user = RedditUser(username)
    print(user)
except UserNotFoundError:
    print(f"User {username} not found")
except NoDataError:
    print(f"No data available for user {username}")

print(f"Processing complete... {datetime.datetime.now() - start}")
