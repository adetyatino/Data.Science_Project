# ---------------------------------------------
# FILE: penjelasan.py
# ---------------------------------------------

# 1. Grafik Logistic Regression (Accuracy: 83.02%)
DESC_LR = """
[Deskripsi]

Grafik Logistic Regression menampilkan nilai koefisien fitur untuk memprediksi attrition karyawan. Koefisien positif menunjukkan variabel yang meningkatkan peluang resign, sementara koefisien negatif menunjukkan variabel yang menurunkannya.

Berdasarkan grafik, faktor seperti OverTime, WorkLifeBalance, dan JobSatisfaction memiliki pengaruh signifikan. Karyawan yang sering lembur, memiliki keseimbangan hidup yang buruk, atau kepuasan kerja rendah cenderung lebih berpotensi untuk keluar dari perusahaan.
"""
CONC_LR = "Kesimpulan: Model ini menunjukkan faktor utama attrition adalah lembur, kepuasan kerja, dan keseimbangan kerja-hidup; perusahaan perlu mengevaluasi beban kerja untuk menekan angka resign."

# 2. Grafik Random Forest (Accuracy: 85.85%)
DESC_RF = """
[Deskripsi]

Grafik Random Forest menunjukkan tingkat kepentingan (feature importance) setiap variabel. Metode ini mengukur kontribusi fitur dalam proses pengambilan keputusan pada kumpulan pohon keputusan (decision trees) untuk menentukan loyalitas karyawan.

Variabel MonthlyIncome, Age, YearsAtCompany memiliki nilai importance tertinggi. Hal ini menandakan faktor finansial dan kenyamanan kerja memiliki peran paling krusial dalam menentukan apakah karyawan akan bertahan atau meninggalkan perusahaan.
"""
CONC_RF = "Kesimpulan: Pendapatan bulanan dan lembur adalah faktor penentu utama; perusahaan disarankan meningkatkan kesejahteraan dan lingkungan kerja demi mempertahankan talenta terbaik."

# 3. Grafik Decision Tree (Accuracy: 85.85%)
DESC_DT = """
[Deskripsi]

Grafik Decision Tree menggambarkan seberapa besar kontribusi suatu fitur dalam membangun pohon keputusan. Fokus utamanya adalah melihat variabel mana yang paling cepat memicu pemisahan data antara karyawan yang resign dan yang tetap.

Data menunjukkan Age dan Monthly Income memiliki nilai importance paling tinggi. Usia muda dan tingkat pendapatan yang belum stabil menjadi pemicu utama attrition, disusul oleh faktor frekuensi lembur yang tinggi.
"""
CONC_DT = "Kesimpulan: Usia dan pendapatan adalah faktor paling berpengaruh; diperlukan perhatian khusus pada kesejahteraan finansial karyawan di kelompok usia tertentu."

# 4. Grafik XGBoost (Accuracy: 83.96%)
DESC_XG = """
[Deskripsi]

Grafik XGBoost menggunakan metode gradient boosting untuk menunjukkan kontribusi fitur dalam meningkatkan performa prediksi. Model ini sangat sensitif terhadap pola-pola data yang menyebabkan ketidakseimbangan status karyawan.

Variabel OverTime muncul sebagai fitur dengan importance tertinggi, menegaskan lembur sebagai pemicu utama attrition. Selain itu, faktor EnvironmentSatisfaction dan JobLevel juga memberikan kontribusi besar dalam keputusan karyawan untuk bertahan.
"""
CONC_XG = "Kesimpulan: Lembur dan kondisi lingkungan kerja merupakan faktor penting; perbaikan kualitas lingkungan kerja dan manajemen beban kerja sangat direkomendasikan."

