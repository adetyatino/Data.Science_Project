import streamlit as st
import pandas as pd
import plotly.express as px
import numpy as np
import penjelasan as teks 
from sklearn.preprocessing import LabelEncoder

# 1. Konfigurasi Halaman
st.set_page_config(page_title="Jaya Jaya Maju HR Analytics", layout="wide")
st.markdown(
    """
    <style>
        /* 5. Garis Horizontal Putih (Divider) */
        hr {
            border: 0;
            border-top: 2px solid white !important;
            opacity: 1;
        }
    </style>
    """,
    unsafe_allow_html=True
)

st.title("Strategic HR Dashboard - Jaya Jaya Maju")
st.markdown("Dashboard Analisis Prediktif & Deskriptif untuk Menekan Attrition Rate (>10%)")

# 2. Load & Data Cleaning
@st.cache_data
def load_and_clean_data():
    # Pastikan file employee_data.csv berada di direktori yang sama
    df = pd.read_csv('employee_data.csv')
    
    #  Cleaning Data Duplikat 
    jml_duplikat = df.duplicated().sum()
    if jml_duplikat > 0:
        # Menghapus baris yang identik seluruh kolomnya
        df = df.drop_duplicates()
    
    # Cleaningnilai Null/NaN pada kolom krusial
    df_cleaned = df.dropna(subset=['Attrition', 'Age', 'MonthlyIncome', 'OverTime']).copy()
    
    # Mapping Label
    df_cleaned['Attrition_Status'] = df_cleaned['Attrition'].map({1.0: 'Resigned', 0.0: 'Stayed'})
    
    return df_cleaned

# --- FUNGSI PLOT (Dikeluarkan dari blok try agar lebih rapi) ---
def plot_bar_pct(data, col, title):
    counts = data.groupby([col, 'Attrition_Status']).size().reset_index(name='Jumlah')
    total_cat = data.groupby(col).size().reset_index(name='Total')
    df_p = pd.merge(counts, total_cat, on=col)
    df_p['Pct'] = (df_p['Jumlah'] / df_p['Total'] * 100).round(1)
    df_p['Label'] = df_p['Jumlah'].astype(str) + " (" + df_p['Pct'].astype(str) + "%)"
    
    fig = px.bar(df_p, x=col, y='Jumlah', color='Attrition_Status', text='Label',
                barmode='group', title=title,
                color_discrete_map={'Resigned': '#EF553B', 'Stayed': '#636EFA'})
    fig.update_traces(textposition='outside')
    return fig


try:
    df = load_and_clean_data()

    #  1. METRICS UTAMA 
    total_k = len(df)
    keluar = int(df['Attrition'].sum())
    attrition_rate = (keluar / total_k) * 100
    
    m1, m2, m3, m4, m5 = st.columns(5)
    m1.metric("Total Karyawan", total_k)
    m2.metric("Karyawan Aktif", total_k - keluar)
    m3.metric("Karyawan Keluar", keluar)
    m4.metric("Attrition Rate", f"{attrition_rate:.2f}%", delta=">10% High Risk", delta_color="inverse")
    m5.metric("Avg Monthly Income", f"$ {df['MonthlyIncome'].mean():,.0f}")

    st.divider()

    # 2. DASHBOARD VISUALISASI
    st.header("Deep Dive Analysis (Full Width Charts)")
    
    # 1. Faktor Utama: OverTime
    fig1 = plot_bar_pct(df, 'OverTime', "1. Faktor Utama: OverTime")
    fig1.update_xaxes(title_text='Over Time')
    st.plotly_chart(fig1, use_container_width=True)
    st.success(teks.DESC_1) 
    st.success(teks.CONC_1) 
    st.markdown("---")
    
    # 2. Level Pekerjaan (Job Level)
    fig3 = plot_bar_pct(df, 'JobLevel', "2. Level Pekerjaan (Job Level)")
    fig3.update_xaxes(title_text='Job Level')
    st.plotly_chart(fig3, use_container_width=True)
    st.success(teks.DESC_2) 
    st.success(teks.CONC_2) 
    st.markdown("---")
    
    # 3. Work-Life Balance
    fig_wlb = plot_bar_pct(df, 'WorkLifeBalance', "3. Work-Life Balance (1=Buruk, 4=Sangat Baik)")
    fig_wlb.update_xaxes(title_text='Work-Life Balance')
    st.plotly_chart(fig_wlb, use_container_width=True)
    st.success(teks.DESC_3) 
    st.success(teks.CONC_3) # Menambahkan tutup kurung yang kurang

except Exception as e:
    st.error(f"Terjadi kesalahan: {e}")