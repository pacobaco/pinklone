from github import Github
import os

def fork_repo(repo_full_name, org=None):
    token = os.getenv("GITHUB_TOKEN")
    g = Github(token)
    repo = g.get_repo(repo_full_name)

    if org:
        org_obj = g.get_organization(org)
        fork = org_obj.create_fork(repo)
    else:
        fork = repo.create_fork()

    return fork.html_url

def fork_repo(full_name, token):
    g = Github(token)
    repo = g.get_repo(full_name)
    return repo.create_fork()

def update_readme_with_dao(repo, dao_link):
    contents = repo.get_readme()
    readme_text = contents.decoded_content.decode()
    new_text = f"## DAO Governance\nThis repo is governed by DAO proposals at: {dao_link}\n\n" + readme_text
    repo.update_file(contents.path, "Add DAO governance info", new_text, contents.sha)

