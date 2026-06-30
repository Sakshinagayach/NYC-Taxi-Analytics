NYC Taxi Analytics: End-to-End Cloud-Based Data Analytics Project

An end-to-end cloud-based Data Analytics project that transforms raw NYC Yellow Taxi trip data into actionable business insights using Python, Google Cloud Platform (GCP), BigQuery, Apache Airflow, Docker, SQL, and Power BI.

Project Overview

The **NYC Taxi Analytics Project** demonstrates the complete lifecycle of a modern cloud-based data analytics solution. The project automates the ingestion, processing, validation, transformation, storage, orchestration, and visualization of NYC Yellow Taxi trip data while following industry-standard Data Analytics and Data Engineering practices.

Starting with raw taxi trip datasets, the pipeline performs data cleaning, validation, and feature engineering using Python. The processed data is converted into Parquet format and stored in Google Cloud Storage (GCS). It is then loaded into Google BigQuery, where SQL transformations build a layered analytical warehouse consisting of **Raw**, **Staging**, **Mart**, and **Analytics** layers.

Apache Airflow orchestrates the complete workflow, while Power BI connects directly to the Analytics layer to deliver interactive dashboards that provide business insights into demand, revenue, operational efficiency, payment behavior, and travel patterns.

---

Business Problem

NYC Yellow Taxi generates millions of trip records every month. Raw transactional data alone cannot answer critical business questions due to inconsistent data quality, missing values, and lack of business-ready structure.

Business stakeholders require answers to questions such as:

- Which pickup zones generate the highest demand?
- Which locations produce the highest revenue?
- What are the busiest hours?
- Which payment methods are preferred?
- Which routes are most profitable?
- How efficiently are taxis operating?

This project solves these challenges by building an automated cloud-based analytics pipeline that transforms raw trip data into reliable business insights.

Project Objectives

- Build an automated end-to-end analytics pipeline.
- Perform data cleaning and validation using Python.
- Apply feature engineering for business analysis.
- Store processed data efficiently in Google Cloud Storage.
- Design a layered analytical warehouse in BigQuery.
- Automate workflows using Apache Airflow.
- Develop Power BI dashboards for business reporting.
- Generate business KPIs and analytical insights.

---

Solution Architecture

                NYC Yellow Taxi Dataset (CSV)
                           │
                           ▼
                 Python Data Processing
       ┌─────────────────────────────────────┐
       │ • Data Cleaning                     │
       │ • Data Validation                   │
       │ • Feature Engineering               │
       └─────────────────────────────────────┘
                           │
                           ▼
           Google Cloud Storage (Parquet Files)
                           │
                           ▼
                 Google BigQuery Warehouse
        ┌──────────┬──────────┬──────────┬──────────┐
        │   Raw    │ Staging  │   Mart   │ Analytics│
        └──────────┴──────────┴──────────┴──────────┘
                           │
                           ▼
             Apache Airflow Orchestration
                           │
                           ▼
                 Power BI Interactive Dashboard
                           │
                           ▼
                 Business Insights & KPI Reporting

---

 Technology Stack


| Programming Language | Python |
| Data Processing | Pandas |
| SQL | BigQuery SQL |
| Cloud Platform | Google Cloud Platform (GCP) |
| Cloud Storage | Google Cloud Storage (GCS) |
| Data Warehouse | Google BigQuery |
| Workflow Orchestration | Apache Airflow |
| Containerization | Docker |
| Visualization | Power BI |
| Version Control | Git & GitHub |
| AI Productivity Tools | ChatGPT & Claude AI |



 Repository Structure

NYC-Taxi-Analytics/
│
├── airflow/
│   ├── dags/
│   ├── include/
│   │   ├── python/
│   │   └── sql/
│   ├── docker-compose.yaml
│   └── requirements.txt
│
├── docs/
├── images/
├── powerbi/
├── README.md
├── LICENSE
└── .gitignore

 Dataset Overview

The project uses the **NYC Yellow Taxi Trip Records** dataset containing:

- Pickup & Drop-off Date/Time
- Pickup & Drop-off Locations
- Passenger Count
- Trip Distance
- Fare Amount
- Tip Amount
- Payment Type
- Total Amount
- Vendor Information

---

Data Processing Pipeline

The Python pipeline performs:

 Data Ingestion
- Read monthly taxi datasets
- Validate schema consistency

Data Cleaning
- Handle missing values
- Remove duplicate records
- Standardize column names

Data Validation
- Validate mandatory fields
- Verify data quality
- Check fare and distance consistency

Feature Engineering

Generated features include:

- Pickup Hour
- Pickup Day
- Pickup Month
- Trip Duration
- Average Speed
- Weekend Indicator
- Peak Hour Indicator

Storage

Processed datasets are converted to **Parquet** format before being uploaded to **Google Cloud Storage**.

Data Warehouse Design

The BigQuery warehouse follows a layered architecture.
Raw Layer > Staging > Mart > Analytics



Workflow Orchestration

Apache Airflow automates the complete analytics workflow.

The project includes three DAGs:

| DAG | Purpose |
|------|----------|
| Data Processing Pipeline | Process monthly taxi data |
| Warehouse Pipeline | Build warehouse layers |
| Analytics Pipeline | Generate KPI tables |

Docker is used to provide a consistent Airflow environment.

---

 Power BI Dashboard

The final Analytics layer connects directly to Power BI.

Dashboard Highlights:

- Demand Analysis
- Revenue Analysis
- Payment Analysis
- Zone Performance
- Route Analysis
- Peak Hour Trends
- Trip Efficiency
- KPI Cards

 Business Questions Answered

This project answers questions such as:

- Which pickup zones have the highest demand?
- Which locations generate the highest revenue?
- What are the busiest hours?
- Which payment methods dominate?
- Which routes perform best?
- How efficient are taxi operations?

 Key KPIs

- Total Trips
- Total Revenue
- Average Fare
- Revenue per Mile
- Average Trip Duration
- Average Speed
- Peak Revenue Hour
- Peak Demand Hour
- Top Pickup Zones
- Top Drop-off Zones
- Payment Distribution

 Skills Demonstrated

- Data Cleaning
- Data Validation
- Feature Engineering
- Python Programming
- SQL Development
- Google Cloud Storage
- BigQuery Data Warehousing
- Apache Airflow
- Docker
- Power BI
- Business Intelligence
- Cloud-Based Analytics



Future Enhancements

- CI/CD using GitHub Actions
- Automated monthly data ingestion
- Data quality monitoring
- Predictive demand forecasting
- Real-time analytics
- Cost optimization in BigQuery

 How to Run
bash
git clone https://github.com/<your-username>/NYC-Taxi-Analytics.git


bash
docker compose up


Run the Airflow DAGs in the following order:

1. Data Processing Pipeline
2. Warehouse Pipeline
3. Analytics Pipeline

Finally, connect Power BI to the Analytics layer in BigQuery.

License

This project is licensed under the MIT License.
