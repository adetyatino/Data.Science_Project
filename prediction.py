import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib.cm as cm  
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder

# Set Page Config
st.set_page_config(page_title="HR Attrition Dashboard - Jaya Jaya Maju", layout="wide")

# Load Data
@st.cache_data
def load_data():
    df = pd.read_csv('employee_data.csv')
    df['Attrition'] = df['Attrition'].fillna(0)
    df['Attrition_Status'] = df['Attrition'].apply(lambda x: 'Resigned' if x == 1 else 'Active')
    return df

df = load_data()

# Sidebar - Filter
st.sidebar.title("Filter Dashboard")
dept_filter = st.sidebar.multiselect("Pilih Departemen:", 
                                     options=df['Department'].unique(), 
                                     default=df['Department'].unique())

filtered_df = df[df['Department'].isin(dept_filter)]

# Judul Utama
st.title("Jaya Jaya Maju: HR Business Dashboard")
st.markdown("Analisis mendalam faktor pemicu *attrition* untuk strategi retensi karyawan.")


# Row 1: KPI Metrics
total_emp = len(filtered_df)
attrition_count = len(filtered_df[filtered_df['Attrition'] == 1])
attrition_rate = (attrition_count / total_emp) * 100 if total_emp > 0 else 0

col1, col2, col3, col4 = st.columns(4)
col1.metric("Total Karyawan", total_emp)
col2.metric("Karyawan Keluar", attrition_count)
col3.metric("Attrition Rate", f"{attrition_rate:.2f}%", delta=f"{attrition_rate-10:.1f}% vs Target 10%", delta_color="inverse")
col4.metric("Rata-rata Gaji", f"${filtered_df['MonthlyIncome'].mean():,.0f}")
st.caption("Di sini terlihat total karyawan, jumlah yang keluar, serta attrition rate.\
            Ini memberikan gambaran cepat kondisi kesehatan SDM di perusahaan.")

# Row 2: OverTime & Career Stagnation
st.markdown("---")
c1, c2 = st.columns(2)

with c1:
    st.markdown ("### 1. Dampak Lembur (OverTime)")
    ot_counts = filtered_df.groupby(['OverTime', 'Attrition_Status']).size().unstack(fill_value=0)
    ot_perc = ot_counts.div(ot_counts.sum(axis=1), axis=0) * 100
    
    fig, ax = plt.subplots(figsize=(8, 6))
    ot_perc.plot(kind='bar', stacked=True, ax=ax, color=["#de1600", '#2ecc71'])
    
    # Label 
    for i, (idx, row) in enumerate(ot_perc.iterrows()):
        cum_height = 0
        for status in ot_perc.columns:
            val = row[status]
            cnt = ot_counts.loc[idx, status]
            if val > 0:
                ax.text(i, cum_height + (val/2), f'{val:.1f}% ({cnt})', 
                        ha='center', va='center', color='white', fontweight='bold', fontsize=9)
                cum_height += val
    ax.set_ylabel("Persentase (%)")
    plt.xticks(rotation=0)
    st.pyplot(fig)
    st.caption("Terlihat bahwa karyawan yang sering lembur memiliki tingkat resign yang jauh lebih tinggi.\
                Ini menunjukkan adanya potensi burnout yang perlu diperhatikan.")

with c2:
    st.markdown ("### 2. Stagnasi Karir (Promosi)")
    fig, ax = plt.subplots(figsize=(8, 6))
    sns.scatterplot(data=filtered_df, x='YearsAtCompany', y='YearsSinceLastPromotion', 
                    hue='Attrition_Status', palette={'Resigned': "#fd1900", 'Active': '#2ecc71'}, alpha=0.6)
    
    ax.axhline(y=3, color='red', linestyle='--', linewidth=2)
    ax.text(x=0, y=3.5, s="Area Rawan Resign (>3 Thn Tanpa Promosi)", color='red', fontweight='bold')
    ax.set_xlabel("Tahun di Perusahaan")
    ax.set_ylabel("Tahun Sejak Promosi Terakhir")
    st.pyplot(fig)
    st.caption("Grafik ini menunjukkan bahwa karyawan yang tidak mendapat promosi lebih dari 3 tahun cenderung memiliki risiko resign lebih besar.")


# Row 3: Compensation Analysis & Job Role
st.markdown("---")
c3, c4 = st.columns(2)

with c3:
    st.markdown ("#### 3. Analisis Kompensasi: Gaji vs Job Level")
    fig, ax = plt.subplots(figsize=(8, 6.5))
    sns.boxplot(data=filtered_df, x='JobLevel', y='MonthlyIncome', hue='Attrition_Status',
                palette={'Resigned': "#f11800", 'Active': '#2ecc71'}, ax=ax)
    ax.set_title("Distribusi Gaji: Karyawan Bertahan vs Keluar")
    ax.set_xlabel("Job Level (1 - 5)")
    ax.set_ylabel("Monthly Income ($)")
    st.pyplot(fig)
    st.caption("Insight: Jika titik berada di bawah garis merah, artinya mereka baru saja mendapat promosi (kurang dari 3 tahun lalu). " 
    " Jika titik berada di atas garis merah, artinya mereka sudah Stagnan atau tidak naik jabatan selama lebih dari 3 tahun.")

