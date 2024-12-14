import requests

# not needed
# from rich import print

name_cache = set()


def get_friends(uid):
    headers = {"Accept": "application/json"}
    r = requests.get(
        "https://friends.roblox.com/v1/users/" + str(uid) + "/friends", headers=headers
    )
    return r.json()


def get_metadata(uid):
    headers = {"Accept": "application/json"}
    r = requests.get(
        "https://friends.roblox.com/v1/metadata?targetUserId=" + str(uid),
        headers=headers,
    )
    return r.json()


def fill_missing_data(friends_list_data):
    for item in friends_list_data["data"]:
        id_value = item["id"]
        metadata = get_metadata(id_value)
        username = metadata["userName"]
        display_name = metadata["displayName"]
        item["name"] = username
        item["displayName"] = display_name

    return friends_list_data
