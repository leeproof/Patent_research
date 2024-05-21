import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Load the CSV file
csv_file_path = 'filing_dates.csv'
df = pd.read_csv(csv_file_path)

# Extract the year from the filing dates
df['Filing Dates'] = pd.to_datetime(df['Filing Dates'], errors='coerce')
df['Year'] = df['Filing Dates'].dt.year

# Count the number of applications per year
applications_per_year = df['Year'].value_counts().sort_index()

# Create a line chart
# st.title('Num of Patent Applications by Year')

plt.figure(figsize=(10, 6))
plt.plot(applications_per_year.index, applications_per_year.values, marker='o')
plt.xlabel('Year')
plt.ylabel('Number of Applications')
plt.title('Number of Patent Applications by Year')
plt.grid(True)

# Display the line chart in Streamlit
st.pyplot(plt)