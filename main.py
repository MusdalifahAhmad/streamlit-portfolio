import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
from wordcloud import WordCloud
import joblib
import os


st.set_page_config(page_title="Portofolio Musdalifah Ahmad", layout="wide")

# Gaya pastel
sns.set_palette("pastel")
st.markdown("""
    <style>
    .main { background-color: #f8f9fa; }
    h1, h2, h3 { color: #3f3f3f; }
    </style>
""", unsafe_allow_html=True)

# Sidebar Navigasi
st.sidebar.title("📂 Navigasi")
menu = st.sidebar.radio("Pilih Proyek", [
    "Profil",
    "Customer Satisfaction",
    "People Analytics",
    "Churn Analysis",
    "Sales EDA",
    "Regression"
])

# Halaman Profil
if menu == "Profil":
    st.title("👩‍💻 Musdalifah Ahmad")
    st.subheader("Data Analyst | Data-Driven Professional")
    st.markdown("""
    Hai! I am a results-driven professional with over 4 years of experience in Data analysis, Sales, Marketing, and Management. Here are some of my projects:
    - Customer churn and retention analysis
    - Customer satisfaction and sentiment analysis
    - Sales data exploration and visualization
    - Predictive regression for business decision-making

    📧 Email: musdalifahahmad5@gmail.com  
    💼 LinkedIn: [linkedin.com/in/musdalifah](https://linkedin.com/in/musdalifah)
    """)

# CUSTOMER SATISFACTION & SENTIMENT
elif menu == "Customer Satisfaction":
    st.title("📋 Customer Satisfaction & Sentiment Analysis")
    # Placeholder - data loading & visualisasi akan ditambahkan dari notebook
    st.metric("Average CSAT", "4.2")
    st.plotly_chart(px.pie(names=["Positive", "Neutral", "Negative"], values=[60, 25, 15],
                           color_discrete_sequence=px.colors.qualitative.Pastel))
    st.plotly_chart(px.bar(x=["Freshdesk", "Jira", "ServiceNow"], y=[120, 80, 60],
                           labels={'x': 'Platform', 'y': 'Jumlah Ulasan'},
                           color_discrete_sequence=px.colors.qualitative.Pastel))
    wordcloud = WordCloud(background_color='white', colormap='Pastel1').generate("pelayanan cepat mudah nyaman responsif")
    fig, ax = plt.subplots()
    ax.imshow(wordcloud, interpolation='bilinear')
    ax.axis("off")
    st.pyplot(fig)
    st.markdown("**Conclusion:** The majority of customers are satisfied with the ticketing system, but some platforms require improvement in customer service features.")

# PEOPLE ANALYTICS
elif menu == "People Analytics":
    st.title("👥 People Analytics")
    st.plotly_chart(px.histogram(x=["20-29", "30-39", "40-49"], y=[3.5, 4.0, 3.2],
                                 labels={'x': 'Usia', 'y': 'Job Satisfaction'},
                                 color_discrete_sequence=px.colors.qualitative.Pastel))
    st.plotly_chart(px.bar(x=["Low", "Medium", "High"], y=[3.0, 4.1, 2.8],
                           labels={'x': 'Workload', 'y': 'Satisfaction'},
                           color_discrete_sequence=px.colors.qualitative.Pastel))
    st.markdown("**Conclusion:** Job satisfaction is influenced by age and workload. A medium workload provides the highest satisfaction level.")


# CHURN ANALYSIS
elif menu == "Churn Analysis":
    st.title("🔁 Churn Analysis")
    st.plotly_chart(px.bar(x=["Total_Trans_Amt", "Avg_Open_To_Buy", "Tenure"],
                           y=[0.45, 0.32, 0.23],
                           labels={'x': 'Feature', 'y': 'Importance'},
                           color_discrete_sequence=px.colors.qualitative.Pastel))
    st.markdown("**Conclusion:** Customers with low transaction volumes and small credit limits are more likely to churn. It is important to focus on data-driven interventions for retention.")

# SALES EDA
elif menu == "Sales EDA":
    st.title("📊 Sales Exploratory Data Analysis")
    st.plotly_chart(px.histogram(x=["18-25", "26-35", "36-45"], y=[200, 300, 150],
                                 labels={'x': 'Age', 'y': 'Jumlah Pembelian'},
                                 color_discrete_sequence=px.colors.qualitative.Pastel))
    st.plotly_chart(px.box(x=["A", "B", "C"], y=[200, 220, 180],
                           labels={'x': 'Kota', 'y': 'Rata-rata Pembelian'},
                           color_discrete_sequence=px.colors.qualitative.Pastel))
    st.markdown("**Conclusion:** The 26–35 age group is the most active group of buyers. Marketing strategies can be focused on this segment in cities with high purchasing power.")

# REGRESSION
elif menu == "Regression":
    st.title("📈 Regression Predictive Analysis")
    st.metric("MAE", "0.42")
    st.metric("RMSE", "0.55")
    st.plotly_chart(px.scatter(x=[1, 2, 3], y=[1.1, 1.9, 3.2], labels={'x': 'Actual', 'y': 'Predicted'},
                               color_discrete_sequence=px.colors.qualitative.Pastel))
    st.line_chart(pd.DataFrame({"Error": [0.2, 0.1, 0.3]}))
    st.markdown("**Conclusion:** The regression model shows a performance that is suitable for initial predictions; however, there is still room for improvement in its error distribution.")
