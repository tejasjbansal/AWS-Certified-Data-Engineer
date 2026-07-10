# AWS Data Engineering & Analytics Course Notes

This repository contains structured notes, code samples, and exercises following an
AWS-focused Data Engineering / Data Analytics course. Content is organized into one
folder per course section, numbered to match the original course outline so the
repo structure mirrors the curriculum.

## 📁 Repository Structure

Run [`create_course_structure.py`](./create_course_structure.py) to generate the
full folder layout below. Each folder contains its own `README.md` stub with the
lecture count and total duration for that section, ready to be filled in with
notes, diagrams, and code as you progress through the course.

| # | Section | Lectures | Duration |
|---|---------|----------|----------|
| 01 | Introduction | 5 | 16 min |
| 02 | Data Ingestion | 6 | 36 min |
| 03 | Querying with Athena | 6 | 28 min |
| 04 | AWS Glue Deep Dive | 18 | 1 hr 48 min |
| 05 | Serverless Compute with Lambda | 3 | 21 min |
| 06 | Data Streaming | 15 | 1 hr 58 min |
| 07 | Storage with S3 | 20 | 1 hr 49 min |
| 08 | Other Storage Services | 6 | 46 min |
| 09 | DynamoDB | 19 | 2 hr |
| 10 | Redshift Datawarehouse | 29 | 2 hr 43 min |
| 11 | Other Database Services | 8 | 46 min |
| 12 | Compute Services | 5 | 29 min |
| 13 | Analytics | 23 | 2 hr 7 min |
| 14 | Machine Learning with SageMaker | 4 | 25 min |
| 15 | Application Integration | 13 | 1 hr 20 min |
| 16 | Management, Monitoring, and Governance | 23 | 2 hr 8 min |
| 17 | Containers | 6 | 37 min |
| 18 | Migration | 6 | 33 min |
| 19 | VPCs | 5 | 11 min |
| 20 | Security | 7 | 38 min |

**Totals:** 20 sections · 227 lectures · ~24 hr 39 min of content

## 🚀 Getting Started

### Prerequisites
- Python 3.7+
- Git
- An AWS account (free tier is sufficient for most hands-on labs)
- AWS CLI configured with valid credentials (`aws configure`)

### Setup

1. Clone this repository:
   ```bash
   git clone https://github.com/<your-username>/aws-data-engineering-course.git
   cd aws-data-engineering-course
   ```

2. Generate the folder structure (if not already present, or to regenerate it
   in a fresh location):
   ```bash
   python create_course_structure.py .
   ```
   Pass a different path as an argument to create the structure elsewhere, e.g.:
   ```bash
   python create_course_structure.py ./notes
   ```

3. Start working through the sections in order — each folder's `README.md`
   is a placeholder you can expand with your own notes, architecture diagrams,
   sample code, and links to AWS documentation as you complete that section.

## 🗂️ How to Use This Repo

- **Notes**: Add markdown notes directly into each section's `README.md`.
- **Code samples**: Drop scripts, notebooks, CloudFormation/Terraform templates,
  or Lambda function code into the relevant section folder.
- **Diagrams**: Store architecture diagrams (e.g., `.png`, `.drawio`) alongside
  the notes for that section.
- **Consistent naming**: Keep the `NN-Section-Name` folder naming convention
  if you add new sections, so ordering stays consistent with the course.

## 🛠️ Script Details

`create_course_structure.py`:
- Defines all 20 sections with their lecture counts and durations.
- Slugifies each section name into a filesystem-safe folder name
  (e.g., `AWS Glue Deep Dive` → `AWS-Glue-Deep-Dive`).
- Prefixes each folder with a two-digit index (`01`, `02`, ...) so folders
  sort correctly in file explorers and on GitHub.
- Creates a `README.md` stub inside each folder (since Git doesn't track
  empty directories) pre-filled with the lecture count and duration.
- Is idempotent — re-running it won't overwrite existing README content.

## 📚 Topics Covered

This course spans the core AWS services used in modern data engineering
pipelines, including:

- **Ingestion & Streaming**: Kinesis, Data Ingestion patterns, Data Streaming
- **Storage**: S3, DynamoDB, and other storage services
- **Processing & ETL**: AWS Glue, Lambda, Compute services
- **Querying & Warehousing**: Athena, Redshift, other database services
- **Analytics & ML**: Analytics services, SageMaker
- **Integration & Ops**: Application Integration, Management/Monitoring/Governance
- **Infrastructure**: Containers, VPCs, Migration, Security

## 🤝 Contributing

This is primarily a personal learning repository, but suggestions, corrections,
or additional resources are welcome via pull request or issue.

## 📄 License

This project is licensed under the MIT License — see the [LICENSE](./LICENSE)
file for details. Course content itself remains the property of its original
creator; this repo only contains original notes and code written while
following along.
