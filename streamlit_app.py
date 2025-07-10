import streamlit as st
import os
from dao.vote_manager import save_vote, count_votes
import uuid
import pandas as pd
from dao.dao_simulation import DAOVoting
from ranking.seo_vector_ranker import rank_repos
import deploy.fork_repo as fr
import streamlit as st
from crawler.fetch_mit_repos import fetch_mit_repos_for_user
from ranking.seo_vector_ranker import rank_repos_from_df
from deploy.fork_repo import fork_repo

st.title("🧬 Pinklone: Fork-to-Impact Engine")
token = st.secrets.get("GITHUB_TOKEN")

username = st.text_input("GitHub Username", placeholder="e.g. pacobaco")

if st.button("Search and Rank"):
    if not token:
        st.error("Add GITHUB_TOKEN in Streamlit Secrets.")
        st.stop()

    df = fetch_mit_repos_for_user(username, token)
    if df.empty:
        st.warning("No MIT repos found.")
    else:
        ranked = rank_repos_from_df(df)
        st.success(f"Ranked {len(ranked)} repos.")
        for i, row in ranked.iterrows():
            st.markdown(f"### {row['name']} ({row['stars']}⭐)")
            st.markdown(row['description'])
            st.markdown(f"[🔗 Repo Link]({row['url']})")
            if st.button(f"Fork {row['name']}", key=f"fork_{i}"):
                try:
                    fork_repo(row['full_name'], token)
                    st.success("✅ Forked!")
                except Exception as e:
                    st.error(f"❌ Fork failed: {e}")



#import streamlit as st

# Load token into environment
os.environ["GITHUB_TOKEN"] = st.secrets["GITHUB_TOKEN"]

st.markdown("""
Discover high-value MIT-licensed open-source projects, vote on which to fork, and track impact potential.
""")

from crawler.search_and_save_mit_repos import search_mit_repos

st.subheader("🌐 Search & Populate MIT Repo List")

if st.button("Search Top Repos"):
    with st.spinner("Searching GitHub..."):
        token = st.secrets["GITHUB_TOKEN"]
        df = search_mit_repos(token, max_pages=3)  # You can increase to 10+

        if df is not None and not df.empty:
            st.success(f"🎉 Found {len(df)} high-quality MIT repos.")
            st.dataframe(df)
        else:
            st.warning("No qualifying repos found.")

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
        


for i, row in ranked.iterrows():
    repo_id = str(uuid.uuid5(uuid.NAMESPACE_URL, row['url']))

    st.markdown(f"### {row['name']} ({row['stars']}⭐)")
    st.markdown(f"{row['description']}")
    st.markdown(f"[🔗 Repo]({row['url']})")

    col1, col2 = st.columns([2,1])
    with col1:
        if st.button("✅ Vote to Adopt", key=f"vote_{i}"):
            voter = st.session_state.get("user", f"anon-{i}")
            save_vote(repo_id, voter)
            st.success("🗳️ Vote recorded.")

    with col2:
        st.markdown(f"🗳️ Votes: **{count_votes(repo_id)}**")