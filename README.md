# Openly Agent & Claims Dashboard

## Project Overview

This project addresses key operational challenges faced by Openly, a tech-enabled homeowners insurance provider that works exclusively with independent agents.

### The Problem We’re Solving
- **Agent Friction:** Independent agents often face difficulties in efficiently managing quote-to-policy workflows, impacting sales conversions and customer experience.  
- **Claims Delays:** Slow claims processing causes customer dissatisfaction and damages Openly’s reputation for empathy and urgency.  
- **Lack of Predictive Insights:** Without predictive analytics, it’s hard to proactively identify bottlenecks or high-risk claims before they escalate.

### Why It Matters to Openly
Openly’s unique business model depends on empowering independent agents with better technology and insights. Improving agent performance and claims efficiency will:  
- Enhance agent productivity and retention  
- Accelerate claims resolution and customer satisfaction  
- Support scalable growth across new states and agencies  
- Align with Openly’s values of empathy, transparency, and collaboration

---

## Tech Stack & Components

- **Power BI** – Interactive dashboard visualizing agent performance and claims metrics  
- **Python (Jupyter Notebook)** – Data cleaning, feature engineering, and predictive modeling for claim delay risk  
- **Datasets** – Public and mock data simulating agents, quotes, policies, and claims  
- **Presentation Materials** – Executive summary and demo video walkthrough

---

## How to Run / View the Project

1. **Dashboard:**  
   - Open the Power BI Desktop file (`Agent_Claims_Dashboard.pbix`) with Power BI Desktop (free download from Microsoft).  
   - Alternatively, view screenshots or PDF export in the `/docs` folder.

2. **Predictive Model:**  
   - Run the Jupyter Notebook (`claim_delay_prediction.ipynb`) in any Python environment (Anaconda recommended).  
   - Install dependencies via `pip install -r requirements.txt` (includes pandas, scikit-learn, matplotlib).  
   - The notebook cleans data, trains a Random Forest classifier, and outputs delay risk predictions as CSV.

3. **Data:**  
   - CSV files are located in the `/data` folder with detailed data dictionaries.

4. **Presentation:**  
   - Watch the demo video linked in the README or located in `/docs`.

---

## Next Steps & Extensions

- Integrate Openly’s real agent and claims data for deeper, customized insights.  
- Expand the predictive model with more features and improved accuracy.  
- Build an automated pipeline to refresh dashboards and predictions in real-time.  
- Add a user feedback loop for agents to directly report issues or suggest improvements.  
- Collaborate cross-functionally to embed this tool into Openly’s agent support systems.

---

## Contact

For questions or collaboration, please contact:

**Rahul Ambaragonda**  
[LinkedIn Profile](https://www.linkedin.com/in/rahul-ambaragonda)  
rahul.analytics0@gmail.com

---

*This project is a demonstration of initiative and problem-solving aligned with Openly’s mission and values.*
