# 📊 ETL Countries Pipeline

A modular ETL pipeline built in Python to extract, transform, and load country data from a public API into a relational database.

## 📌 Overview

This project implements a complete ETL workflow:

- **Extract**: fetches data from the REST Countries API  
- **Transform**: cleans and structures the dataset  
- **Load**: persists data into a relational database  

The goal is to simulate a real-world data engineering pipeline with a clear and maintainable structure.

## 🧱 Architecture
data/<br>
├── raw/ # Raw extracted data<br>
├── processed/ # Transformed data<br>

db/<br>
├── schema.sql # Database schema<br>

src/<br>
├── extract.py # Extract data from API<br>
├── transform.py # Transform raw data<br>
├── load.py # Load data into storage/database<br>
├── pipeline.py # ETL orchestration<br>
├── utils/<br>
│ └── logger.py # Logging module<br>
├── connect/<br>
│ ├── connection.py # Database connection<br>
│ └── config.py # Configuration<br>

## ⚙️ Tech Stack

- Python
- MySQL
- mysql-connector-python
- Pandas
- Requests

## 🔄 Pipeline Flow

1. **Extract**
   - Consumes REST Countries API
   - Stores raw data in `data/raw/`

2. **Transform**
   - Filters relevant fields
   - Handles inconsistencies
   - Outputs clean data to `data/processed/`

3. **Load**
   - Inserts data into the database
   - Applies constraints and indexing

## 🚀 How to Run

### 1. Clone the repository
```bash
git clone https://github.com/mxavier-dev/etl-countries-pipeline.git
cd etl-countries-pipeline
```
### 2. Create virtual environment
```bash
python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows
```
### 3. Install dependencies
```bash
pip install -r requirements.txt
```
### 4. Set up the database

Make sure you have MySQL running, then execute the schema:
```bash
mysql -u root -p -e "CREATE DATABASE etl_countries;"
mysql -u root -p etl_countries < db/schema.sql
```

### 5. Run the pipeline
```bash
python -m src.pipeline
```

## 🧠 Design Decisions
 - Modular architecture (separation of concerns)
 - Logging system for pipeline monitoring
 - Clear data layer separation (raw vs processed)
 - SQL schema defined separately from application logic
## ⚠️ Notes
- API endpoint is currently defined directly in the code (no environment configuration)
- Data files are not versioned (data/ is ignored via .gitignore)
- This project is focused on learning and simulating real ETL workflows
## 📈 Roadmap
- Externalize configuration using environment variables
- Implement upsert logic
- Add automated tests
- Orchestrate with Airflow

## 📫 Contact

Developed by **Matheus de Freitas Xavier** • [Linkedin Profile](https://www.linkedin.com/in/matheus-xavier-a14b0732a)
