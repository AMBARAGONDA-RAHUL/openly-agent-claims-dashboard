# Openly Risk & Claims Analytics Framework

## 📌 Project Overview
This repository is a **data-driven demonstration** of how Openly could enhance its **financial risk analysis**, **loss reserving**, and **claims efficiency** through modern analytics, predictive modeling, and interactive dashboards.

The project is directly inspired by Openly’s **Financial (Risk) Analyst** role and addresses key responsibilities outlined in the job description:
- Loss reserving analysis and modeling
- Risk horizon tracking and benchmarking
- Predictive analytics for claim delays
- Stochastic modeling for capital and liquidity planning
- Support for BCAR and S&P ERM accreditation

---

## 🚩 Key Business Challenges Addressed

1. **Accurate Loss Reserving**  
   Without precise reserve estimates, insurers risk under- or over-reserving, impacting profitability and solvency metrics.

2. **Emerging Risk Identification**  
   Market conditions, catastrophe exposure, or regional claim trends may not be detected early enough to act.

3. **Claims Delay Management**  
   Delayed claims settlements can damage customer satisfaction, affect liquidity, and trigger regulatory or ratings risk.

4. **Capital Adequacy Stress Testing**  
   Fluctuations in claims severity or frequency can impact BCAR and ERM ratings if not modeled and planned for proactively.

---

## 💡 Why This Matters to Openly
As an **agent-first, tech-enabled** insurer, Openly thrives when it can:
- Provide **fast, fair claims** while preserving capital adequacy  
- Detect and mitigate **emerging risks early**  
- Build a **risk-aware culture** supported by actionable analytics  

This framework demonstrates exactly how Openly could operationalize these principles using **Python**, **Power BI**, and **data science best practices**.

---

## 🛠 Tech Stack

- **Power BI** – Interactive, visual analytics dashboards for financial and claims KPIs  
- **Python (Pandas, NumPy, scikit-learn)** – Data cleaning, modeling, and Monte Carlo simulations  
- **Matplotlib / Seaborn** – Data visualizations  
- **Jupyter Notebook** – Reproducible workflows  
- **Mock/Public Data** – Simulated data for agents, claims, and loss triangles  

---

## 📊 Core Features

### 1. Loss Reserving Model  
- Uses **Chain-Ladder** method on mock loss triangle data  
- Estimates Incurred But Not Reported (IBNR) reserves  
- Produces reserve adequacy KPIs for dashboard display  

### 2. Risk Horizon Dashboard  
- Interactive Power BI dashboard visualizing:  
  - Loss ratio trends by region/product line  
  - Geographic and product risk heatmaps  
  - Key solvency and liquidity ratios  

### 3. Claims Delay Prediction  
- **Random Forest Classifier** predicts claims likely to be delayed or escalated  
- Features include claim type, amount, agent performance, and region risk factors  
- Output integrated into risk dashboard as red/yellow/green flags  

### 4. Capital Adequacy Stress Test  
- Monte Carlo simulation of catastrophe loss scenarios  
- Shows effect on solvency ratios & mock BCAR score  
- Allows “what-if” exploration for strategic planning  

---

## 📂 Repository Structure

```
openly-risk-analytics-framework/
│
├── data/
│   ├── agents.csv
│   ├── claims.csv
│   ├── loss_triangle.csv
│   └── data_dictionary.md
│
├── notebooks/
│   ├── claims_delay_model.ipynb
│   ├── loss_reserving_simulation.ipynb
│   └── capital_stress_test.ipynb
│
├── dashboard/
│   ├── openly_risk_dashboard.pbix
│   ├── screenshots/
│   └── dashboard_export.pdf
│
├── docs/
│   ├── Executive_Summary.pdf
│   └── demo_video_link.txt
│
├── requirements.txt
├── README.md
└── LICENSE
```

---

## 🚀 How to Run

### 1️⃣ View Dashboards
- Install **[Power BI Desktop](https://powerbi.microsoft.com/desktop/)**  
- Open `dashboard/openly_risk_dashboard.pbix`  
- Or view exported PDF in `/dashboard/screenshots/`

### 2️⃣ Run Python Models
```
pip install -r requirements.txt
jupyter notebook notebooks/claims_delay_model.ipynb
jupyter notebook notebooks/loss_reserving_simulation.ipynb
jupyter notebook notebooks/capital_stress_test.ipynb
```

### 3️⃣ Explore Data
- All mock/public datasets are in `/data/` with a `data_dictionary.md` explaining each field.

---

## 📈 Potential Extensions
- Integrate with **Openly’s live data pipelines** for daily insights  
- Expand to **multi-line insurance portfolios**  
- Add **agent behavior and customer sentiment analysis**  
- Automate KPI email reports to stakeholders  

---

## 📞 Contact
**Rahul Ambaragonda**  
🔗 [LinkedIn](https://www.linkedin.com/in/rahul-ambaragonda)  
📧 rahul.analytics0@gmail.com  

---

> ⚠ **Disclaimer:** This is a demonstration project using simulated and public datasets.  
> All numbers and scenarios are illustrative only.
