🛡️ PII Shield – Intelligent PII Detector & Masker

AI Prototype Challenge 2025

Team Name

PII Shield Innovators

Project Title

PII Detector & Masker using Hybrid Regex + AI Detection

Team Members

Name| Role
V. Anjali| Project Lead, Full Stack Development, Integration, Documentation

S. Venkata Hemanth Kumar| Backend Development

K. Saisri| Testing & Validation

S. Sri Ramya| Documentation & Demo Support

---
# Collaborations

https://github.com/anjalivilluri [V.Anjali]

https://github.com/Kumar-lab-sys [Hemanth kumar]

https://github.com/kandregulasaisri3-source [K.Sai sri]

https://github.com/ramyasenapathi [S. Sri ramya]

Problem Statement

Organizations often store customer information in datasets such as CSV and JSON files.

These datasets may accidentally contain Personally Identifiable Information (PII) such as:

- Email Addresses
- Mobile Numbers
- PAN Numbers
- Aadhaar Numbers

Sharing such data without masking can lead to:

- Privacy violations
- Security risks
- Regulatory compliance issues

This project automatically detects and masks sensitive information before datasets are shared or processed further.

---

Business Problem

Datasets accidentally contain sensitive information.

Organizations need a simple and automated solution to:

1. Detect PII data.
2. Generate a masked version of the dataset.
3. Produce a compliance report.
4. Reduce privacy risks.

---

Project Objective

Develop a working AI-assisted prototype that:

- Reads CSV files.
- Detects PII information.
- Masks sensitive values.
- Generates reports.
- Provides analytics through a web dashboard.
- Allows downloading of masked output files.

---

Features Implemented

PII Detection

Detects:

- Email Addresses
- Phone Numbers
- PAN Numbers
- Aadhaar Numbers

---

PII Masking

Examples:

Original| Masked
rahul@gmail.com| r****@gmail.com
9876543210| 98******10
ABCDE1234F| A********F
123456789012| ********9012

---

Compliance Reporting

Generates:

- Email Count
- Phone Count
- PAN Count
- Aadhaar Count
- Total PII Count
- Compliance Score

---

Interactive Dashboard

Displays:

- Detection Statistics
- Compliance Score
- Analytics Charts
- Download Option

---

Scan History

Maintains previous scan statistics inside:

data/scan_history.json

---

AI Capability Demonstrated

This project demonstrates a Hybrid AI Detection approach.

Layer 1 – Regex Detection

Uses regular expressions to identify:

- Emails
- Phone Numbers
- PAN
- Aadhaar

Layer 2 – AI Fallback Classifier

A lightweight AI-inspired classifier is used as a secondary validation layer.

Workflow:

Input File
↓
Regex Detection
↓
AI Validation Layer
↓
Masking Engine
↓
Report Generation
↓
Dashboard Output

This demonstrates an AI-assisted data privacy workflow while remaining fully free and offline.

---

Technology Stack

Programming Language

Python 3.13

Framework

Flask

Data Processing

Pandas

Frontend

HTML

CSS

JavaScript

Testing

Pytest

Version Control

GitHub

---

Project Architecture

User Uploads CSV
↓
Flask Web Application
↓
CSV Processing Engine
↓
Regex + AI Detection Layer
↓
Masking Engine
↓
Report Generator
↓
Dashboard Analytics
↓
Masked File Download

---

Folder Structure

PII-Detector-Masker/

├── ai/

├── detector/

├── processors/

├── templates/

├── static/

├── tests/

├── docs/

├── input/

├── output/

├── uploads/

├── utils/

├── README.md

├── requirements.txt

└── web_app.py

---

Setup Instructions

Step 1

Clone Repository

https://github.com/anjalivilluri/PII-Detector-Masker-Prototype.git

---

Step 2

Navigate to Project

cd PII-Detector-Masker

---

Step 3

Create Virtual Environment

python -m venv venv

---

Step 4

Activate Environment

Windows:

venv\Scripts\activate

---

Step 5

Install Dependencies

pip install -r requirements.txt

---

Run Instructions

Start Application

python web_app.py

Open Browser

http://127.0.0.1:5000

---

How to Use

1. Open application.
2. Upload sample CSV file.
3. Click Scan.
4. System detects PII.
5. Dashboard displays results.
6. Download masked file.

---

Sample Input

sample_data/sample.csv

---

Sample Output

output/masked.csv

output/report.json

---

Test Cases

Run:

pytest

Expected Result:

All tests should pass successfully.

---

Assumptions

- Input file contains valid CSV structure.
- PAN follows standard PAN format.
- Aadhaar contains 12 digits.
- Phone number contains 10 digits.
- Emails contain valid email structure.

---

Limitations

- Currently supports only Email, Phone, PAN, and Aadhaar.
- Does not connect to external LLM APIs.
- Prototype intended for demonstration purposes only.
- Not designed for production-scale datasets.

---

Project Contributions

V. Anjali

Primary contributor responsible for:

- Project planning
- System design
- Flask integration
- Dashboard development
- Testing coordination
- Documentation preparation
- Final submission packaging

---

Deliverables Included

✅ Source Code

✅ README Documentation

✅ AI Usage Note

✅ Sample Data

✅ Expected Outputs

✅ Test Cases

✅ Demo Video

✅ Team Information

---

Demo Video

Video Link:

https://drive.google.com/file/d/1IuKbajBTZIG8qC1WsZ0JRC5N1ttMLY1P/view?usp=drivesdk

---
# Live Demo
https://pii-detector-masker-prototype.onrender.com

Future Enhancements

- Support JSON upload from UI.
- Add OCR-based PII detection.
- Integrate Gemini/OpenAI APIs.
- Add Role-Based Access Control.
- Generate PDF compliance reports.

---

Conclusion

PII Shield provides an easy-to-use AI-assisted privacy protection solution that automatically detects and masks sensitive information from datasets. The project demonstrates practical application of data privacy, data engineering, and AI-assisted automation using a lightweight and fully offline architecture.
