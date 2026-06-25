import requests
def fetchReviews(id):
    requests.get("https://store.steampowered.com/appreviews/{}?json=1".format(id))
