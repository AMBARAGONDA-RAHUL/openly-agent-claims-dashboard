import pandas as pd
import numpy as np

# Load data
policies = pd.read_csv('../data/policies.csv')
events = pd.read_csv('../data/disaster_events.csv')

simulations = 1000
results = []

for i in range(simulations):
    simulated_event = events.sample(1).iloc[0]
    severity = simulated_event['severity'] * np.random.uniform(0.8, 1.2)
    affected_policies = policies[policies['region'] == simulated_event['region']].copy()

    if affected_policies.empty:
        continue

    affected_policies['gross_payout'] = affected_policies['policy_value'] * affected_policies['avg_claim_severity'] * 0.25 * severity
    affected_policies['net_payout'] = affected_policies['gross_payout'] * (1 - affected_policies['reinsurance_coverage'])
    total_net = affected_policies['net_payout'].sum()
    solvency_ratio = 300_000_000 / total_net

    results.append({
        'simulation': i+1,
        'event_type': simulated_event['event_type'],
        'region': simulated_event['region'],
        'total_net_payout': total_net,
        'solvency_ratio': solvency_ratio
    })

monte_carlo_df = pd.DataFrame(results)
monte_carlo_df.to_csv('../data/monte_carlo_summary.csv', index=False)
print("Monte Carlo simulation saved to data/monte_carlo_summary.csv")
