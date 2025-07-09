from github import Github
import csv
import os

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

