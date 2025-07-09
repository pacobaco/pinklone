import streamlit as st
import pandas as pd
from dao.dao_simulation import DAOVoting
from ranking.seo_vector_ranker import rank_repos
import deploy.fork_repo as fr

st.title("🔗 ForkStackDAO Dashboard")

st.markdown("""
Discover high-value MIT-licensed open-source projects, vote on which to fork, and track impact potential.
""")

st.subheader("1. Ranked Open Source Projects")
ranked_df = rank_repos('data/mit_repo_list.csv')
st.dataframe(ranked_df[['name', 'url', 'seo_vector_score']].head(10))

st.subheader("2. DAO Voting Simulation")
dao = DAOVoting()

top_projects = ranked_df['name'].head(5).tolist()
for project in top_projects:
    dao.propose(project)

selected = st.selectbox("Vote for a project to fork:", top_projects)
user = st.text_input("Your username:")
weight = st.slider("Vote weight:", 1, 10, 1)

if st.button("Submit Vote"):
    dao.vote(user, selected, weight)
    st.success(f"Vote recorded for {selected} with weight {weight}")

st.subheader("Voting Results")
results = dao.results()
results_df = pd.DataFrame(results, columns=['Project', 'Votes'])
st.dataframe(results_df)

st.subheader("3. Fork Top Candidate")

if not results_df.empty:
    top_winner = results_df.iloc[0]['Project']
    if st.button(f"Fork '{top_winner}' on GitHub"):
        full_name = ranked_df[ranked_df['name'] == top_winner].iloc[0]['url'].replace("https://github.com/", "")
        forked_url = fr.fork_repo(full_name)
        st.success(f"Forked at: {forked_url}")