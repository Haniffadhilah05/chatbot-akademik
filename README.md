# 🤖 Chatbot Akademik Universitas Lampung

Chatbot cerdas berbasis web untuk membantu mahasiswa mengakses informasi akademik dengan mudah dan cepat. Dibangun menggunakan Flask, Natural Language Processing (NLTK), dan Machine Learning (Naive Bayes).

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![Flask](https://img.shields.io/badge/Flask-3.1.2-green.svg)
![NLTK](https://img.shields.io/badge/NLTK-3.9.2-orange.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)

## 📋 Deskripsi

Chatbot Akademik adalah aplikasi web interaktif yang dirancang untuk menjawab pertanyaan seputar layanan akademik di Universitas Lampung. Chatbot ini menggunakan teknik Natural Language Processing dan algoritma Machine Learning untuk memahami pertanyaan mahasiswa dan memberikan jawaban yang relevan.

### ✨ Fitur Utama

- 💬 **Chat Interface**: Antarmuka chat yang user-friendly dan responsif
- 🧠 **NLP Processing**: Memahami berbagai variasi pertanyaan mahasiswa
- 📚 **Informasi Akademik**: Menjawab pertanyaan seputar:
  - Jadwal kuliah
  - Nilai dan KHS
  - Registrasi dan KRS
  - Informasi umum akademik
- 🎯 **Machine Learning**: Menggunakan Naive Bayes Classifier untuk klasifikasi intent
- 🔄 **Real-time Response**: Respons chatbot secara real-time

## 🛠️ Teknologi yang Digunakan

- **Backend**: Flask 3.1.2
- **Machine Learning**: Scikit-learn 1.7.2
- **NLP**: NLTK 3.9.2
- **Frontend**: HTML, CSS, JavaScript
- **Model**: Naive Bayes Classifier
- **Feature Extraction**: CountVectorizer

## 📁 Struktur Project

```
chatbot-akademik/
│
├── app.py                  # Aplikasi Flask utama
├── chat.py                 # Modul chatbot dan logika prediksi
├── train_chatbot.py        # Script untuk melatih model
├── train_model.py          # Script alternatif training
├── requirements.txt        # Dependencies Python
├── README.md              # Dokumentasi project
│
├── data/
│   └── intents.json       # Dataset pertanyaan dan jawaban
│
├── static/
│   └── style.css          # Styling untuk web interface
│
├── templates/
│   └── index.html         # Template HTML untuk chat interface
│
└── __pycache__/           # Python cache files
```

## 🚀 Cara Instalasi

### Prerequisites

Pastikan Anda telah menginstal:
- Python 3.8 atau lebih baru
- pip (Python package installer)

### Langkah Instalasi

1. **Clone repository ini**
   ```bash
   git clone https://github.com/Haniffadhilah05/chatbot-akademik.git
   cd chatbot-akademik
   ```

2. **Buat virtual environment (opsional tapi disarankan)**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # Untuk Linux/Mac
   # atau
   venv\Scripts\activate     # Untuk Windows
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Download NLTK data**
   ```python
   python -c "import nltk; nltk.download('punkt'); nltk.download('wordnet')"
   ```

5. **Latih model chatbot**
   ```bash
   python train_chatbot.py
   ```
   
   Script ini akan menghasilkan 3 file model:
   - `model.pkl` - Model Naive Bayes yang telah dilatih
   - `vectorizer.pkl` - CountVectorizer untuk preprocessing
   - `labels.pkl` - Label kategori intent

6. **Jalankan aplikasi**
   ```bash
   python app.py
   ```

7. **Buka browser dan akses**
   ```
   http://localhost:5000
   ```

## 💡 Cara Penggunaan

1. Buka aplikasi di browser (http://localhost:5000)
2. Ketik pertanyaan Anda di kolom chat
3. Tekan Enter atau klik tombol kirim
4. Chatbot akan memberikan jawaban berdasarkan pertanyaan Anda

### Contoh Pertanyaan

- "Halo, apa kabar?"
- "Bagaimana cara melihat jadwal kuliah?"
- "Gimana cara lihat nilai KHS?"
- "Kapan registrasi semester depan?"
- "Terima kasih"

## 🔧 Kustomisasi

### Menambah Intent Baru

Untuk menambah pertanyaan dan jawaban baru, edit file `data/intents.json`:

```json
{
  "tag": "nama_intent",
  "patterns": [
    "Pertanyaan 1?",
    "Pertanyaan 2?"
  ],
  "responses": [
    "Jawaban 1",
    "Jawaban 2"
  ]
}
```

Setelah mengedit, latih ulang model:
```bash
python train_chatbot.py
```

### Mengubah Tampilan

Edit file `static/style.css` untuk mengubah styling web interface.

## 📊 Cara Kerja Model

1. **Data Loading**: Memuat dataset dari `intents.json`
2. **Preprocessing**: 
   - Tokenisasi teks
   - Lemmatization dengan WordNetLemmatizer
   - Konversi ke lowercase
3. **Feature Extraction**: CountVectorizer untuk mengubah teks ke vektor numerik
4. **Training**: Naive Bayes Classifier untuk klasifikasi intent
5. **Prediction**: Model memprediksi intent dan mengembalikan respons acak dari intent tersebut

## 🤝 Kontribusi

Kontribusi sangat diterima! Silakan:

1. Fork repository ini
2. Buat branch baru (`git checkout -b feature/AmazingFeature`)
3. Commit perubahan Anda (`git commit -m 'Add some AmazingFeature'`)
4. Push ke branch (`git push origin feature/AmazingFeature`)
5. Buat Pull Request

## 📝 License

Distributed under the MIT License. See `LICENSE` for more information.

## 👥 Author

**Haniffadhilah**
- GitHub: [@Haniffadhilah05](https://github.com/Haniffadhilah05)

## 🙏 Acknowledgments

- Universitas Lampung untuk inspirasi project
- NLTK untuk library NLP
- Scikit-learn untuk framework Machine Learning
- Flask untuk web framework

## 📞 Kontak & Support

Jika ada pertanyaan atau menemukan bug, silakan buat issue di repository ini atau hubungi developer.

---

⭐ Jangan lupa berikan star jika project ini bermanfaat!
