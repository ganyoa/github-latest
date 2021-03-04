import sys
import json

import requests

# Use Like python githubber.py JASchilz
# (or another user name)

if __name__ == "__main__":
    """
    Retrieve a list of "events" associated with the given user name
    Print out the time stamp associated with the first event in that list.
    """
    try:
        username = sys.argv[1]
    except IndexError:
        print('Enter github user name')
        sys.exit()

    response = requests.get('https://api.github.com/users/{}/events'.format(username))
    events = json.loads(response.content)

    print(events[0]['created_at'])