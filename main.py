import requests
def run():
    app_id = int(input("Enter Steam app ID: "))
    fetchReviews(app_id)
def fetchReviews(app_id):
    url = f"https://store.steampowered.com/appreviews/{app_id}?json=1"
    response = requests.get(url)
    response.raise_for_status()
    data = response.json()
    reviews = data["reviews"]
    scoredesc = data["query_summary"]["review_score_desc"]
    print(f"General Feelings: {scoredesc}")
    for review in reviews:
        playtime_minutes = review["author"]["playtime_at_review"]
        print()
        print("---> " + review["author"]["personaname"] +
              ", with {} minutes, says: ".format(playtime_minutes))
        print(review["review"])
        print("-" * 80)
    returnReviewText(reviews)
    voteBalance(reviews)
def returnReviewText(reviews):
    reviewTexts = []
    for review in reviews:
        reviewTexts.append(review["review"])
    for text in reviewTexts:
        print(text)

def voteBalance(reviews):
    positive_count = 0
    negative_count = 0
    for review in reviews:
        if review["voted_up"]:
            positive_count += 1
        else:
            negative_count += 1
    print("Positive:", positive_count)
    print("Negative:", negative_count)

run()