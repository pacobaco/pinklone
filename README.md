# 🧬 Pinklone

**Pinklone** is a decentralized, DAO-enabled platform that discovers, ranks, and deploys underutilized MIT-licensed GitHub repositories using SEO signals, poverty stack scoring, and community voting. It enables collective decision-making around forking open-source software for social good — especially in low-resource contexts.

---

## 🚀 Features

### ✅ Core Modules
| Feature                        | Free Tier | Premium Tier |
|-------------------------------|-----------|---------------|
| 🔍 Search by GitHub username  | ✅        | ✅            |
| 📈 SEO Vector Ranker          | ✅        | ✅            |
| 🗳 DAO Voting System           | Mock DAO  | Snapshot-integrated w/ wallet |
| 💼 Freelancer-Ready Filter     | ✅        | ✅            |
| 🌍 Poverty Stack Index         | ✅        | ✅            |
| 🧾 Fork and Deploy Button      | GitHub only | + Auto deploy to Streamlit/HF |
| 🧠 Bounty Engine               | View only | Submit + earn credits |
| 🌐 IPFS Metadata Storage       | ❌        | ✅            |
| 🤖 Telegram Bot Interface      | Read-only | Write-enabled (vote/fork) |
| 📊 DAO Dashboard               | ✅        | ✅            |
| 🧬 Fork Graph Viewer           | ✅        | ✅            |
| 🧩 AI Explainers for Repos     | ❌        | ✅ (GPT-powered summaries) |
| 🏦 DAO Credits → Token Bridge | ❌        | ✅            |

---

## 💸 Monetization & Premium Tiers

Pinklone offers a freemium model with optional **DAO+ Tier** for serious contributors, communities, or DAO nodes:

### 🔓 Free Tier
- Search, rank, and view metrics
- Vote anonymously
- Simulated fork tools
- Earn limited credits via microtasks

### 🪙 DAO+ Premium Tier (Unlocks)
- Real **Snapshot voting**
- IPFS metadata archive
- **Credit tracking → token mapping**
- Full DAO reputation system
- Telegram bot write access (via key/wallet)
- AI-powered project summarizer
- Export project impact reports

---

## 📁 Project Structure

```bash
pinklone/
├── streamlit_app.py
├── .streamlit/config.toml
├── data/
├── crawler/
├── ranking/
├── deploy/
├── premium/
├── dao/
├── dashboard/
├── graphs/
├── ipfs/
├── reputation/
├── tasks/
├── remixer/
├── agents/
├── social/
├── token/
├── requirements.txt
└── README.md
```

---

## 🛠 Setup Instructions

```bash
git clone https://github.com/pacobaco/pinklone.git
cd pinklone
pip install -r requirements.txt
streamlit run streamlit_app.py
```

Add your `.streamlit/secrets.toml` for API keys and tokens.

---

## 🤝 Contributing

Join the DAO, submit a repo, earn credits, or submit proposals.