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
        r = requests.get("https://anilist.co/api/anime/1", headers = {"Authorization":"Bearer {token}".format(token=self.token)})
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

    # Series
    def series_request(self, series_type, end=""):
        return self.get_request("{series_type}/{end}".format(series_type=series_type, end=end))

    def get_series_page(self, series_type, series_id):
        return self.series_request(series_type, "{series_id}/page".format(series_id=series_id))

    def get_series_characters(self, series_type, series_id):
        return self.series_request(series_type, "{series_id}/characters".format(series_id=series_id))

    def get_series_staff(self, series_type, series_id):
        return self.series_request(series_type, "{series_id}/staff".format(series_id=series_id))

    def get_series_actors(self, series_type, series_id):
        return self.series_request(series_type, "{series_id}/actors".format(series_id=series_id))

    def get_airing(self, series_id):
        return self.series_request("anime","{series_id}/airing".format(series_id=series_id))

    def get_genre_list(self):
        return self.get_request("genre_list")

    def get_series_search(self, series_type, query):
        return self.series_request(series_type, "/search/{query}".format(query=query))

    # Characters
    def character_request(self, end):
        return self.get_request("character/{end}".format(end=end))

    def get_character_page(self, character_id):
        return self.character_request("{character_id}/page".format(character_id=character_id))

    def get_character_search(self, query):
        return self.character_request("search/{query}".format(query=query))

    # Staff
    def staff_request(self, end):
        return self.get_request("staff/{id}".format(id=id))

    def get_staff_page(self, staff_id):
        return self.staff_request("{staff_id}/page".format(staff_id=staff_id))

    def staff_search(self, query):
        return self.staff_request("search/{query}".format(query=query))

    # Studio
    def studio_request(self, end):
        return self.get_request("studio/{end}".format(end=end))

    def get_studio_page(self, studio_id):
        return self.studio_request("{studio_id}/page".format(studio_id=studio_id))

    def studio_search(self, query):
        return self.studio_request("search/{query}".format(query=query))

    # Reviews
    def get_review(self, series_type, review_id):
        return self.get_request("{series_type}/review/{review_id}".format(series_type=series_type, review_id=review_id))

    def get_series_review(self, series_type, series_id):
        return self.get_request("{series_type}/{series_id}".format(series_type=series_type, series_id=series_id))

    def get_user_review(self, user):
        return self.get_request("user/{user}/reviews".format(user=user))
