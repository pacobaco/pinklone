# premium/tier_manager.py

import json
import os

CREDIT_FILE = "data/user_credits.json"

def load_credits():
    if not os.path.exists(CREDIT_FILE):
        return {}
    with open(CREDIT_FILE, "r") as f:
        return json.load(f)

def save_credits(data):
    with open(CREDIT_FILE, "w") as f:
        json.dump(data, f, indent=2)

def get_user_credit(user_id):
    credits = load_credits()
    return credits.get(user_id, 0)

def add_credits(user_id, amount):
    credits = load_credits()
    credits[user_id] = credits.get(user_id, 0) + amount
    save_credits(credits)

def is_premium(user_id):
    return get_user_credit(user_id) >= 100  # Threshold for premium
    
def get_user_tier(user_id):
    credits = get_user_credit(user_id)
    if credits >= 100:
        return "DAO+ Premium"
    elif credits >= 50:
        return "Contributor"
    return "Free Tier"