# Row 3 section 2
with c4:
    st.markdown("##### 4. Analisis Kompensasi: Gaji vs Job Level (Semua Karyawan)")
    fig, ax = plt.subplots(figsize=(10, 8))
    sns.boxplot(
        data=filtered_df, 
        x='JobLevel', 
        y='MonthlyIncome', 
        hue='Attrition_Status',
        palette={'Resigned': "#FF1900", 'Active': "#02ff70"}, 
        ax=ax,
        showfliers=False, 
        boxprops=dict(alpha=0.2)
    )
    sns.stripplot(
        data=filtered_df, 
        x='JobLevel', 
        y='MonthlyIncome', 
        hue='Attrition_Status',
        palette={'Resigned': "#ff2a12", 'Active': "#007b33"}, 
        dodge=True, 
        jitter=True, 
        alpha=0.7, 
        ax=ax
    )
    ax.set_title("Distribusi Gaji per Job Level", fontsize=10)
    ax.set_xlabel("Job Level", fontsize=9)
    ax.set_ylabel("Monthly Income ($)", fontsize=9)
    handles, labels = ax.get_legend_handles_labels()
    ax.legend(handles[0:2], labels[0:2], title='Status', fontsize=8)
    st.pyplot(fig)
    st.caption("Insight: Titik-titik menunjukkan posisi gaji setiap karyawan secara individu.")

st.info("Di bagian kompensasi, kita bandingkan gaji berdasarkan level jabatan.\
Terlihat bahwa karyawan yang resign, khususnya di level bawah, seringkali memiliki gaji yang lebih rendah dibanding rekan selevelnya.")

# Rw 4: Job Role Attrition
st.markdown("---")
st.markdown("### 5. Pekerjaan dengan Attrition Tertinggi")

role_attrition = filtered_df.groupby('JobRole')['Attrition'].mean().sort_values(ascending=False) * 100
fig, ax = plt.subplots(figsize=(11, 6))
import matplotlib.cm as cm
import numpy as np
colors = cm.Greens_r(np.linspace(0, 0.6, len(role_attrition))) 
sns.barplot(
    x=role_attrition.values, 
    y=role_attrition.index, 
    palette=colors,  
    ax=ax,
    edgecolor='black', 
    linewidth=0.5
)
ax.axvline(x=10, color='red', linestyle='--', linewidth=1.5, alpha=0.8, label='Threshold 10%')
ax.set_xlabel("Attrition Rate (%)", fontsize=10)
ax.set_ylabel("Job Role", fontsize=10)
ax.grid(axis='x', linestyle=':', alpha=0.6)
sns.despine(ax=ax, right=True, top=True)
st.pyplot(fig)
st.caption("Berikutnya, kita identifikasi job role dengan tingkat attrition tertinggi.\
Ini penting untuk membantu HR fokus pada posisi yang paling berisiko kehilangan talenta.")

# Row 5: Top Factors
st.markdown("---")
st.markdown("#### 6. Top 10 Faktor Pendorong Attrition")


# ================================
# PROSES MACHINE LEARNING 
# ================================
df_ml = filtered_df.copy()
le = LabelEncoder()

# Encoding kolom kategori
for col in df_ml.select_dtypes(include=['object']).columns:
    if col != 'Attrition_Status':
        df_ml[col] = le.fit_transform(df_ml[col].astype(str))

# Fitur (X) dan target (y)
drop_cols = ['Attrition', 'Attrition_Status', 'EmployeeId', 'EmployeeCount', 'Over18', 'StandardHours', 'EmployeeNumber']
X = df_ml.drop([c for c in drop_cols if c in df_ml.columns], axis=1)
y = df_ml['Attrition']

# Training Model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X, y)
feat_importances = pd.Series(model.feature_importances_, index=X.columns).nlargest(10).sort_values(ascending=True)

# 2. PERBAIKAN NAMA LABEL (Menambah Spasi)
import re
feat_importances.index = [re.sub(r"(\w)([A-Z])", r"\1 \2", str(x)) for x in feat_importances.index]
fig, ax = plt.subplots(figsize=(12, 6)) 
try:
    cmap = plt.colormaps.get_cmap('viridis_r')
except AttributeError:
    cmap = cm.get_cmap('viridis_r')
colors = cmap(np.linspace(0.1, 0.8, len(feat_importances)))
ax.barh(feat_importances.index, feat_importances.values, color=colors)

