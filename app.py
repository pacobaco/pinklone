import os
from crawler.fetch_mit_repos import fetch_mit_repos
from ranking.seo_vector_ranker import rank_repos
from dao.dao_simulation import DAOVoting

if __name__ == '__main__':
    print("--- ForkStackDAO Pipeline Start ---")
    token = os.getenv('GITHUB_TOKEN')
    csv_path = 'data/mit_repo_list.csv'

    print("Fetching repos...")
    fetch_mit_repos(token, csv_path)

    print("Ranking repos...")
    ranked_df = rank_repos(csv_path)
    top_repo = ranked_df.iloc[0]['name']
    print(f"Top candidate: {top_repo}")

    print("Simulating DAO vote...")
    dao = DAOVoting()
    dao.propose(top_repo)
    dao.vote('user1', top_repo, 5)
    print(dao.results())