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
* **Python (Versi 3.8 atau lebih baru):** Bahasa pemrograman utama.
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

#### Machine Learning Models & Insights 
##### 1. Grafik Logistic Regression (Accuracy: 83.02%)
Grafik Logistic Regression menampilkan nilai koefisien dari setiap fitur yang digunakan dalam model untuk memprediksi attrition karyawan. Nilai koefisien menunjukkan seberapa besar pengaruh suatu variabel terhadap kemungkinan karyawan keluar dari perusahaan. Koefisien yang bernilai positif menunjukkan bahwa variabel tersebut meningkatkan peluang karyawan untuk resign, sedangkan koefisien yang bernilai negatif menunjukkan bahwa variabel tersebut menurunkan kemungkinan resign.
Berdasarkan grafik tersebut, beberapa variabel seperti OverTime, WorkLifeBalance, dan JobSatisfaction memiliki pengaruh yang cukup signifikan terhadap attrition karyawan. Hal ini menunjukkan bahwa karyawan yang sering bekerja lembur, memiliki keseimbangan kerja-hidup yang buruk, atau memiliki tingkat kepuasan kerja yang rendah cenderung lebih berpotensi untuk keluar dari perusahaan. Selain itu, faktor lain seperti MonthlyIncome, YearsAtCompany, dan JobLevel juga turut mempengaruhi keputusan karyawan untuk tetap bekerja atau resign.””
###### Kesimpulan Grafik Logistic Regression
Model Logistic Regression dengan akurasi 83.02% menunjukkan bahwa faktor utama yang mempengaruhi attrition adalah lembur (OverTime), kepuasan kerja, dan keseimbangan kerja-hidup, sehingga perusahaan perlu memperhatikan beban kerja dan meningkatkan kepuasan karyawan untuk mengurangi tingkat resign.

##### 2. Grafik Decision Tree (Accuracy: 85.85%)
Grafik Decision Tree: Feature Importance menunjukkan tingkat kepentingan setiap variabel dalam proses pengambilan keputusan model Decision Tree untuk memprediksi apakah seorang karyawan akan resign atau tetap bekerja. Nilai importance menggambarkan seberapa besar kontribusi suatu fitur dalam membangun pohon keputusan dan menentukan hasil prediksi.
Berdasarkan grafik tersebut, variabel Age dan MonthlyIncome memiliki nilai importance paling tinggi dibandingkan variabel lainnya. Hal ini menunjukkan bahwa usia dan tingkat pendapatan merupakan faktor yang sangat berpengaruh dalam menentukan kemungkinan karyawan keluar dari perusahaan. Selain itu, faktor OverTime juga memiliki pengaruh yang cukup besar, yang menunjukkan bahwa frekuensi lembur dapat meningkatkan potensi attrition. Variabel lain seperti YearsAtCompany, EnvironmentSatisfaction, dan JobSatisfaction juga berperan dalam model, meskipun pengaruhnya tidak sebesar variabel utama. Sementara itu, WorkLifeBalance dan JobLevel memiliki tingkat pengaruh yang relatif lebih rendah.
###### Kesimpulan Grafik Decision Tree
Model Decision Tree dengan akurasi 85.85% menunjukkan bahwa usia, pendapatan bulanan, dan lembur merupakan faktor utama yang mempengaruhi kemungkinan karyawan resign, sehingga perusahaan perlu memperhatikan kesejahteraan finansial dan beban kerja karyawan untuk mengurangi tingkat attrition.

##### 3. Grafik K-Nearest Neighbors (Accuracy: 83.96%)
Grafik Prediksi KNN: Sebaran Usia vs Gaji menunjukkan distribusi karyawan berdasarkan usia (Age) dan pendapatan bulanan (MonthlyIncome) yang kemudian diprediksi oleh model K-Nearest Neighbors (KNN) untuk menentukan kemungkinan attrition. Model KNN bekerja dengan cara mengelompokkan karyawan berdasarkan kemiripan profil dengan karyawan lain yang memiliki karakteristik serupa.
Dari grafik tersebut terlihat bahwa karyawan tersebar pada berbagai kelompok usia dan tingkat pendapatan. Sebagian besar karyawan berada pada rentang usia sekitar 25 hingga 40 tahun dengan pendapatan bulanan yang relatif bervariasi. Model KNN memprediksi kemungkinan attrition dengan melihat kedekatan posisi data dengan karyawan lain yang memiliki pola serupa. Dengan demikian, jika seorang karyawan memiliki profil yang mirip dengan karyawan yang sebelumnya resign, maka kemungkinan besar model juga akan memprediksi bahwa karyawan tersebut berpotensi resign.
###### Kesimpulan Grafik KNN
Model K-Nearest Neighbors dengan akurasi 83.96% menunjukkan bahwa kemiripan profil karyawan berdasarkan usia dan pendapatan dapat digunakan untuk memprediksi kemungkinan attrition, sehingga perusahaan dapat mengidentifikasi kelompok karyawan yang memiliki risiko resign lebih tinggi.

