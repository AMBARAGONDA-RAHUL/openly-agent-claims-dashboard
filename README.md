# 🏦 Openly Financial Risk & Reserving Analytics Framework

This open-source repository delivers a **professional-grade analytics platform for insurance financial risk, reserving, and capital planning**—the foundation of financial stability and regulatory compliance for any fast-growing, agent-led insurer. Designed in collaboration with Openly’s values and business challenges, this framework provides transparent, reproducible reserving models, risk dashboards, and capital stress testing, with a strategic extension for agent performance and business growth analytics.

---

## 🚀 Core Mission

**Financial risk and reserving analytics come first.**  
This platform empowers Openly’s Finance and Risk teams to **model loss reserves, benchmark and stress-test capital, and monitor solvency KPIs with confidence**—required for both day-to-day operations and regulatory accreditation.

**Business and agent analytics are value-added:**  
By integrating agent onboarding funnels, claims efficiency tracking, and growth insights, this solution also helps Openly accelerate agent productivity, improve forecasting, and scale with integrity.

---

## 📊 Core Features

### **Financial Risk & Reserving**
- **Loss Reserving**: Chain-ladder and IBNR modeling—auditable, reproducible, and ready for regulatory review.
- **Risk Benchmarking**: Real-time dashboards for solvency ratios, regional/product risk heatmaps, and emerging risk detection.
- **Capital Adequacy & Stress Testing**: Monte Carlo simulation for catastrophe planning, BCAR/S&P ERM support, and “what-if” scenario analysis.

### **Business & Agent Analytics**
- **Agent Onboarding Funnel**: Track time from signup to first quote, first policy, and early conversion—identify bottlenecks and accelerate agent ramp-up.
- **Retention & Cohort Benchmarking**: Compare new vs. veteran agent performance, flag retention risks, and empower data-driven talent investment.
- **Claims Efficiency**: Predict and flag claims likely to be delayed, improving service speed and cash flow.

---

## 🛠 Tech Stack

- **Power BI** – Interactive, executive-level dashboards for risk, reserving, and agent analytics.
- **Python (Pandas, NumPy, scikit-learn, statsmodels)** – Data cleaning, modeling, and predictive analytics.
- **Jupyter Notebook** – Reproducible, transparent workflows.
- **CSV/Excel** – Realistic mock agent, claims, and reserving datasets for portfolio demonstration.
- **Matplotlib/Seaborn** – Data visualization and reporting.

---

## 📂 Repository Structure

```
openly-risk-analytics/
│
├── data/
│   ├── agents.csv                # Agent onboarding and performance milestones
│   ├── claims.csv                # Claims lifecycle and delay risk
│   ├── loss_triangle.csv         # Actuarial reserving (loss development)
│   └── data_dictionary.md        # Field-by-field documentation
│
├── notebooks/
│   ├── reserving_simulation.ipynb  # Chain-ladder reserving & IBNR
│   ├── risk_benchmarking.ipynb     # Solvency, liquidity, heatmaps
│   ├── capital_stress_test.ipynb   # Monte Carlo stress scenarios
│   ├── agent_onboarding.ipynb      # Funnel, retention, cohort analysis
│   └── claims_delay_prediction.ipynb  # ML for delay risk
│
├── dashboard/
│   ├── openly_analytics.pbix         # Power BI dashboard
│   ├── screenshots/                  # Dashboard previews
│   └── dashboard_export.pdf          # Exported dashboard (for PDF review)
│
├── docs/
│   ├── Executive_Summary.md          # Business impact & recommendations
│   └── demo_video_link.txt           # Link to your video walkthrough
│
├── requirements.txt                  # Python dependencies
├── LICENSE                           # Project license
└── README.md                         # This file
```

---

## 🚀 How to Run

### **Explore the Data**
All datasets are in `/data/`. See `data_dictionary.md` for field-by-field documentation.

### **Run Python Analytics**
Clone this repo, install dependencies, then launch Jupyter:
```
pip install -r requirements.txt
jupyter notebook notebooks/
```
Open notebooks for reserving, risk, capital stress, agent, and claims analytics.

### **View Dashboards**
- Install [Power BI Desktop](https://powerbi.microsoft.com/desktop/).
- Open `/dashboard/openly_analytics.pbix` for interactive exploration.
- View `/dashboard/dashboard_export.pdf` or screenshots for a quick overview.

### **Review Documentation**
- **Executive Summary:** See `/docs/Executive_Summary.md` for business context and recommendations.
- **Video Walkthrough:** Follow the link in `/docs/demo_video_link.txt` for a guided tour of the project.

---

## 📈 Further Steps

- **Integrate with Openly’s live data**: Replace mock CSVs with direct database or API connections for real-time analytics.
- **Expand to new products/regions**: Adapt data schema and dashboards for commercial, auto, or multi-state portfolios.
- **Automate reporting**: Schedule email/Slack alerts for emerging risks, onboarding delays, or reserve triggers.
- **Add customer/agent sentiment**: Incorporate survey or support ticket data for a 360° view of risk and growth.

---

## 🛠️ Disclaimer

This project uses **simulated and public datasets** for demonstration. All numbers and scenarios are illustrative.

---

