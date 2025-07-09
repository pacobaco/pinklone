class DAOVoting:
    def __init__(self):
        self.proposals = {}
        self.votes = {}

    def propose(self, repo_name):
        self.proposals[repo_name] = 0

    def vote(self, user, repo_name, weight=1):
        if repo_name not in self.proposals:
            print(f"Proposal '{repo_name}' not found.")
            return
        self.proposals[repo_name] += weight
        self.votes.setdefault(user, {})[repo_name] = self.votes[user].get(repo_name, 0) + weight

    def results(self):
        return sorted(self.proposals.items(), key=lambda x: x[1], reverse=True)

if __name__ == '__main__':
    dao = DAOVoting()
    dao.propose('open-edtech-platform')
    dao.vote('alice', 'open-edtech-platform', weight=3)
    dao.vote('bob', 'open-edtech-platform', weight=2)
    print(dao.results())