##### 4. Grafik Random Forest (Accuracy: 85.85%)
Grafik Random Forest menunjukkan tingkat kepentingan (feature importance) dari setiap variabel dalam memprediksi attrition karyawan. Berbeda dengan Logistic Regression yang menggunakan koefisien, Random Forest mengukur seberapa besar kontribusi setiap fitur dalam proses pengambilan keputusan pada kumpulan pohon keputusan (decision trees).
Dari grafik tersebut terlihat bahwa beberapa variabel seperti MonthlyIncome, Age, dan YearsAtCompany  memiliki nilai importance yang relatif lebih tinggi dibandingkan variabel lainnya. Hal ini menunjukkan bahwa faktor finansial, kepuasan kerja, serta pengalaman kerja di perusahaan memiliki peran besar dalam menentukan apakah seorang karyawan akan bertahan atau meninggalkan perusahaan. Variabel lain seperti Age, JobLevel, dan EnvironmentSatisfaction juga memberikan kontribusi dalam model, meskipun pengaruhnya tidak sebesar variabel utama.
###### Kesimpulan Grafik Random Forest
Model Random Forest dengan akurasi 85.85% menunjukkan bahwa pendapatan bulanan, lembur, kepuasan kerja, dan lama bekerja di perusahaan merupakan faktor paling penting dalam menentukan attrition karyawan, sehingga perusahaan perlu meningkatkan kesejahteraan serta menciptakan lingkungan kerja yang lebih nyaman untuk mempertahankan karyawan.

##### 5. Grafik XGBoost (Accuracy: 83.96%)
Grafik XGBoost: Feature Importance menunjukkan kontribusi masing-masing fitur dalam model XGBoost untuk memprediksi attrition karyawan. Model ini menggunakan metode gradient boosting, yaitu menggabungkan beberapa pohon keputusan untuk meningkatkan performa prediksi.
Dari grafik tersebut terlihat bahwa variabel OverTime memiliki nilai importance paling tinggi dibandingkan variabel lainnya. Hal ini menunjukkan bahwa karyawan yang sering bekerja lembur memiliki kemungkinan lebih besar untuk keluar dari perusahaan. Selain itu, faktor EnvironmentSatisfaction, JobLevel, dan JobSatisfaction juga memiliki kontribusi cukup besar dalam model, yang menunjukkan bahwa kondisi lingkungan kerja, tingkat jabatan, serta kepuasan kerja dapat mempengaruhi keputusan karyawan untuk bertahan atau resign. Variabel lain seperti WorkLifeBalance, YearsAtCompany, Age, dan MonthlyIncome tetap memberikan kontribusi dalam model meskipun tingkat pengaruhnya lebih kecil.
###### Kesimpulan Grafik XGBoost
Model XGBoost dengan akurasi 83.96% menunjukkan bahwa lembur (OverTime), kepuasan terhadap lingkungan kerja, dan tingkat jabatan merupakan faktor penting dalam memprediksi attrition karyawan, sehingga perusahaan perlu meningkatkan kualitas lingkungan kerja serta mengelola beban kerja karyawan dengan lebih baik.

##### 6. Grafik Clustering (Segmentasi Karyawan - K-Means)
Grafik Segmentasi Karyawan (K-Means) menunjukkan hasil pengelompokan karyawan menggunakan algoritma K-Means Clustering berdasarkan variabel Age dan MonthlyIncome. Metode ini mengelompokkan karyawan ke dalam beberapa segmen berdasarkan kemiripan karakteristik tanpa menggunakan label attrition sebagai target utama.
Dari grafik tersebut terlihat bahwa karyawan terbagi menjadi tiga kelompok utama (cluster). Cluster pertama umumnya terdiri dari karyawan dengan usia relatif muda dan pendapatan yang lebih rendah. Cluster kedua terdiri dari karyawan dengan usia menengah dan pendapatan yang lebih stabil. Sementara cluster ketiga berisi karyawan dengan usia yang lebih tinggi serta pendapatan yang lebih besar. Selain itu, distribusi status karyawan yang resign dan tetap bekerja juga dapat terlihat dalam setiap cluster, yang menunjukkan bahwa pola attrition dapat berbeda pada setiap kelompok karyawan.
###### Kesimpulan Grafik Clustering
Hasil Clustering K-Means menunjukkan bahwa karyawan dapat dikelompokkan menjadi beberapa segmen berdasarkan usia dan tingkat pendapatan, sehingga perusahaan dapat merancang strategi retensi karyawan yang berbeda untuk setiap kelompok guna mengurangi tingkat attrition.

