# Proyek Akhir: Menyelesaikan Permasalahan Perusahaan Edutech

## Business Understanding
Jaya Jaya Maju adalah sebuah perusahaan multinasional yang memiliki skala operasional besar. Berdiri sejak tahun 2000, perusahaan ini telah tumbuh secara signifikan hingga memiliki aset sumber daya manusia yang besar, yakni lebih dari 1.000 karyawan yang tersebar di berbagai wilayah di seluruh negeri. Sebagai pemain lama di industri, stabilitas operasional menjadi kunci keberlangsungan bisnis mereka.


### Permasalahan Bisnis
1. Tingginya Attrition Rate perusahaan masalah utama yang dihadapi adalah rasio jumlah karyawan yang keluar (attrition rate) telah mencapai angka di atas 10%. Hal ini dianggap mengkhawatirkan bagi stabilitas operasional perusahaan yang memiliki lebih dari 1000 karyawan.

2. Permasalahan (Problem Statement)
    - Tingginya Angka Atrisi: Perusahaan menghadapi hilangnya talenta yang signifikan, terutama pada departemen krusial seperti Sales dan R&D.
    - Stagnasi Karier: Adanya indikasi karyawan meninggalkan perusahaan karena masa tunggu promosi yang terlalu lama (stagnasi).
    - Isu Work-Life Balance: Kebijakan lembur yang intensif berkorelasi langsung dengan keputusan karyawan untuk mengundurkan diri.
    - Ketidakseimbangan Kompensasi: Adanya potensi ketimpangan gaji pada level jabatan tertentu yang memicu ketidakpuasan karyawan.

3. Cakupan Proyek (Project Scope)
    - Analisis Data Historis: Mengolah data karyawan Jaya Jaya Maju untuk mengidentifikasi pola pengunduran diri.
    - Visualisasi Dashboard: Membangun HR Business Dashboard menggunakan Tableau untuk memonitor metrik atrisi secara real-time.
    - Identifikasi Feature Importance: Menentukan faktor-faktor utama (seperti usia, pendapatan, dan lembur) yang paling memengaruhi atrisi.
    - Segmentasi Departemen: Melakukan drill-down analisis berdasarkan departemen dan tingkat jabatan untuk menemukan titik kritis permasalahan.


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

7.  Hasil analisis mengarahkan pada faktor-faktor seperti berikut:
    - Beban Kerja (Overtime): Mengevaluasi kaitan antara jam kerja tambahan dengan kecenderungan karyawan untuk keluar.
    - Kompensasi: Menganalisis apakah tingkat gaji bulanan (Monthly Income) dan kenaikan gaji (Percent Salary Hike) sudah kompetitif untuk mempertahankan karyawan.
    - Stagnasi Karir: Mengidentifikasi apakah lamanya waktu sejak promosi terakhir (Years Since Last Promotion) memicu keluarnya karyawan.
    - Kepuasan Kerja & Lingkungan: Meninjau skor kepuasan kerja (Job Satisfaction) dan kepuasan lingkungan (Environment Satisfaction) terhadap status attrition

8.  Permasalahan ini diselesaikan dengan membangun business dashboard yang mencakup:
    - KPI Utama: Memantau jumlah total karyawan, jumlah karyawan yang keluar, serta persentase attrition secara keseluruhan.
    - Demografi & Peran: Memetakan departemen (seperti Sales atau Research & Development) dan posisi pekerjaan yang paling rentan mengalami pengunduran diri.
    - Filter Interaktif: Memungkinkan manajer HR untuk menyaring data berdasarkan departemen tertentu guna pengambilan keputusan yang lebih spesifik.


### Persiapan
Sumber data: `employee_data.csv` https://github.com/dicodingacademy/dicoding_dataset/blob/main/employee/employee_data.csv

Setup environment: Untuk menjalankan analisis data dan dashboard interaktif Jaya Jaya Maju, perlu mempersiapkan perangkat lunak, pustaka Python, dan struktur folder yang sesuai.


