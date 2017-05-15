import requests

class getAniList:
    def __init__(self, client_id, client_secret):
        self.client_id = client_id
        self.client_secret = client_secret
        self.token = requests.post("https://anilist.co/api/auth/access_token", data={"grant_type":"client_credentials", "client_id":self.client_id, "client_secret":self.client_secret}).json()["access_token"]

    def get_request(self, url):
        self.update_token()
        r = requests.get(
            "https://anilist.co/api/{url}".format(
                url = url
            ),
            headers = {"Authorization":"Bearer {token}".format(token=self.token)}
        )
        return r.json()

    def update_token(self):
        r = requests.get("https://anilist.co/api/user/josh", headers = {"Authorization":"Bearer {token}".format(token=self.token)})
        if "error" in r.json():
            self.token = requests.post("https://anilist.co/api/auth/access_token", data={"grant_type":"client_credentials", "client_id":self.client_id, "client_secret":self.client_secret}).json()["access_token"]

    def force_update_token(self):
        self.token = requests.post("https://anilist.co/api/auth/access_token", data={"grant_type":"client_credentials", "client_id":self.client_id, "client_secret":self.client_secret}).json()["access_token"]

    # Users
    def user_request(self, user, end=""):
        return self.get_request("user/{user}/{end}".format(user=user, end=end))

    def get_user(self, user):
        return self.user_request(user)

    def get_user_activity(self, user):
        return self.user_request(user, "activity")

    def get_user_followers(self, user):
        return self.user_request(user, "followers")

    def get_user_following(self, user):
        return self.user_request(user, "following")

    def get_user_favourites(self, user):
        return self.user_request(user, "favourites")

    def get_user_search(self, user):
        return self.user_request("search", user)

    def get_user_animelist(self, user):
        return self.user_request(user, "animelist")

    def get_user_animelist_raw(self, user):
        return self.user_request(user, "animelist/raw")

    def get_user_mangalist(self, user):
        return self.user_request(user, "mangalist")

    def get_user_mangalist_raw(self, user):
        return self.user_request(user, "animelist/raw")
