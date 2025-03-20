import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

df = pd.read_csv('res_dpre.csv')
features=['Age', 'Quality of Sleep',  'Physical Activity Level','Heart Rate', 'Daily Steps',
        'Systolic', 'Diastolic', 'Gender_Female',
       'Gender_Male', 'Occupation_Accountant', 'Occupation_Doctor',
       'Occupation_Engineer', 'Occupation_Lawyer', 'Occupation_Nurse',
       'Occupation_Sales Representative', 'Occupation_Salesperson',
       'Occupation_Scientist', 'Occupation_Software Engineer',
       'Occupation_Teacher', 'predicted_sleep_disorder']
df_selected = df[features].dropna()  

#
scaler = StandardScaler()
scaled_features = scaler.fit_transform(df_selected)


kmeans = KMeans(n_clusters=3, random_state=42, n_init=10)
df_selected['Cluster'] = kmeans.fit_predict(scaled_features)
print(df_selected['Cluster'] )

# Visualize the clusters
plt.figure(figsize=(5, 6))
plt.scatter(df_selected['Age'], df_selected['Physical Activity Level'], c=df_selected['Cluster'], cmap='viridis')
plt.xlabel('Age')
plt.ylabel('Physical Activity Level')
plt.title('Clusters Visualization')
plt.colorbar(label='Cluster')
plt.savefig('vis2.png', dpi=300, bbox_inches='tight')
plt.show()

cluster_counts = df_selected['Cluster'].value_counts()
with open('k.txt', 'w') as f:
    for cluster, count in cluster_counts.items():
        f.write(f'Cluster {cluster}: {count} records\n')
