# Proyek Akhir: Menyelesaikan Permasalahan Perusahaan Edutech

## Business Understanding
Jaya Jaya Maju adalah sebuah perusahaan multinasional yang memiliki skala operasional besar. Berdiri sejak tahun 2000, perusahaan ini telah tumbuh secara signifikan hingga memiliki aset sumber daya manusia yang besar, yakni lebih dari 1.000 karyawan yang tersebar di berbagai wilayah di seluruh negeri. Sebagai pemain lama di industri, stabilitas operasional menjadi kunci keberlangsungan bisnis mereka.


### Permasalahan Bisnis
1. Tingginya Attrition Rate Perusahaan: Masalah utama yang dihadapi adalah rasio jumlah karyawan yang keluar (attrition rate) telah mencapai angka di atas 10%. Hal ini dianggap mengkhawatirkan bagi stabilitas operasional perusahaan yang memiliki lebih dari 1000 karyawan.

2. Identifikasi Faktor Pemicu Attrition: Perusahaan kesulitan menentukan variabel mana yang paling berkontribusi terhadap keputusan karyawan untuk berhenti. Analisis diarahkan pada faktor-faktor seperti:
    - Beban Kerja (Overtime): Mengevaluasi kaitan antara jam kerja tambahan dengan kecenderungan karyawan untuk keluar.
    - Kompensasi: Menganalisis apakah tingkat gaji bulanan (Monthly Income) dan kenaikan gaji (Percent Salary Hike) sudah kompetitif untuk mempertahankan karyawan.
    - Stagnasi Karir: Mengidentifikasi apakah lamanya waktu sejak promosi terakhir (Years Since Last Promotion) memicu keluarnya karyawan.
    - Kepuasan Kerja & Lingkungan: Meninjau skor kepuasan kerja (Job Satisfaction) dan kepuasan lingkungan (Environment Satisfaction) terhadap status attrition

3. Efektivitas Monitoring Data: Manajemen HR belum memiliki alat yang mampu memantau metrik karyawan secara real-time dan komprehensif. Permasalahan ini diselesaikan dengan membangun business dashboard yang mencakup:
    - KPI Utama: Memantau jumlah total karyawan, jumlah karyawan yang keluar, serta persentase attrition secara keseluruhan.
    - Demografi & Peran: Memetakan departemen (seperti Sales atau Research & Development) dan posisi pekerjaan yang paling rentan mengalami pengunduran diri.
    - Filter Interaktif: Memungkinkan manajer HR untuk menyaring data berdasarkan departemen tertentu guna pengambilan keputusan yang lebih spesifik.


### Cakupan Proyek
1. Integrasi dan Pembersihan Data
    - Melakukan pemrosesan data mentah dari file employee_data.csv.
    - Menangani data yang hilang (missing values) pada kolom target (Attrition).
    - Melakukan transformasi data untuk kategorisasi status karyawan (Aktif vs Resigned).

2. Monitoring Metrik Utama (KPI Dashboard)
    - Menampilkan jumlah total karyawan untuk memantau skala organisasi.
    - Menghitung jumlah karyawan yang keluar secara real-time berdasarkan filter. 
    - Memantau Attrition Rate dan membandingkannya dengan ambang batas target perusahaan (10%).
    - Menganalisis rata-rata pendapatan bulanan (Monthly Income) sebagai indikator kesejahteraan.

3. Analisis Faktor Perilaku dan Beban Kerja
    - Analisis Lembur (OverTime): Mengevaluasi korelasi antara frekuensi lembur dengan keputusan karyawan untuk resign (deteksi potensi burnout).
    - Analisis Stagnasi Karir: Memetakan hubungan antara masa kerja di perusahaan dengan waktu promosi terakhir untuk mengidentifikasi area rawan pengunduran diri akibat kurangnya perkembangan karir.

4. Analisis Kompensasi dan Struktur Jabatan
    - Audit Distribusi Gaji: Menganalisis rentang gaji berdasarkan tingkatan jabatan (Job Level) untuk melihat adanya ketimpangan kompensasi antara karyawan yang bertahan dan yang keluar.
    - Identifikasi Jabatan Berisiko: Melakukan pemetaan terhadap tingkat attrition di setiap peran pekerjaan (Job Role) untuk menentukan departemen atau posisi yang memerlukan intervensi segera (contoh: Sales, Lab Technician).

5. Pemodelan Prediktif (Machine Learning)
    - Mengimplementasikan algoritma Random Forest Classifier untuk menentukan variabel yang paling berpengaruh terhadap pengunduran diri.
    - Feature Importance: Mengidentifikasi 10 faktor utama (seperti pendapatan, usia, lembur, dsb.) yang menjadi pemicu terbesar attrition berdasarkan data historis.

