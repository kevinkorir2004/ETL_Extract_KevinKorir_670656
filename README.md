# ETL Extract Lab(project name)

**Name**: Kevin Korir  
**Student ID**: 670656

---

##  Project Description

This project demonstrates the use of **ETL (Extract, Transform, Load)** techniques — focusing specifically on **Full Extraction** and **Incremental Extraction**. It uses a synthetic dataset that simulates retail transactions.

The ETL logic is implemented in a Jupyter Notebook (`etl_extract.ipynb`) and includes:
- Loading a full dataset
- Extracting only records added or updated since the last run
- Saving the latest extraction time to track future runs

---

##  Tools Used

- Python 3.x
- Jupyter Notebook
- `pandas`
- `datetime`
- `random` and `csv` (for synthetic data generation)

---

## How to Run

1.Install Python & Dependencies  
   
2.Run Notebook
Open etl_extract.ipynb using Jupyter Notebook (VS Code, Anaconda, or JupyterLab), then run all cells in order.

3.Watch It Work

Section 1 loads and displays the full dataset.

Section 2 simulates a previous extraction time and extracts only new/updated records.

Section 3 saves the new timestamp to last_extraction.txt.#   E T L _ E x t r a c t _ K e v i n k o r i r _ 6 7 0 6 5 6 

---

##  Lab 4 – Transform in ETL

This update extends the original ETL pipeline by applying **data transformations** to both full and incremental extracts.

###  Applied Transformations

1. **Remove Duplicates** – Ensures clean data by dropping duplicate rows  
2. **Add `total_price` Column** – Enriches data with total = price × quantity  
3. **Standardize Dates** – Formats `transaction_date` as `YYYY-MM-DD`

###  Output Files

- `transformed_full.csv`: Cleaned and enriched full dataset  
- `transformed_incremental.csv`: Cleaned and enriched incremental dataset  

These transformations prepare the data for easier analysis, visualization, or loading into a database.

 
 
