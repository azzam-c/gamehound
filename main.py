import requests

def run():
    app_id = int(input("Enter Steam app ID: "))
    fetch_reviews(app_id)

def fetch_reviews(app_id):
    url = f"https://store.steampowered.com/appreviews/{app_id}?json=1"
    response = requests.get(url)
    response.raise_for_status()
    data = response.json()
    if not data.get("success"):
        print("Steam could not find reviews for that app ID.")
        return
    reviews = data.get("reviews", [])
    score_desc = data["query_summary"]["review_score_desc"]
    if not reviews:
        print("No reviews were returned for this game.")
        return
    review_texts = get_review_texts(reviews)
    stats = analyze_basic_stats(reviews)
    print()
    print("=" * 80)
    print("GAMEHOUND REVIEW REPORT")
    print("=" * 80)
    print(f"General Feelings: {score_desc}")
    print(f"Reviews Analyzed: {stats['total_reviews']}")
    print(f"Positive: {stats['positive_count']}")
    print(f"Negative: {stats['negative_count']}")
    print(f"Recommendation Rate: {stats['recommendation_rate']:.1f}%")
    print(f"Average Playtime at Review: {stats['average_playtime_hours']:.1f} hours")
    print(f"Usable Review Texts for ML: {len(review_texts)}")
    print("=" * 80)
    print_reviews(reviews)

def print_reviews(reviews):
    for review in reviews:
        playtime_minutes = review["author"]["playtime_at_review"]
        playtime_hours = playtime_minutes / 60
        username = review["author"]["personaname"]
        review_text = review["review"]
        print()
        print(f"---> {username}, with {playtime_hours:.1f} hours, says:")
        print(review_text)
        print("-" * 80)

def get_review_texts(reviews):
    review_texts = []
    for review in reviews:
        text = review["review"].strip()
        if len(text) >= 10:
            review_texts.append(text)
    return review_texts

def analyze_basic_stats(reviews):
    positive_count = 0
    negative_count = 0
    total_playtime_minutes = 0
    for review in reviews:
        if review["voted_up"]:
            positive_count += 1
        else:
            negative_count += 1

        total_playtime_minutes += review["author"]["playtime_at_review"]
    total_reviews = len(reviews)
    recommendation_rate = positive_count / total_reviews * 100
    average_playtime_hours = total_playtime_minutes / total_reviews / 60
    return {
        "total_reviews": total_reviews,
        "positive_count": positive_count,
        "negative_count": negative_count,
        "recommendation_rate": recommendation_rate,
        "average_playtime_hours": average_playtime_hours
    }

run()