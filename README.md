# Proyek Akhir: Menyelesaikan Permasalahan Perusahaan Edutech

## Business Understanding

Jaya Jaya Maju adalah sebuah perusahaan multinasional yang memiliki skala operasional besar. Berdiri sejak tahun 2000, perusahaan ini telah tumbuh secara signifikan hingga memiliki aset sumber daya manusia yang besar, yakni lebih dari 1.000 karyawan yang tersebar di berbagai wilayah di seluruh negeri. Sebagai pemain lama di industri, stabilitas operasional menjadi kunci keberlangsungan bisnis mereka.

### Permasalahan Bisnis

Permasalahan utama Jaya Jaya Maju berpusat pada tingginya angka attrition di atas 10% yang mengancam stabilitas operasional dan efisiensi biaya perusahaan. Kondisi ini dipicu oleh beban kerja yang tidak sehat akibat lembur berlebihan serta adanya ketimpangan kompensasi, di mana banyak karyawan, terutama pada level junior, merasa gaji mereka tidak kompetitif dibandingkan beban tugas yang diberikan.

Selain masalah finansial, perusahaan menghadapi tantangan stagnasi karir yang serius di mana karyawan yang tidak mendapat promosi lebih dari tiga tahun cenderung memilih untuk mengundurkan diri. Kurangnya sistem pemantauan berbasis data membuat manajemen sulit melakukan intervensi proaktif pada jabatan kritis seperti tim sales dan teknisi laboratorium, sehingga perusahaan terus terjebak dalam siklus rekrutmen yang boros akibat gagal mempertahankan talenta terbaiknya.

### Cakupan Proyek

1. Integrasi dan Pembersihan Data

-Melakukan pemrosesan data mentah dari file employee_data.csv.

-Menangani data yang hilang (missing values) pada kolom target (Attrition).

-Melakukan transformasi data untuk kategorisasi status karyawan (Aktif vs Resigned).

2. Monitoring Metrik Utama (KPI Dashboard)

-Menampilkan jumlah total karyawan untuk memantau skala organisasi.

-Menghitung jumlah karyawan yang keluar secara real-time berdasarkan filter. 

-Memantau Attrition Rate dan membandingkannya dengan ambang batas target perusahaan (10%).

-Menganalisis rata-rata pendapatan bulanan (Monthly Income) sebagai indikator kesejahteraan.

3. Analisis Faktor Perilaku dan Beban Kerja

-Analisis Lembur (OverTime): Mengevaluasi korelasi antara frekuensi lembur dengan keputusan karyawan untuk resign (deteksi potensi burnout).

-Analisis Stagnasi Karir: Memetakan hubungan antara masa kerja di perusahaan dengan waktu promosi terakhir untuk mengidentifikasi area rawan pengunduran diri akibat kurangnya perkembangan karir.

4. Analisis Kompensasi dan Struktur Jabatan

-Audit Distribusi Gaji: Menganalisis rentang gaji berdasarkan tingkatan jabatan (Job Level) untuk melihat adanya ketimpangan kompensasi antara karyawan yang bertahan dan yang keluar.

-Identifikasi Jabatan Berisiko: Melakukan pemetaan terhadap tingkat attrition di setiap peran pekerjaan (Job Role) untuk menentukan departemen atau posisi yang memerlukan intervensi segera (contoh: Sales, Lab Technician).

5. Pemodelan Prediktif (Machine Learning)

-Mengimplementasikan algoritma Random Forest Classifier untuk menentukan variabel yang paling berpengaruh terhadap pengunduran diri.

-Feature Importance: Mengidentifikasi 10 faktor utama (seperti pendapatan, usia, lembur, dsb.) yang menjadi pemicu terbesar attrition berdasarkan data historis.

6. Pelaporan Strategis dan Rekomendasi

- Menyediakan ringkasan temuan utama secara otomatis berdasarkan data yang difilter.

- Menghasilkan rencana aksi (Action Plan) strategis yang mencakup penyesuaian gaji, evaluasi beban kerja, dan perbaikan jalur promosi bagi manajemen HR.

### Persiapan

Sumber data: `employee_data.csv` https://github.com/dicodingacademy/dicoding_dataset/blob/main/employee/employee_data.csv

Setup environment:

```bash
# Instalasi library yang dibutuhkan
pip install streamlit pandas matplotlib seaborn numpy scikit-learn
```

**To run the Streamlit prediction:**
```bash
streamlit run streamlit_app.py
```

### Business Dashboard

Jelaskan tentang business dashboard yang telah dibuat. Jika ada, sertakan juga link untuk mengakses dashboard tersebut.

## Conclusion

Jelaskan konklusi dari proyek yang dikerjakan.

### Rekomendasi Action Items (Optional)

Berikan beberapa rekomendasi action items yang harus dilakukan perusahaan guna menyelesaikan permasalahan atau mencapai target mereka.

- action item 1
- action item 2
