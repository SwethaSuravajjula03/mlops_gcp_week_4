# IRIS Pipeline Homework

This repository contains a simple data pipeline for the classic IRIS dataset, including:

- **Data loading** and validation  
- **Model training** and evaluation  
- **Unit tests** (pytest) for both data-validation and evaluation  
- A **sanity-check GitHub Actions** workflow that comments test reports via CML  

---

## 📂 Project Structure

```
iris-homework/
├── data/
│   └── iris.csv              # Raw IRIS dataset
├── src/
│   └── data_validation.py
    |__ evaluation.py      # Load, validate, train & evaluate functions
├── tests/
│   └── test_data_validation.py
    |__ test_data_evaluation.py # pytest tests for data and model
├── .github/
│   └── workflows/
│       └── sanity_test.yml   # On-demand sanity testing + CML report
├── requirements.txt          # Pinned Python dependencies
└── README.md                 # This file
```

---

## ⚙️ Prerequisites

- Python 3.9 or 3.10  
- Git  
- (Optional) [CML CLI](https://cml.dev) for GitHub Actions reporting  

---



---

## Usage

Run the pipeline script directly:



You’ll see output indicating:
- Schema valid?  
- No nulls?  
- Model accuracy  

---

## ✅ Running Tests

Execute all unit tests with pytest:

```bash
pytest -q
```

Tests cover:
- `validate_schema`  
- `validate_no_nulls`  
- `train_and_evaluate` (accuracy ≥ 0.90)  

---

## GitHub Actions Sanity Test

A manual “Sanity test” workflow is defined in `.github/workflows/sanity_test.yml`. To trigger it:

1. In GitHub, navigate to **Actions → Sanity test → Run workflow**.  
2. It will:
   - Verify critical files/directories exist  
   - Install dependencies  
   - Run pytest  
   - Post a test-log comment back via CML  

---

## Contributing

1. **Branch from `dev`** for new features or fixes.  
2. Add or update tests under `tests/`.  
3. Commit & push to `dev`, open a PR → `main`.  
4. Ensure CI passes before merging.  



