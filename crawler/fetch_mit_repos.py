from github import Github
import csv
import os

def fetch_mit_repos_for_user(username, token):
    g = Github(token)
    user = g.get_user(username)
    repos = user.get_repos()

    mit_repos = []
    for repo in repos:
        if repo.license and repo.license.spdx_id == "MIT":
            mit_repos.append({
                "name": repo.name,
                "full_name": repo.full_name,
                "description": repo.description or "",
                "url": repo.html_url,
                "stars": repo.stargazers_count,
                "updated": repo.updated_at.date().isoformat()
            })
    return pd.DataFrame(mit_repos)

def fetch_mit_repos(token, output_path):
    g = Github(token)
    query = 'license:mit stars:>50 fork:true'
    repos = g.search_repositories(query=query)

    with open(output_path, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(['name', 'url', 'stars', 'description'])
        for repo in repos:
            writer.writerow([repo.name, repo.html_url, repo.stargazers_count, repo.description])

if __name__ == '__main__':
    token = os.getenv('GITHUB_TOKEN')
    fetch_mit_repos(token, '../data/mit_repo_list.csv')