#### Deep Learning & Pattern Analysis
##### 1. Grafik Neural Networks (Accuracy: 82.08%)
Grafik ANN Feature Activation menunjukkan tingkat aktivitas atau pengaruh setiap fitur dalam model Artificial Neural Network (ANN) untuk memprediksi apakah seorang karyawan akan resign atau tetap bekerja. Semakin besar nilai aktivitas suatu fitur, semakin besar pula kontribusinya dalam menentukan prediksi attrition.
Dari grafik terlihat bahwa beberapa variabel memiliki pengaruh paling besar terhadap keputusan karyawan untuk keluar dari perusahaan, yaitu MonthlyIncome, JobSatisfaction, WorkLifeBalance, dan OverTime. Hal ini menunjukkan bahwa faktor ekonomi dan keseimbangan kehidupan kerja memiliki peranan penting dalam menentukan loyalitas karyawan. Selain itu, variabel seperti YearsAtCompany, Age, dan JobLevel juga memiliki pengaruh yang cukup signifikan, yang menunjukkan bahwa pengalaman kerja dan posisi jabatan juga turut mempengaruhi keputusan resign. Sementara itu, EnvironmentSatisfaction tetap berperan tetapi memiliki tingkat aktivitas yang relatif lebih rendah dibandingkan faktor lainnya.
###### Kesimpulan Grafik Neural Network
Model Neural Network dengan akurasi 82.08% menunjukkan bahwa pendapatan bulanan, kepuasan kerja, keseimbangan kerja-hidup, dan lembur merupakan faktor utama yang mempengaruhi attrition karyawan. Artinya, perusahaan perlu meningkatkan kesejahteraan finansial serta menciptakan lingkungan kerja yang lebih seimbang agar dapat menekan tingkat resign.

##### 2. Grafik Interaksi Pola Kompleks (Heatmap Age vs Monthly Income)
Grafik kedua merupakan heatmap interaksi antara Age dan MonthlyIncome terhadap rata-rata attrition. Warna pada heatmap menunjukkan peluang resign, dimana warna yang semakin terang menandakan tingkat attrition yang semakin tinggi.
Dari visualisasi terlihat bahwa tingkat resign paling tinggi berada pada kelompok karyawan berusia muda dengan pendapatan relatif rendah. Hal ini menunjukkan bahwa karyawan yang masih berada di tahap awal karier cenderung lebih mudah berpindah pekerjaan, terutama jika kompensasi yang diterima tidak cukup kompetitif. Sebaliknya, karyawan dengan usia yang lebih tinggi dan pendapatan yang lebih besar cenderung memiliki tingkat attrition yang lebih rendah, yang menunjukkan stabilitas karier dan loyalitas yang lebih tinggi terhadap perusahaan.
Selain itu, heatmap juga menunjukkan bahwa pada kelompok usia menengah dengan pendapatan yang lebih tinggi, tingkat attrition relatif lebih rendah. Hal ini mengindikasikan bahwa peningkatan gaji dan perkembangan karier dapat menjadi faktor penting dalam mempertahankan karyawan.
###### Kesimpulan Grafik Heatmap
Peluang resign paling tinggi terjadi pada karyawan muda dengan pendapatan rendah, sedangkan karyawan yang lebih senior dengan gaji lebih tinggi cenderung lebih loyal. Oleh karena itu, perusahaan perlu memberikan jalur karier yang jelas dan kompensasi yang kompetitif bagi karyawan muda untuk mengurangi risiko attrition di masa depan.

