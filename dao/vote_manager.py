import json
import os

VOTE_PATH = "data/votes.json"

def load_votes():
    if os.path.exists(VOTE_PATH):
        with open(VOTE_PATH, "r") as f:
            return json.load(f)
    return {}

def save_vote(repo_id, voter):
    votes = load_votes()
    votes.setdefault(repo_id, set()).add(voter)
    with open(VOTE_PATH, "w") as f:
        json.dump({k: list(v) for k, v in votes.items()}, f)

def count_votes(repo_id):
    votes = load_votes()
    return len(votes.get(repo_id, []))