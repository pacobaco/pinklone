# agents/repo_recommender.py

def recommend_next_repo(repo_data):
    top_repo = repo_data.sort_values("score", ascending=False).iloc[0]
    return (
        f"🎯 Recommended fork target: **{top_repo['name']}**\n"
        f"📌 Reason: Highest SEO + social impact score ({top_repo['score']})"
    )
