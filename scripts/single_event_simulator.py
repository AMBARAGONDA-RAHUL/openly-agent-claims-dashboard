# Openly Real-Time Catastrophe Impact Simulator - Single Event
import pandas as pd

# Load data
policies = pd.read_csv('../data/policies.csv')
agents = pd.read_csv('../data/agents.csv')
events = pd.read_csv('../data/disaster_events.csv')

# Select first event
event = events.iloc[0]
print(f"Simulating Event: {event['event_type']} in {event['region']} (Severity: {event['severity']})\n")

# Filter policies
affected_policies = policies[policies['region'] == event['region']].copy()

# Calculate payouts
severity_factor = 0.25 * event['severity']
affected_policies['gross_payout'] = affected_policies['policy_value'] * affected_policies['avg_claim_severity'] * severity_factor
affected_policies['net_payout'] = affected_policies['gross_payout'] * (1 - affected_policies['reinsurance_coverage'])

# Totals
total_gross = affected_policies['gross_payout'].sum()
total_net = affected_policies['net_payout'].sum()
reserves = 300_000_000
solvency_ratio = reserves / total_net

# Output
print(f"Total Policies Impacted: {len(affected_policies)}")
print(f"Total Gross Payout: ${total_gross:,.0f}")
print(f"Total Net Payout: ${total_net:,.0f}")
print(f"Solvency Ratio: {solvency_ratio:.2f}")

# Save results
affected_policies.to_csv('../data/output_catastrophe.csv', index=False)