ax.set_xlabel('Importance Score', fontsize=10)
ax.set_title('Top 10 Feature Importance (Random Forest)', fontsize=11) 
ax.tick_params(axis='y', labelsize=10) 
ax.grid(axis='x', linestyle='--', alpha=0.5)

plt.tight_layout()
st.pyplot(fig)
st.caption("saya menggunakan machine learning ini untuk menemukan faktor paling berpengaruh terhadap attrition.\
Hasilnya menunjukkan beberapa faktor utama seperti overtime, income, dan lama tidak promosi.")

# SECTION KESIMPULAN LENGKAP 
st.markdown("---")
st.header("Kesimpulan & Rekomendasi Strategis")

col_a, col_b = st.columns(2)

with col_a:
    st.subheader(" Temuan Utama")
    st.markdown(f"""
        1. **Faktor Paling Berpengaruh:** Variabel **{feat_importances.index[-1]}** terdeteksi sebagai faktor utama yang mendorong karyawan meninggalkan perusahaan.
        2. **Masalah Kompensasi:** Grafik kompensasi menunjukkan bahwa karyawan yang *Exited* pada **Job Level 1 & 2** seringkali memiliki pendapatan di bawah rata-rata rekan sejawatnya di level yang sama.
        3. **Beban Kerja:** Karyawan yang lembur (*OverTime*) memiliki tingkat attrition yang jauh lebih ekstrem dibanding yang tidak.
        4. **Stagnasi Karir:** Karyawan yang tidak mendapatkan promosi dalam 3 tahun terakhir memiliki risiko keluar yang signifikan.
        5. **Job Role Rawan:** Beberapa job role seperti **Sales** dan **Lab Technician** memiliki tingkat attrition lebih dari 10%, menandakan area kritis untuk intervensi.
        6. **Target Attrition:** Saat ini, attrition rate berada di sekitar {attrition_rate:.2f}%, yang masih di atas target ideal 10%.
        7. **Kondisi SDM:** Meskipun jumlah karyawan cukup besar, tingkat keluar yang tinggi dapat mengindikasikan masalah dalam retensi dan kepuasan kerja.
        8. **Karyawan Aktif vs Resign:** Perbedaan signifikan dalam distribusi gaji dan beban kerja antara karyawan yang bertahan dan yang keluar menunjukkan adanya ketidakpuasan yang mungkin tidak terdeteksi sebelumnya.
        9. **Faktor Lain:** Selain faktor utama, beberapa variabel lain seperti **YearsAtCompany** dan **JobLevel** juga menunjukkan korelasi dengan attrition, meskipun tidak sekuat faktor utama.
        10. **Kesimpulan Umum:** Kombinasi faktor-faktor ini menunjukkan bahwa masalah attrition di Jaya Jaya Maju bersifat multifaset, melibatkan aspek kompensasi, beban kerja, dan pengembangan karir.

    """)

with col_b:
    st.subheader(" Rencana Aksi (Action Plan)")
    st.markdown("""
        1. **Penyesuaian Gaji:** Lakukan audit penggajian khususnya pada Job Level rendah untuk memastikan gaji tetap kompetitif dengan standar pasar.
        2. **Evaluasi Lembur:** Tinjau kembali distribusi beban kerja di departemen dengan tingkat lembur tinggi untuk mencegah *burnout*.
        3. **Jalur Promosi:** Implementasikan program pengembangan karir atau rotasi jabatan bagi karyawan yang sudah stagnan lebih dari 3 tahun.
        4. **Fokus Retensi:** Prioritaskan intervensi pada peran **Sales** dan **Lab Technician** (atau jabatan dengan rate >10%).
        5. **Program Kesejahteraan:** Pertimbangkan program kesejahteraan karyawan untuk meningkatkan kepuasan kerja dan loyalitas.
        6. **Monitoring Berkelanjutan:** Gunakan dashboard ini secara rutin untuk memantau perubahan dalam metrik kunci dan efektivitas intervensi yang dilakukan.
        7. **Keterlibatan Karyawan:** Lakukan survei kepuasan
        8. kerja untuk mendapatkan feedback langsung dari karyawan tentang faktor-faktor yang mempengaruhi keputusan mereka untuk tetap atau meninggalkan perusahaan.
        9. **Pelatihan Manajerial:** Berikan pelatihan kepada manajer untuk mengenali tanda-tanda ketidakpuasan karyawan dan cara mengatasinya secara proaktif.
        10. **Kultur Perusahaan:** Bangun budaya perusahaan yang mendukung keseimbangan kerja-hidup, pengembangan pribadi, dan penghargaan atas kontribusi karyawan.
    """)

st.info("Dari seluruh analisis ini, perusahaan dapat mengambil langkah strategis seperti penyesuaian gaji, evaluasi beban kerja, dan pengembangan karir karyawan.")
st.success("***Pesan: Dashboard ini dirancang untuk Jaya Jaya Maju guna membantu pengambilan keputusan berbasis data.***")