6. Pelaporan Strategis dan Rekomendasi
    - Menyediakan ringkasan temuan utama secara otomatis berdasarkan data yang difilter.
    - Menghasilkan rencana aksi (Action Plan) strategis yang mencakup penyesuaian gaji, evaluasi beban kerja, dan perbaikan jalur promosi bagi manajemen HR.


### Persiapan
Sumber data: `employee_data.csv` https://github.com/dicodingacademy/dicoding_dataset/blob/main/employee/employee_data.csv

Setup environment: Untuk menjalankan analisis data dan dashboard interaktif Jaya Jaya Maju, perlu mempersiapkan perangkat lunak, pustaka Python, dan struktur folder yang sesuai.


## Perangkat Lunak Utama
Memastikan perangkat lunak berikut sudah terinstal di komputer, berikut yang harus di install:
* **Python (Versi 3.8 atau lebih baru):** Bahasa pemrograman utama.
* **Visual Studio Code (VS Code):** Rekomendasi editor kode untuk menjalankan skrip Python dan Jupyter Notebook.
* **Web Browser:** Untuk menampilkan Dashboard Streamlit.


## Perangkat lunak kedua
1. Instalasi library yang dibutuhkan

```bash
   pip install pandas numpy matplotlib seaborn streamlit scikit-learn joblib
```
#### Pengertian
Pandas: Untuk manipulasi dan analisis data CSV.
Matplotlib & Seaborn: Untuk pembuatan grafik dan visualisasi data.
Streamlit: Framework untuk membangun dashboard bisnis interaktif.
Scikit-learn: Untuk pemodelan machine learning (Random Forest) guna memprediksi attrition.
Joblib: Untuk menyimpan dan memuat model yang telah dilatih.

2. Install All the Requirements Inside "requirements.txt"
```bash
pip install -r requirements.txt 
```

3. To run the Streamlit prediction
```bash
streamlit run streamlit_app.py
```


### Business Dashboard
Fokus utama dashboard ini adalah membedah faktor-faktor pemicu attrition (pengunduran diri karyawan) yang sedang dialami perusahaan. Berikut adalah fitur dan komponen utama dari dashboard tersebut:
1. Metrik Utama (KPI). Pada bagian atas dashboard, terdapat kartu ringkasan (KPI) yang menampilkan data secara real-time berdasarkan filter yang dipilih:
    - Total Employees: Jumlah total karyawan yang terdaftar.
    - Attrition Count: Jumlah karyawan yang telah mengundurkan diri.
	- Attrition Rate: Persentase rasio pengunduran diri terhadap total karyawan (saat ini menjadi perhatian utama karena berada di atas 10%).

2. Visualisasi Faktor Pemicu (Analisis Mendalam). Dashboard ini menampilkan berbagai grafik interaktif untuk menjawab "mengapa" karyawan keluar:
	- Hubungan Overtime & Attrition: Grafik yang menunjukkan apakah kebijakan lembur berkorelasi langsung dengan keputusan karyawan untuk berhenti.
	- Monthly Income vs Job Level: Analisis untuk melihat apakah ada kesenjangan kompensasi pada level jabatan tertentu yang memicu ketidakpuasan.
	- Years Since Last Promotion: Visualisasi untuk mendeteksi stagnasi karir sebagai faktor pemicu keluarnya karyawan.
	- Job Role Analysis: Identifikasi posisi pekerjaan (seperti Sales atau Lab Technician) yang memiliki tingkat attrition paling tinggi.

3. Fitur Interaktif
	- Sidebar Filter: Pengguna dapat menyaring data berdasarkan satu atau beberapa Departemen, sehingga manajer HR dapat melakukan analisis spesifik untuk departemen tertentu tanpa tercampur data lain.

4. Rekomendasi Strategis. Di bagian bawah dashboard, sistem menyajikan poin-poin saran berbasis data, seperti:
	- Evaluasi beban kerja pada departemen dengan tingkat lembur tinggi.
	- Peninjauan jalur promosi bagi karyawan yang sudah stagnan lebih dari 3 tahun.
	- Program retensi khusus untuk jabatan dengan attrition rate kritis.

#### Link Akses Dashboard 

* **Streamlit:** https://datascienceproject-ja5ymavaprmywgbxsyqvjm.streamlit.app/ 

* **Tableau:**   https://public.tableau.com/views/HR_Dashboard_17756247930310/Dashboard1?:language=en-US&:sid=&:redirect=auth&:display_count=n&:origin=viz_share_link


