class ConversationalCommerceRecommendationEngineClient:
    def recommend(self, user_profile: dict, search_intent: str) -> dict:
        prods = [
            {"name": "Hydrating Niacinamide Serum 30ml", "price_usd": 24.50, "match_confidence": "98%"},
            {"name": "Ultra-Gentle Cleansing Balm", "price_usd": 18.00, "match_confidence": "92%"}
        ]
        return {
            "ranked_products": prods,
            "personalized_advice": f"Based on your profile ({user_profile.get('skin_type', 'sensitive')}), these products optimize active ingredients without irritation."
        }