# 5. Grafik K-Nearest Neighbors (Accuracy: 83.96%)
DESC_KN = """
[Deskripsi]

Grafik Prediksi KNN menampilkan sebaran karyawan berdasarkan usia dan pendapatan bulanan. Model ini mengidentifikasi potensi attrition dengan melihat kemiripan profil (kedekatan data) seorang karyawan dengan pola karyawan yang sudah resign sebelumnya.

Distribusi data memperlihatkan konsentrasi attrition pada rentang usia 25 hingga 40 tahun. Jika seorang karyawan memiliki karakteristik yang mirip dengan rekan yang telah keluar, model akan mendeteksi risiko tinggi pada karyawan tersebut.
"""
CONC_KN = "Kesimpulan: Kemiripan profil berdasarkan usia dan gaji dapat memprediksi risiko attrition; identifikasi dini pada kelompok berisiko tinggi sangat dimungkinkan dengan model ini."

# 6. Grafik Clustering (K-Means)
DESC_KM = """
[Deskripsi]

Grafik Segmentasi K-Means membagi karyawan ke dalam tiga cluster utama berdasarkan Age dan MonthlyIncome. Metode unsupervised ini membantu melihat pola kelompok tanpa terikat pada label target sebelumnya.

Cluster pertama mencakup karyawan muda dengan gaji rendah, cluster kedua untuk usia menengah dengan gaji stabil, dan cluster ketiga untuk senior dengan gaji tinggi. Pola attrition terlihat berbeda pada setiap segmen tersebut.
"""
CONC_KM = "Kesimpulan: Segmentasi ini memungkinkan perusahaan merancang strategi retensi yang berbeda dan lebih personal untuk setiap kelompok karyawan."

# 7. Grafik Neural Networks (Accuracy: 82.08%)
DESC_NN = """
[Deskripsi]

Grafik ANN Feature Activation menunjukkan tingkat aktivitas fitur dalam arsitektur saraf tiruan. Semakin tinggi aktivasi fitur, semakin kuat sinyal yang diberikan fitur tersebut dalam menentukan hasil akhir prediksi.

Fitur MonthlyIncome, JobSatisfaction, dan WorkLifeBalance menunjukkan aktivasi tertinggi. Ini membuktikan bahwa dalam pola yang kompleks sekalipun, faktor ekonomi dan keseimbangan hidup tetap menjadi penggerak utama keputusan resign.
"""
CONC_NN = "Kesimpulan: Faktor ekonomi dan keseimbangan kerja-hidup adalah pendorong utama loyalitas; perusahaan perlu menyeimbangkan kompensasi dengan kualitas hidup karyawan."

# 8. Grafik Heatmap Age vs Monthly Income
DESC_PK = """
[Deskripsi]

Heatmap ini menunjukkan interaksi antara usia dan pendapatan terhadap rata-rata attrition. Warna terang mengindikasikan peluang resign yang tinggi, memberikan gambaran visual area "zona kuning" pada profil karyawan.

Tingkat resign tertinggi ditemukan pada karyawan muda dengan pendapatan rendah (tahap awal karier). Sebaliknya, karyawan senior dengan gaji tinggi cenderung berada di zona stabil dengan tingkat loyalitas yang jauh lebih besar.
"""
CONC_PK = "Kesimpulan: Jalur karier yang jelas dan kompensasi kompetitif sangat krusial bagi karyawan muda agar mereka tidak mencari peluang di tempat lain."

# 9. Grafik Faktor Utama: OverTime
DESC_1 = """
[Deskripsi]

Grafik ini membandingkan status attrition berdasarkan kebiasaan lembur. Terlihat perbedaan mencolok di mana kelompok non-lembur cenderung stabil, sedangkan kelompok lembur memiliki proporsi resign yang jauh lebih besar.

Tercatat 31,9% karyawan yang lembur memilih untuk resign, berbanding terbalik dengan hanya 10,8% pada kelompok non-lembur. Ini menjadi bukti kuat bahwa beban waktu kerja berlebih berkorelasi langsung dengan keluarnya karyawan.
"""
CONC_1 = "Kesimpulan: Kebijakan lembur yang tidak terkendali meningkatkan risiko resign; pengelolaan jam kerja yang sehat adalah kunci menurunkan attrition."

