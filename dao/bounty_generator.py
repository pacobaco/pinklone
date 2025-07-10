# dao/bounty_generator.py

def generate_bounty(title, repo_name, reward_credits):
    return {
        "title": title,
        "repo": repo_name,
        "reward": reward_credits,
        "status": "open"
    }