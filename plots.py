import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

graphql_df = pd.read_csv('data/most_popular_repos_graphql.csv', delimiter=';')
rest_df = pd.read_csv('data/most_popular_repos_rest.csv', delimiter=';')

sns.set(style="whitegrid")

plt.rc('axes', titlesize=18, labelsize=14)
plt.rc('legend', fontsize=18)
plt.rc('xtick', labelsize=18)
plt.rc('ytick', labelsize=18)

plt.figure(figsize=(7, 6))
sns.histplot(graphql_df['Response Time'], bins=20, kde=True, color='blue', label='GraphQL')
plt.xlabel('Response Time (s)')
plt.ylabel('Frequency')
plt.title('Histogram of Response Time (GraphQL)', fontweight='bold')
plt.legend()
plt.show()

plt.figure(figsize=(7, 6))
sns.histplot(rest_df['Response Time'], bins=20, kde=True, color='orange', label='REST')
plt.xlabel('Response Time (s)')
plt.ylabel('Frequency')
plt.title('Histogram of Response Time (REST)', fontweight='bold')
plt.legend()
plt.show()

total_response_size_graphql = graphql_df['Response Size'].sum()
total_response_size_rest = rest_df['Response Size'].sum()

plt.figure(figsize=(8, 6))
bar_plot = sns.barplot(x=['GraphQL', 'REST'], y=[total_response_size_graphql, total_response_size_rest], palette=['blue', 'orange'])
plt.xlabel('API Type')
plt.ylabel('Total Response Size (bytes)')
plt.title('Total Response Size Comparison', fontweight='bold')

for index, value in enumerate([total_response_size_graphql, total_response_size_rest]):
    plt.text(index, value, f'{value:.2f}', ha='center', va='bottom', fontweight='bold', fontsize=14)

plt.show()