#### Install Perangkat Lunak Utama 
Memastikan perangkat lunak berikut sudah terinstal di komputer, berikut yang harus di install:
* **Python (Versi 3.14 atau lebih baru):** Bahasa pemrograman utama.
* **Visual Studio Code (VS Code):** Rekomendasi editor kode untuk menjalankan skrip Python dan Jupyter Notebook.
* **Web Browser:** Untuk menampilkan Dashboard Streamlit.

#### Install Perangkat lunak kedua
1. Setelah Pyhton dan Visual Studio Code (VS Code) terinstall di PC/Laptop, selanjutnya bisa membuka VS Code. Setelah VS Code terbuka cari icon Extensions biasanya di layar bagian kiri ketikan Python pada Search Extensions in Marketplace, selanjutnya install Extension Python setelah itu  klik tulisan "Terminal" di pojok kiri atas setelah itu muncul dashboard TERMINAL dan ketikan pada TERMINAL 
```bash
python --version  # untuk mengtahui python berhasil terinstall atau terhubung dengan VS Code
```
jika sudah muncul "Python 3.14.2" tandanya sudah terinstall. Tulisan "Python 3.14.2" yang muncul bisa jika versi yang digunakan berbeda. 

2. Selanjutnya pastikan sudah memiliki file-file berikut dalam satu folder proyek:
    - notebook.ipynb
    - prediction.py
    - employee_data.csv (wajib ada karena script prediction.py membacanya)
    - requirements.txt (jika belum ada, bisa membuatnya berdasarkan library yang digunakan di file yang telah di download).

3. Jika baru pertama kali mendapatkan folder proyek (yang berisi prediction.py dan notebook.ipynb). Library yang harus dimiliki yaitu pandas, streamlit, scikit-learn, matplotlib, seaborn, dan joblib. Jika belum ada requirements.txt, jalankan:
```bash
   pip install pandas numpy matplotlib seaborn streamlit joblib
``` 
- Pandas: Untuk manipulasi dan analisis data CSV.
- Matplotlib & Seaborn: Untuk pembuatan grafik dan visualisasi data.
- Streamlit: Framework untuk membangun dashboard bisnis interaktif.
- Joblib: Untuk menyimpan dan memuat model yang telah dilatih.

4. Selnajutnya menginstal library pihak ketiga yang digunakan dalam kode `prediction.py` library ini tidak datang secara bawaan saat perlu di instal secara manual di Python dengan perintah berikut:
```bash 
pip install plotly xgboost scikit-learn
```
- Scikit-learn: Untuk pemodelan machine learning (Random Forest) guna memprediksi attrition.
- xgboost: Memprediksi data terstruktur/tabular dengan cepat dan akurat.

5. Terkahir jalankan Streamlit prediction.py dengan mengetik perintah berikut di terminal:

pastikan folder sudah benar (sesuai langkah No. 2)
```bash
streamlit run prediction.py
```
6. Selanjutnya Install All the Requirements Inside "requirements.txt" dengan mengetik perintah beriktu di terminal:
```bash
pip install -r requirements.txt 
```

### Business Dashboard

#### Link Akses Dashboard 

* **Streamlit:** https://datascienceproject-ja5ymavaprmywgbxsyqvjm.streamlit.app/ 


#### Deep Dive Analysis (Bar Charts with Percentages)
##### 1. Grafik Faktor Utama: OverTime
Grafik Faktor Utama: OverTime menunjukkan perbandingan jumlah karyawan yang resign dan tetap bekerja (stayed) berdasarkan status lembur. Dari grafik terlihat bahwa sebagian besar karyawan yang tidak melakukan lembur (No) tetap bekerja di perusahaan, yaitu sekitar 670 orang (89,2%), sementara 81 orang (10,8%) memilih resign. Sebaliknya, pada kelompok karyawan yang melakukan lembur (Yes), jumlah karyawan yang resign relatif lebih tinggi dibandingkan kelompok yang tidak lembur, yaitu 98 orang (31,9%), sedangkan 209 orang (68,1%) tetap bekerja.
Data ini menunjukkan bahwa proporsi karyawan yang keluar dari perusahaan lebih besar pada kelompok yang sering melakukan lembur. Hal ini mengindikasikan bahwa beban kerja tambahan atau waktu kerja yang lebih panjang dapat mempengaruhi keputusan karyawan untuk meninggalkan perusahaan.
###### Kesimpulan Grafik OverTime
Karyawan yang sering melakukan lembur memiliki kemungkinan resign lebih tinggi dibandingkan karyawan yang tidak lembur, sehingga perusahaan perlu mengelola beban kerja dan jam kerja secara lebih seimbang untuk mengurangi tingkat attrition.