#### Deep Dive Analysis (Bar Charts with Percentages)
##### 1. Grafik Faktor Utama: OverTime
Grafik Faktor Utama: OverTime menunjukkan perbandingan jumlah karyawan yang resign dan tetap bekerja (stayed) berdasarkan status lembur. Dari grafik terlihat bahwa sebagian besar karyawan yang tidak melakukan lembur (No) tetap bekerja di perusahaan, yaitu sekitar 670 orang (89,2%), sementara 81 orang (10,8%) memilih resign. Sebaliknya, pada kelompok karyawan yang melakukan lembur (Yes), jumlah karyawan yang resign relatif lebih tinggi dibandingkan kelompok yang tidak lembur, yaitu 98 orang (31,9%), sedangkan 209 orang (68,1%) tetap bekerja.
Data ini menunjukkan bahwa proporsi karyawan yang keluar dari perusahaan lebih besar pada kelompok yang sering melakukan lembur. Hal ini mengindikasikan bahwa beban kerja tambahan atau waktu kerja yang lebih panjang dapat mempengaruhi keputusan karyawan untuk meninggalkan perusahaan.
###### Kesimpulan Grafik OverTime
Karyawan yang sering melakukan lembur memiliki kemungkinan resign lebih tinggi dibandingkan karyawan yang tidak lembur, sehingga perusahaan perlu mengelola beban kerja dan jam kerja secara lebih seimbang untuk mengurangi tingkat attrition.

##### 2. Grafik Kepuasan Lingkungan Kerja (Environment Satisfaction 1–4)
Grafik Kepuasan Lingkungan Kerja menunjukkan perbandingan jumlah karyawan yang resign dan tetap bekerja berdasarkan tingkat kepuasan terhadap lingkungan kerja yang dinilai dari skala 1 hingga 4. Skala yang lebih tinggi menunjukkan tingkat kepuasan yang lebih baik terhadap kondisi lingkungan kerja di perusahaan.
Dari grafik terlihat bahwa pada tingkat kepuasan lingkungan kerja yang rendah (level 1), jumlah karyawan yang resign relatif lebih tinggi yaitu sekitar 57 orang (27,3%), dibandingkan dengan tingkat kepuasan yang lebih tinggi. Seiring meningkatnya tingkat kepuasan lingkungan kerja dari level 2 hingga 4, persentase karyawan yang resign cenderung menurun. Pada tingkat kepuasan tertinggi (level 4), sebagian besar karyawan tetap bekerja di perusahaan yaitu sekitar 274 orang (87,3%), sementara yang resign hanya 40 orang (12,7%).
Hal ini menunjukkan bahwa semakin tinggi tingkat kepuasan terhadap lingkungan kerja, semakin besar kemungkinan karyawan untuk bertahan di perusahaan.
###### Kesimpulan Grafik Kepuasan Lingkungan Kerja
Karyawan dengan kepuasan lingkungan kerja yang rendah memiliki kemungkinan resign lebih tinggi, sehingga perusahaan perlu meningkatkan kualitas lingkungan kerja agar dapat mempertahankan karyawan.

##### 3. Level Pekerjaan (Job Level)
Berdasarkan data employee_data.csv yang diolah menggunakan script Python siap.py, grafik Level Pekerjaan (Job Level) menunjukkan perbandingan jumlah karyawan yang resign dan tetap bekerja (stayed) berdasarkan tingkat jabatan dalam perusahaan yang dikategorikan dari level 1 hingga level 5.
Grafik tersebut memperlihatkan bahwa pada Job Level 1, jumlah karyawan yang resign relatif paling tinggi dibandingkan level lainnya, yaitu sekitar 108 orang (27,4%), sedangkan 286 orang (72,6%) tetap bekerja. Pada Job Level 2, tingkat resign menurun secara signifikan dengan 37 orang (10,2%) yang resign dan 327 orang (89,8%) tetap bekerja. Pada Job Level 3, jumlah karyawan yang resign sekitar 25 orang (15,2%), sementara 140 orang (84,8%) tetap bertahan di perusahaan. Selanjutnya pada Job Level 4, tingkat resign menjadi sangat rendah yaitu sekitar 4 orang (5,0%), dengan 76 orang (95,0%) tetap bekerja. Hal yang sama juga terlihat pada Job Level 5, di mana hanya 5 orang (9,1%) yang resign dan 50 orang (90,9%) tetap bekerja.
Data tersebut menunjukkan bahwa karyawan pada level jabatan yang lebih rendah cenderung memiliki tingkat attrition yang lebih tinggi dibandingkan karyawan pada level jabatan yang lebih tinggi. Hal ini dapat disebabkan oleh peluang karier yang lebih terbatas, tingkat gaji yang lebih rendah, atau keinginan untuk mencari kesempatan kerja yang lebih baik di tempat lain.
###### Kesimpulan Grafik Job Level
Karyawan pada level pekerjaan yang lebih rendah memiliki tingkat resign yang lebih tinggi, sedangkan karyawan dengan jabatan yang lebih tinggi cenderung lebih loyal terhadap perusahaan, sehingga perusahaan perlu memberikan peluang pengembangan karier dan peningkatan kompensasi bagi karyawan pada level awal untuk mengurangi tingkat attrition.

