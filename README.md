# 📊 ETL Countries Pipeline

A modular ETL pipeline built in Python to extract, transform, and load country data from a public API into a database.

## 📌 Overview

This project implements a complete ETL workflow:

- **Extract**: fetches data from the REST Countries API  
- **Transform**: cleans and structures the dataset  
- **Load**: persists data into a database  

The goal is to simulate a real-world data engineering pipeline with a clear and maintainable structure.

## 🧱 Architecture
```
etl_pokeapi/
├── data/
│   ├── raw/
│   └── processed/
│
├── db/
│   └── schema.sql
│
├── src/
│   ├── connect/
│   │   ├── config.py
│   │   └── connection.py
│   │
│   ├── utils/
│   │   └── logger.py
│   │
│   ├── extract.py
│   ├── transform.py
│   ├── load.py
│   └── pipeline.py
│
├── .gitignore
└── README.md
```

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

## 📊 Sample Output

Example of processed and structured data loaded into the database:

| Name        | Region   | Capital      | Population |
|-------------|----------|--------------|------------|
| Brazil      | Americas | Brasília     | 213993437  |
| Germany     | Europe   | Berlin       | 83240525   |
| Japan       | Asia     | Tokyo        | 125836021  |

## 📸 Database Preview

Example query result from MySQL:

*Command used:\
SELECT name,region,capital,population\
FROM countries\
ORDER BY population DESC\
LIMIT 5;*\
<img width="445" height="129" alt="shot-2026-03-30_19-00-18" src="https://github.com/user-attachments/assets/56eb9d42-1b01-4764-9717-c0a80529db2b" /><br>

## 🚀 How to Run

### 1. Clone the repository
```bash
git clone https://github.com/mxavier-dev/countries-etl-pipeline.git
cd etl-countries-pipeline/
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
> If you encounter a "python not found" error, make sure Python is installed and added to your system PATH.  
> On some systems, you may need to use `python3` instead of `python`.

## 🧠 Design Decisions
 - Modular architecture (separation of concerns)
 - Logging system for pipeline monitoring
 - Clear data layer separation (raw vs processed)
 - SQL schema defined separately from application logic
## ⚠️ Notes
- API endpoint is currently defined directly in the code (no environment configuration)
- Data files are not versioned (data/ is ignored via .gitignore)
- This project is focused on learning and simulating real ETL workflows

## 📫 Contact

Developed by **Matheus de Freitas Xavier** • [Linkedin Profile](https://www.linkedin.com/in/matheus-xavier-a14b0732a)
