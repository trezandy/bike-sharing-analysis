import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load data
day_df = pd.read_csv('day.csv')

# Preprocessing
day_df['dteday'] = pd.to_datetime(day_df['dteday'])

# Title and description
st.title("Bike Sharing Analysis Dashboard")
st.markdown("""
This dashboard provides insights into bike sharing data based on weather conditions, weekdays, and user patterns.
""")

# Step 1: Display Dataset Info
st.header("Data Overview")
st.write("### First 5 Rows of the Dataset")
st.dataframe(day_df.head())
st.write("### Dataset Info")
st.write(day_df.info())

# Step 2: Visualize Outliers and Data Distribution
st.header("Data Cleaning")
st.write("Pemeriksaan Outlier pada Kolom Numerik")
numeric_columns = ['temp', 'hum', 'windspeed', 'casual', 'registered', 'cnt']

# Boxplot before cleaning
fig, ax = plt.subplots(figsize=(14, 6))
sns.boxplot(data=day_df[numeric_columns], palette='Set3', ax=ax)
ax.set_title('Pemeriksaan Outlier pada Kolom Numerik')
ax.grid(True)
st.pyplot(fig)

# Step 3: Distribution Analysis
st.header("Data Distribution")
st.write("### Distribusi Temperatur")
fig, ax = plt.subplots(figsize=(14, 6))
sns.histplot(data=day_df, x='temp', bins=20, kde=True, color='blue', alpha=0.7, ax=ax)
ax.set_title('Distribusi Temperatur')
ax.set_xlabel('Temperatur (Normalized)')
ax.set_ylabel('Frekuensi')
ax.grid(True)
st.pyplot(fig)

st.write("### Distribusi Kelembaban")
fig, ax = plt.subplots(figsize=(14, 6))
sns.histplot(data=day_df, x='hum', bins=20, kde=True, color='green', alpha=0.7, ax=ax)
ax.set_title('Distribusi Kelembaban')
ax.set_xlabel('Kelembaban (Normalized)')
ax.set_ylabel('Frekuensi')
ax.grid(True)
st.pyplot(fig)

# Step 4: Correlation Heatmap
st.header("Correlation Analysis")
fig, ax = plt.subplots(figsize=(10, 6))
correlation_matrix = day_df[numeric_columns].corr()
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', center=0, ax=ax)
ax.set_title('Heatmap Korelasi Variabel Numerik')
st.pyplot(fig)

# Step 5: Impact of Weather on Bike Usage
st.header("Pengaruh Cuaca terhadap Penggunaan Sepeda")
fig, ax = plt.subplots(figsize=(14, 6))
sns.scatterplot(data=day_df, x='temp', y='cnt', hue='weathersit', palette='coolwarm', s=100, ax=ax)
ax.set_title('Pengaruh Temperatur terhadap Penggunaan Sepeda Berdasarkan Kondisi Cuaca')
ax.set_xlabel('Temperatur (Normalized)')
ax.set_ylabel('Jumlah Pengguna Sepeda (cnt)')
ax.grid(True)
st.pyplot(fig)

# Step 6: Bike Usage Distribution on Working vs Non-Working Days
st.header("Distribusi Penggunaan Sepeda pada Hari Kerja vs Hari Libur")
fig, ax = plt.subplots(figsize=(14, 6))
sns.boxplot(data=day_df, x='workingday', y='cnt', hue='workingday', palette='Set2', dodge=False, ax=ax)
ax.set_title('Distribusi Penggunaan Sepeda pada Hari Kerja vs Hari Libur')
ax.set_xlabel('Hari Kerja (0: Libur, 1: Kerja)')
ax.set_ylabel('Jumlah Pengguna Sepeda (cnt)')
ax.grid(True)
st.pyplot(fig)

# Conclusion
st.header("Conclusion")
st.markdown("""
- **Pengaruh Cuaca**: Temperatur yang lebih tinggi cenderung meningkatkan penggunaan sepeda, terutama saat kondisi cuaca lebih cerah.
- **Hari Kerja vs Hari Libur**: Penggunaan sepeda lebih tinggi pada hari kerja, kemungkinan karena penggunaan untuk perjalanan rutin seperti ke kantor.
- **Outliers**: Analisis outliers membantu membersihkan data sehingga lebih siap untuk analisis lanjutan.
""")