##### 4. Grafik Masa Kerja & Usia (Kelompok Usia)
Grafik Masa Kerja & Usia (Kelompok Usia) menunjukkan distribusi karyawan yang resign dan tetap bekerja berdasarkan kelompok usia, yaitu 18–30 tahun, 31–40 tahun, 41–50 tahun, dan 51–60 tahun. Dari grafik tersebut terlihat bahwa kelompok usia 31–40 tahun memiliki jumlah karyawan terbanyak yang tetap bekerja, yaitu sekitar 364 orang (85,2%), dengan 63 orang (14,8%) yang resign. Pada kelompok usia 18–30 tahun, jumlah karyawan yang resign relatif lebih tinggi yaitu 73 orang (26,3%), dibandingkan kelompok usia lainnya.
Sementara itu, kelompok usia 41–50 tahun dan 51–60 tahun menunjukkan tingkat resign yang lebih rendah, masing-masing sekitar 11,4% dan 11,9%. Hal ini menunjukkan bahwa karyawan dengan usia yang lebih matang cenderung memiliki tingkat loyalitas yang lebih tinggi terhadap perusahaan dibandingkan karyawan yang lebih muda.
###### Kesimpulan Grafik Kelompok Usia
Karyawan berusia muda (18–30 tahun) memiliki tingkat resign lebih tinggi dibandingkan kelompok usia yang lebih tua, sehingga perusahaan perlu memberikan peluang pengembangan karier, pelatihan, dan kompensasi yang menarik untuk mempertahankan karyawan muda.

##### 5. Grafik Hubungan Kerja (Relationship Satisfaction)
Grafik Hubungan Kerja (Relationship Satisfaction) menunjukkan perbandingan jumlah karyawan yang resign dan tetap bekerja berdasarkan tingkat kepuasan terhadap hubungan kerja dengan rekan kerja atau atasan. Tingkat kepuasan ini juga diukur menggunakan skala 1 hingga 4, di mana nilai yang lebih tinggi menunjukkan hubungan kerja yang lebih baik.
Dari grafik terlihat bahwa pada tingkat kepuasan hubungan kerja yang rendah (level 1), jumlah karyawan yang resign cukup tinggi yaitu sekitar 46 orang (22,9%). Namun, ketika tingkat kepuasan hubungan kerja meningkat, persentase karyawan yang tetap bekerja juga semakin besar. Pada tingkat kepuasan yang lebih tinggi seperti level 3 dan 4, sebagian besar karyawan memilih untuk tetap bekerja di perusahaan dengan persentase sekitar 84–85%, sementara jumlah karyawan yang resign relatif lebih kecil.
Hal ini menunjukkan bahwa hubungan kerja yang baik dengan rekan kerja maupun atasan dapat meningkatkan loyalitas karyawan terhadap perusahaan.
###### Kesimpulan Grafik Hubungan Kerja
Karyawan yang memiliki hubungan kerja yang baik dengan rekan kerja dan atasan cenderung lebih bertahan di perusahaan, sehingga perusahaan perlu membangun budaya kerja yang positif dan kolaboratif untuk menekan tingkat attrition.

#### Strategic Insights: Faktor Penentu Attrition
##### A. Grafik Distribusi Gaji: Karywan Resign Cederung Bergaji Rendah 
Grafik Attrition Status menunjukkan perbandingan jumlah karyawan yang resign dan yang tetap bekerja (stayed) di perusahaan. Dari grafik tersebut terlihat bahwa jumlah karyawan yang tetap bekerja jauh lebih besar dibandingkan dengan jumlah karyawan yang keluar dari perusahaan. Hal ini menunjukkan bahwa secara umum sebagian besar karyawan masih memilih untuk bertahan di perusahaan.
Meskipun demikian, masih terdapat sejumlah karyawan yang memutuskan untuk resign, yang menunjukkan adanya faktor-faktor tertentu yang mempengaruhi keputusan tersebut, seperti beban kerja, kepuasan kerja, lingkungan kerja, atau faktor kompensasi.
#### Kesimpulan Grafik Distribusi Gaji: Karywan Resign Cederung Bergaji Rendah 
Sebagian besar karyawan tetap bertahan di perusahaan, namun tingkat attrition yang menerima gaji rendah terutama di bawah $5000 tetap perlu diperhatikan agar perusahaan dapat mengidentifikasi faktor-faktor yang menyebabkan karyawan memilih untuk resign.