##### 2. Level Pekerjaan (Job Level)
Berdasarkan data employee_data.csv yang diolah menggunakan script Python siap.py, grafik Level Pekerjaan (Job Level) menunjukkan perbandingan jumlah karyawan yang resign dan tetap bekerja (stayed) berdasarkan tingkat jabatan dalam perusahaan yang dikategorikan dari level 1 hingga level 5.
Grafik tersebut memperlihatkan bahwa pada Job Level 1, jumlah karyawan yang resign relatif paling tinggi dibandingkan level lainnya, yaitu sekitar 108 orang (27,4%), sedangkan 286 orang (72,6%) tetap bekerja. Pada Job Level 2, tingkat resign menurun secara signifikan dengan 37 orang (10,2%) yang resign dan 327 orang (89,8%) tetap bekerja. Pada Job Level 3, jumlah karyawan yang resign sekitar 25 orang (15,2%), sementara 140 orang (84,8%) tetap bertahan di perusahaan. Selanjutnya pada Job Level 4, tingkat resign menjadi sangat rendah yaitu sekitar 4 orang (5,0%), dengan 76 orang (95,0%) tetap bekerja. Hal yang sama juga terlihat pada Job Level 5, di mana hanya 5 orang (9,1%) yang resign dan 50 orang (90,9%) tetap bekerja.
Data tersebut menunjukkan bahwa karyawan pada level jabatan yang lebih rendah cenderung memiliki tingkat attrition yang lebih tinggi dibandingkan karyawan pada level jabatan yang lebih tinggi. Hal ini dapat disebabkan oleh peluang karier yang lebih terbatas, tingkat gaji yang lebih rendah, atau keinginan untuk mencari kesempatan kerja yang lebih baik di tempat lain.
###### Kesimpulan Grafik Job Level
Karyawan pada level pekerjaan yang lebih rendah memiliki tingkat resign yang lebih tinggi, sedangkan karyawan dengan jabatan yang lebih tinggi cenderung lebih loyal terhadap perusahaan, sehingga perusahaan perlu memberikan peluang pengembangan karier dan peningkatan kompensasi bagi karyawan pada level awal untuk mengurangi tingkat attrition.

#### 3. Grafik Work-Life Balance (1  Buruk, 4  Sangat Baik)
Grafik Work-Life Balance menunjukkan perbandingan jumlah karyawan yang resign dan tetap bekerja (stayed) berdasarkan tingkat keseimbangan antara kehidupan kerja dan kehidupan pribadi yang dinilai dalam skala 1 hingga 4, di mana nilai yang lebih tinggi menunjukkan keseimbangan yang lebih baik.
Dari grafik terlihat bahwa pada tingkat Work-Life Balance yang rendah (level 1), proporsi karyawan yang resign cukup tinggi yaitu sekitar 18 orang (32,1%), sedangkan 38 orang (67,9%) tetap bekerja. Pada level 2, jumlah karyawan yang resign masih cukup signifikan yaitu 45 orang (17,9%), sementara 206 orang (82,1%) tetap bekerja. Pada level 3, jumlah karyawan yang tetap bekerja meningkat cukup besar yaitu 544 orang (85,3%), dengan 94 orang (14,7%) yang resign. Sementara pada level 4, sebagian besar karyawan tetap bekerja yaitu sekitar 91 orang (80,5%), dan hanya 22 orang (19,5%) yang resign.
Hal ini menunjukkan bahwa karyawan yang memiliki keseimbangan kerja dan kehidupan pribadi yang lebih baik cenderung lebih bertahan di perusahaan.
##### Kesimpulan Grafik Work-Life Balance
Semakin baik keseimbangan antara pekerjaan dan kehidupan pribadi, semakin rendah kemungkinan karyawan untuk resign, sehingga perusahaan perlu mendukung kebijakan kerja yang fleksibel dan beban kerja yang seimbang.


