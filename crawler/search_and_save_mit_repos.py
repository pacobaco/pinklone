from github import Github
import pandas as pd
import time

def search_mit_repos(token, max_pages=3, save_path="data/mit_repo_list.csv"):
    """
    Search GitHub for MIT-licensed repos with at least 10 stars,
    and save to CSV for Pinklone.
    """

    g = Github(token)
    query = 'license:mit stars:>10 archived:false'
    results = []

    for page in range(1, max_pages + 1):
        try:
            repos = g.search_repositories(query=query, sort="stars", order="desc").get_page(page - 1)
        except Exception as e:
            print(f"Search error: {e}")
            break

        for repo in repos:
            try:
                if repo.description and len(repo.description) > 10:
                    results.append({
                        "name": repo.full_name,
                        "description": repo.description,
                        "url": repo.html_url,
                        "stars": repo.stargazers_count,
                        "updated": repo.updated_at.date().isoformat()
                    })
            except Exception as e:
                print(f"Skip repo {repo.full_name}: {e}")
                continue

        time.sleep(1)  # avoid hitting rate limits

    df = pd.DataFrame(results)
    df.to_csv(save_path, index=False)
    return df