# 10. Grafik Kelompok Usia
DESC_2 = """
[Deskripsi]

Grafik ini memetakan attrition berdasarkan empat kelompok usia. Kelompok 31–40 tahun merupakan segmen paling stabil, sementara kelompok termuda (18–30 tahun) menunjukkan tingkat kerentanan tertinggi.

Persentase resign pada usia 18–30 tahun mencapai 26,3%, jauh di atas kelompok usia lainnya. Hal ini mengindikasikan bahwa loyalitas cenderung meningkat seiring dengan bertambahnya kematangan usia dan stabilitas posisi di perusahaan.
"""
CONC_2 = "Kesimpulan: Karyawan muda lebih rentan resign; perusahaan perlu memberikan program pengembangan dan apresiasi ekstra agar mereka merasa memiliki masa depan di perusahaan."

# 11. Grafik Kepuasan Lingkungan Kerja
DESC_3 = """
[Deskripsi]

Visualisasi ini menunjukkan hubungan antara level kepuasan lingkungan (skala 1-4) dengan keputusan bertahan. Karyawan di level 1 (sangat tidak puas) memiliki tingkat attrition mencapai 27,3%.

Sebaliknya, pada level tertinggi (level 4), angka resign turun drastis menjadi hanya 12,7%. Data ini menegaskan bahwa kualitas fasilitas dan atmosfer kerja fisik berdampak langsung pada kenyamanan jangka panjang.
"""
CONC_3 = "Kesimpulan: Lingkungan kerja yang buruk adalah pemicu resign; investasi pada kenyamanan ruang kerja dapat meningkatkan retensi secara signifikan."

# 12. Grafik Hubungan Kerja (Relationship Satisfaction)
DESC_4 = """
[Deskripsi]

Grafik ini mengukur dampak hubungan interpersonal terhadap loyalitas. Pada level kepuasan hubungan yang rendah (level 1), tingkat resign mencapai 22,9%, menandakan adanya konflik atau ketidakcocokan dengan rekan/atasan.

Ketika kepuasan hubungan meningkat ke level 3 dan 4, stabilitas karyawan mencapai di atas 84%. Hubungan kerja yang harmonis terbukti menjadi perekat yang kuat bagi karyawan untuk tetap bertahan meskipun menghadapi tantangan kerja lainnya.
"""
CONC_4 = "Kesimpulan: Budaya kerja kolaboratif dan hubungan atasan-bawahan yang baik sangat menentukan loyalitas; program team-building dapat menjadi solusi preventif."

# 13. Level Pekerjaan (Job Level)
DESC_5 = """
[Deskripsi]

Berdasarkan data yang diolah skrip siap.py, grafik ini menunjukkan attrition pada tiap jenjang jabatan. Job Level 1 memiliki angka resign tertinggi (27,4%), yang kemudian menurun drastis pada level jabatan yang lebih senior.

Pada Job Level 4 dan 5, tingkat loyalitas mencapai di atas 90.9%. Hal ini mencerminkan bahwa semakin tinggi jabatan, semakin besar tanggung jawab dan fasilitas yang didapat, sehingga keinginan untuk pindah kerja menjadi semakin rendah.
"""
CONC_5 = "Kesimpulan: Attrition terfokus pada level entry; perusahaan harus memperkuat jalur karier dan kompensasi di level awal untuk menjaga stabilitas staf."

# 14. Grafik Attrition Status (Resigned vs Stayed)
DESC_6 = """
[Deskripsi]

Grafik ini memberikan gambaran makro mengenai perbandingan jumlah karyawan yang tetap bertahan dibandingkan dengan yang keluar. Secara visual, mayoritas karyawan masih memilih untuk loyal dan berkarir di perusahaan.

Meskipun mayoritas bertahan, keberadaan kelompok yang resign tetap menjadi sinyal penting untuk dianalisis. Identifikasi faktor pemicu harus dilakukan agar angka yang kecil ini tidak berkembang menjadi tren yang merugikan perusahaan.
"""
CONC_6 = "Kesimpulan: Secara umum kondisi loyalitas baik, namun pemantauan faktor penyebab resign tetap wajib dilakukan untuk menjaga angka attrition tetap di bawah batas aman."

