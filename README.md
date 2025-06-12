🛍️ Customer Segmentation using K-Means Clustering
📌 Overview
This project uses unsupervised learning techniques to segment customers based on demographic and behavioral traits. By applying K-Means Clustering, we can group customers into distinct segments such as high spenders, young shoppers, and budget-conscious customers. These insights can help businesses tailor marketing strategies, personalize offers, and improve customer retention.

🔍 Dataset
Source: Kaggle - Mall Customer Segmentation Dataset

Description: The dataset contains information on customer Gender, Age, Annual Income, and Spending Score (1–100) assigned by the shopping mall based on customer behavior.

💻 Tools & Libraries
Python

Pandas, NumPy

Scikit-learn (KMeans, PCA, preprocessing)

Matplotlib, Seaborn (visualization)

✅ Approach Used
Loaded and explored customer data (gender, age, income, spending score).

Preprocessed the data:

Converted categorical variables (e.g., gender) to numeric.

Scaled features using StandardScaler.

Applied the Elbow Method to determine the optimal number of clusters (chose 5).

Trained a K-Means Clustering model to group customers.

Reduced dimensionality using PCA (Principal Component Analysis) to visualize clusters in 2D.

Analyzed average values within each cluster to define customer personas.

⚠️ Challenges Faced
Choosing the correct number of clusters.

Visualizing multi-dimensional data effectively.

Interpreting the characteristics and business meaning of each cluster.

📈 Model Performance & Potential Improvements
Successfully grouped customers into meaningful segments.

Identified distinct customer types like:

High-income high spenders

Young shoppers with moderate spending

Low-income customers with high spending scores

Future improvements:

Explore other clustering techniques like DBSCAN or hierarchical clustering.

Evaluate clusters using Silhouette Score.

Use additional customer features (e.g., purchase history).

Improve visuals using interactive plots (e.g., Plotly).

![image](https://github.com/user-attachments/assets/6f5cf210-e0b4-454a-8ed0-18ca8c5d6802)
![image](https://github.com/user-attachments/assets/df745f6a-fe4c-469b-b54e-4a70df789779)
![image](https://github.com/user-attachments/assets/dbf5543b-21ff-42c2-811f-4a1f07ac405d)
![image](https://github.com/user-attachments/assets/e91e1f30-44e7-4959-8cd9-fc3f69fb64d0)
![image](https://github.com/user-attachments/assets/b0708122-1c64-4567-a70d-4bd2827bb849)
![image](https://github.com/user-attachments/assets/0aaf9052-d00e-4bdb-96da-cb840d251eab)