#### B. Grafik Work-Life Balance (1  Buruk, 4  Sangat Baik)
Grafik Work-Life Balance menunjukkan perbandingan jumlah karyawan yang resign dan tetap bekerja (stayed) berdasarkan tingkat keseimbangan antara kehidupan kerja dan kehidupan pribadi yang dinilai dalam skala 1 hingga 4, di mana nilai yang lebih tinggi menunjukkan keseimbangan yang lebih baik.
Dari grafik terlihat bahwa pada tingkat Work-Life Balance yang rendah (level 1), proporsi karyawan yang resign cukup tinggi yaitu sekitar 18 orang (32,1%), sedangkan 38 orang (67,9%) tetap bekerja. Pada level 2, jumlah karyawan yang resign masih cukup signifikan yaitu 45 orang (17,9%), sementara 206 orang (82,1%) tetap bekerja. Pada level 3, jumlah karyawan yang tetap bekerja meningkat cukup besar yaitu 544 orang (85,3%), dengan 94 orang (14,7%) yang resign. Sementara pada level 4, sebagian besar karyawan tetap bekerja yaitu sekitar 91 orang (80,5%), dan hanya 22 orang (19,5%) yang resign.
Hal ini menunjukkan bahwa karyawan yang memiliki keseimbangan kerja dan kehidupan pribadi yang lebih baik cenderung lebih bertahan di perusahaan.
##### Kesimpulan Grafik Work-Life Balance
Semakin baik keseimbangan antara pekerjaan dan kehidupan pribadi, semakin rendah kemungkinan karyawan untuk resign, sehingga perusahaan perlu mendukung kebijakan kerja yang fleksibel dan beban kerja yang seimbang.

#### C. Grafik Dampak Jarak Rumah Terhadap Keputusan Resign
Grafik Dampak Jarak Rumah Terhadap Keputusan Resign menunjukkan distribusi jumlah karyawan yang resign dan tetap bekerja (stayed) berdasarkan jarak rumah mereka dari tempat kerja yang diukur dalam kilometer. Grafik ini memperlihatkan bahwa sebagian besar karyawan yang tetap bekerja berada pada jarak rumah yang relatif dekat dengan tempat kerja, terutama pada jarak yang lebih pendek.
Namun, ketika jarak rumah semakin jauh, jumlah karyawan yang resign cenderung mulai meningkat meskipun jumlahnya tidak terlalu dominan dibandingkan karyawan yang tetap bekerja. Hal ini menunjukkan bahwa jarak rumah yang jauh dapat menjadi salah satu faktor yang mempengaruhi kenyamanan dan keputusan karyawan untuk tetap bekerja atau meninggalkan perusahaan.
##### Kesimpulan Grafik Jarak Rumah
Semakin jauh jarak rumah karyawan dari tempat kerja, semakin besar kemungkinan karyawan mengalami ketidaknyamanan yang dapat meningkatkan risiko resign, sehingga perusahaan dapat mempertimbangkan kebijakan kerja fleksibel atau dukungan transportasi.

#### D. Grafik Kepuasan Kerja (Job Satisfaction 1–4)
Grafik Job Satisfaction menunjukkan distribusi karyawan yang resign dan tetap bekerja berdasarkan tingkat kepuasan kerja yang dinilai dalam skala 1 hingga 4, di mana angka yang lebih tinggi menunjukkan tingkat kepuasan kerja yang lebih baik.
Dari grafik terlihat bahwa pada tingkat kepuasan kerja yang rendah (level 1), jumlah karyawan yang resign relatif lebih tinggi dibandingkan dengan tingkat kepuasan yang lebih tinggi. Seiring meningkatnya tingkat kepuasan kerja dari level 2 hingga level 4, jumlah karyawan yang tetap bekerja menjadi lebih dominan dibandingkan yang resign. Hal ini menunjukkan bahwa kepuasan kerja memiliki pengaruh terhadap keputusan karyawan untuk tetap bekerja atau meninggalkan perusahaan.
##### Kesimpulan Grafik Job Satisfaction
Karyawan dengan tingkat kepuasan kerja yang lebih tinggi cenderung lebih bertahan di perusahaan, sehingga perusahaan perlu meningkatkan kepuasan kerja melalui lingkungan kerja yang baik, peluang pengembangan karier, serta sistem penghargaan yang adil.