# 15. Grafik Kepuasan Kerja (Job Satisfaction)
DESC_7 = """
[Deskripsi]

Grafik ini memetakan dampak kepuasan kerja terhadap keputusan resign. Terlihat pola linier di mana semakin rendah kepuasan kerja (level 1), semakin tinggi jumlah karyawan yang memutuskan untuk mengakhiri masa kerjanya.

Dominasi karyawan yang bertahan mulai terlihat jelas pada level kepuasan 3 dan 4. Hal ini membuktikan bahwa pemenuhan ekspektasi kerja dan pemberian makna pada pekerjaan efektif dalam menahan keinginan karyawan untuk resign.
"""
CONC_7 = "Kesimpulan: Kepuasan kerja adalah fondasi retensi; sistem penghargaan yang adil dan makna kerja yang jelas perlu terus dikomunikasikan kepada karyawan."

# 16. Grafik Work-Life Balance
DESC_8 = """
[Deskripsi]

Grafik ini menunjukkan perbandingan status attrition berdasarkan keseimbangan hidup. Pada level terendah (level 1), proporsi resign sangat tinggi yaitu 32,1%, menunjukkan dampak buruk dari ketidakseimbangan hidup.

Kestabilan karyawan meningkat signifikan pada level 3 dengan tingkat bertahan mencapai 85,3%. Hal ini menegaskan bahwa kebijakan yang mendukung kehidupan pribadi karyawan sangat dihargai dan berdampak pada loyalitas jangka panjang.
"""
CONC_8 = "Kesimpulan: Keseimbangan kerja dan kehidupan pribadi yang buruk adalah ancaman serius bagi retensi; kebijakan kerja fleksibel sangat disarankan."

# 17. Grafik Masa Kerja (Years at Company)
DESC_9 = """
[Deskripsi]

Grafik ini menyoroti bahwa risiko attrition tertinggi berada pada karyawan dengan masa kerja pendek (karyawan baru). Banyak dari mereka yang memutuskan keluar sebelum mencapai masa bakti yang lama di perusahaan.

Karyawan dengan masa kerja lebih lama menunjukkan stabilitas yang lebih tinggi. Ini sering kali berkaitan dengan telah ditemukannya kecocokan budaya, kemapanan posisi, serta benefit yang meningkat seiring senioritas.
"""
CONC_9 = "Kesimpulan: Karyawan baru berada di zona risiko; program orientasi (onboarding) yang efektif sangat diperlukan untuk membantu mereka beradaptasi lebih cepat."

# 18. Grafik Jarak Rumah
DESC_10 = """
[Deskripsi]

Grafik ini memperlihatkan bagaimana faktor geografis mempengaruhi keputusan resign. Karyawan yang tinggal dekat dengan kantor cenderung lebih stabil dibandingkan mereka yang memiliki jarak tempuh sangat jauh.

Meskipun tidak menjadi faktor tunggal, peningkatan jarak rumah berkorelasi dengan munculnya ketidaknyamanan. Kelelahan di perjalanan dapat menjadi alasan tambahan yang memperkuat keinginan karyawan untuk mencari tempat kerja yang lebih dekat.
"""
CONC_10 = "Kesimpulan: Jarak rumah mempengaruhi kenyamanan kerja; dukungan transportasi atau kebijakan kerja dari rumah (WFH) dapat menjadi solusi untuk karyawan yang tinggal jauh."

# 19. Grafik Sebaran Usia
DESC_11 = """
[Deskripsi]

Grafik distribusi usia ini menunjukkan area konsentrasi attrition pada kelompok usia produktif awal (25-40 tahun). Di rentang usia ini, mobilitas karier biasanya masih sangat tinggi karena karyawan aktif mencari peluang terbaik.

Sebaliknya, stabilitas mulai terbentuk pada kelompok usia senior. Karyawan yang lebih matang cenderung memprioritaskan keamanan kerja dan telah memiliki ikatan yang lebih kuat dengan nilai-nilai perusahaan.
"""
CONC_11 = "Kesimpulan: Kelompok usia muda memerlukan perhatian lebih dalam hal pengembangan karier; retensi dapat ditingkatkan dengan memberikan kepastian jenjang profesi yang jelas."