## Conclusion
Berdasarkan analisis terhadap faktor lembur, tingkat jabatan, dan keseimbangan kehidupan kerja (Work-Life Balance), dapat disimpulkan bahwa beban kerja dan stabilitas karier merupakan pendorong utama keputusan karyawan untuk meninggalkan perusahaan (attrition).
1.	Tekanan Kerja (Lembur & WLB): Terdapat korelasi kuat antara beban kerja berlebih dan pengunduran diri. Karyawan yang lembur memiliki risiko resign 3x lebih besar dibanding yang tidak, dan mereka dengan skor Work-Life Balance rendah (level 1) menunjukkan tingkat ketidakpuasan yang signifikan.
2.	Kerentanan Level Awal: Karyawan pada Job Level 1 adalah kelompok yang paling rentan dengan tingkat attrition tertinggi (27,4%). Hal ini menunjukkan adanya masalah retensi pada posisi entry-level, yang kemungkinan dipicu oleh kompensasi yang belum kompetitif atau jalur karier yang kurang jelas.
3.	Loyalitas di Level Atas: Seiring naiknya jabatan (Level 4 & 5), loyalitas karyawan meningkat secara drastis, yang mengindikasikan bahwa investasi jangka panjang perusahaan pada level senior jauh lebih stabil.


### Rekomendasi Action Items (Optional)
Untuk menekan tingkat attrition dan meningkatkan retensi karyawan, berikut adalah rekomendasi tindakan yang dapat diambil:
1. Manajemen Beban Kerja & Kebijakan Lembur
   - Evaluasi Kapasitas Tim: Melakukan audit beban kerja pada departemen yang memiliki frekuensi lembur tinggi untuk menentukan apakah perlu ada penambahan personel atau redistribusi tugas.
   - Insentif & Kompensasi Lembur: Memastikan skema kompensasi lembur tetap kompetitif dan memberikan penghargaan non-finansial (seperti time-off tambahan) bagi mereka yang sering bekerja ekstra.
2. Penguatan Program Retensi untuk Job Level 1
   - Career Path Planning: Menyusun peta jalan karier (career roadmap) yang jelas bagi karyawan level awal agar mereka melihat masa depan jangka panjang di perusahaan.
   - Mentorship Program: Menghubungkan karyawan level 1 dengan mentor dari level 4 atau 5 untuk meningkatkan keterikatan emosional dan profesional terhadap perusahaan.
   - Review Gaji & Benefit: Melakukan benchmarking gaji khususnya untuk posisi level awal agar tetap kompetitif di pasar tenaga kerja.
3. Peningkatan Kualitas Work-Life Balance
   - Fleksibilitas Kerja: Menerapkan kebijakan kerja fleksibel (seperti remote working atau flexible hours) untuk membantu karyawan mencapai keseimbangan hidup yang lebih baik.
   - Budaya "Right to Disconnect": Mendorong budaya perusahaan yang menghormati waktu pribadi karyawan di luar jam kerja resmi untuk mencegah burnout.
4. Monitoring & Feedback Berkala
   - Survei Kepuasan Proaktif: Melakukan survei Work-Life Balance secara berkala, terutama bagi tim yang teridentifikasi memiliki jam lembur tinggi, sebelum mereka mencapai titik jenuh.
   - Exit Interview Mendalam: Fokus mendalami alasan spesifik pada karyawan Level 1 yang resign untuk terus memperbarui strategi retensi.

