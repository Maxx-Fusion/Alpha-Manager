import requests


def get_user():
    # return user profile information
    response = requests.get(
        'https://api.clashofclans.com/v1/players/%23L8RGGOCJ')
    user_json = response.json()
    print(user_json)


get_user()