#### E. Grafik Masa Kerja: Attrition Tinggi pada Karyawan Baru
Grafik Masa Kerja: Attrition Tinggi pada Karyawan Baru menunjukkan distribusi masa kerja karyawan yang resign dan tetap bekerja di perusahaan. Grafik ini memperlihatkan bahwa karyawan yang resign cenderung memiliki masa kerja yang lebih pendek, yang berarti banyak karyawan yang keluar dari perusahaan pada tahap awal karier mereka.
Sebaliknya, karyawan yang tetap bekerja umumnya memiliki masa kerja yang lebih lama, yang menunjukkan bahwa semakin lama seseorang bekerja di perusahaan, semakin besar kemungkinan mereka untuk bertahan. Hal ini dapat disebabkan oleh meningkatnya stabilitas karier, pengalaman kerja, serta peningkatan posisi atau kompensasi seiring bertambahnya masa kerja.
##### Kesimpulan Grafik Masa Kerja
CONC_9   Karyawan dengan masa kerja yang lebih pendek memiliki risiko attrition yang lebih tinggi, sehingga perusahaan perlu memberikan program orientasi, pelatihan, dan pengembangan karier bagi karyawan baru untuk meningkatkan retensi.

#### F. Grafik Sebaran Usia: Karyawan Muda Lebih Rentan Resign
Grafik Sebaran Usia Karyawan menunjukkan distribusi usia karyawan yang resign dan tetap bekerja dalam perusahaan. Dari grafik terlihat bahwa sebagian besar karyawan berada pada rentang usia sekitar 25 hingga 40 tahun. Pada kelompok usia ini juga terlihat jumlah karyawan yang resign relatif lebih tinggi dibandingkan kelompok usia yang lebih tua.
Sebaliknya, pada kelompok usia yang lebih tinggi, jumlah karyawan yang resign cenderung lebih sedikit dan sebagian besar tetap bekerja di perusahaan. Hal ini menunjukkan bahwa karyawan yang lebih muda cenderung lebih aktif mencari peluang karier baru, sedangkan karyawan yang lebih senior cenderung memiliki stabilitas kerja yang lebih tinggi.
##### Kesimpulan Grafik Sebaran Usia
Karyawan berusia lebih muda memiliki kecenderungan attrition yang lebih tinggi, sedangkan karyawan yang lebih senior cenderung lebih loyal terhadap perusahaan, sehingga perusahaan perlu memberikan peluang pengembangan karier dan peningkatan kesejahteraan bagi karyawan muda untuk meningkatkan retensi. 


## Conclusion
1. Faktor Utama Pemicu Attrition (Top Predictors). Dari pengujian berbagai model (Random Forest, Decision Tree, XGBoost, dan ANN), terdapat tiga faktor konsisten yang paling memengaruhi keputusan karyawan untuk resign:
  - Beban Kerja (OverTime): Karyawan yang sering melakukan lembur memiliki risiko resign jauh lebih tinggi (31,9%) dibandingkan yang tidak lembur (10,8%).
  - Kompensasi (Monthly Income): Pendapatan bulanan merupakan variabel krusial. Karyawan dengan gaji lebih rendah, terutama di level jabatan awal (Job Level 1), memiliki kecenderungan keluar yang sangat tinggi (27,4%).
  - Faktor Demografis (Usia & Masa Kerja): Karyawan muda dalam rentang usia 18–30 tahun dan mereka dengan masa kerja yang singkat (new hires) adalah kelompok yang paling rentan untuk resign.

2. Kualitas Lingkungan & Hubungan Kerja. Kepuasan internal sangat menentukan loyalitas karyawan:
  - Lingkungan & Hubungan: Karyawan dengan tingkat kepuasan lingkungan dan hubungan kerja yang rendah (skala 1) memiliki peluang resign yang signifikan. Sebaliknya, hubungan baik dengan atasan dan rekan kerja meningkatkan loyalitas hingga di atas 84%.
  - Work-Life Balance: Keseimbangan hidup dan kerja yang buruk (skala 1) memicu attrition hingga 32,1%. Hal ini menegaskan bahwa fleksibilitas dan beban kerja yang manusiawi sangat penting.

3. Akurasi Model Prediksi. Model machine learning yang digunakan memiliki performa yang sangat baik dalam memetakan pola attrition:
  - Random Forest dan Decision Tree memberikan akurasi tertinggi sebesar 85,85%, menunjukkan bahwa pola data sangat dipengaruhi oleh segmentasi hierarkis seperti pendapatan, usia, dan status lembur.
  - XGBoost (83,96%) dan Logistic Regression (83,02%) memperkuat temuan bahwa variabel OverTime adalah prediktor tunggal terkuat.

