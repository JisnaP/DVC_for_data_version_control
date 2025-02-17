# DVC Practice Repository

This repository is a practice setup for **Data Version Control (DVC)**, demonstrating how to version and manage datasets efficiently using DVC with Git and Amazon S3 as remote storage.

## 📌 Project Overview
This repository contains:
- Different versions of dataset files managed using **DVC**.
- **Git** version control for tracking code changes.
- **Amazon S3 remote storage** for storing dataset versions.
- Example scripts for loading and processing data using **Pandas**.

## 📂 Repository Structure
```
DVC_for_data_version_control/
│── data/                  # Local dataset directory (tracked by DVC)
│── stage.py               # Sample script for data processing
│── data.dvc               # DVC-tracked file (points to data location)
│── .dvc/                  # DVC metadata folder
│── .gitignore             # Ignore files like DVC cache
│── README.md              # This file
│── requirements.txt       # Python dependencies
```

## 🚀 Getting Started

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/JisnaP/DVC_for_data_version_control.git
cd DVC_for_data_version_control
```

### 2️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

### 3️⃣ Set Up DVC & Configure Remote Storage
```bash
dvc init
dvc remote add mystorage s3://mystoragebucketdvc/dvcdata
```
Ensure your AWS credentials are configured using:
```bash
aws configure
```

### 4️⃣ Pull a Specific Data Version
To pull a specific version of data:
```bash
git checkout v2  # Switch to version 2
```
```bash
dvc pull -r mystorage
```

### 5️⃣ Running the Script
```bash
python stage.py
```

## 📌 Versioning Data with DVC

### Adding & Committing Data to DVC
```bash
dvc add data/people.json
```
```bash
git add data.dvc .gitignore
```
```bash
git commit -m "Added version 1 of dataset"
```
```bash
dvc push -r mystorage  # Push data to S3
```

### Switching Between Data Versions
```bash
git checkout v2  # Switch to version 2
```
```bash
dvc pull -r mystorage  # Pull version 2 from remote
```

## 🤝 Collaborating on This Repository
- **Share the repository** with team members via GitHub.
- **Grant IAM access** to the S3 bucket.
- **Pull the latest data version** using `git pull` and `dvc pull`.

## 📜 License
This repository is for educational purposes.



