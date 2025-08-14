🏦 Openly Real-Time Catastrophe Impact Simulator
This open-source repository delivers a professional-grade analytics platform for insurance financial risk, catastrophe planning, and capital adequacy—the foundation of financial stability and regulatory compliance for any fast-growing, agent-led insurer. Designed in alignment with Openly’s mission and risk challenges, this framework provides transparent, reproducible catastrophe impact simulations, risk dashboards, and solvency analysis, with a strategic extension for agent-level exposure and business growth analytics.

🚀 Core Mission
Real-time catastrophe risk modeling comes first.
This platform empowers Openly’s Finance and Risk teams to simulate loss scenarios, benchmark regional exposures, stress-test capital, and monitor solvency KPIs with confidence—supporting both regulatory compliance and strategic financial planning.

Business and agent analytics are value-added:
By integrating agent-level exposure, policy risk concentrations, and claims delay prediction, this solution also helps Openly accelerate operational decision-making, improve forecasting, and scale with integrity.

📊 Core Features
Financial Risk & Catastrophe Modeling
- Catastrophe Simulation: Estimate gross/net claims payouts by region and severity—auditable, reproducible, and regulatory-ready.
- Risk Benchmarking: Dashboards for solvency ratios, regional risk heatmaps, and emerging exposure detection.
- Capital Adequacy & Stress Testing: Scenario analysis and Monte Carlo simulation for extreme events, BCAR/S&P ERM support, and “what-if” projections.

Business & Agent Analytics
- Agent Exposure Analysis: Track portfolio concentration, identify high-risk regions, and optimize agent allocation.
- Claims Delay Prediction: Predict policies likely to face delayed settlements to improve cash flow and service efficiency.
- What-If Scenario Planning: Adjust event severity, policy coverage, or reinsurance to assess financial impact.

🛠 Tech Stack
- Power BI – Interactive, executive-level dashboards for catastrophe, risk, and agent analytics.
- Python (Pandas, NumPy, scikit-learn) – Data cleaning, modeling, and predictive analytics.
- Jupyter Notebook – Reproducible, transparent workflows.
- CSV/Excel – Realistic mock agent, policy, and disaster datasets for portfolio demonstration.
- Matplotlib/Seaborn – Data visualization and reporting.

📂 Repository Structure
openly-catastrophe-simulator/
│
├── data/
│   ├── policies.csv                  # Policy and exposure data
│   ├── agents.csv                    # Agent onboarding and performance data
│   ├── disaster_events.csv           # Simulated catastrophe events
│   └── data_dictionary.md            # Field-by-field documentation
│
├── notebooks/
│   └── catastrophe_simulator.ipynb   # Real-time simulation of catastrophe impact
│
├── dashboard/
│   ├── catastrophe_dashboard.pbix    # Power BI dashboard
│   ├── screenshots/                  # Dashboard previews
│   └── dashboard_export.pdf          # Exported dashboard for PDF review
│
├── docs/
│   ├── Executive_Summary.md          # Business impact & recommendations
│   └── demo_video_link.txt           # Link to your demo video walkthrough
│
├── requirements.txt                  # Python dependencies
├── LICENSE                           # Project license
└── README.md                         # This file

🚀 How to Run

**Explore the Data**
All datasets are in /data/. See `data_dictionary.md` for field-by-field documentation.

**Run Python Analytics**
Clone this repo, install dependencies, then launch Jupyter:

```bash
pip install -r requirements.txt
jupyter notebook notebooks/catastrophe_simulator.ipynb
````

Open the notebook to simulate catastrophe events, compute gross/net payouts, and analyze reserve adequacy.

**View Dashboards**
Install Power BI Desktop.
Open `/dashboard/catastrophe_dashboard.pbix` for interactive exploration.
View `/dashboard/dashboard_export.pdf` or screenshots for a quick overview.

**Review Documentation**

* Executive Summary: See `/docs/Executive_Summary.md` for business context and recommendations.
* Video Walkthrough: Follow the link in `/docs/demo_video_link.txt` for a guided tour of the project.

🛠️ Disclaimer
This project uses simulated and public datasets for demonstration. All numbers and scenarios are illustrative.


