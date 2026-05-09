# Anomaly Target Detection in Hyperspectral Images
## Project Structure

```
project/
├── Backend/
│   ├── app.py              # Flask API server
│   ├── config.py           # AWS config (reads from .env)
│   ├── s3_utils.py         # S3 upload/download helpers
│   ├── pipeline_runner.py  # Orchestrates ML pipeline
│   └── report_generator.py # PDF report generation
├── models/
│   ├── autoencoder_model.py
│   ├── LRaSMD.py
│   ├── pca_rf_svm.py
│   └── saved_models/       # Pre-trained model files (not in git)
├── pipeline/
│   └── anomaly_pipeline.py
├── utils/
│   ├── load_mat.py
│   ├── preprocess.py
│   ├── save_image.py
│   └── visualize.py
├── templates/index.html
├── static/
├── data/                   # Not in git — add your .mat files here
├── .env.example            # Template for credentials
├── .gitignore
└── requirements.txt
```

---

## Setup

### 1. Install dependencies
```bash
pip install -r requirements.txt
```

### 2. Configure AWS (optional — project works without S3)
```bash
cp .env.example .env
# Edit .env and fill in your AWS credentials
```
> If you skip this step, S3 uploads are silently skipped and everything else works normally.

### 3. Add your data
Place `.mat` or `.npy` hyperspectral files in `data/input/`.

### 4. (First time) Train models
```bash
python train_pca_svm.py
python train_autoencoder.py
```

### 5. Run the server
```bash
cd Backend
python app.py
```

Open `http://localhost:5000` in your browser.

---

