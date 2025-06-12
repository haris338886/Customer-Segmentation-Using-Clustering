import pandas as pd               
import matplotlib.pyplot as plt   
import seaborn as sns            
from sklearn.cluster import KMeans              
from sklearn.preprocessing import StandardScaler 
from sklearn.decomposition import PCA           

df = pd.read_csv('Mall_Customers.csv')

print(df.head())

print(df.info())       
print(df.describe())   

sns.countplot(x='Gender', data=df)
plt.title('Gender Distribution')
plt.show()

sns.histplot(df['Age'], bins=20, kde=True)
plt.title('Age Distribution')
plt.xlabel('Age')
plt.ylabel('Count')
plt.show()

sns.scatterplot(x='Annual Income (k$)', y='Spending Score (1-100)', data=df)
plt.title('Annual Income vs Spending Score')
plt.show()

df['Gender'] = df['Gender'].map({'Male': 0, 'Female': 1})

features = df[['Gender', 'Age', 'Annual Income (k$)', 'Spending Score (1-100)']]

scaler = StandardScaler()
scaled_features = scaler.fit_transform(features)

wcss = []  
for i in range(1, 11):
    kmeans = KMeans(n_clusters=i, random_state=42)
    kmeans.fit(scaled_features)
    wcss.append(kmeans.inertia_)

plt.plot(range(1, 11), wcss, marker='o')
plt.title('Elbow Method - Find the best number of clusters')
plt.xlabel('Number of Clusters (k)')
plt.ylabel('WCSS')
plt.grid(True)
plt.show()

k = 5
kmeans = KMeans(n_clusters=k, random_state=42)
df['Cluster'] = kmeans.fit_predict(scaled_features)

pca = PCA(n_components=2)
pca_features = pca.fit_transform(scaled_features)

df['PCA1'] = pca_features[:, 0]
df['PCA2'] = pca_features[:, 1]

plt.figure(figsize=(10,6))
sns.scatterplot(x='PCA1', y='PCA2', hue='Cluster', palette='Set2', data=df, s=100)
plt.title('Customer Segments (K-Means Clustering)')
plt.show()

cluster_summary = df.groupby('Cluster')[['Gender', 'Age', 'Annual Income (k$)', 'Spending Score (1-100)']].mean()
print("Cluster Summary:")
print(cluster_summary)