## Conclusion
1. Faktor Utama Pemicu Attrition. Proyek ini berhasil mengidentifikasi beberapa variabel kunci yang menyebabkan tingginya angka pengunduran diri (di atas 10%):
    - Beban Kerja (Overtime): Terdapat korelasi signifikan antara karyawan yang sering bekerja lembur dengan keputusan untuk keluar. Keseimbangan kerja-hidup (work-life balance) menjadi isu krusial.
    - Stagnasi Karir: Karyawan yang tidak mendapatkan promosi dalam jangka waktu lama (lebih dari 3 tahun) cenderung mencari peluang di tempat lain.
    - Kompensasi vs Level Jabatan: Ketidaksesuaian antara tingkat pendapatan bulanan (Monthly Income) dengan tanggung jawab pekerjaan (Job Level) memicu ketidakpuasan.

2. Area Paling Berisiko. Analisis menunjukkan bahwa attrition tidak tersebar merata, melainkan terkonsentrasi pada area tertentu:
    - Departemen: Sektor seperti Sales dan Research & Development menunjukkan dinamika perputaran karyawan yang lebih tinggi dibandingkan departemen lainnya.
    - Jabatan Spesifik: Peran seperti Sales Executive dan Lab Technician memerlukan perhatian khusus karena memiliki tingkat pengunduran diri yang kritis.

3. Solusi Monitoring Melalui Dashboard. Proyek ini telah menghasilkan alat pemantauan berbasis Streamlit yang memungkinkan manajemen HR untuk:
    - Memantau angka attrition secara real-time melalui metrik KPI.
    - Melakukan intervensi yang lebih tertarget dengan memfilter data berdasarkan departemen.
    - Melihat visualisasi faktor penyebab secara langsung tanpa perlu melakukan pengolahan data manual yang rumit.

4. Rekomendasi Strategis untuk Perusahaan. Sebagai tindak lanjut dari temuan proyek, perusahaan disarankan untuk:
    - Evaluasi Kebijakan Lembur: Mengurangi beban kerja berlebih untuk mencegah burnout.
    - Peninjauan Karir: Memperjelas jalur promosi dan pengembangan diri bagi karyawan potensial.
    - Penyesuaian Kompensasi: Melakukan benchmarking gaji untuk memastikan kompensasi tetap kompetitif di pasar.


### Rekomendasi Action Items (Optional)
Berdasarkan hasil analisis data dan identifikasi faktor-faktor pemicu attrition pada Jaya Jaya Maju, berikut adalah beberapa action items strategis yang direkomendasikan untuk menekan angka pengunduran diri hingga di bawah 10%:
  1. Evaluasi dan Redesain Kebijakan Lembur (Work-Life Balance) Analisis menunjukkan korelasi kuat antara Overtime dan Attrition. Perusahaan perlu meninjau kembali beban kerja di departemen dengan tingkat lembur tinggi (seperti R&D atau Sales). Solusinya bisa berupa penambahan personil, otomatisasi tugas rutin, atau penerapan sistem kompensasi lembur yang lebih adil dan transparan.

  2. Optimalisasi Jalur Karir dan Promosi Internal Karyawan yang stagnan lebih dari 3 tahun tanpa promosi ditemukan lebih rentan untuk keluar. Perusahaan harus mengimplementasikan program Career Path yang jelas, melakukan Performance Review berkala yang berorientasi pada pengembangan, serta memprioritaskan rekrutmen internal untuk posisi manajerial.

  3. Penyesuaian Struktur Kompensasi Berbasis Level Jabatan Perlu dilakukan benchmarking gaji, terutama untuk level jabatan menengah ke bawah yang memiliki Monthly Income rendah namun beban kerja tinggi. Pastikan kenaikan gaji (Percent Salary Hike) selaras dengan penilaian kinerja (Performance Rating) untuk meningkatkan loyalitas.

  4. Program Retensi Khusus untuk Peran Kritis Fokuskan intervensi pada jabatan dengan attrition rate tertinggi, seperti Sales Executive dan Lab Technician. Berikan insentif non-finansial seperti fleksibilitas kerja, program pelatihan/sertifikasi, atau lingkungan kerja yang lebih suportif berdasarkan skor Environment Satisfaction yang rendah.
  
  5. Pemanfaatan Dashboard untuk Monitoring Proaktif Manajemen HR harus menggunakan Business Dashboard yang telah dibuat sebagai alat monitor bulanan. Dengan mendeteksi tren attrition lebih awal di departemen tertentu, HR dapat melakukan diskusi dua arah (Stay Interview) sebelum karyawan memutuskan untuk mengundurkan diri.
