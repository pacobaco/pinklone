# streamlit_app.py

import streamlit as st
import pandas as pd
#from premium.upgrade_panel import upgrade_panel
from premium.tier_manager import is_premium, get_user_credit, add_credits
from ranking.seo_vector_ranker import rank_repos
from premium.upgrade_panel import upgrade_panel
#from premium.tier_manager import is_premium, get_user_tier, get_credits, add_credits
from deploy.fork_repo import fork_repo
from dao.proposals import save_proposal, load_proposals
from social.comments import load_comments, save_comment

st.set_page_config(page_title="Pinklone DAO Forker", layout="wide")
st.title("🧬 Pinklone: DAO-powered MIT Repo Discovery")

# Sidebar Account Info
with st.sidebar:
    st.header("👤 Account")
    st.write(f"Tier: `{get_user_tier()}`")
    st.write(f"Credits: `{get_credits()}`")
    if st.button("🎁 Add Demo Credits"):
        add_credits(5)
    upgrade_panel()

# Load Ranked Repos
try:
    ranked_df = rank_repos("data/mit_repo_list.csv")
except Exception as e:
    st.error(f"❌ Failed to load repo list: {e}")
    st.stop()

st.subheader("🏆 Ranked MIT Repos")

for i, row in ranked_df.iterrows():
    with st.expander(f"{i+1}. {row['name']}"):
        st.write(row['description'])
        st.write(f"🌐 [View Repo]({row['url']})")

        # Fork Button (Premium only)
        if is_premium():
            if st.button(f"🚀 Fork {row['name']}", key=f"fork_{i}"):
                fork_repo(row['url'])
                st.success("✅ Repo forked!")
        else:
            st.warning("🔒 Forking requires Premium access.")

        # Comments Section
        st.markdown("**💬 Community Comments**")
        comments = get_comments(row['url'])
        for c in comments:
            st.markdown(f"- 🗣 **{c['user']}**: {c['text']}")
        new_comment = st.text_input("Leave a comment", key=f"comment_{i}")
        if st.button("➕ Add Comment", key=f"btn_{i}"):
            add_comment(row['url'], st.session_state.get("user_id", "anon"), new_comment)

# DAO Proposal Panel
st.markdown("---")
st.header("🏛 Submit a DAO Proposal")

with st.expander("📤 New Proposal"):
    title = st.text_input("Proposal Title")
    desc = st.text_area("Proposal Description")
    if st.button("Submit Proposal"):
        submit_proposal(title, desc, st.session_state.get("user_id", "anon"))
        st.success("✅ Proposal submitted!")

upgrade_panel()
st.subheader("🗳 Current Proposals")
for p in get_proposals():
    st.markdown(f"### 🗳 {p['title']}")
    st.markdown(f"_{p['description']}_ — by `{p['user']}`")