4. Strategi Retensi yang Direkomendasikan. Untuk menekan angka attrition, perusahaan perlu fokus pada beberapa area strategis:
  - Evaluasi Beban Kerja: Mengurangi frekuensi lembur atau memberikan kompensasi lembur yang lebih kompetitif serta manajemen waktu yang lebih efisien.
  - Penyesuaian Kompensasi & Karier: Memberikan perhatian khusus pada Job Level awal dan karyawan muda melalui struktur gaji yang kompetitif dan jalur karier yang jelas untuk memberikan rasa stabilitas.
  - Peningkatan Budaya Kerja: Meningkatkan kualitas lingkungan fisik dan sosial di kantor untuk menaikkan skor kepuasan kerja dan hubungan kerja.
  - Program Onboarding & Mentoring: Memberikan pendampingan ekstra bagi karyawan baru dan muda untuk meningkatkan keterikatan (engagement) mereka sejak awal masa kerja.

* Ringkasan Akhir: Pemicu utama karyawan resign adalah kombinasi antara kelelahan kerja (lembur), faktor finansial (gaji rendah), dan ketidakpuasan lingkungan. Perusahaan yang mampu menyeimbangkan beban kerja dan memberikan penghargaan finansial serta sosial yang adil akan memiliki tingkat retensi yang jauh lebih stabil.


### Rekomendasi Action Items (Optional)
1. Manajemen Beban Kerja & Kesejahteraan
   - Audit Kebijakan Lembur (Overtime): Melakukan peninjauan terhadap departemen dengan jam lembur tertinggi. Terapkan batas maksimal lembur mingguan dan pastikan distribusi tugas dilakukan secara merata untuk menghindari burnout.
   - Program Fleksibilitas Kerja: Mengingat pentingnya Work-Life Balance, perusahaan dapat menerapkan kebijakan kerja fleksibel (seperti hybrid working atau flexible hours) untuk meningkatkan kenyamanan karyawan.
2. Strategi Kompensasi & Pengembangan Karier
   - Peninjauan Gaji pada Job Level Rendah: Melakukan salary benchmarking khusus untuk karyawan di Job Level 1 dan 2 agar tetap kompetitif di pasar, karena kelompok ini memiliki risiko resign tertinggi akibat faktor finansial.
   - Jalur Karier yang Transparan (Career Pathing): Menyusun dan mensosialisasikan peta karier yang jelas bagi karyawan muda (usia 18–30 tahun) agar mereka melihat prospek jangka panjang di dalam perusahaan.
3. Peningkatan Lingkungan & Budaya Kerja
   - Perbaikan Fasilitas & Atmosfer Kantor: Meningkatkan kualitas lingkungan fisik kantor berdasarkan masukan dari survei kepuasan (Environment Satisfaction).
   - Pelatihan Kepemimpinan (Leadership Training): Menyelenggarakan pelatihan bagi manajer dan supervisor untuk meningkatkan Relationship Satisfaction, fokus pada cara membangun hubungan profesional yang suportif dengan bawahan.
4. Intervensi Khusus Karyawan Baru & Muda
   - Revitalisasi Program Onboarding: Memperkuat program orientasi bagi karyawan dengan masa kerja di bawah 2 tahun. Sertakan sistem buddy atau mentor untuk membantu mereka beradaptasi lebih cepat.
   - Program Mentoring & Engagement: Mengadakan sesi focus group discussion (FGD) rutin khusus untuk karyawan muda guna mendengar aspirasi dan tantangan yang mereka hadapi di tahap awal karier.
5. Optimasi Operasional & Kebijakan
   - Dukungan Mobilitas/Transportasi: Untuk karyawan yang tinggal jauh dari kantor, pertimbangkan pemberian tunjangan transportasi tambahan atau izin bekerja dari rumah secara berkala untuk mengurangi kelelahan akibat perjalanan.
   - Survei Kepuasan Berkala: Menggunakan variabel-variabel penting (seperti Job Satisfaction dan Relationship Satisfaction) sebagai indikator utama dalam survei kepuasan karyawan tahunan untuk mendeteksi potensi attrition lebih dini.
6. Pemanfaatan data science lanjutan untuk sistem peringatan dini (Early Warning System) dengan memanfaatkan model Random Forest atau XGBoost yang telah dibuat untuk memprediksi profil karyawan yang berisiko tinggi resign setiap kuartal, sehingga tim HR dapat melakukan intervensi preventif secara personal.

