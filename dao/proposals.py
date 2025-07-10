# dao/proposals.py

import json
import os

PROPOSALS_FILE = "data/proposals.json"

def load_proposals():
    if not os.path.exists(PROPOSALS_FILE):
        return []
    with open(PROPOSALS_FILE, "r") as f:
        return json.load(f)

def save_proposal(proposal):
    proposals = load_proposals()
    proposals.append(proposal)
    with open(PROPOSALS_FILE, "w") as f:
        json.dump(proposals, f, indent=2)