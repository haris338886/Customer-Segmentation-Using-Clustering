# 🛍️ Customer Segmentation using K-Means Clustering

## 📌 Overview

This project applies **unsupervised machine learning** to segment customers based on their demographic and behavioral attributes. By using **K-Means Clustering**, customers are grouped into distinct clusters such as **high spenders**, **young shoppers**, and **budget-conscious users**. These insights are valuable for personalized marketing, customer engagement, and business growth.

---

## 🔍 Dataset

- **Source**: [Kaggle - Mall Customer Segmentation Dataset](https://www.kaggle.com/datasets/vjchoudhary7/customer-segmentation-tutorial)
- **Description**: Contains records of customers with fields:
  - `Gender`
  - `Age`
  - `Annual Income (k$)`
  - `Spending Score (1–100)` — a metric assigned by the mall based on customer behavior.

---

## 💻 Tools & Libraries

- **Language**: Python  
- **Libraries**:
  - `Pandas`, `NumPy` – Data processing
  - `Matplotlib`, `Seaborn` – Visualization
  - `Scikit-learn` – KMeans, PCA, preprocessing

---

## ✅ Approach Used

1. **Data Exploration**: Loaded and examined gender, age, income, and spending data.
2. **Preprocessing**:
   - Converted categorical variables (e.g., `Gender`) into numerical values.
   - Scaled numerical features using `StandardScaler`.
3. **Elbow Method**: Used to determine the optimal number of clusters (k = 5).
4. **Clustering**: Applied **K-Means Clustering** to segment customers.
5. **Dimensionality Reduction**: Used **PCA** to visualize clusters in 2D space.
6. **Cluster Analysis**: Interpreted customer groups based on average feature values.

---

## ⚠️ Challenges Faced

- Choosing an appropriate number of clusters.
- Visualizing and interpreting multi-dimensional data in 2D.
- Deriving meaningful business insights from abstract cluster outputs.

---

## 📈 Model Performance & Future Improvements

- **Results**:
  - Identified clear customer groups like:
    - High-income, high spenders
    - Low-income, high spenders
    - Young, moderate spenders

- **Potential Enhancements**:
  - Try alternative clustering techniques (e.g., DBSCAN, Hierarchical Clustering).
  - Use **Silhouette Score** for better cluster validation.
  - Include more behavioral data (purchase frequency, product categories).
  - Create interactive dashboards with **Plotly** or **Power BI**.

---

## 📊 Visualizations

### 🧾 Elbow Method  
![Elbow Method](https://github.com/user-attachments/assets/6f5cf210-e0b4-454a-8ed0-18ca8c5d6802)

### 💡 PCA Clusters (2D Visualization)  
![PCA Clusters](https://github.com/user-attachments/assets/df745f6a-fe4c-469b-b54e-4a70df789779)

### 📌 Cluster Distributions  
![Cluster Distributions](https://github.com/user-attachments/assets/dbf5543b-21ff-42c2-811f-4a1f07ac405d)  
![Cluster Bars](https://github.com/user-attachments/assets/e91e1f30-44e7-4959-8cd9-fc3f69fb64d0)  
![Age vs Spending](https://github.com/user-attachments/assets/b0708122-1c64-4567-a70d-4bd2827bb849)  
![Gender Split](https://github.com/user-attachments/assets/0aaf9052-d00e-4bdb-96da-cb840d251eab)

