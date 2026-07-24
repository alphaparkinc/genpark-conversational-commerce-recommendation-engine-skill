from client import ConversationalCommerceRecommendationEngineClient

def main():
    client = ConversationalCommerceRecommendationEngineClient()
    res = client.recommend({"skin_type": "dry/sensitive"}, "Best hydration serum under $30")
    print(res["personalized_advice"])
    print("Ranked Products:")
    for p in res["ranked_products"]:
        print(f"  - {p['name']} (${p['price_usd']}) [Match: {p['match_confidence']}]")

if __name__ == "__main__":
    main()
