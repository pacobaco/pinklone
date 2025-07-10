# social/comments.py

import json
import os

COMMENTS_FILE = "data/comments.json"

def load_comments():
    if not os.path.exists(COMMENTS_FILE):
        return []
    with open(COMMENTS_FILE, "r") as f:
        return json.load(f)

def save_comment(repo_name, user, comment):
    comments = load_comments()
    comments.append({"repo": repo_name, "user": user, "comment": comment})
    with open(COMMENTS_FILE, "w") as f:
        json.dump(comments, f, indent=2)
