import pandas as pd

# Load data
policies = pd.read_csv('../data/policies.csv')
agents = pd.read_csv('../data/agents.csv')
events = pd.read_csv('../data/disaster_events.csv')

multi_event_summary = []

for _, event in events.iterrows():
    affected_policies = policies[policies['region'] == event['region']].copy()
    if affected_policies.empty:
        continue

    severity_factor = 0.25 * event['severity']
    affected_policies['gross_payout'] = affected_policies['policy_value'] * affected_policies['avg_claim_severity'] * severity_factor
    affected_policies['net_payout'] = affected_policies['gross_payout'] * (1 - affected_policies['reinsurance_coverage'])

    merged = affected_policies.merge(agents, on='agent_id', how='left')

    agent_summary = merged.groupby('agent_id').agg({
        'policy_id': 'count',
        'performance_score': 'mean'
    }).reset_index().rename(columns={'policy_id': 'policies_affected',
                                     'performance_score': 'avg_performance_score'})

    agent_summary['event_type'] = event['event_type']
    agent_summary['region'] = event['region']
    agent_summary['total_gross_payout'] = merged['gross_payout'].sum()
    agent_summary['total_net_payout'] = merged['net_payout'].sum()
    agent_summary['solvency_ratio'] = 300_000_000 / agent_summary['total_net_payout']

    multi_event_summary.append(agent_summary)

multi_event_df = pd.concat(multi_event_summary, ignore_index=True)
multi_event_df.to_csv('../data/multi_event_summary.csv', index=False)
print("Multi-event summary saved to data/multi_event_summary.csv")
