import requests
def run():
    id=int(input('Enter steam app ID: '))
    fetchReviews(id)
def fetchReviews(id):
    url= f"https://store.steampowered.com/appreviews/{id}?json=1"
    response = requests.get(url)
    response.raise_for_status()
    data = response.json()
    scoredesc = data["query_summary"]["review_score_desc"]
    print(f"General Feelings: {scoredesc}")
    for review in data["reviews"]:
        print("")
        hours_at_post = review["author"]["playtime_at_review"]
        print("---> " + review["author"]["personaname"] + ", with {} hours, says: ".format(hours_at_post))
        print(review["review"])
        print("--------------------------------------------------------------------------------------------------------------------------------------------------------------")
    def returnReviewText(id):
        reviews = data["reviews"]
        reviewTexts = []
        for review in reviews:
            reviewTexts.append(review["review"])
        for text in reviewTexts:
            print(text)
fetchReviews(1778820)
##  for dict in data:   ##tries to scan thru for each dictionary in data, but each data key is of a different type
##      print(dict)