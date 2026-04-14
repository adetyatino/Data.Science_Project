import streamlit as st
import pandas as pd
import plotly.express as px
import numpy as np
import penjelasan as teks
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.neural_network import MLPClassifier 
from sklearn.cluster import KMeans
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.metrics import accuracy_score
from xgboost import XGBClassifier

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
    
    # Cleaning: Hapus nilai Null/NaN pada kolom krusial
    df_cleaned = df.dropna(subset=['Attrition', 'Age', 'MonthlyIncome', 'OverTime']).copy()
    
    # Mapping Label
    df_cleaned['Attrition_Status'] = df_cleaned['Attrition'].map({1.0: 'Resigned', 0.0: 'Stayed'})
    
    return df_cleaned
    
try:
    df = load_and_clean_data()
    

    # --- BAGIAN 1: METRICS UTAMA ---
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

    # --- BAGIAN 2: MACHINE LEARNING (PREDICTIVE ANALYTICS) ---
    st.header("Machine Learning Models & Insights")
    
    # Preprocessing ML
    ml_data = df[['Attrition', 'Age', 'MonthlyIncome', 'JobLevel', 'JobSatisfaction', 
                  'EnvironmentSatisfaction', 'OverTime', 'YearsAtCompany', 'WorkLifeBalance']].copy()
    
    le = LabelEncoder()
    ml_data['OverTime'] = le.fit_transform(ml_data['OverTime'])
    
    X = ml_data.drop('Attrition', axis=1)
    y = ml_data['Attrition']
    features_list = X.columns.tolist() # Fix: Definisikan features_list
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Scaller khusus untuk KNN
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)

    col_ml1, col_ml2 = st.columns(2)

    with col_ml1:
        # A. Logistic Regression
        lr = LogisticRegression(max_iter=1000)
        lr.fit(X_train, y_train)
        acc_lr = accuracy_score(y_test, lr.predict(X_test)) # Tambah akurasi
        st.subheader(f"1. Logistic Regression (Acc: {acc_lr:.2%})")
        coeffs = pd.DataFrame({'Fitur': X.columns, 'Koefisien': lr.coef_[0]}).sort_values(by='Koefisien')
        fig_lr = px.bar(coeffs, x='Koefisien', y='Fitur', orientation='h', title="Faktor Pendorong Attrition (Regresi)")
        st.plotly_chart(fig_lr, use_container_width=True)
        st.success(teks.DESC_LR) # Tambah penjelasan singkat
        st.success(teks.CONC_LR) # Tambah insight strategis 

        # B. Decision Tree
        dt = DecisionTreeClassifier(max_depth=5, random_state=42)
        dt.fit(X_train, y_train)
        acc_dt = accuracy_score(y_test, dt.predict(X_test))
        st.subheader(f"2. Decision Tree (Acc: {acc_dt:.2%})")
        feat_imp_dt = pd.DataFrame({'Fitur': X.columns, 'Importance': dt.feature_importances_}).sort_values(by='Importance')
        fig_dt = px.bar(feat_imp_dt, x='Importance', y='Fitur', orientation='h', title="Pohon Keputusan: Feature Importance")
        st.plotly_chart(fig_dt, use_container_width=True)
        st.success(teks.DESC_DT) # Tambah penjelasan singkat
        st.success(teks.CONC_DT) # Tambah insight strategis

        # C. K-Nearest Neighbors (KNN)
        knn = KNeighborsClassifier(n_neighbors=5)
        knn.fit(X_train_scaled, y_train)
        acc_knn = accuracy_score(y_test, knn.predict(X_test_scaled))
        st.subheader(f"3. K-Nearest Neighbors (Acc: {acc_knn:.2%})")
        st.write("KNN mengelompokkan karyawan berdasarkan kemiripan profil (Age, Income, dll).")
        # Visualisasi sederhana untuk KNN (Scatter profil tetangga)
        fig_knn_val = px.scatter(X_test, x='Age', y='MonthlyIncome', color=knn.predict(X_test_scaled).astype(str),
                                  title="Prediksi KNN: Sebaran Usia vs Gaji", labels={'color': 'Prediksi Attrition'})
        fig_knn_val = px.scatter(
            X_test, 
            x='Age', 
            y='MonthlyIncome', 
            color=knn.predict(X_test_scaled).astype(str),
            title="Prediksi KNN: Sebaran Usia vs Gaji", 
            labels={'color': 'Prediksi Attrition', 
                    'Age': 'Age (Years)', 
                    'MonthlyIncome': 'Monthly Income ($)'}, 
            color_discrete_sequence=px.colors.qualitative.T10 
        )
        st.plotly_chart(fig_knn_val, use_container_width=True)
        st.success(teks.DESC_KN) # Tambah penjelasan singkat
        st.success(teks.CONC_KN) # Tambah insight strategis    

    with col_ml2:
        # D. Random Forest
        rf = RandomForestClassifier(n_estimators=100, random_state=42)
        rf.fit(X_train, y_train)
        acc_rf = accuracy_score(y_test, rf.predict(X_test))
        st.subheader(f"4. Random Forest (Acc: {acc_rf:.2%})")
        feat_imp_rf = pd.DataFrame({'Fitur': X.columns, 'Importance': rf.feature_importances_}).sort_values(by='Importance')
        fig_rf = px.bar(feat_imp_rf, x='Importance', y='Fitur', orientation='h', title="Random Forest: Feature Importance")
        st.plotly_chart(fig_rf, use_container_width=True)
        st.success(teks.DESC_RF) # Tambah penjelasan singkat
        st.success(teks.CONC_RF) # Tambah insight strategis

        # E. XGBoost
        xgb = XGBClassifier(use_label_encoder=False, eval_metric='logloss')
        xgb.fit(X_train, y_train)
        acc_xgb = accuracy_score(y_test, xgb.predict(X_test))
        st.subheader(f"5. XGBoost (Acc: {acc_xgb:.2%})")
        feat_imp_xgb = pd.DataFrame({'Fitur': X.columns, 'Importance': xgb.feature_importances_}).sort_values(by='Importance')
        fig_xgb = px.bar(feat_imp_xgb, x='Importance', y='Fitur', orientation='h', title="XGBoost: Feature Importance (Best Performer)")
        st.plotly_chart(fig_xgb, use_container_width=True)
        st.success(teks.DESC_XG) # Tambah penjelasan singkat
        st.success(teks.CONC_XG) # Tambah insight strategis

        # F. Clustering
        st.subheader("6. Clustering (Segmentasi Karyawan)")

        # 1. Jalankan KMeans terlebih dahulu agar kolom 'Segment' tersedia
        kmeans = KMeans(n_clusters=3, random_state=42, n_init=10)
        df['Segment'] = kmeans.fit_predict(df[['Age', 'MonthlyIncome']]).astype(str)

        # 2. Tentukan mapping warna
        warna_segmen = {
            "0": "#7C85FF", # Biru
            "1": "#EF553B", # Merah
            "2": "#00E2A5"  # Hijau
        }

        # 3. Buat satu plot yang mencakup semua parameter (Warna, Simbol, dan Label)
        fig_cluster = px.scatter(
            df, 
            x='Age', 
            y='MonthlyIncome', 
            color='Segment', # Menggunakan kolom yang sudah jadi string
            symbol='Attrition_Status', 
            title="Segmentasi Karyawan (K-Means)",
            color_discrete_map=warna_segmen,
            labels={ 
                "Attrition_Status": "Status Attrition",
                "Age": "Usia (Years)",
                "MonthlyIncome": "Monthly Income ($)"
            },
            category_orders={"Segment": ["0", "1", "2"]}
        )

        # 4. Tampilkan grafik
        st.plotly_chart(fig_cluster, use_container_width=True)
        st.success(teks.DESC_KM) # Tambah penjelasan singkat
        st.success(teks.CONC_KM) # Tambah insight strategis
    st.divider()

    # --- BAGIAN 3: DEEP LEARNING & PATTERN ANALYSIS ---
    st.header("Deep Learning & Pattern Analysis")
    col_dl1, col_dl2 = st.columns(2)

    with col_dl1:
        # ANN
        ann = MLPClassifier(hidden_layer_sizes=(64, 32), max_iter=500, random_state=42)
        ann.fit(X_train_scaled, y_train)
        acc_ann = accuracy_score(y_test, ann.predict(X_test_scaled))
        
        st.subheader(f"1. Neural Networks (Acc: {acc_ann:.2%})")
        ann_weights = np.abs(ann.coefs_[0]).sum(axis=1)
        ann_imp_df = pd.DataFrame({'Fitur': features_list, 'Aktivitas': ann_weights}).sort_values(by='Aktivitas')
        fig_ann = px.bar(ann_imp_df, x='Aktivitas', y='Fitur', orientation='h', title="ANN Feature Activation", color_discrete_sequence=["#5AD000"], template="plotly_white")
        st.plotly_chart(fig_ann, use_container_width=True)
        st.success(teks.DESC_NN) # Tambah penjelasan singkat
        st.success(teks.CONC_NN) # Tambah insight strategis

    with col_dl2:
        st.subheader("2. Interaksi Pola Kompleks")
        fig_inter = px.density_heatmap(df, x="Age", y="MonthlyIncome", z="Attrition", 
                                        histfunc="avg", title="Heatmap Peluang Resign (Age vs Income)", 
                                        color_continuous_scale='Viridis', template="plotly_white")
        fig_inter.update_xaxes(title_text='Monthly Income ($)')
        fig_inter.update_yaxes(title_text='Age (Years)')
        st.plotly_chart(fig_inter, use_container_width=True)
        st.success(teks.DESC_PK) # Tambah penjelasan singkat
        st.success(teks.CONC_PK) # Tambah insight strategis  

    st.divider()

    # --- BAGIAN 4: DASHBOARD VISUALISASI ---
    st.header("Deep Dive Analysis (Bar Charts with Percentages)")
    
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

    c1, c2 = st.columns(2)
    with c1:
        # Simpan hasil fungsi ke variabel, update labelnya, lalu tampilkan
        fig1 = plot_bar_pct(df, 'OverTime', "1. Faktor Utama: OverTime")
        fig1.update_xaxes(title_text='Over Time')
        st.plotly_chart(fig1, use_container_width=True)
        st.success(teks.DESC_1) # Tambah penjelasan singkat
        st.success(teks.CONC_1) # Tambah insight strategis berdasarkan hasil bar chart

        fig2 = plot_bar_pct(df, 'EnvironmentSatisfaction', "2. Kepuasan Lingkungan Kerja (1-4)")
        fig2.update_xaxes(title_text='Environment Satisfaction')
        st.plotly_chart(fig2, use_container_width=True)
        st.success(teks.DESC_3) # Tambah penjelasan singkat
        st.success(teks.CONC_3) # Tambah insight strategis berdasarkan hasil bar

        fig3 = plot_bar_pct(df, 'JobLevel', "3. Level Pekerjaan (Job Level)")
        fig3.update_xaxes(title_text='Job Level')
        st.plotly_chart(fig3, use_container_width=True)
        st.success(teks.DESC_5) # Tambah penjelasan singkat
        st.success(teks.CONC_5) # Tambah insight strategis berdasarkan hasil bar chart  

    with c2:
        df['AgeGroup'] = pd.cut(df['Age'], bins=[18, 30, 40, 50, 60], labels=['18-30', '31-40', '41-50', '51-60'])
        
        fig4 = plot_bar_pct(df, 'AgeGroup', "4. Masa Kerja & Usia (Kelompok Usia)")
        fig4.update_xaxes(title_text='Age Group')
        st.plotly_chart(fig4, use_container_width=True)
        st.success(teks.DESC_2) # Tambah penjelasan singkat
        st.success(teks.CONC_2) # Tambah insight strategis berdasarkan hasil bar

        fig5 = plot_bar_pct(df, 'RelationshipSatisfaction', "5. Hubungan Kerja (Relationship Satisfaction)")
        fig5.update_xaxes(title_text='Relationship Satisfaction')
        st.plotly_chart(fig5, use_container_width=True)
        st.success(teks.DESC_4) # Tambah penjelasan singkat
        st.success(teks.CONC_4) # Tambah insight strategis berdasarkan hasil bar chart

    # --- BAGIAN BARU: ANALISIS FAKTOR KHUSUS (REQUEST USER) ---
    st.divider()
    st.header("Strategic Insights: Faktor Penentu Attrition")
    st.info("Analisis mendalam berdasarkan profil Karyawan yang Resign vs Stay.")

    col_ins1, col_ins2 = st.columns(2)

    with col_ins1:
        # Analisis Gaji Rendah
        fig_income = px.box(df, x='Attrition_Status', y='MonthlyIncome', color='Attrition_Status',
                           title="A. Distribusi Gaji: Karyawan Resign Cenderung Bergaji Rendah",
                           labels={'Attrition_Status': 'Status Attrition', 'MonthlyIncome': 'Monthly Income ($)'},
                           color_discrete_map={'Resigned': '#EF553B', 'Stayed': '#636EFA'})
        st.plotly_chart(fig_income, use_container_width=True)
        st.success(teks.DESC_6) # Tambah penjelasan singkat
        st.success(teks.CONC_6) # Tambah insight strategis berdasarkan hasil box

        # Work-Life Balance
        fig_wlb = plot_bar_pct(df, 'WorkLifeBalance', "B. Work-Life Balance (1=Buruk, 4=Sangat Baik)")
        fig_wlb.update_xaxes(title_text='Work-Life Balance')
        st.plotly_chart(fig_wlb, use_container_width=True)
        st.success(teks.DESC_8) # Tambah penjelasan singkat
        st.success(teks.CONC_8) # Tambah insight strategis berdasarkan hasil bar

        # Jarak Rumah (Distance From Home)
        if 'DistanceFromHome' in df.columns:
            fig_dist = px.histogram(df, x='DistanceFromHome', color='Attrition_Status', 
                                    barmode='group',
                                   title="C. Dampak Jarak Rumah Terhadap Keputusan Resign",
                                   labels={'DistanceFromHome': 'Distance from Home (km)'},
                                   color_discrete_map={'Resigned': '#EF553B', 'Stayed': '#636EFA'})
            st.plotly_chart(fig_dist, use_container_width=True)
            st.success(teks.DESC_10) # Tambah penjelasan singkat
            st.success(teks.CONC_10) # Tambah insight strategis berdasarkan hasil histogram

    with col_ins2:
        # Kepuasan Kerja (Job Satisfaction)
        fig_jobsat = plot_bar_pct(df, 'JobSatisfaction', "D. Kepuasan Kerja (Job Satisfaction 1-4)")
        fig_jobsat.update_xaxes(title_text='Job Satisfaction')
        st.plotly_chart(fig_jobsat, use_container_width=True)
        st.success(teks.DESC_7) # Tambah penjelasan singkat
        st.success(teks.CONC_7) # Tambah insight strategis berdasarkan hasil

        # Masa Kerja Pendek (Years at Company)
        fig_years = px.violin(df, x='Attrition_Status', y='YearsAtCompany', color='Attrition_Status', box=True,
                             title="E. Masa Kerja: Attrition Tinggi pada Karyawan Baru",
                             labels={'Attrition_Status': 'Attrition Status', 'YearsAtCompany': 'Years at Company'},
                             color_discrete_map={'Resigned': '#EF553B', 'Stayed': '#636EFA'})
        st.plotly_chart(fig_years, use_container_width=True)
        st.success(teks.DESC_9) # Tambah penjelasan singkat
        st.success(teks.CONC_9) # Tambah insight strategis berdasarkan hasil violin

        # Perbandingan Usia (Age)
        fig_age_dist = px.histogram(df, x='Age', color='Attrition_Status', marginal='box',
                                   title="F. Sebaran Usia: Karyawan Muda Lebih Rentan Resign",
                                   labels={'Age': 'Usia (Years)'},
                                   color_discrete_map={'Resigned': '#EF553B', 'Stayed': '#636EFA'})
        st.plotly_chart(fig_age_dist, use_container_width=True)
        st.success(teks.DESC_11) # Tambah penjelasan singkat
        st.success(teks.CONC_11) # Tambah insight strategis berdasarkan hasil histogram

except Exception as e:
    st.error(f"Terjadi kesalahan: {e}")